from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    usertext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    purpose = ""
    msg = ""
    djtext = usertext

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed += i
        djtext = analyzed
        purpose += "-> Removed Punctuations"

    if fullcaps == 'on':
        analyzed = djtext.upper()
        djtext = analyzed
        purpose += "-> Capitalized all"

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        djtext = analyzed
        purpose += "-> Removed new line"

    if extraspaceremover == 'on':
        analyzed = ""
        for index1 in range(len(djtext)):
            if not(djtext[index1] == ' ' and djtext[index1 + 1] == ' '):
                analyzed += djtext[index1]
        djtext = analyzed
        purpose += "-> Removed extra space"

    if charcount == 'on':
        totalchars = len(djtext)
        msg = "Total characters: " + str(totalchars)
        purpose += '-> Counted total characters'

    if removepunc == 'on' or fullcaps == 'on' or newlineremover == 'on' or extraspaceremover == 'on' or charcount == 'on':
        params = {'purpose': purpose, 'analyzed_text': djtext , 'charscount':msg}
        return render(request, 'analyze.html', params)
    else:
        params = {"msg": "error"}
        return render(request, 'index.html',params)
    

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
