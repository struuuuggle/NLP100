#!/bin/sh

wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt
wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz
wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt
wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt
wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz
wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2
wget http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz

nkr -w --overwrite ./rt-polaritydata/rt-polaritydata/rt-polarity.pos
nkr -w --overwrite ./rt-polaritydata/rt-polaritydata/rt-polarity.neg
