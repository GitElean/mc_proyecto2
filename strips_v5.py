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
    sleep(1.1 * beat_duration)
    
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
    sleep(1.1 * beat_duration)
    
    # Apagar las notas después de la duración
    channels[9].noteOff(36, 93)
    channels[9].noteOff(38, 93)
    channels[9].noteOff(42, 93)
    channels[9].noteOff(44, 93)

def play_drum_combination_3():
    # Tocar plato crash, hi-hat cerrado y bombo al mismo tiempo
    channels[9].noteOn(49, 93)  # Crash Cymbal 1
    channels[9].noteOn(42, 93)  # Hi-Hat cerrado
    channels[9].noteOn(36, 93)  # Bombo (Bass Drum)
    
    # Esperar la duración de la nota
    sleep(1.1 * beat_duration)
    
    # Apagar las notas después de la duración
    channels[9].noteOff(49, 93)
    channels[9].noteOff(42, 93)
    channels[9].noteOff(36, 93)
    
def play_drum_combination_4():
    # Tocar plato crash, caja y bombo al mismo tiempo
    channels[9].noteOn(49, 93)  # Crash Cymbal 1
    channels[9].noteOn(38, 93)  # Caja (Snare Drum)
    channels[9].noteOn(36, 93)  # Bombo (Bass Drum)
    
    # Esperar la duración de la nota
    sleep(1.1 * beat_duration)
    
    # Apagar las notas después de la duración
    channels[9].noteOff(49, 93)
    channels[9].noteOff(38, 93)
    channels[9].noteOff(36, 93)

def play_drum_combination_5():
    # Tercer golpe: Solo Hi-Hat cerrado
    channels[9].noteOn(42, 93)  # Hi-Hat cerrado
    
    sleep(1.1 * beat_duration)  # Nota rápida
    
    channels[9].noteOff(42, 93)
    
def play_drum_combination_6():
    # Cuarto golpe: Caja, hi-hat cerrado y plato crash
    channels[9].noteOn(49, 93)  # Crash Cymbal 1
    channels[9].noteOn(38, 93)  # Caja (Snare Drum)
    channels[9].noteOn(42, 93)  # Hi-Hat cerrado
    
    sleep(1.1 * beat_duration)  # Nota normal
    
    channels[9].noteOff(49, 93)
    channels[9].noteOff(38, 93)
    channels[9].noteOff(42, 93)
    
def play_drum_combination_alternate():
    # Tocar bombo
    channels[9].noteOn(38, 93)  # Bombo (Bass Drum)
    sleep(1 * beat_duration)  # Pausa entre el bombo y el hi-hat
    channels[9].noteOff(38, 93)
    
    # Tocar hi-hat cerrado
    channels[9].noteOn(42, 93)  # Hi-Hat cerrado
    sleep(1 * beat_duration)
    channels[9].noteOff(42, 93)


################################################
################################################
################################################



# Bajo eléctrico (corregido)
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
      
   # Play B1 on the 7th fret of the E string with a slight bend
   play_note(1, 35, 1)  # B1
   # Simulate a 1/4 bend and release (B1 remains close to its original pitch)
   play_note(1, 35, 0.5)  # B1 bend
   play_note(1, 34, 0.5)  # Slight bend release
   # Slide down from B1 (7th fret of the E string)
   play_note(1, 35, 1)  # B1 (start of slide)
   play_note(1, 33, 1)  # Slide down to A1
   play_note(1, 31, 1)  # Continue slide to G1


   

# Batería
def drums():
   
   sleep(8)
   for _ in range(2):
      for _ in range(48):
         play_drum_combination_1()
    
      for _ in range(14):
         play_drum_combination_1()
         play_drum_combination_2()
    
      for _ in range(2):
         play_drum_combination_3()
         play_drum_combination_1()
         play_drum_combination_1()
         play_drum_combination_1()
      
      for _ in range(4):
         play_drum_combination_3()
         play_drum_combination_4()
     
      play_drum_combination_1()
      play_drum_combination_2()
      play_drum_combination_5()
      play_drum_combination_6()
      play_drum_combination_5()
   
      play_drum_combination_3()
      play_drum_combination_4()
   
      for _ in range(3):
         play_drum_combination_3()
         play_drum_combination_1()
         play_drum_combination_1()
         play_drum_combination_1()
      
      sleep(8)
      
   for _ in range(36):
      play_drum_combination_alternate()
      
