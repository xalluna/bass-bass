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

        key: chr = chr(cv2.waitKey(1) & 0xFF)

        if key == 'q':
            print("Closing program")
            break

        elif key == ' ':
            img_name = f"{path}/image_{img_counter}.jpg"
            print(img_name)
            cv2.imwrite(img_name, frame)
            print(f"{img_name} written!")
            img_counter += 1

        elif key == 'n':
            path = choose_name()
            img_counter = 0

    cam.release()

    cv2.destroyAllWindows()
#end main

def choose_name() -> Path:
    name = input('Enter name:\n>> ')

    path = Path(__file__).parent.joinpath(f'dataset/{name}')
    if(not path.exists()):
        path.mkdir(0, True)

    return path

if __name__ == '__main__':
    main()