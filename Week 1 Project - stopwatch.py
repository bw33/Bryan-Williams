# Our mini-project for this week will focus on combining
# text drawing in the canvas with timers to build 
# a simple digital stopwatch that keeps track of the 
# time in tenths of a second. The stopwatch should contain 
# "Start", "Stop" and "Reset" buttons. To help guide you
# through this project, we suggest that you download the 
# provided program template for this mini-project and build 
# your stopwatch program as follows:

# Import Module
import simplegui

# Define global variables
tenths_seconds = 0
tenths_seconds2 = 0
seconds = 0
seconds2 = 0
seconds3 = 0 
ten_seconds = 0
ten_seconds2 = 0
minutes = 0
form = 0
count_successful = 0
count_total = 0
counter = 0
counters = 0 
gvariable = True

# Define helper functions

def format(tenths_second):
        global form
        form = str(minutes) + ":" + str(ten_seconds2) + str(seconds2) + "." + str(tenths_seconds2)
    
def format2(counters):
    global counter
    counter = str(count_successful) + " / " + str(count_total)
    
# Define event handlers
def tick():
    gvariable = True
    global tenths_seconds
    tenths_seconds += 1
    global tenths_seconds2
    tenths_seconds2 = tenths_seconds % 10
    global seconds
    seconds = tenths_seconds // 10
    global seconds2
    seconds2 = seconds % 10
    global seconds3 
    seconds3 = tenths_seconds / 10.0
    global ten_seconds
    ten_seconds = tenths_seconds // 100
    global ten_seconds2
    ten_seconds2 = ten_seconds % 6 
    global minutes
    minutes = tenths_seconds // 600
    format(tenths_seconds)

def start():
    global gvariable
    gvariable = True
    timer.start()
        
def stop():
    timer.stop()
    global gvariable 
    if seconds3 / seconds == 1 and gvariable:
        global count_successful 
        count_successful += 1
        global count_total
        count_total += 1
        gvariable = False
    elif seconds3 / seconds != 1 and gvariable:
        count_total +=1
        gvariable = False
    format2(counters)

def reset():
    global tenths_seconds
    tenths_seconds = 0
    global count_successful
    count_successful = 0
    global count_total
    count_total = 0
    format2(counters)
    
def draw(canvas):
    global form
    canvas.draw_text(str(form), [230,250], 25, "white")
    canvas.draw_text(str(counter), [460, 30], 15, "white")
    
# Create a frame
frame = simplegui.create_frame("Stopwatch", 500, 500)

# Register event handlers
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# Start timer and frame
frame.start()
