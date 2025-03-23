from moviepy.video.io.VideoFileClip import VideoFileClip

def trim_video(input_path, output_path, start_time, end_time):
    try:
        # Load the video
        clip = VideoFileClip(input_path)

        # Trim the video
        trimmed_clip =clip.subclipped(start_time, end_time)

        # Save the trimmed video
        trimmed_clip.write_videofile(output_path, codec="libx264", fps=clip.fps)

        print(f"Trimmed video saved as: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example Usage
input_video = "full_video.mp4"
output_video = "trimmed_output.mp4"
start = 10  # Start time in seconds
end = 30    # End time in seconds
n=int(input("enter how many parts "))
for i in range(0,n):
    start=int(input("enter start time"))
    end = int(input("enter end time"))
    output_video =(input("enter name of output video"))
    trim_video(input_video, output_video, start, end)
