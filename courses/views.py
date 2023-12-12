from django.shortcuts import render, redirect

# Create your views here.
from courses.forms import TopicForm, EpisodeForm
from courses.models import Topic, Episode


def index(request):
    topics = Topic.objects.all()
    episodes = Episode.objects.all()
    context = {'topics':topics, 'episodes':episodes}
    return render(request, 'index.html', context)

def showEpisodes(request, episodeid):
    episodes = Episode.objects.get(TopicID=episodeid)
    topic = Topic.objects.get(id=episodes.TopicID)
    context = {'episodes':episodes, 'topic':topic}
    return render(request, "Show_Episodes.html", context)


def createTopic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {'form':form}
    return render(request,"Topic_create.html",context)

def createEpisode(request, topicid):
    topic = Topic.objects.get(id=topicid)
    if request.method != "POST":
        form = EpisodeForm()
    else:
        form = EpisodeForm(request.POST, request.FILES)
        if form.is_valid():
            new_episode = form.save(commit=False)
            new_episode.TopicID = topic
            new_episode.save()
            return redirect('index')
    context = {'form':form, 'topic':topic}
    return render(request, 'Episode_create.html', context)