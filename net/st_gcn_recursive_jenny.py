#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
import subprocess
import time

layout = ['hand_50']
window_size = [200]
batch_size = [32]
dropout = [0.05]

all_start_time = time.time()

for l in layout:
    for ws in window_size:
        for drop in dropout:
            for batch in batch_size:
                start_time = time.time()
                if '26' in l:
                    skeleton = 'upperright'
                elif '50' in l:
                    skeleton = 'upper'
                    batch = 6
                else:
                    skeleton = 'right'
                    batch = 12
                if 'hand' in l:
                    model = 'ST-GCN_hand'
                else:
                    model = 'HG-GCN'

                # folder = l+'/w'+str(ws)+'/dr'+str(int(drop*10))+'/batch'+str(batch) #+'/num'+str(num+1)
                data_path = '/media/cgu/71577730-1a00-4505-adc2-695423d4b07c/Jerry/5G/raw_data/220216_v1.0/model_data/'
                train_feeder = {}
                train_feeder['random_choose'] = False
                train_feeder['random_move'] = False
                train_feeder['window_size'] = ws
                train_feeder['data_path'] = data_path +'train_data.npy'
                train_feeder['label_path'] = data_path + 'train_label.pkl'
                test_feeder = {}
                test_feeder['data_path'] = data_path +'val_data.npy'
                test_feeder['label_path'] = data_path + 'val_label.pkl'

                builder = "python main.py recognition" + \
                          " -w /media/cgu/71577730-1a00-4505-adc2-695423d4b07c/Jerry/5G/raw_data/220216_v1.0/model_data/hand_model" + \
                          " -c /home/cgu/Documents/st-gcn-debug1/config/st_gcn/hand_Jerry_5G/train.yaml" + \
                          ' --train_feeder_args "{}"'.format(train_feeder) + \
                          ' --test_feeder_args "{}"'.format(test_feeder) + \
                          " --batch_size=" + str(batch) + \
                          " --test_batch_size=" + str(batch) + \
                          " --model_args dropout=" + str(drop) + \
                          " --model_args in_channels=" + str(3) + \
                          ' --model_args "{}"'.format({'graph_args':{'layout':l, 'strategy':'spatial'}})

                print(l, ws, drop, batch)
                subprocess.call(builder, shell=True, cwd="/home/cgu/Documents/st-gcn-debug1")
                    
                print('--- cost {:.4f} second ---'.format(time.time()-start_time))

print('--- Experiment End ---')
print('--- cost {:.4f} second ---'.format(time.time()-all_start_time))
                
                           
                                    