# Criminal enterprises, gangs and syndicates

Contributors: [Nina Janeva](https://github.com/cherryninna) and [Zainab Guennoun](https://github.com/zgn2)

Tutors: 
Mr. [Alexandre Dulaunoy](https://github.com/adulau) and Mr. [Christian Studer](https://github.com/chrisr3d)

## Context
This is an academic project, part of the Master's university course **Threat intelligence** taught @ Université de Lorraine. With the help of our tutors, we chose a topic that highlights the names of some of the most influential criminals worldwide and their activities throughout the years. This repository contains the source code of a web scraper that analyses our target [Wikipedia page](https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates) and generates JSON objects.


## Purpose
This project aims to synthesize data about enterprises, gangs, mafias and criminal syndicates involved in organized crime and structure it into specific analysis models that can contribute to the value of the [MISP Project](https://github.com/MISP) and potentially benefit our cyberspace.


## Dependencies

[Python3.x](https://docs.python.org/3/using/index.html), [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup), [spaCy](https://spacy.io/usage), [Requests](https://www.agiratech.com/install-requests-library-in-python)

### Linux
```bash
sudo apt-get install python3.x

pip3 install BeautifulSoup4

pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm

sudo apt install python-requests-doc
```

## Usage

```python
cd src
python3 scraper.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
