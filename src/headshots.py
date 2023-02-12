from pathlib import Path
import cv2

def main():
    path = choose_name()

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("press space to take a photo", 500, 300)

    img_counter = 0

    while True:
        ret, frame = cam.read()

        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow("press space to take a photo", frame)

        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = f"{path}\\image_{img_counter}.jpg"
            print(img_name)
            cv2.imwrite(img_name, frame)
            print(f"{img_name} written!")
            img_counter += 1
        elif k%256 == 110:
            # n pressed
            path = choose_name()
            img_counter = 0

    cam.release()

    cv2.destroyAllWindows()
#end main

def choose_name() -> Path:
    name = input('Enter name:\n>> ')

    path = Path(__file__).parent.joinpath(f'dataset\{name}')
    if(not path.exists()):
        path.mkdir(0, True)

    return path

if __name__ == '__main__':
    main()