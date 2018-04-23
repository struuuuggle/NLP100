# -*- coding: utf-8 -*-
import redis

def repetation(country):
    """
    構築したデータベースから活動場所が'Japan'となっているアーティストの数を求める
    """
    artists = []
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for key in r.keys():
        if r.get(key).decode() == country:
            artists.append(key.decode())
            #print(key.decode())
    return len(artists)


def main():
    print(repetation('Japan'))

if __name__ == '__main__':
    main()
