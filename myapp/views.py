from django.shortcuts import render, HttpResponse, redirect # 
from django.views.decorators.csrf import csrf_exempt # csrf 스킵을 위한 import
import random


# Create your views here.
nextId = 4
topics = [ # 리스트 
{'id':1, 'title':'routing','body':'Routing is ..'}, # 딕셔너리
{'id':2, 'title':'view','body':'View is ..'}, # 딕셔너리
{'id':3, 'title':'model','body':'Model is ..'}, # 딕셔너리
]

def HTMLTemplate(articleTag, id=None):
    global topics # 전역변수 선언 global
    contextUI = '' 
    if id != None:
        contextUI= f'''
            <li>
                <form action = "/delete/" method ="post">
                    <input type="hidden" name="id" value="{id}">
                    <input type="submit" value="delete">
                </form>
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''
    ol=''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>' # '' 앞에 f를 붙이면 {} 내부에 변수를 추가해서 넣을 수 있다. 아래처럼 '''도 가능함  
    return f''' 
    <html>
    <body>
        <h1><a href='/'>Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''


def index(req):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(req, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(req):
    # print('request.method', req.method)
    global nextId
    if req.method =='GET':
        article = '''
            <form actuib="/create/" method="post">
                <p><input type = "text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif req.method =='POST':
        title = req.POST['title']
        body = req.POST['body']
        newTopic = {"id":nextId, "title":title , "body":body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId = nextId + 1
        return redirect(url)

@csrf_exempt
def delete(req):
    global topics 
    if req.method=='POST':
        id = req.POST['id']
        newTopics = []
        for topic in topics: 
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics      
        return redirect('/')
        
@csrf_exempt
def update(req,id):
    global topics
    
    if req.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                }
        article = f'''
        <form actuib="/update/{id}/" method="post">
            <p><input type = "text" name="title" placeholder="title" value="{selectedTopic['title']}"></p>
            <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article,id))
    elif req.method == 'POST':
        title = req.POST['title']
        body = req.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')



    