# https://www.youtube.com/watch?v=mDKM-JtUhhc&list=LL&index=2 3:18:10

mood = input("What is Your mood?: ")

match mood:
    case"hungry":
        print(f'Your mood is "{mood}", get some food!')
    case"mad":
        print(f'Your mood is "{mood}", find something to watch!')
    case"tired":
        print(f'Your mood is "{mood}", go to sleep!')
    case _: # We are using underline fore "else" statement
        print(f'You have no mood')
