"""
Goals for next time:
- replace C# bowl
- decide how to demonstrate the application (3-4 points; make it simple and clear)
(Jan 3rd)

- present project with points/features to: Sugnan:jaltarang-teacher (Jaltarang class zoom beginning), William:musical-peer (Lunch time), Madhav:judge-science-fair (Guests over), Prakash:experienced-science-fair (Guests over), Nachiket-musical-teacher (Sangeeta class in-person beginning; coordinate at end of previous class)
(when oppurtunity comes)
"""

import random
import os
import pygame
#from pydub import AudioSegment
import math

# Pygame
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=0)
pygame.mixer.pre_init(44100, -16, 2, 0) # Lower buffer size
screen = pygame.display.set_mode((750,700))
pygame.display.set_caption("Jaltarang")
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
reg = pygame.font.SysFont("Arial", 30)
pygame.mouse.set_visible(False)

# Stick
stick = pygame.image.load("Stick.jpg")
stick = pygame.transform.scale(stick, (10,250))
stick_rect = stick.get_rect()

### Sound Loading ### DOWN

"""
# File conversion

# Get all M4A files in current directory
m4a_files = [f for f in os.listdir('.') if f.endswith('.m4a')]

# Convert each file
for m4a_file in m4a_files:
    # Load the M4A file
    audio = AudioSegment.from_file(m4a_file, format="m4a")

    # Create WAV filename
    wav_file = m4a_file.replace('.m4a', '.wav')

    # Export as WAV
    audio.export(wav_file, format="wav")
    print(f"Converted {m4a_file} to {wav_file}")
"""

# Sounds
BL = pygame.mixer.Sound("C Jaltarang.wav")
C = pygame.mixer.Sound("C Jaltarang.wav")
CS = pygame.mixer.Sound("C# Jaltarang.wav")
D = pygame.mixer.Sound("D Jaltarang.wav")
DS = pygame.mixer.Sound("D# Jaltarang.wav")
E = pygame.mixer.Sound("E Jaltarang.wav")
F = pygame.mixer.Sound("F Jaltarang.wav")
FS = pygame.mixer.Sound("F# Jaltarang.wav")
G = pygame.mixer.Sound("G Jaltarang.wav")
GS = pygame.mixer.Sound("G# Jaltarang.wav")
A = pygame.mixer.Sound("A Jaltarang.wav")
AS = pygame.mixer.Sound("A# Jaltarang.wav")
B = pygame.mixer.Sound("B Jaltarang.wav")
CH = pygame.mixer.Sound("CH Jaltarang.wav")
CSH = pygame.mixer.Sound("C#H Jaltarang.wav")
DH = pygame.mixer.Sound("DH Jaltarang.wav")
DSH = pygame.mixer.Sound("D#H Jaltarang.wav")
EH = pygame.mixer.Sound("EH Jaltarang.wav")
FH = pygame.mixer.Sound("FH Jaltarang.wav")
FSH = pygame.mixer.Sound("F#H Jaltarang.wav")
GH = pygame.mixer.Sound("GH Jaltarang.wav")

### Sound Loading ### UP

# Circle coordinates and drawing
def draw(COLORS):
  global bowls
  
  inc = 300
  screen.fill((150,75,0))
  bowl1 = (100+inc,102)
  bowl2 = (150+inc,148)
  bowl3 = (200+inc,202)
  bowl4 = (250+inc,248)
  bowl5 = (300+inc,302)
  bowl6 = (350+inc,348)
  bowl7 = (100,352)
  bowl8 = (150,298)
  bowl9 = (200,252)
  bowl10 = (250,198)
  bowl11 = (300,152)
  bowl12 = (350,98)
  bowls = [bowl7,bowl8,bowl9,bowl10,bowl11,bowl12,bowl1,bowl2,bowl3,bowl4,bowl5,bowl6]
  for bowl in bowls:
    pygame.draw.circle(screen, COLORS[bowls.index(bowl)], bowl, 20)
  x,y = pygame.mouse.get_pos()
  screen.blit(stick, (x-10,y-125))

def reset():
  global notes
  global colors
  notes = [C,D,E,F,G,A,B,CH,DH,EH,FH,GH]
  colors = [WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE]
  draw(colors)
reset()

# Hertz
def find_hz(note):
  if note == BL:  return 262 # Actually C
  if note == C:  return 262
  if note == CS: return 277
  if note == D:  return 294
  if note == DS: return 311
  if note == E:  return 330
  if note == F:  return 349
  if note == FS: return 370
  if note == G:  return 392
  if note == GS: return 415
  if note == A:  return 440
  if note == AS: return 466
  if note == B:  return 494
  if note == CH:  return 523
  if note == CSH: return 554
  if note == DH:  return 587
  if note == DSH: return 622
  if note == EH:  return 659
  if note == FH:  return 698
  if note == FSH: return 740
  if note == GH:  return 784

def draw_wave(hz):
  # Wave
  points = []
  for i in range(-800, 0):
    p = (math.sin(math.radians(i* (hz/100) ))) * 100
    points.append(p+500)
  for poin in range(len(points)-1):
    pygame.draw.line(screen, BLACK, (poin,points[poin]), (poin,points[poin+1]))

  title_text = reg.render(str(hz) + " hz", True, BLACK)
  screen.blit(title_text, (300, 600))
  pygame.display.flip()

