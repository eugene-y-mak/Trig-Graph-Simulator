import pygame as p
import math
import variables as v


def draw_sin(surface):
    points = []
    for x in range(0, v.WIDTH):
        y = int((v.AMPLITUDE * v.INCREMENT) * math.sin((v.FREQUENCY * (x/v.INCREMENT)) - v.H_SHIFT) + (v.V_SHIFT * v.INCREMENT +v.HEIGHT//2))
        points.append([x, v.HEIGHT - y])
    p.draw.line(surface, p.Color("black"), (0, v.HEIGHT//2), (v.WIDTH, v.HEIGHT//2), 2)
    p.draw.lines(surface, p.Color("black"), False, points, 3)
    for x in range(0, v.WIDTH, v.INCREMENT):
        p.draw.line(surface, p.Color("black"), (x, v.HEIGHT // 2 + 8), (x, v.HEIGHT // 2 - 8), 2)
    p.draw.circle(surface, p.Color("red"), points[5], 10)
    v.H_SHIFT -= v.SHIFT_SPEED


def draw_cos(surface):
    points = []
    for x in range(0, v.WIDTH):
        y = int((v.COS_AMPLITUDE * v.INCREMENT) * math.cos((v.COS_FREQUENCY * (x/v.INCREMENT)) - v.COS_H_SHIFT) +
                (v.COS_V_SHIFT * v.INCREMENT+ v.HEIGHT//2))
        points.append([x, v.HEIGHT - y])
    p.draw.lines(surface, p.Color("black"), False, points, 3)
    p.draw.line(surface, p.Color("black"), (0, v.HEIGHT//2), (v.WIDTH, v.HEIGHT//2), 2)
    for x in range(0, v.WIDTH, v.INCREMENT):
        p.draw.line(surface, p.Color("black"), (x, v.HEIGHT // 2 + 8), (x, v.HEIGHT // 2 - 8), 2)
    p.draw.circle(surface, p.Color("red"), points[5], 10)
    v.COS_H_SHIFT -= v.COS_SPEED


def draw_tan(surface):
    points = []
    for x in range(0, v.WIDTH):
        y = int((v.TAN_AMPLITUDE * v.INCREMENT) * math.tan((v.TAN_FREQUENCY * (x/v.INCREMENT)) - v.TAN_H_SHIFT) +
                (v.TAN_V_SHIFT * v.INCREMENT + v.HEIGHT//2))
        points.append([x, v.HEIGHT - y])
    p.draw.lines(surface, p.Color("black"), False, points, 3)

    p.draw.line(surface, p.Color("black"), (0, v.HEIGHT//2), (v.WIDTH, v.HEIGHT//2), 2)
    for x in range(0, v.WIDTH, v.INCREMENT):
        p.draw.line(surface, p.Color("black"), (x, v.HEIGHT // 2 + 8), (x, v.HEIGHT // 2 - 8), 2)
    p.draw.circle(surface, p.Color("red"), points[5], 10)

    v.TAN_H_SHIFT -= v.TAN_SPEED


