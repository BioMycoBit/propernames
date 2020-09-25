"""
Combine all Entity .CSVs into 1
"""

from main_01_transcribe import writecsv
import os
import pandas as pd


# Example File
inputfolder = os.path.abspath('data/output/episodes_entities')
outputfile = os.path.abspath('data/output/episodes_entities_combined.csv')


def main():
    files = [os.path.join(inputfolder, file) for file in os.listdir(inputfolder)]

    dfs = []

    # build list of pandas dataframes
    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)

    # combine dataframes
    df_combined = pd.concat(dfs)

    # output to .csv
    pd.DataFrame.to_csv(df_combined, outputfile, index=None)




if __name__ == '__main__':
    main()
