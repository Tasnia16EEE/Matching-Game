import random
import os
import config as gc

from pygame import image, transform

university_count = dict((a, 0) for a in gc.ASSET_FILES)
print(university_count)

def available_university():
    return [university for university, count in university_count.items() if count < 2]

class University:
    def __init__(self, index):
        self.index = index
        self.name = random.choice(available_university())
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.skip = False
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))

        university_count[self.name] += 1
