from image_processor import ImageProcessor
from key_mapping import key_map
import pygame.mixer as mixer
import imutils
import cv2

def main():
	processor = ImageProcessor()
	mixer.init()

	vs = cv2.VideoCapture(0)

	running: bool = True
	searching: bool = True
	
	while running:
		_, frame = vs.read()
		frame = imutils.resize(frame, width=500)

		cv2.imshow("Pao-er Bass", frame)
		
		key: chr = chr(cv2.waitKey(1) & 0xFF)

		if(not key == 'ÿ'):
			running, searching = key_map[key]()

		busy: bool = mixer.music.get_busy()

		if(searching and not busy):
			processor.process_image(frame)
			(is_new_song, new_song) = processor.choose_song()

			if(is_new_song):
				mixer.music.load(new_song)
				mixer.music.play()
				

	vs.release()
	cv2.destroyAllWindows()
#end main

if __name__ == '__main__':
    main()