"""
Spacy nlp
"""
import csv
import os
import spacy

# Example File
exfile = os.path.abspath('data/output/Ep 33 Edburg_otter.ai.csv')
outputfolder = os.path.abspath('data/output')

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")




def main():

    # load csv
    with open(exfile, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        next(csvreader)

        for row in csvreader:

            print(row[3])
            breakpoint()

            doc = nlp(row[3])



            # Analyze syntax
            print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
            print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

            # Find named entities, phrases and concepts
            for entity in doc.ents:
                print(entity.text, entity.label_)

            # print(', '.join(row))


    breakpoint()

    # Process whole documents
    text = ("When Sebastian Thrun started working on self-driving cars at "
            "Google in 2007, few people outside of the company took him "
            "seriously. “I can tell you very senior CEOs of major American "
            "car companies would shake my hand and turn away because I wasn’t "
            "worth talking to,” said Thrun, in an interview with Recode earlier "
            "this week.")
    doc = nlp(text)

    # Analyze syntax
    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

    # Find named entities, phrases and concepts
    for entity in doc.ents:
        print(entity.text, entity.label_)


if __name__ == '__main__':
    main()