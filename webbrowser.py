import webbrowser
from numpy import random

def random_memes():
    while True:
        try:
            inp = input("Give me a number ;) : ")
            inp = abs(int(float(inp)))
            break
        except:
            print('Not a number!')

    if inp > 200:
        inp = random.randint(0,200)
    webbrowser.open(f'https://www.memedroid.com/memes/random/{inp}', new=2)
    
if __name__ == "__main__":
    random_memes()
