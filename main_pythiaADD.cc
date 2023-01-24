
// Example how to create a copy of the event record, where the original one
// is translated to another format, to meet various analysis needs.
// In this specific case the idea is to set up the history information
// of the underlying hard process to be close to the PYTHIA 6 structure.

#include "Pythia8/Pythia.h"
#include "Pythia8Plugins/HepMC2.h"
#include <unistd.h>

using namespace Pythia8;

//--------------------------------------------------------------------------

int run(int nevents, const string & cfgfile, const string & outputfile)
{

  //Set output file names
  // std::srand(500);
  string outname;
  outname = outputfile;

  size_t lastindex = outname.find_last_of("."); 

  string bannerFile = outname.substr(0, lastindex) + "_banner.txt";
  // Generator. Shorthand for the event.
  Pythia pythia("",false); //Set printBanner to false
  pythia.readFile( cfgfile );

  // pythia.settings.writeFileXML(banner)
  // Create basic banner for convenience
  ofstream banner;
  banner.open (bannerFile);
  banner << "<PythiaBanner>\n";
  banner << "<header>\n";
  banner << "<slha>\n";  
  char linebuf[100];
  banner << "BLOCK MASS #\n";
  sprintf(linebuf, "  5000039 %.4f\n", pythia.particleData.m0(5000039));
  banner << linebuf;
  banner << "BLOCK ADDINPUTS #\n";
  sprintf(linebuf, "  1 %s # MD (fundamental scale)\n", pythia.settings.output("ExtraDimensionsLED:MD",false).c_str());
  banner << linebuf;
  sprintf(linebuf, "  2 %s # n (number of extra dim)\n", pythia.settings.output("ExtraDimensionsLED:n",false).c_str());
  banner << linebuf;
  sprintf(linebuf, "  3 %s # Cutoff (on/off)\n", pythia.settings.output("ExtraDimensionsLED:CutOffmode",false).c_str());
  banner << linebuf;
  banner << "</slha>\n";

  // Copy pythia input
  ifstream pythia_file;
  pythia_file.open(cfgfile);
  string line;
  banner << "<PythiaCard>\n";
  while (getline(pythia_file, line)) {
          banner << line << "\n";
        }
  banner << "</PythiaCard>\n";
  
// trying to write hepmc
// Interface for conversion from Pythia8::Event to HepMC event.
  Pythia8ToHepMC ToHepMC(outname);

// Specify file where HepMC events will be stored.
  ToHepMC.set_store_pdf(true);
  ToHepMC.set_store_proc(true);
  ToHepMC.set_store_xsec(false);

  // Create an LHEF object that can access relevant information in pythia. process is the hard event.

  // LHEF3FromPythia8 myLHEF3(&pythia.process, &pythia.settings, &pythia.info, &pythia.particleData);

  // Open a file on which LHEF events should be stored, and write header.
  // myLHEF3.openLHEF(lhefilename);

  // Initialize.
  pythia.init();

  // // Estimate cross-section:
  // for (int i =0; i < 100; ++i){
  //   pythia.next();
  // }
  // double xsecPB = pythia.info.sigmaGen()*1e9;
  // double xsecPBErr = pythia.info.sigmaErr()*1e9;
  // cout << "XSEC estimate = " << xsecPB << endl << endl;

  // pythia.init();

  // Store initialization info in the LHAup object.
  // myLHEF3.setInit();

  // Begin event loop.
  int iAbort = 0;
  int iEvent = 0;
  double xsecPB = 0.;
  double xsecPBErr = 0.;
  // Make the weights have two entries:
  // the first is the pythia (dummy) value
  // and the second is the real weight computed from
  // the estimated cross-section
  vector<double> w = {0.0, 0.0};
  vector<string> wNames = {pythia.info.weightNameVector()[0],"WeightPB"};
  // Number of events to estimate the xsec (10% of events)
  // and determine the correct event weight
  // Limited to the interval: 100 < nXsecEstimate < 1000
  int nXsecEstimate = min(1000,max(100,int(nevents/10.))); 
  while (iEvent < nevents){

      // If failure because reached end of file then exit event loop.
      if (pythia.info.atEndOfFile()) break;

      // Generate events. Quit if failure.
      if (!pythia.next()) {
        if (++iAbort < 10) continue;
        cout << " Event generation aborted prematurely, owing to error!\n";
        break;
      }

      ++iEvent;
      // cout << "ievt = " << iEvent << " sigma = " << pythia.info.sigmaGen()*1e9 << endl;
      // Use the first 100 events to estimate the total xsec
      if ((iEvent < nXsecEstimate) & (xsecPB == 0.0)) continue;
      // Get xsec estimate to be used as event weights
      if(xsecPB == 0.0) {
        iEvent = 1; // Reset event count
        xsecPB = pythia.info.sigmaGen()*1e9;
        xsecPBErr  = pythia.info.sigmaErr()*1e9;
        w[1] = xsecPB/nevents;
      }
      w[0] = pythia.info.weightValueByIndex(0);
      
      // Set weights, fill HEPMC event and write it
      ToHepMC.setWeightNames(wNames);     
      ToHepMC.fillNextEvent( pythia );
      ToHepMC.setXSec(xsecPB, xsecPBErr);
      ToHepMC.setWeights(w);
      ToHepMC.writeEvent();
      
      // Write the HepMC event to file. Done with it.
    //
    // if (iEvent < nShow) hard.list();

  // End of event loop.
  }
  // Final statistics.
  
  pythia.stat();
  // Update the cross section info based on Monte Carlo integration during run.
  // myLHEF3.closeLHEF(true);
  // Done.

  //Write cross-section and number of events and close banner.
  banner << "<GenerationInfo>\n";
  sprintf(linebuf, "#  Number of Events        :       %d\n", iEvent);
  banner << linebuf;
  sprintf(linebuf, "#  Integrated weight (pb)  :      %.4e\n", pythia.info.sigmaGen()*1e9);
  banner << linebuf;
  banner << "</GenerationInfo>\n";
  banner << "</header>\n";
  banner << "</PythiaBanner>\n";
  banner.close();

  return 0;
}

//--------------------------------------------------------------------------



void help( const char * name )
{
	  cout << "syntax: " << name << " [-h] [-f <input file>] [-o <output file>] [-n <number of events>] [-c <pythia cfg file>]" << endl;
	  cout << "        -c <pythia config file>:  pythia config file [pythia8.cfg]" << endl;
	  cout << "        -o <output file>:  output filename for HepMC files [<input file>.hepmc]" << endl;
	  cout << "        -n <number of events>:  Number of events to be generated [100]. If n < 0, it will run over all events in the LHE file" << endl;
  exit( 0 );
};

int main( int argc, const char * argv[] ) {
  int nevents = -1;
  string cfgfile = "pythia8.cfg";
  string outfile = "";
  for ( int i=1; i!=argc ; ++i )
  {
    string s = argv[i];
    if ( s== "-h" )
    {
      help ( argv[0] );
    }

    if ( s== "-c" )
    {
      if ( argc < i+2 ) help ( argv[0] );
      cfgfile = argv[i+1];
      i++;
      continue;
    }


    if ( s== "-n" )
    {
      if ( argc < i+2 ) help ( argv[0] );
      nevents = atoi(argv[i+1]);
      i++;
      continue;
    }

    if ( s== "-o" )
    {
      if ( argc < i+2 ) help ( argv[0] );
      outfile = argv[i+1];
      i++;
      continue;
    }



    cout << "Error. Argument " << argv[i] << " unknown." << endl;
    help ( argv[0] );
  };

  run(nevents, cfgfile, outfile);

  return 0;
}
