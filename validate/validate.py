from __future__ import print_function, division
import pandas as pd
import numpy as np
from os import listdir
from pdb import set_trace

from demos import cmd



def confusion(validate, a , b):
    TP = len(validate[(validate[a] == 'yes') & (validate[b] =='yes')])
    TN = len(validate[(validate[a] != 'yes') & (validate[b] =='no')])
    NN = len(validate[(validate[a] == 'no') & (validate[b] =='no')])
    FP = len(validate[(validate[a] == 'yes') & (validate[b] =='no')])
    FN = len(validate[(validate[a] != 'yes') & (validate[b] =='yes')])
    NP = len(validate[(validate[a] == 'no') & (validate[b] =='yes')])
    print(a+" vs "+b)
    print("TP: " + str(TP))
    print("TN: " + str(TN))
    print("NN: " + str(NN))
    print("FP: " + str(FP))
    print("FN: " + str(FN))
    print("NP: " + str(NP))
    print("Precision: " + str(TP/(TP+FP)))
    print("Recall: " + str(TP/(TP+FN)))


def all_number():
    validate = pd.read_csv("./validate_noheader.csv")
    val_yes = len(validate[(validate['Full text validation (ZY=yes or Majority Vote=yes)'] == 'yes')])
    val_all = len(validate[(validate['Full text validation (ZY=yes or Majority Vote=yes)'] == 'yes') | (validate['Full text validation (ZY=yes or Majority Vote=yes)'] =='no')])


    confusion(validate,'ZY','Majority Vote')
    confusion(validate,'ZY','label')
    confusion(validate,'Majority Vote','label')
    set_trace()

if __name__ == "__main__":
    eval(cmd())