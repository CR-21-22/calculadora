# calculadora

![](calculadoraView.png)

Esta aplicação mostra como se implementa uma página que recolhe informação num formulário, faz seu processamento no back-end, e retorna um resultado associado.

Passos: 
1. Cria-se um [template](https://github.com/CR-21-22/calculadora/blob/main/calculadora/templates/calculadora/index.html) com um formulário `<form>` com input de texto, para recolher uma expressão matemática. 
2. Em [views.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/views.py), cria-se index_view que que renderiza o template. Caso seja submetido o formulário via mensagem HTTP post, extrai a expressão enviada e avalia o resultado. Retorna no contexto a expressão e o resultado.
3. O template [apresentará]([https://github.com/CR-21-22/calculadora/blob/main/calculadora/templates/calculadora/index.html#L17) a expressao matemática e seu resultado, caso existam.

https://user-images.githubusercontent.com/42048382/143500089-452e00d1-d95a-47e4-baac-cf1851796bf1.mp4

