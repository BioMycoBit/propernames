"""
Spacy nlp
"""

from main import writecsv
import csv
import os
import spacy

# Example File
exfile = os.path.abspath('data/output/Ep 33 Edburg_otter.ai.csv')
outputfolder = os.path.abspath('data/output')

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Header
header = ('entitylbl', 'entitytxt')


def main():
    entities = {}

    # load csv
    with open(exfile, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)

        count = 0

        for row in csvreader:

            doc = nlp(row['transcript'])

            # Analyze syntax
            # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
            # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

            # Find named entities, phrases and concepts
            for entity in doc.ents:
                entities.update({count: {'label': entity.label_,
                                 'txt': entity.text, }})
                count += 1


    outputfile = exfile.replace('.csv', '_entities.csv')
    print(f'outputfile: {outputfile}')


    writecsv(file=outputfile, header=header, linesdict=entities)


if __name__ == '__main__':
    main()
