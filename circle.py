import math
import pygame as p
import variables as v

h = 0


def draw_sin(screen):
    global h
    points = []
    py = []
    for x in range(0, v.WIDTH):
        y = int((v.AMPLITUDE * v.INCREMENT) * math.sin((v.FREQUENCY * (x / v.INCREMENT)) - v.H_SHIFT) +
                (v.V_SHIFT * v.INCREMENT + v.HEIGHT // 2))
        if h == 0:
            points.append([int(math.sqrt(math.pow(v.AMPLITUDE * v.INCREMENT, 2) - math.pow(abs((v.V_SHIFT * v.INCREMENT)+ v.HEIGHT//2 - y), 2))) +
                       (v.G_WIDTH - v.WIDTH)//2, v.HEIGHT - y])
            py.append([300, v.HEIGHT - y])
            if points[0][1] == (v.HEIGHT//2 - (v.V_SHIFT * v.INCREMENT)) - (v.AMPLITUDE * v.INCREMENT) + 1:
                h = 1
        elif h == 1:
            points.append([300 - (int(math.sqrt(math.pow(v.AMPLITUDE * v.INCREMENT, 2)
                                                - math.pow(abs(((v.V_SHIFT * v.INCREMENT)+ v.HEIGHT//2) - y), 2))) +
                       (v.G_WIDTH - v.WIDTH)//2), v.HEIGHT - y])
            py.append([300, v.HEIGHT - y])
            if points[0][1] == (v.HEIGHT//2 - (v.V_SHIFT * v.INCREMENT)) + (v.AMPLITUDE * v.INCREMENT):
                h = 0
    p.draw.circle(screen, p.Color("red"), points[0], 10)
    p.draw.circle(screen, p.Color("black"), ((v.G_WIDTH - v.WIDTH)//2, v.HEIGHT//2 -(v.V_SHIFT * v.INCREMENT)), v.AMPLITUDE * v.INCREMENT, 2)
    p.draw.circle(screen, p.Color("black"), ((v.G_WIDTH - v.WIDTH) // 2, v.HEIGHT // 2 - (v.V_SHIFT * v.INCREMENT)),
                  3)
    p.draw.line(screen, p.Color("black"), points[0], py[0])
    p.draw.line(screen, p.Color("black"), ((v.G_WIDTH - v.WIDTH) // 2, v.HEIGHT // 2 - (v.V_SHIFT * v.INCREMENT)), points[0])


def draw_cos(screen):
    global h
    points = []
    py = []
    for x in range(0, v.WIDTH):
        y = int((v.COS_AMPLITUDE * v.INCREMENT) * math.cos((v.COS_FREQUENCY * (x / v.INCREMENT)) - v.COS_H_SHIFT) +
                (v.COS_V_SHIFT * v.INCREMENT + v.HEIGHT // 2))
        if h == 0:
            points.append([int(math.sqrt(math.pow(v.COS_AMPLITUDE * v.INCREMENT, 2) - math.pow(abs((v.COS_V_SHIFT * v.INCREMENT) + v.HEIGHT // 2 - y),
                                                                  2))) +
                           (v.G_WIDTH - v.WIDTH) // 2, v.HEIGHT - y])
            py.append([300, v.HEIGHT - y])
            if points[0][1] == (v.HEIGHT // 2 - (v.COS_V_SHIFT * v.INCREMENT)) - (v.COS_AMPLITUDE * v.INCREMENT) + 1:
                h = 1
        elif h == 1:
            points.append([300 - (int(math.sqrt(math.pow(v.COS_AMPLITUDE * v.INCREMENT, 2) - math.pow(abs(((v.COS_V_SHIFT * v.INCREMENT) + v.HEIGHT // 2) - y), 2))) +
                                  (v.G_WIDTH - v.WIDTH) // 2), v.HEIGHT - y])
            py.append([300, v.HEIGHT - y])
            if points[0][1] == (v.HEIGHT // 2 - (v.COS_V_SHIFT * v.INCREMENT)) + (v.COS_AMPLITUDE * v.INCREMENT):
                h = 0
    p.draw.circle(screen, p.Color("red"), points[0], 10)
    p.draw.circle(screen, p.Color("black"), ((v.G_WIDTH - v.WIDTH) // 2, v.HEIGHT // 2 - (v.COS_V_SHIFT * v.INCREMENT)),
                  v.COS_AMPLITUDE * v.INCREMENT, 2)
    p.draw.circle(screen, p.Color("black"), ((v.G_WIDTH - v.WIDTH) // 2, v.HEIGHT // 2 - (v.COS_V_SHIFT * v.INCREMENT)), 3)
    p.draw.line(screen, p.Color("black"), points[0], py[0])
    p.draw.line(screen, p.Color("black"), ((v.G_WIDTH - v.WIDTH) // 2, v.HEIGHT // 2 - (v.COS_V_SHIFT * v.INCREMENT)),
                points[0])


def draw_tan(screen):
    global h
    points = []
    for x in range(0, v.WIDTH):
        y = int((v.TAN_AMPLITUDE * v.INCREMENT) * math.tan((v.TAN_FREQUENCY * (x / v.INCREMENT)) - v.TAN_H_SHIFT) +
                (v.TAN_V_SHIFT * v.INCREMENT + v.HEIGHT // 2))
        points.append([x, v.HEIGHT -y])
        try:
            int(math.sqrt(math.pow(v.TAN_AMPLITUDE * v.INCREMENT, 2) - math.pow(abs(v.HEIGHT // 2 - y), 2)))
        except ValueError:
            pass
    p.draw.circle(screen, p.Color("black"), ((v.G_WIDTH - v.WIDTH) // 2, v.HEIGHT // 2 - (v.TAN_V_SHIFT * v.INCREMENT)),
                  v.TAN_AMPLITUDE * v.INCREMENT, 2)
    p.draw.circle(screen, p.Color("black"), ((v.G_WIDTH - v.WIDTH)//2, v.HEIGHT//2), 3)
    p.draw.line(screen, p.Color("black"), (0, v.HEIGHT - points[0][1]), (300, points[0][1]))
