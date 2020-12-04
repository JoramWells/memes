from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse

import io  
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize

from .modules import *
#from .forms import QuoteForm

from json import dumps


queryset = PostQ.objects.all()

def LikeView(request):
    post=get_object_or_404(PostQ, id=request.POST.get('post_id'))
    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('index'))
    
def index_view(request):
    stop_words = set(stopwords.words('english'))  
    posts = PostQ.objects.all()
    body = read_data('data.csv')
    
    
    bodyStr = body.to_string()
    text = bodyStr.split()
    filtered_search = [] 
    
    for r in text:
        if r not in stop_words:
            filtered_search.append(r)
             
            dataJson = dumps(filtered_search)
            context = {
            'posts':posts,
            'body':dataJson
            }
    return render(request,'base.html', context)

class QuoteView(ListView):
    model = PostQ
    template_name= 'base.html'
    #paginate_by=3
    
class MemeView(DetailView):
    model = PostQ
    template_name= 'index.html'
    
    def get_context_data(self,*args,**kwargs):
        context=super(MemeView,self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(Post,self.kwargs['pk'])
        total=stuff.total_likes()
        context=total
        return context
    


def query_to_csv(queryset, filename='items.csv', **override):
    field_names = [field.name for field in queryset.model._meta.fields]
    def field_value(row, field_name):
        if field_name in override.keys():
            return override[field_name]
        else:
            return row[field_name]
    with open(filename, 'w+', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerow(field_names) 
        for row in queryset.values(*field_names):
            writer.writerow([field_value(row, field) for field in field_names])


query_to_csv(queryset, filename='data.csv', user=1, group=1)


def add_meme(request):
    if request.method == 'POST':
        if request.POST.get('meme'):
            meme = PostQ()
            meme.body = request.POST.get('meme')
            meme.category = request.POST.get('name')
            meme.save()
    return render(request,'index.html' )
            


def display(request):
    if request.method == 'POST':
        if request.POST.get('keyword'):#if request.POST.get('keyword') and request.POST.get('videos'):
            post=Post()
            post.keyword = request.POST.get('keyword')
            post.min_videos = 10 #request.POST.get('videos')
            post.save()
            q= Post.objects.all().order_by('-created_on')[:1]
            
            query_to_csv(q, filename='serchin.csv', user=1, group=1)
            d = read_data('serchin.csv')
            key = d['keyword']
            key = key[0]
            url = d['min_videos']
            url =url[0]
            sl = SearchView( key,url)
            s2 = sl.postl()
            
            if len(s2) == 0:
                return HttpResponseRedirect('')
            url=[]
            for i in s2:
                c=PostQ.objects.get(id=i)
                url.append(c)
                context={
                    'url':url
                    }
                
            return render(request,'base.html',context)
    else:
        return render(request,'base.html')
    
"""class AddQuoteView(CreateView):
    model=PostQ
    template_name='upload.html'
    form_class = QuoteForm
    ##fields='__all__'
    """
    

    