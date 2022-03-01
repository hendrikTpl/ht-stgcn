import numpy as np
import json
import os

##settings
json_path = "./../Dataset/train/"
out_path = "./../Dataset/data_downsampling/train/"

# json_path = "./../Dataset/val/"
# out_path = "./../Dataset/data_downsampling/val/"

f_ext ="json"

file_name = []

for File in os.listdir(json_path):
    if File.endswith(f_ext):
        file_name.append(File)
    else:
        print("File with extention {} in Folder {} is not found".format(f_ext, json_path))

## Do downsampling to 75 Frames
for i in range(len(file_name)):
    with open(json_path+file_name[i], 'rb') as f:
        jf = json.load(f)
        data = jf['data']   
        label = jf['label']
        label_index=jf['label_index']    
        ##in this case our dataset has mean  around 75 frames
        if len(data)<75: 
            ## TODO:copy file
            j_take = data
            j_dict = {
                "data":j_take,
                "label":label,
                "label_index":label_index
                }
            j_object = json.dumps(j_dict, indent=3)
            # Writing to sample.json
            with open(out_path+file_name[i]+".json", "w") as outfile:
                outfile.write(j_object)
        if 75<=len(data)<150: 
            ## TODO:downsamping with taking every 2 steps
            j_take = data[::2]
            j_dict = {
                "data":j_take,
                "label":label,
                "label_index":label_index
                }
            j_object = json.dumps(j_dict, indent=3)
            # Writing to sample.json
            with open(out_path+file_name[i]+".json", "w") as outfile:
                outfile.write(j_object)

        if 150<=len(data)<=200:
            ## TODO: downsamping with taking every 3 steps
            j_take = data[::3]
            j_dict = {
                "data":j_take,
                "label":label,
                "label_index":label_index
                }
            j_object = json.dumps(j_dict, indent=3)
            # Writing to sample.json
            with open(out_path+file_name[i]+".json", "w") as outfile:
                outfile.write(j_object)

        if 200<=len(data)<300:
            ## TODO: downsamping with taking every 4 steps
            j_take = data[::4]
            j_dict = {
                "data":j_take,
                "label":label,
                "label_index":label_index
                }
            j_object = json.dumps(j_dict, indent=3)
            # Writing to sample.json
            with open(out_path+file_name[i]+".json", "w") as outfile:
                outfile.write(j_object)

        if 300<=len(data)<375:
            ## TODO: downsamping with taking every 5 steps
            j_take = data[::5]
            j_dict = {
                "data":j_take,
                "label":label,
                "label_index":label_index
                }
            j_object = json.dumps(j_dict, indent=3)
            # Writing to sample.json
            with open(out_path+file_name[i]+".json", "w") as outfile:
                outfile.write(j_object)

        if 375 <= len(data)<450:
            ##TODO: do something more here
            j_take = data[::6]
            j_dict = {
                "data":j_take,
                "label":label,
                "label_index":label_index
                }
            j_object = json.dumps(j_dict, indent=3)
            # Writing to sample.json
            with open(out_path+file_name[i]+".json", "w") as outfile:
                outfile.write(j_object)
        if 450 <= len(data)<525:
            ##TODO: do something more here
            j_take = data[::7]
            j_dict = {
                "data":j_take,
                "label":label,
                "label_index":label_index
                }
            j_object = json.dumps(j_dict, indent=3)
            # Writing to sample.json
            with open(out_path+file_name[i]+".json", "w") as outfile:
                outfile.write(j_object)
        if len(data)>=525:
            pass
        



        

        



        

