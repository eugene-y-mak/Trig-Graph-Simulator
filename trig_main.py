import pygame as p
import graph
import variables as v
import input
import circle
import math
Background = p.Color("white")
graph_color = p.Color('#004ba8')
circle_color = p.Color('#3e78b2')


def main():
    p.init()
    screen = p.display.set_mode((v.G_WIDTH, v.G_HEIGHT))
    screen.fill(Background)
    surface = p.Surface((v.WIDTH, v.HEIGHT))
    surface.fill(graph_color)
    surface2 = p.Surface((v.G_WIDTH - v.WIDTH, v.HEIGHT))
    surface2.fill(circle_color)
    p.display.set_caption("Trig Graph Simulation")
    clock = p.time.Clock()
    c = 0
    c2 = 0
    font = p.font.SysFont("Segoe UI", 28)
    font2 = p.font.SysFont("Segoe UI", 12)
    panel = p.Rect(v.G_WIDTH - v.WIDTH, v.HEIGHT, v.I_WIDTH, v.I_HEIGHT)
    buttons = input.draw_buttons(screen)
    sin_boxes = input.draw_boxes(screen)
    cos_boxes = input.draw_cos_boxes(screen)
    tan_boxes = input.draw_tan_boxes(screen)
    pp = input.pause_play(screen)
    new_text = ''
    running = True
    active = False
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            if e.type == p.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(e.pos):
                    v.H_SHIFT = v.H_SHIFT_INIT
                    c = 0
                    p.draw.rect(screen, v.SIN_COLOR_ON, buttons[0])
                    p.draw.rect(screen, v.COS_COLOR, buttons[1])
                    p.draw.rect(screen, v.TAN_COLOR, buttons[2])
                elif buttons[1].collidepoint(e.pos):
                    v.COS_H_SHIFT = v.COS_H_SHIFT_INIT
                    c = 1
                    p.draw.rect(screen, v.SIN_COLOR, buttons[0])
                    p.draw.rect(screen, v.COS_COLOR_ON, buttons[1])
                    p.draw.rect(screen, v.TAN_COLOR, buttons[2])
                elif buttons[2].collidepoint(e.pos):
                    v.TAN_H_SHIFT = v.TAN_H_SHIFT_INIT
                    c = 2
                    p.draw.rect(screen, v.SIN_COLOR, buttons[0])
                    p.draw.rect(screen, v.COS_COLOR, buttons[1])
                    p.draw.rect(screen, v.TAN_COLOR_ON, buttons[2])
                elif pp[0].collidepoint(e.pos):
                    v.SHIFT_SPEED = 0
                    v.COS_SPEED = 0
                    v.TAN_SPEED = 0
                    p.draw.rect(screen, p.Color('#f5aaa3'), pp[0])
                    p.draw.rect(screen, p.Color('#4CE0B3'), pp[1])
                elif pp[1].collidepoint(e.pos):
                    v.SHIFT_SPEED = v.FREQUENCY/15
                    v.COS_SPEED = v.COS_FREQUENCY/15
                    v.TAN_SPEED = v.TAN_FREQUENCY/15
                    p.draw.rect(screen, p.Color("#ED6A5E"), pp[0])
                    p.draw.rect(screen, p.Color('#93ecd1'), pp[1])
                elif sin_boxes[0].collidepoint(e.pos):
                    active = True
                    c2 = 0
                    p.draw.rect(screen, p.Color("black"), sin_boxes[0], 1)
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[1], 1)
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[2], 1)
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[3], 1)
                elif sin_boxes[1].collidepoint(e.pos):
                    active = True
                    c2 = 1
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[0], 1)
                    p.draw.rect(screen, p.Color("black"), sin_boxes[1], 1)
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[2], 1)
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[3], 1)
                elif sin_boxes[2].collidepoint(e.pos):
                    active = True
                    c2 = 2
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[0], 1)
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[1], 1)
                    p.draw.rect(screen, p.Color("black"), sin_boxes[2], 1)
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[3], 1)
                elif sin_boxes[3].collidepoint(e.pos):
                    active = True
                    c2 = 3
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[0], 1)
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[1], 1)
                    p.draw.rect(screen, p.Color("grey"), sin_boxes[2], 1)
                    p.draw.rect(screen, p.Color("black"), sin_boxes[3], 1)
                elif cos_boxes[0].collidepoint(e.pos):
                    active = True
                    c2 = 4
                    p.draw.rect(screen, p.Color("black"), cos_boxes[0], 1)
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[1], 1)
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[2], 1)
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[3], 1)
                elif cos_boxes[1].collidepoint(e.pos):
                    active = True
                    c2 = 5
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[0], 1)
                    p.draw.rect(screen, p.Color("black"), cos_boxes[1], 1)
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[2], 1)
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[3], 1)
                elif cos_boxes[2].collidepoint(e.pos):
                    active = True
                    c2 = 6
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[0], 1)
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[1], 1)
                    p.draw.rect(screen, p.Color("black"), cos_boxes[2], 1)
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[3], 1)
                elif cos_boxes[3].collidepoint(e.pos):
                    active = True
                    c2 = 7
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[0], 1)
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[1], 1)
                    p.draw.rect(screen, p.Color("grey"), cos_boxes[2], 1)
                    p.draw.rect(screen, p.Color("black"), cos_boxes[3], 1)
                elif tan_boxes[0].collidepoint(e.pos):
                    active = True
                    c2 = 8
                    p.draw.rect(screen, p.Color("black"), tan_boxes[0], 1)
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[1], 1)
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[2], 1)
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[3], 1)
                elif tan_boxes[1].collidepoint(e.pos):
                    active = True
                    c2 = 9
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[0], 1)
                    p.draw.rect(screen, p.Color("black"), tan_boxes[1], 1)
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[2], 1)
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[3], 1)
                elif tan_boxes[2].collidepoint(e.pos):
                    active = True
                    c2 = 10
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[0], 1)
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[1], 1)
                    p.draw.rect(screen, p.Color("black"), tan_boxes[2], 1)
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[3], 1)
                elif tan_boxes[3].collidepoint(e.pos):
                    active = True
                    c2 = 11
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[0], 1)
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[1], 1)
                    p.draw.rect(screen, p.Color("grey"), tan_boxes[2], 1)
                    p.draw.rect(screen, p.Color("black"), tan_boxes[3], 1)
            if e.type == p.KEYDOWN:
                if active:
                    if e.key == p.K_RETURN:
                        try:
                            int(new_text)
                        except ValueError:
                            invalid = font2.render("Invalid input", 0, p.Color("black"))
                            screen.blit(invalid, panel)
                        else:
                            if c2 == 0:
                                v.AMPLITUDE = int(new_text)
                            if c2 == 1:
                                v.FREQUENCY = int(new_text)
                                v.SHIFT_SPEED = v.FREQUENCY / 15
                            if c2 == 2:
                                v.V_SHIFT = int(new_text)
                            if c2 == 3:
                                v.H_SHIFT_INIT = int(new_text)
                            if c2 == 4:
                                v.COS_AMPLITUDE = int(new_text)
                            if c2 == 5:
                                v.COS_FREQUENCY = int(new_text)
                                v.COS_SPEED = v.COS_FREQUENCY / 15
                            if c2 == 6:
                                v.COS_V_SHIFT = int(new_text)
                            if c2 == 7:
                                v.COS_H_SHIFT_INIT = int(new_text)
                            if c2 == 8:
                                v.TAN_AMPLITUDE = int(new_text)
                            if c2 == 9:
                                v.TAN_FREQUENCY = int(new_text)
                                v.TAN_SPEED = v.TAN_FREQUENCY / 15
                            if c2 == 10:
                                v.TAN_V_SHIFT = int(new_text)
                            if c2 == 11:
                                v.TAN_H_SHIFT_INIT = int(new_text)
                        new_text = ''
                        p.draw.rect(screen, p.Color("white"), panel)
                        input.draw_buttons(screen)
                        p.draw.rect(screen, p.Color("grey"), tan_boxes[0], 1)
                        p.draw.rect(screen, p.Color("grey"), tan_boxes[1], 1)
                        p.draw.rect(screen, p.Color("grey"), tan_boxes[2], 1)
                        p.draw.rect(screen, p.Color("grey"), tan_boxes[3], 1)
                        p.draw.rect(screen, p.Color("grey"), cos_boxes[0], 1)
                        p.draw.rect(screen, p.Color("grey"), cos_boxes[1], 1)
                        p.draw.rect(screen, p.Color("grey"), cos_boxes[2], 1)
                        p.draw.rect(screen, p.Color("grey"), cos_boxes[3], 1)
                        p.draw.rect(screen, p.Color("grey"), sin_boxes[0], 1)
                        p.draw.rect(screen, p.Color("grey"), sin_boxes[1], 1)
                        p.draw.rect(screen, p.Color("grey"), sin_boxes[2], 1)
                        p.draw.rect(screen, p.Color("grey"), sin_boxes[3], 1)
                        active = False
                    elif e.key == p.K_BACKSPACE:
                        new_text = new_text[:-1]
                        p.draw.rect(screen, p.Color("white"), panel)
                        input.draw_buttons(screen)
                        p.draw.rect(screen, p.Color("grey"), tan_boxes[0], 1)
                        p.draw.rect(screen, p.Color("grey"), tan_boxes[1], 1)
                        p.draw.rect(screen, p.Color("grey"), tan_boxes[2], 1)
                        p.draw.rect(screen, p.Color("grey"), tan_boxes[3], 1)
                        p.draw.rect(screen, p.Color("grey"), cos_boxes[0], 1)
                        p.draw.rect(screen, p.Color("grey"), cos_boxes[1], 1)
                        p.draw.rect(screen, p.Color("grey"), cos_boxes[2], 1)
                        p.draw.rect(screen, p.Color("grey"), cos_boxes[3], 1)
                        p.draw.rect(screen, p.Color("grey"), sin_boxes[0], 1)
                        p.draw.rect(screen, p.Color("grey"), sin_boxes[1], 1)
                        p.draw.rect(screen, p.Color("grey"), sin_boxes[2], 1)
                        p.draw.rect(screen, p.Color("grey"), sin_boxes[3], 1)
                    else:
                        new_text += e.unicode
            if e.type == p.MOUSEBUTTONUP:
                p.draw.rect(screen, v.SIN_COLOR, buttons[0])
                p.draw.rect(screen, v.COS_COLOR, buttons[1])
                p.draw.rect(screen, v.TAN_COLOR, buttons[2])
                p.draw.rect(screen, p.Color('#ED6A5E'), pp[0])
                p.draw.rect(screen, p.Color('#4CE0B3'), pp[1])
        screen.blit(font.render("Sine", 100, p.Color('white')), p.Rect(v.G_WIDTH - v.WIDTH, v.G_HEIGHT - v.I_HEIGHT + 75,
                                                                     v.I_WIDTH // 3, (2 * v.I_HEIGHT // 3)))
        screen.blit(font.render("Cosine", 100, p.Color('white')), p.Rect(v.G_WIDTH - v.WIDTH + v.WIDTH // 3,
                                                                       v.G_HEIGHT - v.I_HEIGHT + 75, v.I_WIDTH // 3,
                                                                         (2 * v.I_HEIGHT // 3)))
        screen.blit(font.render("Tangent", 100, p.Color('white')), p.Rect(v.G_WIDTH - v.WIDTH + 2 * v.WIDTH // 3,
                                                                        v.G_HEIGHT - v.I_HEIGHT + 75, v.I_WIDTH // 3,
                                                                         (2 * v.I_HEIGHT // 3)))
        screen.blit(font.render("Pause", 100, p.Color('black')), pp[0])
        screen.blit(font.render("Play", 100, p.Color('black')), pp[1])
        surface.fill(graph_color)
        surface2.fill(circle_color)
        if c == 0:
            graph.draw_sin(surface)
            circle.draw_sin(surface2)
        elif c == 1:
            graph.draw_cos(surface)
            circle.draw_cos(surface2)
        elif c == 2:
            graph.draw_tan(surface)
            circle.draw_tan(surface2)
        screen.blit(surface, (v.G_WIDTH - v.WIDTH, 0))
        screen.blit(surface2, (0, 0))
        txt_obj = font2.render(new_text, 0, p.Color('black'))
        if c2 == 0:
            screen.blit(txt_obj, sin_boxes[0])
        elif c2 == 1:
            screen.blit(txt_obj, sin_boxes[1])
        elif c2 == 2:
            screen.blit(txt_obj, sin_boxes[2])
        elif c2 == 3:
            screen.blit(txt_obj, sin_boxes[3])
        elif c2 == 4:
            screen.blit(txt_obj, cos_boxes[0])
        elif c2 == 5:
            screen.blit(txt_obj, cos_boxes[1])
        elif c2 == 6:
            screen.blit(txt_obj, cos_boxes[2])
        elif c2 == 7:
            screen.blit(txt_obj, cos_boxes[3])
        elif c2 == 8:
            screen.blit(txt_obj, tan_boxes[0])
        elif c2 == 9:
            screen.blit(txt_obj, tan_boxes[1])
        elif c2 == 10:
            screen.blit(txt_obj, tan_boxes[2])
        elif c2 == 11:
            screen.blit(txt_obj, tan_boxes[3])
        input.draw_text(screen)
        p.display.flip()
        clock.tick(v.MAX_FPS)


main()



