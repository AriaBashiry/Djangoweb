from django.urls import path

from courses import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('createtopic/', views.createTopic, name="createTopicUrl"),
    path('createepisode/<int:topicid>', views.createEpisode, name="createEpisodeUrl"),
    path('showepisodes/<int:episodeid>', views.showEpisodes, name="showEpisodesUrl"),

]