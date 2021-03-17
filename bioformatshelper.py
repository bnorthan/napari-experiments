#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:22:33 2021

@author: bnorthan
"""

import javabridge
import bioformats
import numpy as np

def startjvm():
    javabridge.start_vm(class_path=bioformats.JARS)

def killjvm():
    javabridge.kill_vm()
    
def loadChannel(filename, nz,c):    
    
    img=bioformats.load_image(filename, z=0,c=c,rescale=False)
    img=img[np.newaxis,...]
    
    for cz in range(1,nz):
        temp=bioformats.load_image(filename, z=cz, c=c, rescale=False)
        img=np.vstack((img, temp[np.newaxis,...]))
        
    return img