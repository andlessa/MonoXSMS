#!/usr/bin/env python3

import pandas as pd
import os,glob

def combineWidths(files, outputFile):

    if not files:
        print('No valid files found.')
    else:
        print('Combining %i files' %len(files))

    allData = pd.read_pickle(files[0])
    for f in files[1:]:
        widthData = pd.read_pickle(f)
        allData = pd.concat((allData, widthData), ignore_index=True)

    # allColumns = allData.columns.to_list()
    # orderColumns = ['Coupling', 'Mode', '$m_{med}', '$m_{DM}']
    # orderColumns += [c for c in allColumns if not c in orderColumns]
    # allData = allData[orderColumns]
    # allData.sort_values(['Coupling', 'Mode', '$m_{med}', '$m_{DM}'], inplace=True,
                        #  ascending=[False,False,True,True], ignore_index=True)
    allData.to_pickle(outputFile)

if __name__ == "__main__":
    import argparse    
    ap = argparse.ArgumentParser(description=
            "Merge individual DataFrames for mediator width points to a single DataFrame (pickle file).")
    ap.add_argument('-f', '--inputFiles', required=True,nargs='+',
            help='list of pickle files to be merged', default =[])
    ap.add_argument('-o', '--outputFile', required=True, help='output file.')


    args = ap.parse_args()
    inputFiles = args.inputFiles
    outputFile = args.outputFile
    
    combineWidths(inputFiles,outputFile)