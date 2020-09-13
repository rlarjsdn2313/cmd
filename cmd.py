import weather
import commands
import time
from datetime import datetime
import classroom
import os
import help_h
import crawl
import translate
import mail_manager

def main():
    print("----------CMD----------")
    print("made by Gunwoo")

    cmd = ''
    while cmd != 'exit()':
        cmd = input('william> ')
        if cmd[:7] == 'nowtemp':
            print(str(weather.nowtemp(cmd)))
        elif cmd[:8] == 'finedust':
            print(str(weather.finedust(cmd)))
        elif cmd[:4] == 'cmd':
            commands_s = ''
            while commands_s != 'exit':
                commands_s = input()
                output = str(commands.receive_commands(commands_s))
                print(output, end='')
        elif cmd[:6] == 'cmd -o':
            print(str(commands.r_s_c(cmd)))
        elif cmd[:5] == 'timer':
            d_cmd = cmd[7]
            if d_cmd == 'c':
                c_cmd = int(cmd[9:])
                while c_cmd >= 1:
                    print(c_cmd)
                    time.sleep(1)
                    c_cmd = c_cmd -1
        elif cmd[:] == 'date':
            print(str(datetime.today().strftime("%Y/%m/%d %H:%M:%S")))
        elif cmd[:] == 'classroom':
            classroom.internet(cmd)
        elif cmd[:] == 'google':
            classroom.internet(cmd)
        elif cmd[:] == 'clear':
            os.system('cls')
        elif cmd[:8] == 'crawling':
            n = input('how many image: ')
            crawl.crawling(cmd, n)
        elif cmd[:2] == 'tr':
            go_put = cmd[3:]
            print(translate.get_nmt_translate(go_put))
        elif cmd[:] == 'email':
            receiver = input('input receiver email-address: ')
            contents = input('wirte conntents: ')
            if receiver == 'exit':
                main()
            if contents == 'exit':
                main()
            print(mail_manager.send_email(receiver, contents))
        elif cmd == 'list':
            print(help_h.help())


if __name__ == "__main__":
    main()
