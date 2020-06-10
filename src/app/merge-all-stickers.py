import cv2
from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter
import numpy as np
from os import listdir
from os.path import isfile, join