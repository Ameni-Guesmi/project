from django.shortcuts import render
import openai

# Create your views here.
key="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"

openai.api_key = key

def index1(request):
    return render(request, 'index1.html')

def answer(request):
    question = request.POST.get('question')
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= question,
        temperature=0.9,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
    
    text = response['choices'][0]['text']
    responses={
        'answer':text,
    }
    
    return render(request, 'answer.html', responses)
