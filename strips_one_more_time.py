from javax.sound.midi import MidiSystem, ShortMessage, Synthesizer
from time import sleep
import threading

# Inicializar el sintetizador MIDI
synth = MidiSystem.getSynthesizer()
synth.open()
channels = synth.getChannels()

# Cargar el banco de sonidos y seleccionar los instrumentos
synth.loadInstrument(synth.getDefaultSoundbank().getInstruments()[0])
channels[0].programChange(27)  # Guitarra eléctrica
channels[1].programChange(33)  # Bajo sintético 2
channels[2].programChange(80)  # Sintetizador envolvente
channels[3].programChange(89)  # Sintetizador brillante (estilo Daft Punk)
channels[9].programChange(0)   # Batería acústica
channels[10].programChange(0)   # Batería acústica

BPM = 125
beat_duration = 60.0 / BPM

def play_note(channel, note, duration, volume=93):
    msg_on = ShortMessage()
    msg_on.setMessage(ShortMessage.NOTE_ON, channel, note, volume)
    channels[channel].noteOn(note, volume)
    
    sleep(duration * beat_duration)
    
    msg_off = ShortMessage()
    msg_off.setMessage(ShortMessage.NOTE_OFF, channel, note, volume)
    channels[channel].noteOff(note, volume)

################################################
################################################
################################################



################################################
################################################
################################################
def play_drum_combination_1():

          # Crear y enviar los mensajes para tocar bombo, hi-hat con pedal y caja al mismo tiempo
    msg_on_bass = ShortMessage()
    msg_on_bass.setMessage(ShortMessage.NOTE_ON, 9, 36, 93)  # Bombo (Bass Drum)
    
    msg_on_hihat = ShortMessage()
    msg_on_hihat.setMessage(ShortMessage.NOTE_ON, 9, 44, 93)  # Hi-Hat cerrado con pedal
    
    msg_on_snare = ShortMessage()
    msg_on_snare.setMessage(ShortMessage.NOTE_ON, 9, 38, 93)  # Caja (Snare Drum)
    
    # Enviar las notas simultáneamente
    channels[9].noteOn(36, 93)  # Bombo
    channels[9].noteOn(44, 93)  # Hi-Hat con pedal
    channels[9].noteOn(38, 93)  # Caja
    
    # Esperar la duración de la nota
    sleep(1.5 * beat_duration)
    
    # Apagar las notas después de la duración
    channels[9].noteOff(36, 93)
    channels[9].noteOff(44, 93)
    channels[9].noteOff(38, 93)
    
 
def play_drum_combination_2():
    # Crear y enviar los mensajes para tocar bombo, caja, hi-hat cerrado y hi-hat con pedal simultáneamente
    channels[9].noteOn(36, 93)  # Bombo (Bass Drum)
    channels[9].noteOn(38, 93)  # Caja (Snare Drum)
    channels[9].noteOn(42, 93)  # Hi-Hat cerrado
    channels[9].noteOn(44, 93)  # Hi-Hat con pedal
    
    # Esperar la duración de la nota
    sleep(1.5 * beat_duration)
    
    # Apagar las notas después de la duración
    channels[9].noteOff(36, 93)
    channels[9].noteOff(38, 93)
    channels[9].noteOff(42, 93)
    channels[9].noteOff(44, 93)




################################################
################################################
################################################


# Añadir sintetizador estilo Daft Punk (basado en "One More Time")
def daft_punk_synth():
    sleep(10)  # Para que no empiece inmediatamente
    for _ in range(16):  # Progresión inspirada en "One More Time"
        play_note(3, 60, 0.5)  # C4
        play_note(3, 62, 0.5)  # D4
        play_note(3, 64, 0.5)  # E4
        play_note(3, 67, 0.5)  # G4
        play_note(3, 72, 1.5)  # C5
        
        play_note(3, 60, 0.5)  # C4
        play_note(3, 62, 0.5)  # D4
        play_note(3, 64, 0.5)  # E4
        play_note(3, 67, 0.5)  # G4
        play_note(3, 69, 1.5)  # A4

        # Progresión descendente
        play_note(3, 72, 0.5)  # C5
        play_note(3, 69, 0.5)  # A4
        play_note(3, 67, 0.5)  # G4
        play_note(3, 64, 0.5)  # E4
        play_note(3, 62, 1.5)  # D4
        
        sleep(0.5)  # Pausa dramática
        play_note(3, 60, 1.5)  # C4
        sleep(1.0)

    sleep(10)  # Para que no empiece inmediatamente
    for _ in range(4):  # Progresión final más melancólica
        # Usamos notas más lentas y tonos menores para crear el efecto apagado
        play_note(3, 57, 1.0)  # A3
        play_note(3, 60, 1.0)  # C4
        play_note(3, 64, 0.75)  # E4
        play_note(3, 62, 0.75)  # D4
        play_note(3, 67, 1.5)  # G4
        
        # Progresión descendente más triste
        play_note(3, 64, 0.5)  # E4
        play_note(3, 62, 0.5)  # D4
        play_note(3, 60, 0.75)  # C4
        play_note(3, 57, 0.75)  # A3
        play_note(3, 55, 1.5)  # G3

        sleep(1.0)  # Pausa más larga para darle un sentimiento apagado
        
        # Progresión en tono menor
        play_note(3, 60, 1.0)  # C4
        play_note(3, 64, 0.75)  # E4
        play_note(3, 62, 0.75)  # D4
        play_note(3, 55, 1.5)  # G3
        
        sleep(1.5)  # Pausa dramática final


