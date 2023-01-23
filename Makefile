# Set the shell.
SHELL=/usr/bin/env bash

# Include the configuration.
# -include Makefile.inc

homeDIR = $(shell pwd)

PYTHIA8 := $(homeDIR)/pythia8
HEPMC := $(homeDIR)/HepMC2
LHAPDF := $(homeDIR)/lhapdf6

CXX      := g++
XMLDOC   := $(PYTHIA8)/share/Pythia8/xmldoc
CXXFLAGS := -O3 -std=c++11 -I$(PYTHIA8)/include -I$(PYTHIA8)/include/Pythia8/ -I$(HEPMC)/include -I$(ROOTSYS)/include -I$(LHAPDF)/include -W -Wall -Wshadow -fPIC -pthread -DGZIP
LDFLAGS  := -L$(PYTHIA8)/lib/ -L$(PYTHIA8)/lib -Wl,-rpath,$(PYTHIA8)/lib  -L$(HEPMC)/lib -Wl,-rpath,$(HEPMC)/lib -L$(LHAPDF)/lib -Wl,-rpath,$(LHAPDF)/lib -lpythia8 -lHepMC -DHEPMC2

all: main_pythiaADD.exe

clean:
	rm main_pythiaADD.exe


main_pythiaADD.exe: main_pythiaADD.cc 
	echo $(XMLDOC) > xml.doc
	$(CXX) -o $@ main_pythiaADD.cc $(CXXFLAGS) $(LDFLAGS)


	
	
