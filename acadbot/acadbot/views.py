from django.shortcuts import render
from django import forms
import requests
import pickle
import pandas as pd
from django.http import JsonResponse
import numpy as np
import glob


def home(request):
    return render(request,'index.html')




def output(request):

    if request.method=='POST':
        string=request.POST['query']
        pair=pickle.load(open('model.obj','rb'))
        model=pair[0]
        cvec=pair[1]
        test=cvec.transform([string])
        cat=model.predict(test).astype('int')[0]
        modelpath='model'+str(cat)
        model2,cvec2=pickle.load(open(modelpath,'rb'))
        X=cvec2.transform([string])
        cat2=model2.predict(X).astype(int)[0]
        filepath=glob.glob(glob.glob('data/*')[cat]+'/*')[cat2]
        
        with open(filepath, 'rb') as f:
            lines = [l.decode('utf8', 'ignore') for l in f.readlines()]
            out=' '.join(lines)

    return render(request,'index.html',{'out':out,'inp':string})
