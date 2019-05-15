# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('Hello world')
    return render(request,'home.html')

def count(request):
    user_text=request.GET['text']
    count_len=len(user_text)
    word_dict={}
    for word in user_text:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    items=word_dict.items()
    sorted_count=sorted(items,key=lambda x:x[1],reverse=True)
    return render(request,'count.html',{'user_text':user_text,'count_len':count_len,'dict':word_dict,'item':items,'sort':sorted_count})


def about(request):
    # return HttpResponse('Hello world')
    return render(request,'about.html')