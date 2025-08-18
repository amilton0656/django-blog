from django.shortcuts import render
from contato.contato_form import FormContato

def contato(request):
    return render(request, 'contato/contato.html', {'form': FormContato()})

def processa_contato(request):
    if request.method == 'post':
        contato = FormContato(request.POST)
        if contato.is_valid():
            assunto = contato.cleaned_data['assunto']
            return render(request, 'contato/contato.html', {'form': contato})
        else:
            return render(request, 'contato/contato.html', {'form': contato}) 
    return render(request, 'contato/contato.html', {'form': FormContato()})


