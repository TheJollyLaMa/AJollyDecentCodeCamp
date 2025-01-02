"""This simple python program uses moviepy to cut a video into parts."""

from moviepy.video.io.VideoFileClip import VideoFileClip

def split_video_into_clips(input_path, output_dir, clip_duration):
    """
    Splits a video into clips of specified duration.
    
    Args:
        input_path (str): Path to the input video file.
        output_dir (str): Directory to save the clips.
        clip_duration (int): Duration of each clip in seconds.
    """
    # Load the video file
    video = VideoFileClip(input_path)
    video_duration = int(video.duration)  # Total duration of the video in seconds

    # Loop to create clips
    for start_time in range(0, video_duration, clip_duration):
        end_time = min(start_time + clip_duration, video_duration)
        clip = video.subclipped(start_time, end_time)
        output_path = f"{output_dir}/clip_{start_time}-{end_time}.mp4"
        clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Created clip: {output_path}")

    print("Video splitting complete!")
# video = VideoFileClip("/Users/J/Desktop/BlenderBender/DecentAdverts/DecentAdvert_Coder_reencoded.mp4")

# Usage
input_video_path = "/Users/J/Desktop/BlenderBender/DecentAdverts/DecentAdvert_Coder_reencoded.mp4" #input("Enter the path to the input video file: ")
output_directory = "/Users/J/Desktop/BlenderBender/DecentAdverts" #input("Enter the path to the output directory: ")
clip_duration = 10 #input("Enter the duration of each clip in seconds: ")
split_video_into_clips(input_video_path, output_directory, clip_duration=int(clip_duration))