import os
import math
import time
import base64
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Digital Jaltarang", layout="wide")

st.markdown("""
<style>
    /* Main app background gradient */
    .stApp {
        background: linear-gradient(135deg, #e6d7c3 0%, #c5a880 100%);
    }

    /* Darker matching sidebar */
    [data-testid="stSidebar"] {
        background-color: #b5956c;
    }

    /* Main text */
    h1, h2, h3, p, div.stMarkdown, li {
        color: #2c1e16 !important;
    }

    /* Default buttons */
    .stButton > button {
        background-color: #f8f9fa !important;
        color: #2c1e16 !important;
        border: 1px solid #b5956c !important;
    }

    .stButton > button:hover {
        background-color: #ffffff !important;
        border-color: #2c1e16 !important;
    }

    /* ===================================== */
    /* SIDEBAR BUTTONS — KEEP WIDE           */
    /* ===================================== */

    [data-testid="stSidebar"] .stButton > button {
        min-width: 200px !important;
    }

    /* ===================================== */
    /* START PLAYING — KEEP WIDE             */
    /* ===================================== */

    .stButton > button[kind="primary"] {
        min-width: 170px !important;
    }

    /* ===================================== */
    /* DEFAULT DESKTOP BOWL LAYOUT           */
    /* ===================================== */

    [data-testid="column"] {
        overflow: visible !important;
    }

    [data-testid="column"] [data-testid="stButton"] {
        width: 120px !important;
        min-width: 120px !important;
        max-width: 120px !important;
    }

    [data-testid="column"] [data-testid="stButton"] > button {
        width: 120px !important;
        min-width: 120px !important;
        max-width: 120px !important;
        flex: 0 0 120px !important;
        box-sizing: border-box !important;
        padding-left: 2px !important;
        padding-right: 2px !important;
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: clip !important;
        word-break: keep-all !important;
        line-height: 1.1 !important;
    }

    /* Override Streamlit's text clipping at EVERY level */
    [data-testid="column"] [data-testid="stButton"] > button *,
    [data-testid="column"] [data-testid="stButton"] > button p,
    [data-testid="column"] [data-testid="stButton"] > button span,
    [data-testid="column"] [data-testid="stButton"] > button div {
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: clip !important;
        max-width: none !important;
        text-align: center !important;
    }

    /* Keep the actual label at normal size */
    [data-testid="column"] [data-testid="stButton"] > button p {
        font-size: 14px !important;
        color: #2c1e16 !important;
    }

    /* Desktop Spacing */
    .title-spacer {
        margin-top: 25px;
    }

    /* ===================================== */
    /* MOBILE SHRINK-TO-FIT SOLUTION         */
    /* ===================================== */

    @media (max-width: 768px) {
        /* 1. Force columns to stay in one row */
        div[data-testid="stHorizontalBlock"] {
            flex-wrap: nowrap !important;
            gap: 1px !important;
            margin-top: -15px !important; /* Pulls the bowls up closer to the title */
        }

        /* Hide the massive gap below the reminder on mobile */
        .title-spacer {
            display: none !important;
        }
        
        /* 2. Unlock the hardcoded widths so they can squish */
        div[data-testid="column"] {
            min-width: 0px !important;
            max-width: none !important;
            width: auto !important;
            flex: 1 1 0% !important;
        }

        div[data-testid="column"] [data-testid="stButton"] {
            width: 100% !important;
            min-width: 0px !important;
            max-width: none !important;
        }

        /* 3. Shrink the buttons dramatically to fit */
        div[data-testid="column"] [data-testid="stButton"] > button {
            width: 100% !important;
            min-width: 0px !important;
            max-width: none !important;
            flex: 1 1 auto !important;
            padding: 2px 0px !important;
            min-height: 28px !important; /* Ensure they have height for emojis */
        }
        
        /* 4. CSS Emoji Injection - Hides text and replaces with emojis */
        
        /* Hide all button text */
        div[data-testid="column"] [data-testid="stButton"] > button p {
            font-size: 0px !important; 
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Button 1: ½ Fill -> 🌗 */
        div[data-testid="column"] div.element-container:nth-of-type(3) [data-testid="stButton"] button p::before {
            content: "🌗";
            font-size: 16px !important;
        }
        /* Button 2: Full -> 🌕 */
        div[data-testid="column"] div.element-container:nth-of-type(4) [data-testid="stButton"] button p::before {
            content: "🌕";
            font-size: 16px !important;
        }
        /* Button 3: Empty -> 🌑 */
        div[data-testid="column"] div.element-container:nth-of-type(5) [data-testid="stButton"] button p::before {
            content: "🌑";
            font-size: 16px !important;
        }

        /* 5. Force shrink captions (Hz text) */
        div[data-testid="stCaptionContainer"] p {
            font-size: 9px !important;
            line-height: 1.1 !important;
            margin-bottom: 2px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

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

ALL_PITCHES = [C, CS, D, DS, E, F, FS, G, GS, A, AS, B, CH, CSH, DH, DSH, EH, FH, FSH, GH]

# 12 Bowls for the standard C Major Scale
BASE_NOTES = [C, D, E, F, G, A, B, CH, DH, EH, FH, GH]

if 'started' not in st.session_state:
    st.session_state.started = False
if 'notes' not in st.session_state:
    st.session_state.notes = BASE_NOTES.copy()
if 'water_states' not in st.session_state:
    st.session_state.water_states = [0]*12
if 'last_hz' not in st.session_state:
    st.session_state.last_hz = 262

def play_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            audio_html = f'<audio autoplay src="data:audio/wav;base64,{b64}"></audio>'
            st.session_state.audio_player.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        pass 

def find_hz(note):
    hz_map = {C: 262, CS: 277, D: 294, DS: 311, E: 330, F: 349, FS: 370, G: 392, GS: 415, A: 440, AS: 466, B: 494, CH: 523, CSH: 554, DH: 587, DSH: 622, EH: 659, FH: 698, FSH: 740, GH: 784}
    return hz_map.get(note, 262)

def generate_wave(hz):
    return [math.sin(math.radians(i * (hz / 100.0))) * 100 for i in range(300)]

def get_note_label(note_filename):
    clean_name = note_filename.replace(" Jaltarang.wav", "")
    if "H" in clean_name:
        return clean_name.replace("H", "") + " (High)"
    return clean_name

def water_change(ind, fill_level):
    base_note = BASE_NOTES[ind]
    try:
        base_idx = ALL_PITCHES.index(base_note)
        # Prevents index from dropping below 0 (C)
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

if not st.session_state.started:
    st.title("Digital Jaltarang Bowls")
    st.write("This instrument consists of bowls filled with water to create musical notes.")
    st.write("**Instructions:**")
    st.write("1. Click any **bowl** to hear its sound.")
    st.write("2. Use **½ Fill / 🌗** to lower the pitch by a half-step (easily tune the major scale into a minor scale).")
    st.write("3. Use **Full / 🌕** to lower the pitch by a full step.")
    st.write("4. Use **Empty / 🌑** to return the bowl to its base note.")
    st.write("5. Watch the physical sound waves react in real-time as you play!")
    if st.button("Start Playing", type="primary"):
        st.session_state.started = True
        st.rerun()
    st.stop()

title_col, spacer_col, control_col1, control_col2 = st.columns([3, 1, 1, 1])
with title_col:
    st.markdown("### Bowls (C Major Scale)")
with control_col1:
    if st.button("Return to Instructions"):
        st.session_state.started = False
        st.rerun()
with control_col2:
    if st.button("Reset All Bowls"):
        reset()
        st.rerun()

st.markdown("""
<div style="
    text-align: center;
    margin-top: 8px;
    margin-bottom: 10px;
    font-weight: 600;
    color: #2c1e16;
    font-size: 15px;
">
    Reminder: Hold your phone/device horizontally for the best experience.
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='title-spacer'></div>", unsafe_allow_html=True)
st.session_state.audio_player = st.empty() 

# 12 bowls layout
cols = st.columns(12, gap="small")
y_offsets = [80, 76, 68, 52, 30, 0, 0, 30, 52, 68, 76, 80]

# 0: Ceramic White/Gray, 1: Vibrant Aqua, 2: Deep Sapphire
colors = {0: "#F8F9FA", 1: "#00B4D8", 2: "#03045E"} 

for i in range(12):
    with cols[i]:
        note = st.session_state.notes[i]
        level = st.session_state.water_states[i]
        hz = find_hz(note)
        note_label = get_note_label(note)

        try:
            with open(note, "rb") as f:
                audio_b64 = base64.b64encode(f.read()).decode()
        except FileNotFoundError:
            audio_b64 = ""

        bowl_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                html, body {{
                    margin: 0;
                    padding: 0;
                    width: 100%;
                    height: 190px;
                    background: transparent !important;
                    overflow: hidden;
                }}

                .bowl-stage {{
                    position: relative;
                    width: 100%;
                    height: 190px;
                    overflow: visible;
                }}

                /* Default Desktop Size */
                .bowl {{
                    position: absolute;
                    top: {y_offsets[i]}px;
                    left: 50%;
                    transform: translateX(-50%);
                    width: 88px;
                    height: 88px;
                    border-radius: 50%;
                    background: radial-gradient(
                        circle at 30% 30%,
                        #ffffff 10%,
                        {colors[level]} 80%,
                        #1a1a1a 100%
                    );
                    border: 3px solid #8D99AE;
                    box-shadow:
                        inset -8px -8px 20px rgba(0,0,0,0.6),
                        5px 5px 15px rgba(0,0,0,0.3);
                    cursor: pointer;
                    box-sizing: border-box;
                    transition: transform 0.08s ease;
                }}

                .bowl:active {{
                    transform: translateX(-50%) scale(0.97);
                }}
                
                /* Mobile Size overrides */
                @media (max-width: 80px) {{
                    .bowl {{
                        width: 36px !important;
                        height: 36px !important;
                        /* Restores the curve (0.4 multiplier) but pushes the entire curve 100px downwards */
                        top: calc(100px + ({y_offsets[i]}px * 0.4)) !important; 
                        bottom: auto !important; 
                        border-width: 2px !important;
                        box-shadow: 
                            inset -3px -3px 8px rgba(0,0,0,0.6),
                            2px 2px 5px rgba(0,0,0,0.3) !important;
                    }}
                }}
            </style>
        </head>

        <body>
            <div class="bowl-stage">
                <div class="bowl" id="bowl"></div>
            </div>

            <script>
                const bowl = document.getElementById("bowl");
                const audio = new Audio(
                    "data:audio/wav;base64,{audio_b64}"
                );

                bowl.addEventListener("click", function() {{
                    audio.currentTime = 0;
                    audio.play().catch(function(error) {{
                        console.log("Audio playback failed:", error);
                    }});
                }});
            </script>
        </body>
        </html>
        """

        components.html(
            bowl_html,
            width="stretch",
            height=190,
            scrolling=False
        )

        st.caption(f"<div style='text-align: center; color: #2c1e16;'><b>{note_label}</b><br>{hz} Hz</div>", unsafe_allow_html=True)

        st.button("½ Fill", key=f"h_{i}", use_container_width=True, on_click=water_change, args=(i, 1))
        st.button("Full", key=f"f_{i}", use_container_width=True, on_click=water_change, args=(i, 2))
        st.button("Empty", key=f"e_{i}", use_container_width=True, on_click=water_change, args=(i, 0))

st.divider()
st.markdown(f"### Frequencies: {st.session_state.last_hz} Hz")
st.line_chart(generate_wave(st.session_state.last_hz), height=200, use_container_width=True)
