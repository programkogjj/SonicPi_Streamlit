import streamlit as st
import os

# Definujeme cestu ke složce se zvuky
SOUNDS_DIR = "sounds"

def play_sound(filename):
    path = os.path.join(SOUNDS_DIR, filename)
    if os.path.exists(path):
        st.audio(path)
    else:
        st.error(f"Soubor {filename} nebyl nalezen v adresáři {SOUNDS_DIR}")

st.title("Lekce 1 - Hodnoty, operace a proměnné")

st.markdown("""
V této lekci se naučíme pracovat s tóny, aritmetickými operacemi a proměnnými.
""")

st.divider()

## --- Kapitola 1.1 ---
st.header("1.1 Hodnoty, První tóny")
st.write("Poslechněte si notu C4 (60).")
st.image("midi_board.png", caption="hodnoty tónů v MIDI")

if st.button("Přehrát C4"):
    play_sound("kap1_1.wav")

### Cvičení 1.1.1
st.subheader("Cvičení 1.1.1: Zahraj tóny postupně")
if st.button("Poslechnout 3 tóny"):
    play_sound("cvic1_1_1.wav")

### Cvičení 1.1.2
st.subheader("Cvičení 1.1.2: C dur akord")
if st.button("Poslechnout Akord"):
    play_sound("cvic1_1_2.wav")

### Cvičení 1.1.3
st.subheader("Cvičení 1.1.3: C dur akord rozkladem")
if st.button("Poslechnout Rozklad"):
    play_sound("cvic1_1_3.wav")

st.divider()

## --- Kapitola 1.2 ---
st.header("1.2 Hrajeme si s čísly")
### Cvičení 1.2.1
st.subheader("Cvičení 1.2.1: Kvartsextakord (odčítání)")
if st.button("Poslechnout Kvartsextakord"):
    play_sound("cvic1_2_1.wav")

st.divider()

## --- Kapitola 1.3 ---
st.header("1.3 Proměnné")

### Cvičení 1.3.1
st.subheader("Cvičení 1.3.1: Zkracování pauzy")
if st.button("Poslechnout Zkracování"):
    play_sound("cvic1_3_1.wav")

### Cvičení 1.3.2
st.subheader("Cvičení 1.3.2: Aritmetické prodlužování")
if st.button("Poslechnout Prodlužování (+ 0.3s)"):
    play_sound("cvic1_3_2.wav")

### Cvičení 1.3.3
st.subheader("Cvičení 1.3.3: Geometrické prodlužování")
if st.button("Poslechnout Prodlužování (2x)"):
    play_sound("cvic1_3_3.wav")

st.divider()

## --- Kapitola 1.4 ---
st.header("1.4 Pravidla závorkování")

### Cvičení 1.4.1
st.subheader("Cvičení 1.4.1: Priority Check")
col1, col2 = st.columns(2)
with col1:
    if st.button("Verze A: ton + 12 / 2"):
        play_sound("cvic1_4_1A.wav")
with col2:
    if st.button("Verze B: (ton + 12) / 2"):
        play_sound("cvic1_4_1B.wav")

### Cvičení 1.4.2
st.subheader("Cvičení 1.4.2: Kontrola závorek")
if st.button("Poslechnout závorky"):
    play_sound("cvic1_4_2.wav")

st.divider()

## --- Kapitola 1.5 ---
st.header("1.5 Změna hodnoty proměnné")

### Cvičení 1.5.1
st.subheader("Cvičení 1.5.1: Matematický řetězec")
if st.button("Poslechnout finální tón"):
    st.write("Výsledná hodnota tónu: 35")
    play_sound("cvic1_5_1.wav")

### Cvičení 1.5.2
st.subheader("Cvičení 1.5.2: Změna intenzity a distribuce zvuku")
if st.button("Poslechnout výstup 1.5.2"):
    play_sound("cvic1_5_2.wav")

st.divider()

### Cvičení 1.6.1
st.subheader("Cvičení 1.6.1: Absolutní hodnota")
if st.button("Poslechnout výstup 1.6.1"):
    play_sound("cvic1_6_1.wav")