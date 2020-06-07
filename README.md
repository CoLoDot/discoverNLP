# discoverNLP

discoverNLP is about Natural Language Processing. This is a personnal playground i created in order to discover and improve my knowledge regarding natural language processing.

Activate a virtual env
```
python3 -m venv env
source env/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
python -m spacy download fr_core_news_sm 
python -m spacy download en_core_web_md
python -m spacy download en_core_web_sm
```

Run tests
```
pytest --cov test/
```