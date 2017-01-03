from pynput.mouse import Listener
import sys
import subprocess
import time
import datetime
import WindowsBalloonTip

# the time limit after which the process will call timew stop
time_limit_minutes = 10
# the arguments for subprocess
tw_args = ['C:/cygwin64/bin/run.exe', '-p' ,'/bin', 'bash', '-l', "C:\\cygwin64\\home\\mkluge\\timew_mouse\\call_timew.sh"]

def call_timew(args):
    global tw_args
    theproc = subprocess.Popen(tw_args+args, shell=True)
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


w = WindowsBalloonTip.WindowsBalloonTip()
ml = Listener( on_move=on_move, on_click=on_click, on_scroll=on_scroll)
ml.start()
print("started")

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    seconds = (now - last_mouse_move).seconds
#    print("last move %d seconds ago" % seconds)
    if work_stopped==False and seconds>time_limit_minutes*60:
        stoptime=str(last_mouse_move.hour)+":"+'{:02d}'.format(last_mouse_move.minute)
        print('work stopped '+stoptime)
        call_timew(["stop",stoptime])
        work_stopped=True
        w.balloon_tip("work stopped", "work stopped", icon_path="stop.ico")
    if work_stopped==True and seconds<10:
        starttime=str(now.hour)+":"+'{:02d}'.format(now.minute)
        print('work continued '+starttime)
        call_timew(["continue"])
        work_stopped=False
        w.balloon_tip("work started", "go, do awesome stuff", icon_path="start.ico", duration=5)

ml.stop()
