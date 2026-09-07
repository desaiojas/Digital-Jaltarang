

import random
import os
import math
import streamlit as st

# Streamlit Setup
st.set_page_config(page_title="Jaltarang", layout="wide")

WHITE = "#FFFFFF"
BLACK = "#000000"
BLUE = "#0000FF"

### Sound Loading ### DOWN


# File conversion

# Get all M4A files in current directory
#m4a_files = [f for f in os.listdir('.') if f.endswith('.m4a')]

# Convert each file
#for m4a_file in m4a_files:
    # Load the M4A file
#    audio = AudioSegment.from_file(m4a_file, format="m4a")

    # Create WAV filename
#    wav_file = m4a_file.replace('.m4a', '.wav')

    # Export as WAV
#    audio.export(wav_file, format="wav")
#    print(f"Converted {m4a_file} to {wav_file}")

# Sounds
BL = "C Jaltarang.wav"
C = "C Jaltarang.wav"
CS = "C# Jaltarang.wav"
D = "D Jaltarang.wav"
DS = "D# Jaltarang.wav"
E = "E Jaltarang.wav"
F = "F Jaltarang.wav"
FS = "F# Jaltarang.wav"
G = "G Jaltarang.wav"
GS = "G# Jaltarang.wav"
A = "A Jaltarang.wav"
AS = "A# Jaltarang.wav"
B = "B Jaltarang.wav"
CH = "CH Jaltarang.wav"
CSH = "C#H Jaltarang.wav"
DH = "DH Jaltarang.wav"
DSH = "D#H Jaltarang.wav"
EH = "EH Jaltarang.wav"
FH = "FH Jaltarang.wav"
FSH = "F#H Jaltarang.wav"
GH = "GH Jaltarang.wav"

### Sound Loading ### UP

ALL_PITCHES = [BL, C, CS, D, DS, E, F, FS, G, GS, A, AS, B, CH, CSH, DH, DSH, EH, FH, FSH, GH]

if 'started' not in st.session_state:
    st.session_state.started = False
if 'notes' not in st.session_state:
    st.session_state.notes = [C,D,E,F,G,A,B,CH,DH,EH,FH,GH]
if 'colors' not in st.session_state:
    st.session_state.colors = [WHITE]*12
if 'water_states' not in st.session_state:
    st.session_state.water_states = [0]*12

# Intro / Landing Page
if not st.session_state.started:
    st.title("Digital Jaltarang")
    st.write("Welcome to the Digital Jaltarang! This instrument consists of bowls filled with water to create musical notes.")
    st.write("**Instructions:**")
    st.write("1. Click the play button below any bowl to hear its sound.")
    st.write("2. Use **Half-Fill** to lower the pitch by a half-step.")
    st.write("3. Use **Full-Fill** to lower the pitch by a full step.")
    st.write("4. Use **Empty** to return the bowl to its base note.")
    if st.button("Start Playing", type="primary"):
        st.session_state.started = True
        st.rerun()
    st.stop()

# Circle coordinates and drawing
def draw():
    cols = st.columns(12)
    # Semicircle Y-offsets
    y_offsets = [0, 40, 70, 90, 100, 105, 105, 100, 90, 70, 40, 0]
    
    for i in range(12):
        with cols[i]:
            note = st.session_state.notes[i]
            color = st.session_state.colors[i]
            hz = find_hz(note)
            
            st.markdown(f"<div style='margin-top: {y_offsets[i]}px; width: 60px; height: 60px; border-radius: 50%; background-color: {color}; border: 3px solid black; box-shadow: 2px 2px 5px gray;'></div>", unsafe_allow_html=True)
            st.caption(f"{hz} hz")
            
            # Direct exact filename match based on GitHub repo
            st.audio(note, format="audio/wav")
            
            if st.button("½ Fill", key=f"h_{i}"):
                water_change(i, 1)
            if st.button("Full", key=f"f_{i}"):
                water_change(i, 2)
            if st.button("Empty", key=f"e_{i}"):
                water_change(i, 0)

def reset():
    st.session_state.notes = [C,D,E,F,G,A,B,CH,DH,EH,FH,GH]
    st.session_state.colors = [WHITE]*12
    st.session_state.water_states = [0]*12
    st.rerun()

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

# Water Change
def water_change(ind, fill_level):
    base_notes = [C,D,E,F,G,A,B,CH,DH,EH,FH,GH]
    base_note = base_notes[ind]
    
    try:
        base_idx = ALL_PITCHES.index(base_note)
        new_idx = max(0, base_idx - fill_level) 
        
        st.session_state.notes[ind] = ALL_PITCHES[new_idx]
        st.session_state.water_states[ind] = fill_level
        
        if fill_level == 1:
            st.session_state.colors[ind] = "#ADD8E6"
        elif fill_level == 2:
            st.session_state.colors[ind] = BLUE
        else:
            st.session_state.colors[ind] = WHITE
            
        st.rerun()
    except ValueError:
        pass

hot_cross_buns = [E, D, C, "w", E, D, C, "w", C, C, C, C, D, D, D, D, E, D, C]
twinkle_twinkle = [C, C, G, G, A, A, G, "w", F, F, E, E, D, D, C, "w", G, G, F, F, E, E, D, "w", G, G, F, F, E, E, D, "w", C, C, G, G, A, A, G, "w", F, F, E, E, D, D, C]
high_hot_cross_buns = [EH, DH, CH, "w", EH, DH, CH, "w", CH, CH, CH, CH, DH, DH, DH, DH, EH, DH, CH]
mary = [E, D, C, D, E, E, E, "w", D, D, D, "w", E, G, G, "w", E, D, C, D, E, E, E, E, D, D, E, D, C]
high_mary = [EH, DH, CH, DH, EH, EH, EH, "w", DH, DH, DH, "w", EH, GH, GH, "w", EH, DH, CH, DH, EH, EH, EH, EH, DH, DH, EH, DH, CH]
happier = [E, D, "w", E, D, "w", E, D, D, C, "w", A, G, E, D, C, D, E, "w", A, G, E, D, C, D, C]
happier_intro = [CH, CH, DH, CH, "w", CH, CH, CH, CH, DH, B, "w", GH, GH, EH, EH, DH, DH, CH, CH, CH, CH, CH, CH, DH, "w", CH, "w", CH, CH, DH, CH, "w", CH, CH, G, CH, DH, B, "w", GH, GH, EH, EH, DH, DH, CH, CH, CH, CH, G, CH, DH, "w", CH]
cheap_thrills = [E, A, B, CH, B, A, A, E, E, E, "w", G, D, D, "w", D, E, A, B, CH, B, A, A, E, E, E, "w", G, D, D, "w", D, E, A, B, CH, B, A, A, E, E, E, "w", G, D, D, "w", D, E, A, B, CH, B, A, A, E, E, E, "w", "w", D]
jingle_bells = [E, E, E, "w", E, E, E, "w", E, G, C, D, E, "w", "w", "w", F, F, F, F, F, E, E, E, E, D, D, E, D, "w", G]
high_jingle_bells = [EH, EH, EH, "w", EH, EH, EH, "w", EH, GH, CH, DH, EH, "w", "w", "w", FH, FH, FH, FH, FH, EH, EH, EH, EH, DH, DH, EH, DH, "w", GH]

songs = [hot_cross_buns, mary, twinkle_twinkle, high_hot_cross_buns, high_mary, jingle_bells, high_jingle_bells]

st.markdown("### Digital Jaltarang Controls")
col1, col2 = st.columns(2)
with col1:
    if st.button("Reset All Bowls"):
        reset()

draw()
