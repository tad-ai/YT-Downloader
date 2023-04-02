from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import subprocess
import pytube

download_loc='./'

@csrf_exempt
def home(request):
    if request.method=="POST":
        input_text=request.POST['input_link']
        #output=subprocess.check_output(['python','process_text.py',input_text]).decode('utf-8')
        output=process_text(input_text)
        return render(request, 'index.html', {'output': output})
    else:
        return render(request, 'index.html')
    
def process_text(video_url):
    input_text="Downloaded"

    #video_instance=pytube.YouTube(video_url)
    #stream=video_instance.streams.get_highest_resolution()
    #stream.download()

    return input_text.upper()
