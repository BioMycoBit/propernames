"""
Build Entities Final List
"""

from main_01_transcribe import writecsv
import os
import pandas as pd


in_xlsx = os.path.abspath('data/input/idxs/entities_master_0923_tmp.xlsx')
in_csv = os.path.abspath('data/input/output/episodes_entities_combined.csv')
outputfile = os.path.abspath('data/output/episodes_entities_final.csv')

# Header
header = ('keyword', 'occurrences')


def main():

    stdtbl = pd.read_excel(in_xlsx, usecols=['entityfinaltxt', 'occurrences'], index_col=0)

    # group by entityfinaltxt
    stdtbl1 = stdtbl.groupby(['entityfinaltxt']).sum()

    outputdict = pd.DataFrame.to_dict(stdtbl1)
    finaldict = {}

    # cycle thru outputdict creating dict of dicts (csvwriter format)
    for idx, (k,v) in enumerate(outputdict['occurrences'].items(), 1):
        print(f'{idx} k: {k} v: {v}')
        finaldict.update({idx: {'keyword': k,
                                'occurrences': v}})

    # output to .csv
    writecsv(file=outputfile, header=header, linesdict=finaldict)

    # ############################
    # TODO @2100Hr
    # THIS IS WORKING -> WE NOT HAVE episodes_entities_final.csv which
    # UTILIZES entities_master_*.xlsx and episodes_entities_combined.csv
    # SO NOW WE HAVE OUR KEYWORD LIST AND NOW WE WANT OUR FINAL
    # keyword | occurrences | clip tuples ((ep1, 1:23), (ep4, 10:15))
    # occurrences is going to cause problems ; should just calculate downstream
    # TODO: let's go back and add episode number field to outputs via filename



if __name__ == '__main__':
    main()
