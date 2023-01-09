#!/bin/sh

homeDIR="$( pwd )"

echo "Installation will take place in $homeDIR"

echo "[Checking system dependencies]"
PKG_OK=$(dpkg-query -W -f='${Status}' autoconf 2>/dev/null | grep -c "ok installed")
if test $PKG_OK = "0" ; then
  echo "autoconf not found. Install it with sudo apt-get install autoconf."
  exit
fi
PKG_OK=$(dpkg-query -W -f='${Status}' libtool 2>/dev/null | grep -c "ok installed")
if test $PKG_OK = "0" ; then
  echo "libtool not found. Install it with sudo apt-get install libtool."
  exit
fi
PKG_OK=$(dpkg-query -W -f='${Status}' gzip 2>/dev/null | grep -c "ok installed")
if test $PKG_OK = "0" ; then
  echo "gzip not found. Install it with sudo apt-get install gzip."
  exit
fi
PKG_OK=$(dpkg-query -W -f='${Status}' bzr 2>/dev/null | grep -c "ok installed")
if test $PKG_OK = "0" ; then
  echo "bzr not found. Install it with sudo apt-get install bzr."
  exit
fi

cd $homeDIR

madgraph="MG5_aMC_v3.4.1.tar.gz"
URL=https://launchpad.net/mg5amcnlo/3.0/3.4.x/+download/$madgraph
echo -n "Install MadGraph (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir MG5;
	echo "[installer] getting MadGraph5"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $madgraph -C MG5 --strip-components 1;
	echo "Replacing MG5/Template/NLO/SubProcesses/cuts.f by Cards/CMS-SUS-20-004/cuts.f";
#	cp ./Cards/CMS-SUS-20-004/cuts.f ./MG5/Template/NLO/SubProcesses/cuts.f
	cd $homeDIR;
        rm $madgraph;
fi

#Get HepMC tarball
hepmc="hepmc2.06.11.tgz"
echo -n "Install HepMC2 (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir hepMC_tmp
	URL=http://hepmc.web.cern.ch/hepmc/releases/$hepmc
	echo "[installer] getting HepMC"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $hepmc -C hepMC_tmp;
	mkdir HepMC-2.06.11; mkdir HepMC-2.06.11/build; mkdir HepMC2;
	echo "Installing HepMC in ./HepMC";
	cd HepMC-2.06.11/build;
	../../hepMC_tmp/HepMC-2.06.11/configure --prefix=$homeDIR/HepMC2 --with-momentum=GEV --with-length=MM;
	make;
	make check;
	make install;

	#Clean up
	cd $homeDIR;
	rm -rf hepMC_tmp; rm $hepmc; rm -rf HepMC-2.06.11;
fi

#Get pythia tarball
pythia="pythia8307.tgz"
URL=https://pythia.org/download/pythia83/$pythia
echo -n "Install Pythia (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	if hash gzip 2>/dev/null; then
		mkdir pythia8;
		echo "[installer] getting Pythia"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $pythia -C pythia8 --strip-components 1;
		echo "Installing Pythia in pythia8";
		cd pythia8;
		./configure --with-hepmc2=$homeDIR/HepMC2 --with-root=$ROOTSYS --prefix=$homeDIR/pythia8 --with-gzip
		make -j4; make install;
		cd $homeDIR
		rm $pythia;
	else
		echo "[installer] gzip is required. Try to install it with sudo apt-get install gzip";
	fi
fi


echo -n "Install Delphes (y/n)? "
repo=https://github.com/delphes/delphes
URL=http://cp3.irmp.ucl.ac.be/downloads/$delphes
read answer
if echo "$answer" | grep -iq "^y" ;then
  latest=`git ls-remote --sort="version:refname" --tags $repo  | grep -v -e "pre" | grep -v -e "\{\}" | cut -d/ -f3- | tail -n1`
  echo "[installer] Cloning Delphes version $latest";
  git clone --branch $latest https://github.com/delphes/delphes.git Delphes
  cd Delphes;
  export PYTHIA8=$homeDIR/pythia8;
  echo "[installer] installing Delphes";
  make HAS_PYTHIA8=true;
  rm -rf .git
  cd $homeDIR;
fi



echo -n "Install MadAnalysis (y/n)? "
read answer
repo=https://github.com/MadAnalysis/madanalysis5
if echo "$answer" | grep -iq "^y" ;then
   echo "[installer] getting MadAnalysis";
   latest=`git ls-remote --refs --sort="version:refname" --tags $repo | cut -d/ -f3-|tail -n1`
   git clone --branch $latest git@github.com:MadAnalysis/madanalysis5.git MadAnalysis5;
   cd MadAnalysis5/bin
   echo -e "install fastjet\ninstall zlib\ninstall delphes\ninstall PAD\nexit\n" > mad_install.txt
   ./ma5 -f < mad_install.txt
   rm mad_install.txt
   echo "[installer] replacing MA5 delphes card delphes_card_cms_exo_20_004.tcl by Cards/delphes_card.dat"
   cd $homeDIR
   cp ./Cards/delphes_card.dat ./MadAnalysis5/tools/PAD/Input/Cards/delphes_card_cms_exo_20_004.tcl
   echo "[installer] done";
fi


#
#
# echo -n "Install CutLang (y/n)? "
# read answer
# if echo "$answer" | grep -iq "^y" ;then
#   echo "[installer] getting CutLang";
#   git clone git@github.com:unelg/CutLang.git CutLang;
#   cd CutLang;
#   cd CLA;
#   echo "[installer] compiling CutLang";
#   make;
#   cd ..;
#   rm -rf .git;
#   rm -rf ADLLHCanalyses;
#   echo "[installer] getting ADLLHCanalyses";
#   git clone git@github.com:ADL4HEP/ADLLHCanalyses.git ADLLHCanalyses;
#   rm -rf ADLLHCanalyses/.git
#   cd $homeDIR
# fi

cd $homeDIR
