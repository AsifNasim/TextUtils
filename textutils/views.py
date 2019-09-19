from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def index(Request):
    return render(Request,'index.html')




def analyze(Request):
    #Get the text
    djtext = Request.POST.get('text', 'default')

    # Check checkbox values
    removePunc = Request.POST.get('removePunc', 'off')
    fullcaps = Request.POST.get('fullcaps', 'off')
    newLineRemover = Request.POST.get('newLineRemover', 'off')
    extraSpaceRemover = Request.POST.get('extraSpaceRemover', 'off')
    characterCount = Request.POST.get('characterCounter', 'off')
    #Check which checkbox is on
    if removePunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':' Punctuations Removed ', 'analyzed_text': analyzed}
        djtext = analyzed


    if(fullcaps == "on"):
        analyzed =""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose':' Converted String to Upper Case ', 'analyzed_text': analyzed}
        djtext = analyzed


    if(extraSpaceRemover == "on"):
        analyzed =""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index +1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':' Extra Spaces have been removed ', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newLineRemover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose':' New Line has been removed  ', 'analyzed_text': analyzed}
    if(removePunc != "on" and fullcaps != "on" and extraSpaceRemover != "on" and newLineRemover != "on"):
            return HttpResponse("Please Choose any operations!")


    return render(Request, 'analyze.html', params)
