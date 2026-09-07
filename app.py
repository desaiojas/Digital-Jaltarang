import os
import math
import time
import base64
import streamlit as st

st.set_page_config(page_title="Digital Jaltarang", layout="wide")

# File conversion
# Get all M4A files in current directory
# m4a_files = [f for f in os.listdir('.') if f.endswith('.m4a')]
# Convert each file
# for m4a_file in m4a_files:
#     audio = AudioSegment.from_file(m4a_file, format="m4a")
#     wav_file = m4a_file.replace('.m4a', '.wav')
#     audio.export(wav_file, format="wav")
#     print(f"Converted {m4a_file} to {wav_file}")

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

ALL_PITCHES = [BL, C, CS, D, DS, E, F, FS, G, GS, A, AS, B, CH, CSH, DH, DSH, EH, FH, FSH, GH]
BASE_NOTES = [C, D, E, F, G, A, B, CH, DH, EH, FH, GH]

if 'started' not in st.session_state:
    st.session_state.started = False
if 'notes' not in st.session_state:
    st.session_state.notes = BASE_NOTES.copy()
if 'water_states' not in st.session_state:
    st.session_state.water_states = [0]*12
if 'last_hz' not in st.session_state:
    st.session_state.last_hz = 262

# Audio Injection for seamless playback
def play_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            audio_html = f'<audio autoplay src="data:audio/wav;base64,{b64}"></audio>'
            st.session_state.audio_player.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        pass # Silently fail if wav is missing to prevent crash

def find_hz(note):
    hz_map = {BL: 262, C: 262, CS: 277, D: 294, DS: 311, E: 330, F: 349, FS: 370, G: 392, GS: 415, A: 440, AS: 466, B: 494, CH: 523, CSH: 554, DH: 587, DSH: 622, EH: 659, FH: 698, FSH: 740, GH: 784}
    return hz_map.get(note, 262)

def generate_wave(hz):
    # Pure Python sine wave generation (no numpy needed)
    return [math.sin(math.radians(i * (hz / 100.0))) * 100 for i in range(300)]

def water_change(ind, fill_level):
    base_note = BASE_NOTES[ind]
    try:
        base_idx = ALL_PITCHES.index(base_note)
        new_idx = max(0, base_idx - fill_level) 
        st.session_state.notes[ind] = ALL_PITCHES[new_idx]
        st.session_state.water_states[ind] = fill_level
        st.session_state.last_hz = find_hz(ALL_PITCHES[new_idx])
        play_audio(ALL_PITCHES[new_idx])
    except ValueError:
        pass

def reset():
    st.session_state.notes = BASE_NOTES.copy()
    st.session_state.water_states = [0]*12

# Songs Dictionary
songs = {
    "Hot Cross Buns": [E, D, C, "w", E, D, C, "w", C, C, C, C, D, D, D, D, E, D, C],
    "Twinkle Twinkle": [C, C, G, G, A, A, G, "w", F, F, E, E, D, D, C, "w", G, G, F, F, E, E, D, "w", G, G, F, F, E, E, D, "w", C, C, G, G, A, A, G, "w", F, F, E, E, D, D, C],
    "Mary Had A Little Lamb": [E, D, C, D, E, E, E, "w", D, D, D, "w", E, G, G, "w", E, D, C, D, E, E, E, E, D, D, E, D, C],
    "Jingle Bells": [E, E, E, "w", E, E, E, "w", E, G, C, D, E, "w", "w", "w", F, F, F, F, F, E, E, E, E, D, D, E, D, "w", G]
}

def play_song(song_notes):
    for note in song_notes:
        if note == "w":
            time.sleep(0.4)
        else:
            play_audio(note)
            st.session_state.last_hz = find_hz(note)
            time.sleep(0.4)

# ----------------- UI RENDERING -----------------

if not st.session_state.started:
    st.title("Digital Jaltarang")
    st.write("Welcome to the Digital Jaltarang! This instrument consists of bowls filled with water to create musical notes.")
    st.write("**Instructions:**")
    st.write("1. Click the **Play** button below any bowl to hear its sound.")
    st.write("2. Use **½ Fill** to lower the pitch by a half-step.")
    st.write("3. Use **Full** to lower the pitch by a full step.")
    st.write("4. Use **Empty** to return the bowl to its base note.")
    st.write("5. Watch the physical sound waves react in real-time as you play!")
    if st.button("Start Playing", type="primary"):
        st.session_state.started = True
        st.rerun()
    st.stop()

# Sidebar Controls
with st.sidebar:
    st.title("Controls")
    if st.button("Return to Instructions"):
        st.session_state.started = False
        st.rerun()
    
    st.divider()
    if st.button("Reset All Bowls"):
        reset()
        st.rerun()
        
    st.divider()
    st.subheader("Play Example Songs")
    selected_song = st.selectbox("Choose a song:", list(songs.keys()))
    if st.button(f"Play {selected_song}"):
        play_song(songs[selected_song])

# Main Interface
st.markdown("### The Instrument")
st.session_state.audio_player = st.empty() # Invisible container for audio playback

# Semicircle Layout
cols = st.columns(12)
y_offsets = [0, 40, 70, 90, 100, 105, 105, 100, 90, 70, 40, 0]
colors = {0: "#F5F5F5", 1: "#87CEFA", 2: "#4169E1"} # Empty, Half (Light Blue), Full (Royal Blue)

for i in range(12):
    with cols[i]:
        note = st.session_state.notes[i]
        level = st.session_state.water_states[i]
        hz = find_hz(note)
        
        # 3D CSS Bowl rendering
        bowl_html = f"""
        <div style='
            margin-top: {y_offsets[i]}px; 
            margin-bottom: 20px;
            width: 100%; 
            aspect-ratio: 1; 
            border-radius: 50%; 
            background: radial-gradient(circle at 35% 35%, #ffffff, {colors[level]}); 
            border: 4px solid #2C3E50; 
            box-shadow: inset -5px -5px 15px rgba(0,0,0,0.5), 5px 5px 10px rgba(0,0,0,0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: {'#333' if level == 0 else '#fff'};
        '>
        </div>
        """
        st.markdown(bowl_html, unsafe_allow_html=True)
        st.caption(f"<div style='text-align: center;'><b>{hz} hz</b></div>", unsafe_allow_html=True)
        
        if st.button("▶", key=f"p_{i}", use_container_width=True):
            st.session_state.last_hz = hz
            play_audio(note)
            
        # Compact tuning buttons
        st.button("½ Fill", key=f"h_{i}", use_container_width=True, on_click=water_change, args=(i, 1))
        st.button("Full", key=f"f_{i}", use_container_width=True, on_click=water_change, args=(i, 2))
        st.button("Empty", key=f"e_{i}", use_container_width=True, on_click=water_change, args=(i, 0))

st.divider()
st.markdown(f"### Frequency Visualizer: {st.session_state.last_hz} Hz")
# Dynamic Sine Wave Plot
st.line_chart(generate_wave(st.session_state.last_hz), height=200, use_container_width=True)
