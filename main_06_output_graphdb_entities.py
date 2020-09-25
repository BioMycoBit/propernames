"""
Build Entities Output For GraphDB
"""

from main_01_transcribe import writecsv
import os
import pandas as pd

entities_combined = os.path.abspath('data/output/episodes_entities_combined.csv')
entities_final = os.path.abspath('data/output/episodes_entities_final.csv')
entities_standardization = os.path.abspath('data/input/idxs/entities_standardization.xlsx')

outputcsv = os.path.abspath('data/output/graphdb_output.csv')

def main():

    # read csvs and xlsx into pandas dataframes
    combined = pd.read_csv(entities_combined, usecols=['episodeno', 'entitytxt', 'time'])
    standardization = pd.read_excel(entities_standardization, usecols=['entityfinaltxt', 'entitytxt'])
    final = pd.read_csv(entities_final, usecols=['entityfinaltxt'])

    # combine final .csv and standardization .xlsx (groupedby entityfinaltxt)
    df_final_std = pd.merge(final, standardization)

    # combine new df and combined .csv (groupedby entitytxt)
    df_final_std_comb = pd.merge(df_final_std, combined)

    # drop entitytxt col from df_final_std_comb
    df_final_std_comb = df_final_std_comb.drop(columns="entitytxt")

    # drop_duplicates
    df_final_std_comb = df_final_std_comb.drop_duplicates()

    # output to .csv
    pd.DataFrame.to_csv(df_final_std_comb, outputcsv, index=None)

    # # qc
    # print(f'len(combined): {len(combined)}')
    # print(f'len(standardization): {len(standardization)}')
    # print(f'len(final): {len(final)}')
    # print(f'len(df_finalandstd): {len(df_final_std)}')
    # print(f'len(df_final_std_comb): {len(df_final_std_comb)}')


if __name__ == '__main__':
    main()
