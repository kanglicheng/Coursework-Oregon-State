import os 
import time 

def get_image_path():

    while True:
        with open('image-service.txt', 'r') as f:
            value = f.readline()
            f.close()
            if value.isdigit():
                directory = os.listdir('./images')
                index = len(directory) % int(value) - 1
                time.sleep(1)
                with open('image-service.txt', 'w') as f:
                    f.write('image/{}'.format(directory[index]))

if __name__ == "__main__":
    get_image_path()