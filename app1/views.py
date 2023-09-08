from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista1(recuest):
    html="""
    <h1>Vista uno</h1>
    """
    return HttpResponse(html)