################################################
################################################
################################################

# Bajo eléctrico (modificado)
def bass():
   for _ in range(2):
      for _ in range(12):
         play_note(1, 40, 1.5)  # E2
         play_note(1, 40, 0.5)  # E2
         play_note(1, 43, 0.8)  # G2
         play_note(1, 40, 0.7)  # E2 (ligado)
         play_note(1, 38, 0.5)  # D2
   
         play_note(1, 36, 2.0)  # C2
         play_note(1, 35, 2.0)  # B1

      for _ in range(8):
         play_note(1, 31, 0.5)
   
      for _ in range(8):
         play_note(1, 28, 0.5)

      for _ in range(4):
         play_note(1, 40, 1.5)  # E2
         play_note(1, 40, 0.5)  # E2
         play_note(1, 43, 0.8)  # G2
         play_note(1, 40, 0.7)  # E2 (ligado)
         play_note(1, 38, 0.5)  # D2
   
         play_note(1, 36, 2.0)  # C2
         play_note(1, 35, 2.0)  # B1
      
      for _ in range(8):
         play_note(1, 31, 0.5)
   
      for _ in range(8):
         play_note(1, 28, 0.5)
      
   play_note(1, 36, 2.0)  # C2
   play_note(1, 35, 2.0)  # B1
   
   for _ in range(8):
      play_note(1, 40, 1.5)  # E2
      play_note(1, 40, 0.5)  # E2
      play_note(1, 43, 0.8)  # G2
      play_note(1, 40, 0.7)  # E2 (ligado)
      play_note(1, 38, 0.5)  # D2
   
      play_note(1, 36, 2.0)  # C2
      play_note(1, 35, 2.0)  # B1
      
   for _ in range(8):
      play_note(1, 31, 0.5)
   
   for _ in range(8):
      play_note(1, 28, 0.5)
      
   play_note(1, 35, 1)  # B1
   play_note(1, 35, 0.5)  # B1 bend
   play_note(1, 34, 0.5)  # Slight bend release
   play_note(1, 35, 1)  # B1 (start of slide)
   play_note(1, 33, 1)  # Slide down to A1
   play_note(1, 31, 1)  # Continue slide to G1


# Añadir la nueva función de sintetizador Daft Punk
def drums():
   
   sleep(8)
   for _ in range(3):
      for _ in range(48):
         play_drum_combination_1()
    
      for _ in range(14):
         play_drum_combination_1()
         play_drum_combination_2()
    
   

def guitar():
    sleep(20)  # Espera inicial antes de comenzar la guitarra
    for _ in range(6):
        # Primera sección: añadimos slides y variaciones rítmicas
        play_note(0, 52, 1.5)  # E3
        play_note(0, 55, 1.0)  # G3 - Slide desde E3
        play_note(0, 55, 0.6)  # G3
        play_note(0, 57, 0.6)  # A3 - Hammer-on
        play_note(0, 55, 0.6)  # G3 - Pull-off
        play_note(0, 50, 1.0)  # D3
        play_note(0, 52, 1.0)  # E3 - Ligado
        play_note(0, 48, 2.0)  # C3
        play_note(0, 47, 1.5)  # B2
        sleep(2)
    
    sleep(8)  # Pausa antes de la segunda sección
    
    for _ in range(6):
        # Segunda sección: añadimos octavas y más ligados
        play_note(0, 52, 1.5)  # E3
        play_note(0, 55, 1.0)  # G3 - Slide desde E3
        play_note(0, 55, 0.6)  # G3
        play_note(0, 57, 0.6)  # A3 - Hammer-on
        play_note(0, 55, 0.6)  # G3 - Pull-off
        play_note(0, 50, 1.0)  # D3
        play_note(0, 52, 1.0)  # E3 - Ligado
        play_note(0, 48, 2.0)  # C3
        play_note(0, 47, 1.5)  # B2
        sleep(3)
    
    sleep(8)  # Pausa antes de la tercera sección
    
    for _ in range(4):
        # Tercera sección: patrones más complejos con slides
        play_note(0, 52, 2.0)  # E3
        play_note(0, 55, 1.0)  # G3
        play_note(0, 57, 1.3)  # A3
        play_note(0, 55, 1.0)  # G3 - Slide back to G
        play_note(0, 50, 1.0)  # D3
        play_note(0, 48, 2.5)    # C3
        play_note(0, 47, 2.5)    # B2 
        sleep(3)

################################################
################################################

# Ejecutar los hilos
threading.Thread(target=bass).start()
threading.Thread(target=drums).start()
threading.Thread(target=synth).start()
threading.Thread(target=daft_punk_synth).start()
threading.Thread(target=guitar).start()
