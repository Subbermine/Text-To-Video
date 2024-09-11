from django.shortcuts import render,redirect

def mypage(request):
    return render(request,'myapp/index.html')

def process_form_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')

        video_url = 'videos/spm.mp4'

        print(f"Prompt: {prompt}")
        return render(request, 'video_display.html', {'video_url': video_url})


    return redirect('mypage')
