from django.shortcuts import render

def index(request):

    resultado = expressao = None

    if request.POST:
            expressao = request.POST['expressao'] 
            try:
                resultado = eval(expressao)
            except:
                resultado = "expressão inválida"
    
    context = {
        'resultado': resultado,
        'expressao': expressao
    }
    return render(request, 'calculadora/index.html', context)
