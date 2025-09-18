import cv2 as cv
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(description = 'Programa para segmentar caras')
parser.add_argument('--map_path', '-m', type=str)
parser.add_argument('--wanted_path', '-w', type=str)
args = parser.parse_args()

for n_img in range(1, 5):
    path_map = args.map_path + "/mapa_{}".format(n_img)+".png"
    path_wanted = args.wanted_path + "/wanted_{}".format(n_img)+".png"
    map = cv.imread(path_map)
    wanted = cv.imread(path_wanted)
    wanted_check_GRAY = cv.cvtColor(wanted, cv.COLOR_BGR2GRAY)
    th_check, dst_check = cv.threshold(wanted_check_GRAY, 110, 255, cv.THRESH_BINARY_INV)
    best = 0
    wanted_x = 0
    wanted_y = 0
    dim_map = map.shape[0]
    n = int(dim_map/115)

    for i in range(n):
        for j in range(n):
            x = i*115
            y = j*115
            mapHSV= cv.cvtColor(map, cv.COLOR_BGR2HSV)
            mask = np.zeros(map.shape[:2],np.uint8)
            rect = (x,y,wanted.shape[1],wanted.shape[0])
            bgdModel = np.zeros((1,65),np.float64)
            fgdModel = np.zeros((1,65),np.float64)
            cv.grabCut(mapHSV,mask,rect,bgdModel,fgdModel,1,cv.GC_INIT_WITH_RECT)
            mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
            wantedGrabCut = mapHSV*mask2[:,:,np.newaxis]

            wantedBGR = cv.cvtColor(wantedGrabCut, cv.COLOR_HSV2BGR)

            y1 = y
            y2 = y+115
            x1 = x
            x2 = x+115
            wanted_cut = wantedBGR[y1:y2, x1:x2]

            wantedGRAY = cv.cvtColor(wanted_cut, cv.COLOR_BGR2GRAY)
            th, dst = cv.threshold(wantedGRAY, 110, 255, cv.THRESH_BINARY_INV)

            intersection = cv.countNonZero(dst & dst_check)
            union = cv.countNonZero(dst | dst_check)
            score = intersection / union
            #print("Coordenadas [{},{}] | IoU = {}".format(i,j,score))

            if score > best:
                best = score
                wanted_x = i
                wanted_y = j
    print("Mejor IOU:", best)
    print("Coordenadas: [", wanted_y+1, ",", wanted_x+1, "]", "Pixel: ", "[", wanted_x*115, ",", wanted_y*115, "]")