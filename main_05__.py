"""
Build Clean Entities List
"""

from main_01_transcribe import writecsv
import os
import pandas as pd


# Example File  TODO: _tmp -> remove fields starting with digits to see if this is source of TypeError
in_xlsx = os.path.abspath('data/input/idxs/entities_master_0923_tmp.xlsx')
in_csv = os.path.abspath('data/input/output/episodes_entities_combined.csv')
outputfile = os.path.abspath('data/output/episodes_entities_final.csv')

# Header
header = ('keyword', 'occurrences')

def main():
    # files = [os.path.join(inputfolder, file) for file in os.listdir(inputfolder)]

    stdtbl = pd.read_excel(in_xlsx, usecols=['entityfinaltxt', 'occurrences'], index_col=0)

    print(f'read_excel: {len(stdtbl)} records')

    # breakpoint()
    #
    # # drop entitytxt and entitytype column
    # stdtbl = stdtbl.drop(columns=['entitytxt', 'entitytype'])

    # group by entityfinaltxt
    # stdtbl1 = stdtbl.groupby(['entityfinaltxt', 'occurrences']).sum()
    stdtbl1 = stdtbl.groupby(['entityfinaltxt']).sum()

    print(f'groupby entityfinaltxt: {len(stdtbl1)} records')

    print(f'type(stdtbl1): {type(stdtbl1)}')
    print(stdtbl1.head())

    # output to .csv
    # pd.DataFrame.to_csv(stdtbl, outputfile, index=None)

    outputdict = pd.DataFrame.to_dict(stdtbl1)
    finaldict = {}

    for idx, (k,v) in enumerate(outputdict['occurrences'].items(), 1):
        print(f'{idx} k: {k} v: {v}')
        finaldict.update({idx: {'keyword': k,
                                'occurrences': v}})
    #
    # breakpoint()

    # output to .csv
    writecsv(file=outputfile, header=header, linesdict=finaldict)



if __name__ == '__main__':
    main()
