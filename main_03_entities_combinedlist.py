"""
Build Entities Combined List
"""

from main_01_transcribe import writecsv
import csv
import os

# Example File
inputfolder = os.path.abspath('data/output/episodes_entities')
outputfile = os.path.abspath('data/output/entities_ppl.csv')

# Header
header = ('entitytxt', 'entityfinaltxt')

# Entities of Interest
entities_of_interest = 'PERSON'


def main():
    files = [os.path.join(inputfolder, file) for file in os.listdir(inputfolder)]
    entities = {}
    count = 0

    for file in files:

        # load csv
        with open(file, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                if row['entitylbl'] in entities_of_interest:
                    entities.update({row['entitytxt']: {'txt': row['entitytxt'],
                                                        'finaltxt': row['entitytxt']}})
                    count += 1

    print(f'outputfile: {outputfile}')
    writecsv(file=outputfile, header=header, linesdict=entities)


if __name__ == '__main__':
    main()
