from django.shortcuts import render, redirect
from .forms import MessageForm
from django.views.generic import ListView, CreateView
from .models import Chat, Activity
from django.urls import reverse_lazy

import cohere
from cohere.classify import Example

dominant_emotions = {'anger': 0, 'joy': 0, 'fear': 0, 'disgust': 0, 'guilt': 0, 'sadness':0, 'shame': 0}

class HomeView(CreateView, ListView):
    model = Chat
    fields = ('message', )
    template_name = 'index.html'
    success_url = reverse_lazy('home')
    date = Chat.date_created
    
    def form_valid(self, form):
        response = super(HomeView, self).form_valid(form)
        message = str(form.cleaned_data['message'])
        
        if message.lower() == "exit":
            response = redirect('activity')
            return response
        elif message.lower() == 'hi':
            text = "Hi, I am Moodify, your chatbot to track your mood, record your thought and feeling and accompany you on your mental health journey. \nSo, to get started, can you tell me about your day today?"
        else:
            co = cohere.Client('C6eSlg13MZxqKmUzMXDScQThfggUioOvIVOICV0x') #This is your trial API key
            reply = co.classify(
            model='f934e8b3-ae62-4a1b-815e-900cb99e7e10-ft',
            inputs= [message])

            prediction = reply.classifications[0].prediction
            confidence = reply.classifications[0].confidence
            
           
            
            if (confidence >= 0.5):
                if (prediction == 'anger'):
                    text = "I can't believe that's what happened! You totally have every rights to feel that way. However, before you say something that you regret, shall we just go and get a drink or maybe a breath of fresh air?"
                    dominant_emotions['anger'] += 1
                elif (prediction == 'joy'):
                    text = "Awww I am so happy for you! Please tell me more about it!"
                    dominant_emotions['joy'] += 1
                elif prediction == 'fear':
                    text = "Life can be stressful sometimes, and it's ok to feel anxious about it. Instead, would it help we did something together? Type exit for \"yes\""
                    dominant_emotions['fear'] += 1
                elif (prediction == 'disgust'):
                    text = "We understand why you might feel that way. However, before you say something that you regret, shall we just go and get a drink or maybe a breath of fresh air? Type exit for \"yes\""
                    dominant_emotions['disgust'] += 1
                elif (prediction == 'guilt'):
                    text="We understand how you must feel right now. However, remember no one, maybe even you, will remember whatever happened or going to happen in many many years. Instead, let's take a deep breath and walk me through your story, shall we?"
                    dominant_emotions['guilt'] += 1
                elif (prediction == 'sadness'):
                    dominant_emotions['sadness'] += 1
                    text="We are so sorry for what happened. Do you wish to tell us more about it?"
                elif (prediction == 'shame'):
                    dominant_emotions['shame'] += 1
                    text="We understand why you might feel that way. Let's take a deep breath and walk me through your story, shall we? Type exit for \"yes\""
            else:
                if (prediction != 'joy'):
                    text = "It's ok to feel that way, life truly sucks sometimes! I am always here for you, so do you want to elaborate on what you just said?"
                else:
                    text = "Tell me more about it!!"
        
        reply = Chat(user='B', message=text)
        reply.save()
        return response    

class ActivityView(ListView):
    model = Activity
    template_name = 'activities.html'
    
class ActivityAdd(CreateView):
    model = Activity
    fields = ('title', 'description',)
    template_name='add.html'
    success_url = reverse_lazy('activity')

def summary(response):
    mood = max(dominant_emotions, key=dominant_emotions.get)
    return render(response, 'summary.html', {'mood': mood})
     