#! /usr/bin/python
from concurrent.futures import ThreadPoolExecutor
from image_processor import ImageProcessor
from song_mappings import choose_song
from imutils.video import FPS
from song import Song
import imutils
import time
import cv2

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

		# if(count % 30 == 0):
		# 	Thread(target=image_processing, args=(frame,), daemon=True).start()

		cv2.imshow("Pao-er Bass", frame)
		
		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break
		if key == ord("a"):
			thread_executor.submit(worker, processor, song, frame)
		if key == ord("s"):
			song.stop()
		
		count += 1
		fps.update()

	fps.stop()
	print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
	print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

	thread_executor.shutdown()
	vs.release()
	cv2.destroyAllWindows()
#end main

def worker(processer: ImageProcessor, song: Song, frame) -> None:
	processer.process_image(frame)

	is_new_song: bool = choose_song(song, processer)

	if is_new_song:
		song.play()
#end worker

if __name__ == '__main__':
    main()