from pynput.mouse import Listener
import sys
import subprocess
import time
import datetime

time_limit_minutes = 20

def call_timew(args):
    theproc = subprocess.Popen(['C:/cygwin64/bin/run.exe', '-p' ,'/bin', 'bash', '-l', 'C:\cygwin64\home\mkluge\call_timew.sh']+args, shell=True)
    theproc.communicate()

work_stopped = False
last_mouse_move = datetime.datetime.now()
def on_move(x, y):
    global last_mouse_move
    last_mouse_move = datetime.datetime.now()
#    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    global last_mouse_move
    last_mouse_move = datetime.datetime.now()
#    print('{0} at {1}'.format( 'Pressed' if pressed else 'Released', (x, y)))

def on_scroll(x, y, dx, dy):
    global last_mouse_move
    last_mouse_move = datetime.datetime.now()
#    print('Scrolled {0}'.format( (x, y)))


ml = Listener( on_move=on_move, on_click=on_click, on_scroll=on_scroll)
ml.start()

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    seconds = (now - last_mouse_move).seconds
#    print("last move %d seconds ago" % seconds)
    if work_stopped==False and seconds>time_limit_minutes*60:
        print('work stopped')
        stoptime=str(last_mouse_move.hour)+":"+str(last_mouse_move.minute)
        call_timew(["stop",stoptime])
        work_stopped=True
    if work_stopped==True and seconds<10:
        print('work continued')
        call_timew(["continue"])
        work_stopped=False

ml.stop()
