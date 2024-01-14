import subprocess,os


def getpath():
    return os.getcwd()

def changepath():
    if "platform-tools" not in os.getcwd():
        os.chdir('platform-tools')


def pair(ip, port, pin):
    command="./adb pair {0}:{1} {2}".format(ip, port, pin)
    subprocess.run(command)

def connect(ip, port):
    command="./adb connect {0}:{1}".format(ip, port)
    subprocess.run(command)

def send_event(key):
    command="./adb shell input keyevent "+str(key)
    subprocess.run(command)

def conn_stat():
    result = subprocess.run(["adb", "devices"], shell=True, capture_output=True, text=True)
    if "device" in result.stdout:
        return 0
    if "offline" in result.stdout:
        return 1
# conn_stat

