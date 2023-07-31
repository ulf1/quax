from typing import List
import conllu


def parse_conllu(corpus: List[conllu.models.TokenList]) -> List[dict]:
    """Convert conllu reader output to a list of dictionaries.

    Usage:
    ------
    >>> import conllu
    >>> import quaxa
    >>> corpus = conllu.parse(open('myfile.conllu', 'r').read())
    >>> sents, annot = quaxa.parse_conllu(corpus)
    """

    # process each sentence of a corpus
    sents, annot = [], []
    for sent in corpus:
        if len(sents) > 1:
            sents.append(sent.metadata['text'])

        # process each token of a sentence
        s = []
        for tok in sent:
            d = {
                "id": tok['id'],
                'text': tok['form'],
                'lemma': tok['lemma'],
                'upos': tok['upos'],
                'feats': tok['feats'],
                'head': tok['head'],
                'deprel': tok['deprel']
            }
            s.append(d)
        annot.append(s)

    # done
    return sents, annot