def voice():
   sleep(15.25)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 67, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 1)
   sleep(1.75)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.75)
   play_note(10, 64, 1.5)
   sleep(0.75)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 71, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   sleep(2)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 1)
   play_note(10, 64, 1)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.75)
   play_note(10, 64, 1.5)
   sleep(1)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 69, 0.5)
   play_note(10, 71, 0.5)
   play_note(10, 69, 0.5)
   play_note(10, 69, 0.5)
   play_note(10, 67, 0.75)
   play_note(10, 67, 0.75)
   play_note(10, 64, 1)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 63, 0.75)
   play_note(10, 63, 0.75)
   play_note(10, 64, 1.5)
   sleep(3)
   play_note(10, 64, .5)
   play_note(10, 62, .5)
   play_note(10, 64, 1)
   play_note(10, 64, .75)
   play_note(10, 64, 0.75)
   play_note(10, 64, 1)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.75)
   play_note(10, 64, 1.5)
   sleep(3)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 1)
   play_note(10, 64, 1.5)
   play_note(10, 64, 1)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 1)
   sleep(16)
   sleep(3)
   sleep(15.25)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 67, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   sleep(2)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 1)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.5)
   play_note(10, 64, 1)
   sleep(.75)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 71, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   sleep(2)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.75)
   sleep(0.75)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 69, 0.5)
   play_note(10, 71, 0.5)
   play_note(10, 69, 0.5)
   play_note(10, 69, 0.5)
   play_note(10, 67, 0.75)
   play_note(10, 67, 0.75)
   play_note(10, 64, 1)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 63, 0.75)
   play_note(10, 63, 0.75)
   play_note(10, 64, 1.5)
   sleep(6.25)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 62, 0.5)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 1.0)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.75)
   play_note(10, 64, 0.5)
   sleep(6)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 1)
   play_note(10, 64, 1.5)
   play_note(10, 64, 1)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 0.5)
   play_note(10, 64, 1)
   sleep(1.5)
   sleep(48)
   sleep(1.25)


def guitar():
   sleep(20)
   for _ in range(6):
      play_note(0, 52, 1.5)  # E3
      play_note(0, 52, 0.5)  # E3
      play_note(0, 55, 0.8)  # G3
      play_note(0, 52, 0.7)  # E3
      play_note(0, 50, 0.5)  # D3
      play_note(0, 48, 2)    # C3
      play_note(0, 47, 2)    # B2 
      sleep(4)
   sleep(12)   
   for _ in range(6):
      play_note(0, 52, 1.5)  # E3
      play_note(0, 52, 0.5)  # E3
      play_note(0, 55, 0.8)  # G3
      play_note(0, 52, 0.7)  # E3
      play_note(0, 50, 0.5)  # D3
      play_note(0, 48, 2)    # C3
      play_note(0, 47, 2)    # B2 
      sleep(4)
   sleep(12)   
   for _ in range(4):
      play_note(0, 52, 1.5)  # E3
      play_note(0, 52, 0.5)  # E3
      play_note(0, 55, 0.8)  # G3
      play_note(0, 52, 0.7)  # E3
      play_note(0, 50, 0.5)  # D3
      play_note(0, 48, 2)    # C3
      play_note(0, 47, 2)    # B2 
      sleep(4)
   
   

   
   
   
      
# Ejecutar los hilos
threading.Thread(target=bass).start()
threading.Thread(target=drums).start()
threading.Thread(target=voice).start()
threading.Thread(target=guitar).start()








