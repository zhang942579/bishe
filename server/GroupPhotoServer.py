
import numpy as np
from torch.utils.data import Dataset
from PIL import Image
import cv2


class VideoReader(Dataset):
    def __init__(self, video, transform=None):

        self.img = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
        self.transform = transform

    def __len__(self):
        return 1

    def __getitem__(self, idx):

        frame = Image.fromarray(np.asarray(self.img))
        if self.transform is not None:
            frame = self.transform(frame)
        return frame