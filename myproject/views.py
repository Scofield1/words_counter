from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)

def counter(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        word = len(text.split())
        char = len("".join(text))
    context = {"word": word, "char": char, 'text': text}
    return render(request, 'counter.html', context)