import random 
import time 
def generate_rand_int(start, end):

    return random.randint(start, end)

def run():
    while True:
        time.sleep(1)
        with open('prng-service.txt', 'r') as f:
            value = f.readline()
            f.close()
            if value == "run":
                with open('prng-service.txt', 'w') as f:
                    rand_int = generate_rand_int(1, 20)
                    print('generated number is {}'.format(rand_int))
                    f.write(str(rand_int))
        f.close()
        
if __name__ == "__main__":
    run()

