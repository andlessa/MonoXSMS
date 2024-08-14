# MonoXSMS
Repository for storing the code and results for studies related to LHC Mono-X searches and simplified models (SMS).


## Folder Structure

 * [Cards](./Cards): Cards for generating events with MadGraph5
 * [modelFiles](./modelFiles): UFO files for the Simplified DM models
 * [CMS-EXO-20-004](./CMS-EXO-20-004): Stores [auxiliary](./CMS-EXO-20-004/AuxInfo) data from ATLAS and CMS, along with [instructions to produce the validation results](./CMS-EXO-20-004/validation/validationNotes.md) and the [validation results](./CMS-EXO-20-004/validation/README.md).

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
 


[^1]: In recent python versions the installation of LHAPDF6 through MadGraph might fail, because it uses an old LHAPDF version. In order to install it,
     one needs to modify the lhapdf6 version to its [latest version](https://lhapdf.hepforge.org/downloads/) in MG5/HEPTools/HEPToolsInstallers/HEPToolInstaller.py
     and run (within the MG5 folder):
     ```
     ./HEPTools/HEPToolsInstallers/HEPToolInstaller.py lhapdf6
     ```     
