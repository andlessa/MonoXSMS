# MonoXSMS
Repository for storing the code and results for studies related to LHC Mono-X searches and simplified models (SMS)


## Repo Description

 * [monoJet](./monoJet): Stores data and code for the mono-jet analyses

## External Packages


Currently the following tools can be installed and might be needed for running the 
recasting codes:

  * [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes)
  * [Pythia8](https://pythia.org/)
  * [HepMC](http://hepmc.web.cern.ch/hepmc/)
  * [MadGraph5](https://launchpad.net/mg5amcnlo/)
  * [CheckMATE](https://github.com/CheckMATE2/checkmate2)

Execting:

```
./installes.sh
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
