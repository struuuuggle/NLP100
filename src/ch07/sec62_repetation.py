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
    try:
        print(repetation('Japan'))
    except Exception:
        print("Redis server not found!\nBefore you run this script, the command below.\n")
        print("$ redis-server")
        print("$ python sec60_build.py")
        print("$ python sec61_search_kvs.py\n")

if __name__ == '__main__':
    main()
