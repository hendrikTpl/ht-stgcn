import cv2
import json
import numpy as np

# with open('format-fix2.json', 'rb') as f:
#     data = json.load(f)
with open('./Dataset/train/26_upper_30_Use1.json', 'rb') as f:
    data = json.load(f)
data = data['data']

radius = 8
color = (0, 0, 255)
thickness = -1

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('26_upper_30_Use1.json.avi', fourcc, 20.0,
                          (int(1920), int(1920)))
for i in range(len(data)):
    canvas = (np.ones((1920, 1920, 3))*255).astype('uint8')
    for frame in data[i]['skeleton']:
        for coor_id in range(0, len(frame['pose']), 2):
            # if coor_id ==2:
            #     continue
            center_coordinates  = (int(frame['pose'][coor_id]), int(frame['pose'][coor_id+1]))
            # print(coordinate)
            canvas = cv2.circle(canvas, center_coordinates, radius, color, thickness)
    # cv2.imwrite('coba.png', canvas)
    out.write(canvas)
out.release()
#print(len(data))