#! /usr/bin/python
from concurrent.futures import ThreadPoolExecutor
from image_processor import ImageProcessor
from song_mappings import choose_song
from imutils.video import FPS
from song import Song
import imutils
import time
import cv2
from time import sleep

def main():
	processor = ImageProcessor()
	song = Song('')
	thread_executor = ThreadPoolExecutor(max_workers=10)

	vs = cv2.VideoCapture(0)
	time.sleep(2.0)

	fps = FPS().start()
	count = 0
	
	while True:
		_, frame = vs.read()
		frame = imutils.resize(frame, width=500)


		cv2.imshow("Pao-er Bass", frame)
		

		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break
		if key == ord("s"):
			song.stop()
		
		count += 1
		fps.update()

		if(not song.is_playing()):
			processor.process_image(frame)

			is_new_song: bool = choose_song(song, processor)
			if is_new_song:
				song.play()

	fps.stop()
	print("Elasped time: {:.2f}".format(fps.elapsed()))
	print("FPS: {:.2f}".format(fps.fps()))

	thread_executor.shutdown()
	vs.release()
	cv2.destroyAllWindows()
#end main

if __name__ == '__main__':
    main()