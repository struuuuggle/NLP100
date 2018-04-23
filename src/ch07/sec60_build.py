# -*- coding: utf-8 -*-
import os
import json
import gzip
import redis
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/artist.json.gz")

def build(filename):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    with gzip.open(filename, 'r') as f:
        for line in f:
            json_dict = json.loads(line)
            try:
                r.set(json_dict['name'], json_dict['area'])
            except KeyError:
                continue

def main():
    build(data)

if __name__ == '__main__':
    main()
