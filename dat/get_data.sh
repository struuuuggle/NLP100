#!/bin/sh

URL_LIST='
http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt
http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz
http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt
http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt
http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz
http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2
http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz
'

for url in ${URL_LIST}
do
    wget $url
done

tar -zxvf rt-polaritydata.tar.gz
nkf -w --overwrite ./rt-polaritydata/rt-polarity.pos
nkf -w --overwrite ./rt-polaritydata/rt-polarity.neg

exit 0
