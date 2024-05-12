from django.shortcuts import render
import os
import openai


# Create your views here.
def get_image_url(prompt):
    key = os.environ['OPENAI_API_KEY']
    
    openai.api_key = key
    openai.Model = "dall-e-2"

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']

    return image_url


def home(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        image_url = get_image_url(prompt)

        if image_url:
            return render(request, 'index.html', {
                'image_url': image_url,
                'image_description': prompt,
            })
        else:
            return render(request, 'index.html', {
                'image_url': 'An error occured. Please try again.',
            })
    return render(request, 'index.html')