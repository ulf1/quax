import csv
import conllu
import random
import quaxa

random.seed(42)

from spacy_conll import init_parser

nlp = init_parser("de_dep_news_trf",
                  "spacy",
                  include_headers=True)

def demo_corpus(file_in, file_out):
    scores = []
    with open(file_in, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        id, sent = line.split('\t')
        doc = nlp(sent)
        # spacy conll format
        conll = doc._.conll_str
        doc = nlp(text)
        anno = []
        # Iterate over the tokens in the document
        for token in doc:
            # Create a dictionary for each token
            token_dict = {
                'text': token.text,
                'lemma': token.lemma_,
                'upos': token.pos_,
                'xpos': token.tag_,
                'dep': token.dep_,
                'head': token.head.text,
                'children': [child.text for child in token.children]
            }
            # Append the token dictionary to the dependency tree
            anno.append(token_dict)
            # use content lemmata as headwords
            lemmas_content = [tok.get('lemma') for tok in anno if tok.get('upos') in {'NOUN', 'VERB', 'ADJ'}]
            for headword in lemmas_content:
                factor = quaxa.total_score(
                            headword=headword, txt=sent, annotation=anno)
                scores.append([id, sent, headword, factor])
    with open(file_out, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Sentence', 'Headword', 'Score'])
        writer.writerows(scores)
    return scores


if __name__ == '__main__':
    demo_corpus('corpus/sentences.txt', 'corpus/scores.txt')
