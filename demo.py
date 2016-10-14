import os
import sys

import rm
import sim
import qr
import s7
import msg

def clear():
    if sys.platform=='win32':os.system('cls')
    else:os.system('clear')

if __name__ == '__main__':
    while(True):
        print(5*'-'+'[menu]'+5*'-')
        print("[0]: exit")
        print('[1]: QR')
        print('[2]: iteration')
        print('[3]: rotation')
        print('[4]: variant')
        print('[5]: numbers and vectors')
        try:
            com = int(input('enter: '))
        except:
            clear()
            print('wrong command, press enter to continue...')
            raw_input()
            clear()
            continue
        if com==0:
            clear()
            break
        elif com==1:
            clear()
            qr.main()
            print('end of task, press enter to continue...')
            raw_input()
            clear()
        elif com==2:
            clear()
            sim.main()
            print('end of task, press enter to continue...')
            raw_input()
            clear()
        elif com==3:
            clear()
            rm.main()
            print('end of task, press enter to continue...')
            raw_input()
            clear()
        elif com==4:
            clear()
            msg.main()
            print('end of task, press enter to continue...')
            raw_input()
            clear()
        elif com==5:
            clear()
            s7.main()
            print('end of task, press enter to continue...')
            raw_input()
            clear()
        else:
            clear()
            print('wrong command, press enter to continue...')
            raw_input()
            clear()
    