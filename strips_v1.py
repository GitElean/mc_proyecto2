from javax.sound.midi import MidiSystem, ShortMessage, Synthesizer
from time import sleep
import threading

# Inicializar el sintetizador MIDI
synth = MidiSystem.getSynthesizer()
synth.open()
channels = synth.getChannels()

BPM = 150
beat_duration = 60.0 / BPM

def play_note(channel, note, duration, volume=93):
    # Crear y enviar un mensaje para tocar la nota
    msg_on = ShortMessage()
    msg_on.setMessage(ShortMessage.NOTE_ON, channel, note, volume)
    channels[channel].noteOn(note, volume)
    
    sleep(duration * beat_duration)
    
    # Apagar la nota
    msg_off = ShortMessage()
    msg_off.setMessage(ShortMessage.NOTE_OFF, channel, note, volume)
    channels[channel].noteOff(note, volume)

def guitar():
    sleep(8)
    for _ in range(6):
        play_note(0, 52, 1.5)  # E3
        play_note(0, 52, 0.5)  # E3
        play_note(0, 55, 0.8)  # G3
        play_note(0, 52, 0.7)  # E3
        play_note(0, 50, 0.5)  # D3
        play_note(0, 48, 2)    # C3
        play_note(0, 47, 2)    # B2
    
    # Continúa con las otras partes...

def bass():
    for _ in range(7):
        play_note(1, 40, 1.5)  # E2
        play_note(1, 40, 0.5)  # E2
        play_note(1, 43, 0.8)  # G2
        play_note(1, 40, 0.7)  # E2
        play_note(1, 38, 0.5)  # D2
        play_note(1, 36, 2)    # C1
        play_note(1, 35, 2)    # B1

    # Continúa con las otras partes...

def drums():
    sleep(8)
    for _ in range(24):
        play_note(9, 36, 1)  # Bass Drum
        play_note(9, 38, 1)  # Snare Drum
    
    # Continúa con las otras partes...

def piano_or_voice():
    sleep(22.5)
    play_note(2, 62, 0.5)  # D4
    play_note(2, 64, 0.5)  # E4
    play_note(2, 62, 0.5)  # D4
    play_note(2, 68, 0.5)  # G#4
    play_note(2, 61, 0.5)  # C#4
    play_note(2, 64, 4.5)  # E4
    
    # Continúa con las otras partes...

# Ejecutar los hilos
threading.Thread(target=guitar).start()
threading.Thread(target=bass).start()
threading.Thread(target=drums).start()
threading.Thread(target=piano_or_voice).start()
