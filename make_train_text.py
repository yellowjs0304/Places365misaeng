import os

dirname="/media/ailab/96de7966-5f99-4f8f-81d0-35ddb1898e9f/JS/places365_misaeng/data/"
train_file = "train.txt"
f = open(train_file,mode="w")

for (path, dir, files) in os.walk(dirname):
    for filename in files:
        full_filename = path+'/'+filename
        f.write(full_filename+'\n')
        print(full_filename)
f.close()