def play_note(note):
  ind = notes.index(note)
  prev = colors[ind]
  colors[ind] = BLACK
  if note == E:
    pygame.time.wait(10)
  note.play()
  draw(colors)
  draw_wave(find_hz(note))
  # Draw title text last, so nothing overwrites it
  
  pygame.display.flip()
  pygame.time.wait(speed)

  # Change
  colors[ind] = prev
  draw(colors)
  draw_wave(find_hz(note))
  freq_text = reg.render(str(find_hz(note)) + " hz", True, BLACK)
  screen.blit(freq_text, (300, 600))
  pygame.display.flip()

# Water Change
def water_change(ind, orig, mod):
  if notes[ind] == orig:
    notes[ind] = mod
    colors[ind] = (0,0,255)
  elif notes[ind] == mod:
    notes[ind] = orig
    colors[ind] = WHITE
  draw(colors)
  draw_wave(find_hz(notes[ind]))

hot_cross_buns = [E, D, C, "w", E, D, C, "w", C, C, C, C, D, D, D, D, E, D, C], [E, D, C, D, E, E, E, "w", D, D, D, "w", E, G, G, "w", E, D, C, D, E, E, E, E, D, D, E, D, C]
twinkle_twinkle = [C, C, G, G, A, A, G, "w", F, F, E, E, D, D, C, "w", G, G, F, F, E, E, D, "w", G, G, F, F, E, E, D, "w", C, C, G, G, A, A, G, "w", F, F, E, E, D, D, C]
high_hot_cross_buns = [EH, DH, CH, "w", EH, DH, CH, "w", CH, CH, CH, CH, DH, DH, DH, DH, EH, DH, CH]
mary = [E, D, C, D, E, E, E, "w", D, D, D, "w", E, G, G, "w", E, D, C, D, E, E, E, E, D, D, E, D, C]
high_mary = [EH, DH, CH, DH, EH, EH, EH, "w", DH, DH, DH, "w", EH, GH, GH, "w", EH, DH, CH, DH, EH, EH, EH, EH, DH, DH, EH, DH, CH]
jingle_bells = [E, E, E, "w", E, E, E, "w", E, G, C, D, E, "w", "w", "w", F, F, F, F, F, E, E, E, E, D, D, E, D, "w", G]
high_jingle_bells = [EH, EH, EH, "w", EH, EH, EH, "w", EH, GH, CH, DH, EH, "w", "w", "w", FH, FH, FH, FH, FH, EH, EH, EH, EH, DH, DH, EH, DH, "w", GH]
happier = [E, D, "w", E, D, "w", E, D, D, C, "w", A, G, E, D, C, D, E, "w", A, G, E, D, C, D, C]
happier_intro = [CH, CH, DH, CH, "w", CH, CH, CH, CH, DH, B, "w", GH, GH, EH, EH, DH, DH, CH, CH, CH, CH, CH, CH, DH, "w", CH, "w", CH, CH, DH, CH, "w", CH, CH, G, CH, DH, B, "w", GH, GH, EH, EH, DH, DH, CH, CH, CH, CH, G, CH, DH, "w", CH]
cheap_thrills = [E, A, B, CH, B, A, A, E, E, E, "w", G, D, D, "w", D, E, A, B, CH, B, A, A, E, E, E, "w", G, D, D, "w", D, E, A, B, CH, B, A, A, E, E, E, "w", G, D, D, "w", D, E, A, B, CH, B, A, A, E, E, E, "w", "w", D]
jingle_bells = [E, E, E, "w", E, E, E, "w", E, G, C, D, E, "w", "w", "w", F, F, F, F, F, E, E, E, E, D, D, E, D, "w", G]
high_jingle_bells = [EH, EH, EH, "w", EH, EH, EH, "w", EH, GH, CH, DH, EH, "w", "w", "w", FH, FH, FH, FH, FH, EH, EH, EH, EH, DH, DH, EH, DH, "w", GH]

songs = [hot_cross_buns, mary, twinkle_twinkle, high_hot_cross_buns, high_mary, jingle_bells, high_jingle_bells]

save = C
played = False
speed = 300
running = True
while running:
  draw(colors)
  draw_wave(find_hz(save))

  played = False
  # Events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      x,y = pygame.mouse.get_pos()

      # Bowls
      for bowl in bowls:
        if x in range(bowl[0]-20,bowl[0]+20) and y in range(bowl[1]-125,bowl[1]+125):
          note = notes[bowls.index(bowl)]
          play_note(note)
          save = note
          played = True

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_SPACE:
        reset()
      if event.key == pygame.K_1:
        water_change(0, C, BL)
      if event.key == pygame.K_2:
        water_change(1, D, CS)
      if event.key == pygame.K_3:
        water_change(2, E, DS)
      if event.key == pygame.K_4:
        water_change(3, F, E)
      if event.key == pygame.K_5:
        water_change(4, G, FS)
      if event.key == pygame.K_6:
        water_change(5, A, GS)
      if event.key == pygame.K_7:
        water_change(6, B, AS)
      if event.key == pygame.K_8:
        water_change(7, CH, B)
      if event.key == pygame.K_9:
        water_change(8, DH, CSH)
      if event.key == pygame.K_0:
        water_change(9, EH, DSH)
      if event.key == pygame.K_COMMA:
        water_change(10, FH, EH)
      if event.key == pygame.K_PERIOD:
        water_change(11, GH, FSH)
      if event.key == pygame.K_UP:
        song = random.choice(songs)
        speed = 300
        reset()
        for note in song:
          if note == "w":
            pygame.time.wait(speed)
            #clock.tick(speed)
          else:
            print(note)
            try:
              play_note(note)
            except:
              pass
            #clock.tick(speed)
          pygame.time.wait(speed)
          #clock.tick(speed)


  draw(colors)
  draw_wave(find_hz(save))
  pygame.display.flip()
  clock.tick(speed)
