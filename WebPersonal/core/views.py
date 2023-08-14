from django.shortcuts import render, HttpResponse 

html_base = """
    <h1>Mi web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about">Acerca de...</a></li>
        <li><a href="/contact">Contacto del Grupo</a></li>
        <li><a href="/cat">Catalago</a></li>
        <li><a href="/tend">Tendencia del momento</a></li>

    </ul>
        
"""
# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html") 

def contact(request):
    return render(request, "core/contact.html")

# def cata(request):
#     return render(request, "core/cata.html")

#def tend(request):
 #   return render(request, "core/tend.html")