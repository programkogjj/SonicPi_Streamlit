import streamlit as st
from psonic import *

# Initialize Sonic Pi Connection
try:
    synth_server.set_parameter('127.0.0.1', 4557, 4560, None)
except Exception as e:
    st.error(f"Could not connect to Sonic Pi: {e}")

st.title("Lekce 1 - Hodnoty, operace a proměnné")

st.markdown("""
V této lekci se naučíme pracovat s tóny, aritmetickými operacemi a proměnnými.
""")

st.divider()

## --- Kapitola 1.1 ---
st.header("1.1 Hodnoty, První tóny")
st.write("Spusťte tlačítko níže pro zahrání noty C4 (60).")
st.image("midi_board.png", caption="hodnoty tónů v MIDI")

if st.button("Play C4"):
    play(60)

### Cvičení 1.1.1: Zahraj tóny
st.subheader("Cvičení 1.1.1: Zahraj tóny postupně")
if st.button("Spustit 3 tóny (1s pauza)"):
    play(60)
    sleep(1)
    play(62)
    sleep(1)
    play(64)

### Cvičení 1.1.2: C dur akord
st.subheader("Cvičení 1.1.2: C dur akord")
if st.button("Spustit Akord"):
    play(60)
    play(64)
    play(67)

### Cvičení 1.1.3: C dur akord rozkladem
st.subheader("Cvičení 1.1.3: C dur akord rozkladem")
if st.button("Spustit Rozklad"):
    for note in [60, 64, 67]:
        play(note)
        sleep(0.5)

st.divider()

## --- Kapitola 1.2 ---
st.header("1.2 Hrajeme si s čísly")
st.markdown("""
Python podporuje tyto operace:
* `+`, `-`, `*`, `/`
* `//` (celočíselné), `%` (modulo), `**` (mocnina)
""")

### Cvičení 1.2.1: Kvartsextakord
st.subheader("Cvičení 1.2.1: Kvartsextakord (odčítání)")
if st.button("Spustit Kvartsextakord"):
    zaklad = 60
    play(zaklad)
    play(zaklad - 5)
    play(zaklad - 8)

st.divider()

## --- Kapitola 1.3 ---
st.header("1.3 Proměnné")

### Cvičení 1.3.1: Aritmetická posloupnost (Zkracování)
st.subheader("Cvičení 1.3.1: Zkracování pauzy")
if st.button("Spustit Zkracování"):
    ton = 50
    pauza = 2.0
    rozdil = 0.5    
    for _ in range(5):
        play(ton)
        sleep(pauza)
        pauza -= rozdil

### Cvičení 1.3.2: Aritmetická posloupnost (Prodlužování)
st.subheader("Cvičení 1.3.2: Aritmetické prodlužování")
if st.button("Spustit Prodlužování (+ 0.3s)"):
    ton = 50
    pauza = 0.3
    for _ in range(5):
        play(ton)
        sleep(pauza)
        pauza += 0.3

### Cvičení 1.3.3: Geometrická posloupnost (Prodlužování)
st.subheader("Cvičení 1.3.3: Geometrické prodlužování")
if st.button("Spustit Prodlužování (2x)"):
    ton = 50
    pauza = 0.3
    for _ in range(5):
        play(ton)
        sleep(pauza)
        pauza *= 2

st.divider()

## --- Kapitola 1.4 ---
st.header("1.4 Pravidla závorkování")

### Cvičení 1.4.1: Priority Check
st.subheader("Cvičení 1.4.1: Priority Check")
col1, col2 = st.columns(2)
with col1:
    if st.button("Verze A: ton + 12 / 2"):
        play(60 + 12 / 2) # 66
with col2:
    if st.button("Verze B: (ton + 12) / 2"):
        play((60 + 12) / 2) # 36


### Cvičení 1.4.1: Priority Check
st.subheader("Cvičení 1.4.2: Kontrola závorek")
if st.button("Spustit závorky"):
    play(60 + (4 * 2))      
    sleep((1 / 2) + (1 / 4))
    play(60 + (2 * 2))

st.divider()

## --- Kapitola 1.5 ---
st.header("1.5 Změna hodnoty proměnné")

### Cvičení 1.5.1: Přepis hodnoty za chodu
st.subheader("Cvičení 1.5.1: Matematický řetězec")
if st.button("Zahrát finální tón"):
    a = 30
    a *= 5   # 150
    a -= 50  # 100
    a /= 20  # 5
    a **= 3  # 125
    a %= 45  # 35
    st.write(f"Výsledná hodnota tónu: {a}")
    play(a)

### Cvičení 1.5.2: Změna intenzity a disribuce zvuku
st.subheader("Cvičení 1.5.2: Změna intenzity a disribuce zvuku")
if st.button("Zahrát výstup 1.5.2"):
    play(60, amp=1, pan=-1)
    sleep(0.5)
    
    # Tón 2: Tichý, vpravo
    play(64, amp=0.3, pan=1)
    sleep(0.5)
    
    # Tón 3: Střední hlasitost, vlevo
    play(67, amp=0.7, pan=-1)
    sleep(0.5)
    
    # Tón 4: Postupné utichnutí, vpravo
    play(72, amp=0.1, pan=1)
    sleep(0.5)

st.divider()

###Cvičení 1.6.1: absolutní hodnota
st.subheader("Cvičení 1.6.1: Absolutní hodnota")
if st.button("Zahrát výstup 1.6.1"):
    a = abs(70 - 120)
    play(a)