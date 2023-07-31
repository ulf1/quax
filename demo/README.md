## Download Corpus

To download the corpus (part of [Wortschatz Universität Leipzig](https://wortschatz.uni-leipzig.de/en/download/German) project), execute the following bash commands:

```
wget -q http://pcai056.informatik.uni-leipzig.de/downloads/corpora/deu-de_web_2021_10K.tar.gz
tar xzf deu-de_web_2021_10K.tar.gz
mkdir corpus
mv deu-de_web_2021_10K/deu-de_web_2021_10K-sentences.txt corpus/sentences.txt
rm -rf deu-de_web_2021_10K deu-de_web_2021_10K.tar.gz
```

Sentences are saved to `corpus/sentences.txt`, scores will be saved to `corpus/scores.csv`.

To parse the sentences with SpaCy, run as well:

`python -m spacy download de_dep_news_trf-3.5.0 --direct`

