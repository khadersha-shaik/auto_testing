import pandas as pd
from moviepy.video.io.VideoFileClip import VideoFileClip

def trim_video(input_path, output_path, start_time, end_time):
    try:
        # Load the video
        clip = VideoFileClip(input_path)

        # Trim the video
        trimmed_clip = clip.subclipped(start_time, end_time)

        # Save the trimmed video
        trimmed_clip.write_videofile(output_path, codec="libx264", fps=clip.fps)

        print(f"Trimmed video saved as: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
# Load trimming details from Excel
    excel_file = "trim_info.xlsx"
    df = pd.read_excel(excel_file)

# Path to the input video
    input_video = "full_video.mp4"

# Iterate through each row in the Excel sheet
    for index, row in df.iterrows():
        start = row["Start Time (sec)"]
        end = row["End Time (sec)"]
        output_video = row["Output Filename"]
        print(input_video, output_video, start, end)
    
    # Trim the video based on the values from the Excel sheet
        trim_video(input_video, output_video, start, end)
