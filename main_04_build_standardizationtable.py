"""
Build Entities Standardization Table
"""

from main_01_transcribe import writecsv
import csv
import os

import collections

# Example File
inputfolder = os.path.abspath('data/output/episodes_entities')
outputfile = os.path.abspath('data/output/episodes_entities_standardizationtable.csv')

# Header
header = ('entitytype', 'entitytxt', 'entityfinaltxt', 'occurrences')

# Entities of Interest
entities_of_interest = 'PERSON'


def main():
    files = [os.path.join(inputfolder, file) for file in os.listdir(inputfolder)]

    # entities = {}
    entities = []
    count = 0
    output = collections.defaultdict(int)

    for file in files:


        # load csv
        with open(file, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                entities.append([(row['entitytxt'], row['entitylbl'])])


    for elem in entities:
        output[elem[0]] += 1

    print(f'outputfile: {outputfile}')


    outputdict = {}

    # k: ('john von Neumann', 'PERSON') v: 1

    for k,v in output.items():
        outputdict.update({k[0]: {
                                  'type': k[1],
                                  'entity': k[0],
                                  'entityfinal': k[0],  # duplicated
                                  'count': v}})

    writecsv(file=outputfile, header=header, linesdict=outputdict)


if __name__ == '__main__':
    main()
