"""
Build Entities Final List
"""

from main_01_transcribe import writecsv
import os
import pandas as pd


in_xlsx = os.path.abspath('data/input/idxs/entities_standardization.xlsx')
in_csv = os.path.abspath('data/input/output/episodes_entities_combined.csv')
outputfile = os.path.abspath('data/output/episodes_entities_final.csv')

# Header
header = ('entityfinaltxt', 'occurrences')


def main():

    stdtbl = pd.read_excel(in_xlsx, usecols=['entityfinaltxt', 'occurrences'])

    # convert all entityfinaltxt to string NOT SURE IF NEEDED OR HANDLED BY BELOW ENCODE / DECODE
    stdtbl['entityfinaltxt'] = [str(entity) for entity in stdtbl['entityfinaltxt']]


    # group by entityfinaltxt
    stdtbl1 = stdtbl.groupby(['entityfinaltxt']).sum()

    outputdict = pd.DataFrame.to_dict(stdtbl1)
    finaldict = {}

    # cycle thru outputdict creating dict of dicts (csvwriter format)
    for idx, (k,v) in enumerate(outputdict['occurrences'].items(), 1):
        finaldict.update({idx: {'keyword': k.encode('utf-8', 'ignore').decode('windows-1252'),
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




if __name__ == '__main__':
    main()
