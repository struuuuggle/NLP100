import os

# Go to /Users/Polaris/NLP100/
# then do these commands

#my_path = os.path.join(DATA_DIR, "hogehoge.txt")
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir) # expect: /Users/Polaris/Documents/NLP100/src
data_path = os.path.join(current_dir, "data/hogehoge.txt")
print(data_path) # expect: /Users/Polaris/Documents/NLP100/src/data/hogehoge.txt
# print(__file__)
