from curses.ascii import isdigit
import time
def issue_command():

    while True:

        command = input('type "R" to start the program or Q to quit: ')
        if command == "Q":
            break
        elif command == "R": 
            with open('prng-service.txt', 'w') as f:
                f.write('run')
            f.close()
            time.sleep(3)
            with open('prng-service.txt', 'r') as f:
                value = f.readline()
                if value.isdigit():
                    ff = open('image-service.txt', 'w')
                    ff.write(value)
                    ff.close()
                    time.sleep(2)
                    ff =  open('image-service.txt', 'r')
                    path = ff.readline()
                    ff.close()
                    print(path)
            f.close()




if __name__ == "__main__":
    issue_command()