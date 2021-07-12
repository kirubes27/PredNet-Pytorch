# -*- coding: utf-8 -*-

import os
import numpy as np
import h5py

# dataDir = '../coxlab-prednet-cc76248/kitti_data/'
# trainSet_path = os.path.join(dataDir, 'X_train.hkl')
# train_sources = os.path.join(dataDir, 'sources_train.hkl')
# testSet_path = os.path.join(dataDir, 'X_test.hkl')
# test_sources = os.path.join(dataDir, 'sources_test.hkl')

# @200.121
dataDir = 'C:\\Users\\kirub\\Desktop\\Summer project 2021\\PredNet_pytorch-master\\kitti_data\\prednet_kitti_data'                                 
#dataDir = '/media/sdb1/chenrui/kitti_data/h5/' ##Changed the path version from mac to windows + original was a .h5 file, however mine is .hkl     
trainSet_path = os.path.join(dataDir, 'X_train.h5')
train_sources = os.path.join(dataDir, 'sources_train.h5')
testSet_path  = os.path.join(dataDir, 'X_test.h5')
test_sources  = os.path.join(dataDir, 'sources_test.h5')


h5f = h5py.File(testSet_path,'r')
#testSet = h5f['X_test'][:]
testSet = h5f['data_0'][:]

#print(testSet)
# print(type(testSet))    # <class 'numpy.ndarray'>
# print(testSet.shape)    # (832, 128, 160, 3)