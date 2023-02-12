from imutils import paths
from pathlib import Path
import face_recognition
import pickle
import cv2
import sys
import os

def main():
	imagePaths = list(paths.list_images("dataset"))

	knownEncodings = []
	knownNames = []

	for (i, imagePath) in enumerate(imagePaths):
		sys.stdout.write(f'\rProcessing image {i + 1}/{len(imagePaths)}')
		sys.stdout.flush()

		name = imagePath.split(os.path.sep)[-2]

		image = cv2.imread(imagePath)
		rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		face_locations = face_recognition.face_locations(rgb_image,
			model="hog")

		encodings = face_recognition.face_encodings(rgb_image, face_locations)

		for encoding in encodings:
			knownEncodings.append(encoding)
			knownNames.append(name)

	print("\n\rSerializing encodings...")
	data = {"encodings": knownEncodings, "names": knownNames}

	path = Path(__file__).parent.joinpath('data-model')

	if(not path.exists()):
		path.mkdir(0, True)

	f = open("data-model\\encodings.pickle", "wb")
	f.write(pickle.dumps(data))
	f.close()

	print("\nComplete :D")

if __name__ == '__main__':
	main()