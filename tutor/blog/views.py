from django.shortcuts import render

from django.http import HttpResponse

def index(request):
      context = {
      'Judul' : 'blog1',
      'h1' : 'Django',
      'menu' : [['/blog','Home'],['/blog/recent','Recent'],['/blog/post','Post']]
      }
      return render(request, 'blog/index.html', context)

def recent(request):
      # context = {
      # 'Judul' : 'blog2',
      # 'h1' : 'Python'
      # }
      return HttpResponse("RECENT BLOG")

def post(request):
      return HttpResponse("POST BLOG")

