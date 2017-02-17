from random import sample
from psychopy import core, event, gui, visual

WIN = visual.Window((800, 600), color="black", units="pix")
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.')
FIX = visual.TextStim(WIN, text='+', height=40, color='white', pos=(0, 0))
COLORS = ['white', '#FFDA00', '#52FFAE', '#3E0DE4',
          '#F8E214', '#CDF118', '#A52A2A', '#1118BB', '#6C3EFF']
POSITIONS = [
    [(-100, 100), (100, 100)],
    [(-100, 100), (100, 100), (-100, -100), (100, -100)],
    [(100,100), (-100,100) ,(-150,0), (150,0),(-100,-100),(100,-100)],
    [(100, 200), (100, -200), (-100, 200), (200, 100), (200, -100), (-200, 100), (-200, -100), (-100, -200)]
]
T = (0.3, 2)


def notify(alert_wait_time=0.3, fix_wait_time=0.5, win=WIN):
    ALERT_MSG.draw()
    win.flip()
    event.waitKeys(keyList='space')
    core.wait(alert_wait_time)
    FIX.draw()
    win.flip()
    core.wait(fix_wait_time)


def draw_square(fill_color, pos, size=(100, 100), line_color="black"):
    square = visual.Rect(WIN, fillColor=fill_color, pos=pos, lineColor=line_color, size=size)
    square.draw()
    return square


def trial(shapes, colors, positions, wait_times, win=WIN, tries=4, display_wait_time=2):
    for i in range(shapes):
        draw_square(colors[i], positions[i])
    win.flip()

    core.wait(display_wait_time)

    col = sample(colors, tries)
    pos = sample(positions, tries)
    results = motivate(col[:tries/2], pos[:tries/2], wait_times[0])
    results += motivate(col[tries/2:], pos[tries/2:], wait_times[1])
    return results
    # TODO: aggregate results


def motivate(colors, positions, wait_time, win=WIN, wait_keys=('k', 's')):
    rv = []
    # cue
    for i in range(len(positions)):
        draw_square(COLORS[0], positions[i])
    win.flip()

    core.wait(wait_time)

    # res
    for i in range(len(positions)):
        draw_square(colors[i], positions[i])
        win.flip()
        t1 = core.getTime()
        ans = event.waitKeys(keyList=wait_keys)
        t2 = core.getTime()
        rv.append((ans, t1, t2))

    return rv


def main():
    info = {'cond': ['2000ms'], 'ID': '', 'age': '', 'gender': ['Male', 'Female']}
    gui.DlgFromDict(dictionary=info, title='VWM Task', order=['ID', 'cond', 'age'])
    for idx, n in enumerate((2, 4, 6, 8)):
        tries = 2 if n == 2 else 4
        colors = sample(COLORS[1:], n)
        positions = sample(POSITIONS[idx], n)
        notify()
        print(trial(n, colors, positions, sample(T, 2), tries=tries))


if __name__ == '__main__':
    main()
