"""
Spacy nlp
"""

from main_01_transcribe import writecsv
import csv
import os
import spacy

# Example File
inputfolder = os.path.abspath('data/output/episodes')
outputfolder = os.path.abspath('data/output/episodes_entities')

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Header
header = ('episode', 'episodeno', 'entitylbl', 'entitytxt', 'time')


def main():

    files = [os.path.join(inputfolder, file) for file in os.listdir(inputfolder)]

    for file in files:
        entities = {}

        # load csv
        with open(file, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)

            count = 0

            for row in csvreader:

                # print(f'row: {row}')
                # breakpoint()

                doc = nlp(row['transcript'])

                # Analyze syntax
                # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
                # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

                # Find named entities, phrases and concepts
                for entity in doc.ents:

                    # print(f'{type(entity)} {entity.text} {entity.label_}')

                    entities.update({count: {'episode': row["episode"],
                                             'episodeno': row["episodeno"],
                                             'label': entity.label_,
                                             'txt': entity.text,
                                             'time': row["time"]}})
                    count += 1


        outputfile = os.path.join(outputfolder,
                                  os.path.basename(file).replace('.csv', '_entities.csv'))

        print(f'outputfile: {outputfile}')
        writecsv(file=outputfile, header=header, linesdict=entities)


if __name__ == '__main__':
    main()
