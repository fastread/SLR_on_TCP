from __future__ import print_function, division
import pandas as pd
import numpy as np
from os import listdir
from pdb import set_trace

from demos import cmd



def find_number():
    prior = pd.read_csv('../search/prior.csv')
    zhe = pd.read_csv('../screen/test_prior_90.csv')
    zhe_yes = set(zhe['PDF Link'][np.where(np.array(zhe['code']) == "yes")[0]])
    zhe_no = set(zhe['PDF Link'][np.where(np.array(zhe['code']) == "no")[0]])
    zhe_unlabel = set(zhe['PDF Link'][np.where(np.array(zhe['code']) == "unlabel")[0]])
    print(len(zhe_yes & set(prior['PDF Link'])))
    print(len(zhe_no & set(prior['PDF Link'])))

def collect_result(path="./result/"):
    files = listdir(path)
    keys = ["ID",	"Document Title", "Abstract",	"Year",	"PDF Link",	"code"]
    all = {}
    for file in files:
        result = pd.read_csv(path+file)
        for i in xrange(len(result)):
            if result['ID'][i] in all:
                if result['code'][i]!=all[result['ID'][i]]['code']:
                    all[result['ID'][i]]['code'] = "inconsistent"
            else:
                all[result['ID'][i]] = {}
                for key in keys:
                    all[result['ID'][i]][key] = result[key][i]
    df = pd.DataFrame(data=all.values(),columns=keys)
    df.to_csv("./inconsistent.csv",index=False)

def doublecheck():
    result = pd.read_csv("./inconsistent.csv")
    double = pd.read_csv("./doublecheck_FF.csv")
    for i in xrange(len(double)):
        j = result["ID"].tolist().index(double["ID"][i])
        result["code"][j]=double['code'][i]
    result.to_csv("./final.csv",index=False)

def validate():
    zhe = pd.read_csv('../screen/test_prior_90.csv')
    final = pd.read_csv("./final.csv")
    FN=0
    FP=0
    TP=0
    TN=0
    hidden=0
    miss=0
    stat = []
    final2=final.copy()
    for i in xrange(len(final)):
        try:
            j = zhe['PDF Link'].tolist().index(final['PDF Link'][i])
        except:
            miss+=1
            stat.append("miss")
            final2['code'][i]='undetermined'
            continue
        final2['code'][i] = zhe['code'][j]
        if final['code'][i]=="yes":
            if zhe['code'][j]=="yes":
                TP+=1
                stat.append("TP")
            elif zhe['code'][j]=="no":
                FN+=1
                stat.append("FN")
            else:
                hidden+=1
                stat.append("hidden")
        else:
            if zhe['code'][j]=="yes":
                FP+=1
                stat.append("FP")
            elif zhe['code'][j]=="no":
                TN+=1
                stat.append("TN")
            else:
                stat.append("ignore")
    final['status'] = pd.Series(stat, index=final.index)
    final.to_csv("./validate_90.csv", index=False)
    final2.to_csv("./whatif_90.csv", index=False)
    print("TP: " + str(TP))
    print("TN: " + str(TN))
    print("FP: " + str(FP))
    print("FN: " + str(FN))
    print("hidden: " + str(hidden))
    set_trace()


def all_in():
    zhe = pd.read_csv('../screen/test_prior_90.csv')
    validate = pd.read_csv("./validate_noheader.csv")
    FF = pd.read_csv("./doublecheck_FF.csv")
    for i,id in enumerate(FF['ID']):
        validate['FF'][id] = FF['code'][i]

    pdf = zhe['PDF Link'].tolist()


    for i in xrange(len(validate)):
        try:
            j = pdf.index(validate['PDF Link'][i])
        except:
            validate['ZY'][i]='undetermined'
            continue
        validate['ZY'][i] = zhe['code'][j]
    for i, full in enumerate(validate['Full text validation (ZY=yes or Majority Vote=yes)']):
        if pd.isnull(full):
            validate['label'][i] = validate['Majority Vote'][i]
            if validate['Majority Vote'][i] == 'yes' or validate['ZY'][i] == 'yes':
                validate['Full text validation (ZY=yes or Majority Vote=yes)'][i] = 'yes'
    set_trace()
    validate.to_csv("./validate_noheader.csv", index=False)

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