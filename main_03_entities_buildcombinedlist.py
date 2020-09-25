"""
Create Entities_Combined and Episodes_Combined CSVs Utilizing Pandas
Combine CSVs in Folder into Single CSV
"""

import os
import pandas as pd


def combine_csvs(infolder, outputcsv):
    """ combine list of csvs into csv """
    files = [os.path.join(infolder, file) for file in os.listdir(infolder) if file.endswith('.csv')]

    dfs = []

    # build list of pandas dataframes
    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)

    # combine dataframes
    df_combined = pd.concat(dfs)

    # output to .csv
    pd.DataFrame.to_csv(df_combined, outputcsv, index=None)


# Transcripts
transcripts = (os.path.abspath('data/output/episodes'),
               os.path.abspath('data/output/episodes_combined.csv'))

# Entities
entities = (os.path.abspath('data/output/episodes_entities'),
            os.path.abspath('data/output/episodes_entities_combined.csv'))


def main():
    # output episodes_entities_combined.csv
    combine_csvs(entities[0], entities[1])
    combine_csvs(transcripts[0], transcripts[1])


if __name__ == '__main__':
    main()
