from django.shortcuts import render, redirect
from django.http import HttpResponse
import torch
from diffusers import CogVideoXPipeline
from diffusers.utils import export_to_video
import os


def home(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        second=request.POST.get("numberInput")
        print(f"Prompt: {prompt}\nTime:{second}")
        func(prompt,second)
        return redirect("second_page")

    return render(request, "myapp/index.html")


def secondpage(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        second=request.POST.get("numberInput")
        print(f"Prompt: {prompt}")
        func(prompt,second)
        return redirect("second_page")

    return render(request, "myapp/second.html")

def func(prompt,second):
    second=int(second)
    print(type(second))
    frames=second*8
    if os.path.exists(r"C:\Users\kende\OneDrive\Desktop\MiniProject\Text-To-Video\myapp\static\videos\output.mp4"):
        os.remove(r"C:\Users\kende\OneDrive\Desktop\MiniProject\Text-To-Video\myapp\static\videos\output.mp4")
    pipe = CogVideoXPipeline.from_pretrained("THUDM/CogVideoX-2b",torch_dtype=torch.float16)

    pipe.enable_model_cpu_offload()
    pipe.enable_sequential_cpu_offload()
    pipe.vae.enable_slicing()
    pipe.vae.enable_tiling()

    # Number of frames to generate in chunks (e.g., 49 frames per chunk)
    frames_per_chunk = 49
    # Total number of frames you want to generate
    total_frames = int(frames)

    # List to store all generated frames
    all_frames = []
    
    # Generating frames in chunks
    for i in range(total_frames // frames_per_chunk):
        video_chunk = pipe(
            prompt=prompt,
            num_videos_per_prompt=1,
            num_inference_steps=50,
            num_frames=frames_per_chunk,  # Fixed frames per chunk
            guidance_scale=6,
            generator=torch.Generator(device="cuda").manual_seed(42 + i),  # Changing seed for each chunk
        ).frames[0]

        all_frames.extend(video_chunk)

    # Generate any remaining frames
    remaining_frames = total_frames % frames_per_chunk
    if remaining_frames > 0:
        print("hlo")
        video_chunk = pipe(
            prompt=prompt,
            num_videos_per_prompt=1,
            num_inference_steps=50,
            num_frames=remaining_frames,  # Generate the remaining frames
            guidance_scale=6,
            generator=torch.Generator(device="cuda").manual_seed(42 + (total_frames // frames_per_chunk)),  # New seed for remaining frames
        ).frames[0]

        all_frames.extend(video_chunk)

    # Export all frames to a video
    export_to_video(all_frames, "output.mp4", fps=8)

    os.rename(os.getcwd()+'\\output.mp4',r"C:\Users\kende\OneDrive\Desktop\MiniProject\Text-To-Video\myapp\static\videos\output.mp4")
