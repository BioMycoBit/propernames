import spacy
from spacy.gold import GoldParse
# from spacy.language import EntityRecognizer
from spacy.pipeline import EntityRecognizer

# nlp = spacy.load('en', entity=False, parser=False)
nlp = spacy.load('en_core_web_sm', entity=False, parser=False)

doc_list = []
doc = nlp('Llamas make great pets.')
doc_list.append(doc)
gold_list = []
gold_list.append(GoldParse(doc, [u'ANIMAL', u'O', u'O', u'O']))

ner = EntityRecognizer(nlp.vocab, entity_types=['ANIMAL'])
ner.update(doc_list, gold_list)