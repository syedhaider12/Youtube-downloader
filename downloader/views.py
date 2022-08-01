
from django.shortcuts import redirect, render
from pytube import YouTube





def main(request):
    if request.method == 'POST':
        link = request.POST.get('videourl')
        ta=YouTube(link)
        
        
        return render(request , 'home.html', {'ta': ta})
    else:
        return render(request, 'home.html')

def haider(request,id):
    if request.method == 'POST':
        #if request.POST['audio']:
        value = request.POST.get('audi')
        urll  = f'https://www.youtube.com/watch?v={id}'
        print(value)
        if value == '1':
            print('shah jee')
            
            yt=YouTube(urll)
           
            yt.streams.filter(progressive=True)
            stream = yt.streams.get_by_itag(18)
            stream.download("C:\AERO\Downloads\Video")
            print("downlaod")
        elif value == 2:
            yt=YouTube(urll)
            yt = YouTube(id)
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.get_by_itag(137)
            stream.download()
        elif value == '3':
            yt=YouTube(urll)
            yt = YouTube(id)
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.filter(only_audio=True).first()
            stream.download()
           
        else:
            pass
    return render(request,'home.html')


    

