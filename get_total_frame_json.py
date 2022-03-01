import os
import pandas as pd
import json
import numpy as np

# json_path = "./../Dataset/train/"
# json_path = "./../Dataset/val/"
#json_path = "./../Dataset/data_downsampling/train/"
json_path = "./../Dataset/data_downsampling/val/"

f_ext ="json"

file_name = []
info = []
for File in os.listdir(json_path):
    if File.endswith(f_ext):
        file_name.append(File)
    else:
        print("File with extention {} in Folder {} is not found".format(f_ext, json_path))

for i in range(len(file_name)):
    with open(json_path+file_name[i], 'rb') as f:
        jf = json.load(f)
        data = jf['data']
        label = jf['label']
        info.append([file_name[i],len(data),label])
        print("File:{} T length (frames):{} Label:{}".format(file_name[i], len(data),label))

json_info = pd.DataFrame(info)
json_info.to_csv("json_info_val_downsampling75.csv",header=["File", "T_Frames","Label"], index=False)
