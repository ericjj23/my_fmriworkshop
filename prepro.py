#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:54:01 2017

@author: fsluser
"""

import glob
import os
import shutil
import pdb
import pandas
import argparse
  

def prepro(basedir):
    print('thing thing thing '+basedir)
def main():
    basedir='/home/fsluser/Desktop/ds000030_R1.0.5'
    prepro(basedir)    
main()

os.system('bet' input x output -F')
%we have to do pass a variable as a string
use %s
os.system('bet %s %s -F'%(x, output))
percent fills sequentially
also can do %i and %f 
print(os.system('echo $FSLDIR'))
input=glob.glob('/home/fsluser/Desktop/ds000030_R1.0.5/sub-*bart-*/func/sub-*.nii.gz')
print(input[0:10])
len(input)
input[-1]
x=input[0]
print(my path is'+x)

y=x.split('/')
print(y)
sub=y[5]
print(sub)

%nicer version
sub=input('/')[5]
print(sub)
%input was defined by glob
%same in matlab

%now split on the dot

subtask=input[1].split('/')[7].split('.')[0]
print(subtask)
output=subtask+'_brain'
print(output)
