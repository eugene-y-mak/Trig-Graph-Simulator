import variables as v
import pygame as p


def draw_buttons(screen):
    panel = p.Rect(v.G_WIDTH - v.WIDTH, v.HEIGHT, v.I_WIDTH, v.I_HEIGHT)
    p.draw.rect(screen, p.Color("white"), panel)
    button = p.Rect(0, 0, v.I_WIDTH // 3, 2 * v.I_HEIGHT//3)
    sin_button = button.clamp(panel).move(0, v.I_HEIGHT//3)
    cos_button = button.clamp(panel).move(v.WIDTH//3, v.I_HEIGHT//3)
    tan_button = button.clamp(panel).move(2*v.WIDTH//3, v.I_HEIGHT//3)
    p.draw.rect(screen, v.SIN_COLOR, sin_button)
    p.draw.rect(screen, v.COS_COLOR, cos_button)
    p.draw.rect(screen, v.TAN_COLOR, tan_button)
    return sin_button, cos_button, tan_button


def draw_text(screen):
    font = p.font.SysFont("Courier New", 12)
    texts = [" Amplitude: " + str(v.AMPLITUDE), " Frequency: " + str(v.FREQUENCY), " Vert. Shift: " + str(v.V_SHIFT),
             "Init. Horiz. Shift: " + str(v.H_SHIFT_INIT)]
    for x in range(3):
        p.draw.line(screen, p.Color("black"), (v.G_WIDTH - v.WIDTH + (x * v.I_WIDTH//3), v.HEIGHT),
                    (v.G_WIDTH - v.WIDTH + (x * v.I_WIDTH//3), v.G_HEIGHT), 1)
    for x in range(3):
        if x == 1:
            texts = [" Amplitude: " + str(v.COS_AMPLITUDE), " Frequency: " + str(v.COS_FREQUENCY),
                     " Vert. Shift: " + str(v.COS_V_SHIFT),
                     "Init. Horiz. Shift: " + str(v.COS_H_SHIFT_INIT)]
        if x == 2:
            texts = [" Amplitude: " + str(v.TAN_AMPLITUDE), " Frequency: " + str(v.TAN_FREQUENCY),
                     " Vert. Shift: " + str(v.TAN_V_SHIFT),
                     "Init. Horiz. Shift: " + str(v.TAN_H_SHIFT_INIT)]
        panel = p.Rect((x * v.I_WIDTH//3) + (v.G_WIDTH - v.WIDTH), v.HEIGHT, v.I_WIDTH // 6, v.I_HEIGHT // 12)
        for i in range(len(texts)):
            text_obj = font.render(texts[i], 0, p.Color('black'))
            if i == 0:
                text_loc = panel.move(0, 0)
                screen.blit(text_obj, text_loc)
            elif i == 1:
                text_loc = panel.move(v.I_WIDTH // 6, 0)
                screen.blit(text_obj, text_loc)
            elif i == 2:
                text_loc = panel.move(0, v.I_HEIGHT // 6)
                screen.blit(text_obj, text_loc)
            elif i == 3:
                text_loc = panel.move(v.I_WIDTH//6, v.I_HEIGHT//6)
                screen.blit(text_obj, text_loc)


def draw_boxes(screen):
    box = p.Rect((v.G_WIDTH - v.WIDTH) + 5, (v.HEIGHT + v.I_HEIGHT // 12), (v.I_WIDTH // 6) - 10, (v.I_HEIGHT // 12) - 2)
    amp_box = box.move(0, 0)
    freq_box = box.move(v.I_WIDTH//6, 0)
    v_box = box.move(0, v.I_HEIGHT//6)
    h_box = box.move(v.I_WIDTH//6, v.I_HEIGHT//6)
    p.draw.rect(screen, p.Color("grey"), amp_box, 1)
    p.draw.rect(screen, p.Color("grey"), freq_box, 1)
    p.draw.rect(screen, p.Color("grey"), v_box, 1)
    p.draw.rect(screen, p.Color("grey"), h_box, 1)
    return amp_box, freq_box, v_box, h_box


def draw_cos_boxes(screen):
    box = p.Rect((v.G_WIDTH - v.WIDTH) + 5 + v.I_WIDTH//3, v.HEIGHT + v.I_HEIGHT // 12, (v.I_WIDTH // 6) - 10, (v.I_HEIGHT // 12) - 2)
    cos_amp_box = box.move(0, 0)
    cos_freq_box = box.move(v.I_WIDTH // 6, 0)
    cos_v_box = box.move(0, v.I_HEIGHT // 6)
    cos_h_box = box.move(v.I_WIDTH // 6, v.I_HEIGHT // 6)
    p.draw.rect(screen, p.Color("grey"), cos_amp_box, 1)
    p.draw.rect(screen, p.Color("grey"), cos_freq_box, 1)
    p.draw.rect(screen, p.Color("grey"), cos_v_box, 1)
    p.draw.rect(screen, p.Color("grey"), cos_h_box, 1)
    return cos_amp_box, cos_freq_box, cos_v_box, cos_h_box


def draw_tan_boxes(screen):
    box = p.Rect((v.G_WIDTH - v.WIDTH) + 5 + 2 * v.I_WIDTH // 3, v.HEIGHT + v.I_HEIGHT // 12, (v.I_WIDTH // 6) - 10,
                 (v.I_HEIGHT // 12) - 2)
    tan_amp_box = box.move(0, 0)
    tan_freq_box = box.move(v.I_WIDTH // 6, 0)
    tan_v_box = box.move(0, v.I_HEIGHT // 6)
    tan_h_box = box.move(v.I_WIDTH // 6, v.I_HEIGHT // 6)
    p.draw.rect(screen, p.Color("grey"), tan_amp_box, 1)
    p.draw.rect(screen, p.Color("grey"), tan_freq_box, 1)
    p.draw.rect(screen, p.Color("grey"), tan_v_box, 1)
    p.draw.rect(screen, p.Color("grey"), tan_h_box, 1)
    return tan_amp_box, tan_freq_box, tan_v_box, tan_h_box


def pause_play(screen):
    panel = p.Rect(0, v.HEIGHT, v.G_WIDTH - v.WIDTH, v.G_HEIGHT - v.HEIGHT)
    p.draw.rect(screen, p.Color("white"), panel)
    button = p.Rect(0, v.HEIGHT, (v.G_WIDTH - v.WIDTH)/2, v.G_HEIGHT - v.HEIGHT)
    pause = button.clamp(panel).move(0, 0)
    play = button.clamp(panel).move((v.G_WIDTH-v.WIDTH)/2, 0)
    p.draw.rect(screen, p.Color('#ED6A5E'), pause)
    p.draw.rect(screen, p.Color("#4CE0B3"), play)
    return pause, play
