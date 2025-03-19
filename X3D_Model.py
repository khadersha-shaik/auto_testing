import torch
import torchvision.transforms as transforms
from pytorchvideo.data.encoded_video import EncodedVideo
model = x3d_m(pretrained=True)
model.eval()

def preprocess_video(video_path):
    video = EncodedVideo.from_path(video_path)
    start_time = 0  # Start time in seconds
    end_time = 2  # Extract the first 2 seconds
    video_data = video.get_clip(start_time, end_time)

    # Remove ToTensor() since video_data["video"] is already a tensor
    transform = transforms.Compose([
        transforms.Resize((182, 182)),  # Resize to expected input size
        transforms.CenterCrop(160),  # Crop center
    ])

    frames = transform(video_data["video"])  # Already a tensor, no need for ToTensor()
    return frames.unsqueeze(0)  # Add batch dimension

# Load and preprocess video
video_tensor = preprocess_video("video.mp4")
print(video_tensor.shape)  # Debugging output

with torch.no_grad():
    predictions = model(video_tensor)
