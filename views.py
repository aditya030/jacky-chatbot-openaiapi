from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import openai

openai.api_key = "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"

def chat(request):
    return render(request, "index.html")

def chatAPI(request):
    if request.method == "POST":
        prompt = request.POST.get('prompt')
        if not prompt:
            return HttpResponseBadRequest("Prompt cannot be empty.")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return JsonResponse(response.choices[0].text, safe=False)

    return HttpResponseBadRequest("Invalid request method.")
