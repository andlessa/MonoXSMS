# MonoXSMS
Repository for storing the code and results for studies related to LHC Mono-X searches and simplified models (SMS)


## Repo Description

 * [AuxInfo](./AuxInfo): Stores official auxiliary data from ATLAS and CMS
 * [Cards](./Cards): Cards for generating events with MadGraph5
 * [modelFiles](./modelFiles): UFO files for the Simplified DM models
 * [notebooks](./notebooks): Jupyter notebooks for recasting and plotting
 * [Refs](./Refs): Useful links to references

## External Packages


Currently the following tools can be installed and might be needed for running the 
recasting codes:

  * [MadGraph5](https://launchpad.net/mg5amcnlo/)[^1]
  * [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes)
  * [Pythia8](https://pythia.org/)
  * [HepMC](http://hepmc.web.cern.ch/hepmc/)


Executing:

```
./installer.sh
```

Will try to fetch the required packages and install them in the current folder.


### Additional Dependencies

The following packages/tools must already be installed in the system:

 * autoconf
 * libtool
 * gzip
 * bzr
 * [ROOT](https://root.cern/)
 
In addition the variable $ROOTSYS must be properly defined.
 
For installing ROOT the following steps can be taken:

 1. Download the tarball from [ROOT releases](https://root.cern/install/all_releases/)
 2. Install all the required dependencies (see [ROOT dependencies](https://root.cern/install/dependencies/))
 3. Extract the tarball to root-src
 4. Make the build and installation dirs (mkdir root-build root-<version>)
 5. In the buld folder run:

```
cmake ../root-src -DCMAKE_INSTALL_PREFIX=$homeDIR/root-<version> -Dall=ON -Dmemstat=OFF
make
make install
```

[^1] In recent python versions the installation of LHAPDF6 through MadGraph might fail, because it uses an old LHAPDF version. In order to install it,
     one needs to modify the lhapdf6 version to its [latest version](https://lhapdf.hepforge.org/downloads/) in MG5/HEPTools/HEPToolsInstallers/HEPToolInstaller.py
     and run (within the MG5 folder):
     ```
     ./HEPTools/HEPToolsInstallers/HEPToolInstaller.py lhapdf6
     ```
