from javax.sound.midi import MidiSystem, Sequence, Track, MidiEvent, ShortMessage, MetaMessage
from java.io import File

# Configuración inicial
sequence = Sequence(Sequence.PPQ, 480)
drum_track = sequence.createTrack()

# Función para agregar una nota
# Ajustes en la función de agregar notas
def add_note_with_duration(track, channel, pitch, velocity, start_tick, duration):
    duration *= 2  # Multiplicamos la duración por 2 en lugar de 3
    on = ShortMessage()
    on.setMessage(ShortMessage.NOTE_ON, channel, pitch, velocity)
    track.add(MidiEvent(on, start_tick))
    
    off = ShortMessage()
    off.setMessage(ShortMessage.NOTE_OFF, channel, pitch, 0)
    track.add(MidiEvent(off, start_tick + duration))

# El resto de las funciones se ajustarían multiplicando el valor de los ticks por 3.


# Función para establecer el tempo
def set_tempo(track, bpm):
    tempo = int(60000000 / bpm)  # Usamos 60000000 para un cálculo estándar de tempo
    data = bytes([
        (tempo >> 16) & 0xFF,
        (tempo >> 8) & 0xFF,
        tempo & 0xFF
    ])
    meta_message = MetaMessage()
    meta_message.setMessage(0x51, data, len(data))
    track.add(MidiEvent(meta_message, 0))


# Establecer el tempo de la canción (123 BPM)
set_tempo(drum_track, 123)
# Declaración de canales
BASS_CHANNEL = 0
GUITAR_CHANNEL = 1
DRUM_CHANNEL = 9
PIANO_CHANNEL = 2  # Si decides usar piano o voz


# Compases
# Ajuste de funciones
def add_silence_compas(track, start_tick):
    # 8 segundos * 480 ticks por segundo (ajuste para asegurar que duren 8 segundos completos)
    ticks_for_silence = 480 * 8 * 2 # 3840 ticks
    return start_tick + ticks_for_silence


# Ajustes en las funciones con duración incrementada
def add_kick_compas(track, start_tick):
    tick = start_tick
    for _ in range(16):  # 16 golpes (2 por segundo en 8 segundos)
        add_note_with_duration(track, DRUM_CHANNEL, 35, 100, tick, 240)  # Bombo en canal 9
        tick += 480  # Espacio de 480 ticks entre golpes
    return tick


def add_kick_variation_compas(track, start_tick):
    tick = start_tick
    for i in range(16):  # 16 golpes (2 por segundo en 8 segundos)
        add_note_with_duration(track, DRUM_CHANNEL, 35, 100, tick, 240)  # Bombo en canal 9
        if i % 2 == 0:  # Variación en cada golpe par (más frecuente)
            add_note_with_duration(track, DRUM_CHANNEL, 38, 100, tick, 240)  # Caja en canal 9
        tick += 480  # Espacio de 480 ticks entre golpes
    return tick



def add_hihat_snare_compas(track, start_tick):
    tick = start_tick
    for i in range(8):  # Ajustado a 8 golpes en 8 segundos
        add_note_with_duration(track, DRUM_CHANNEL, 42, 100, tick, 240)  # Hi-Hat cerrado en canal 9
        add_note_with_duration(track, DRUM_CHANNEL, 38, 100, tick + 240, 240)  # Caja en canal 9
        tick += 960  # Espacio de 960 ticks entre golpes
    return tick



def add_triplet_compas(track, start_tick):
    tick = start_tick
    for i in range(24):  # 24 golpes (3 golpes por segundo para tresillos)
        add_note_with_duration(track, DRUM_CHANNEL, 42, 100, tick, 160)  # Hi-Hat cerrado en canal 9
        if i % 8 == 0:
            add_note_with_duration(track, DRUM_CHANNEL, 38, 100, tick + 240, 240)  # Caja en canal 9
        tick += 320  # Espacio de 320 ticks para tresillos
    return tick



def add_silence_final_compas(track, start_tick):
    # 8 segundos * 480 ticks por segundo (ajuste para asegurar que duren 8 segundos completos)
    ticks_for_silence_final = 480 * 8 * 2  # 3840 ticks
    return start_tick + ticks_for_silence_final


def add_bass_intro(track, start_tick):
    tick = start_tick
    pitch = 40  # MIDI pitch para E1
    for _ in range(8):  # El riff de introducción tiene 8 notas
        add_note_with_duration(track, BASS_CHANNEL, pitch, 100, tick, 480)  # Nota de bajo en canal 0
        tick += 960  # Espacio de 960 ticks para el ritmo del bajo en la intro
    return tick

def add_bass_verse(track, start_tick):
    tick = start_tick
    pitch = 40  # MIDI pitch para E1
    for _ in range(16):  # El bajo toca 16 veces en el verso
        add_note_with_duration(track, BASS_CHANNEL, pitch, 100, tick, 480)  # Nota de bajo en canal 0
        tick += 960  # Mantenemos el mismo ritmo
    return tick


def add_guitar_verse(track, start_tick):
    tick = start_tick
    pitch = 52  # MIDI pitch para E2
    for _ in range(8):  # La guitarra entra en un patrón menos frecuente
        add_note_with_duration(track, GUITAR_CHANNEL, pitch, 100, tick, 960)  # Acorde de guitarra en canal 1
        tick += 1920  # La guitarra tiene menos intervenciones, 1920 ticks de espacio
    return tick



# Ensamblaje de los compases con los instrumentos en sus canales
next_tick = add_bass_intro(drum_track, 0)  # Bajo en la introducción, 8 notas fuertes en canal 0
next_tick = add_silence_compas(drum_track, next_tick)  # Silencio de 8 segundos para la batería

for _ in range(3):  # Un ciclo debería durar 1 minuto y 12 segundos
   next_tick = add_bass_verse(drum_track, next_tick)  # Verso del bajo en canal 0
   next_tick = add_guitar_verse(drum_track, next_tick)  # Verso de la guitarra en canal 1

   for _ in range(3):
       next_tick = add_kick_compas(drum_track, next_tick)  # Batería en canal 9, 24 segundos en total
   for _ in range(2):
       next_tick = add_kick_variation_compas(drum_track, next_tick)  # Batería en canal 9, 16 segundos en total
   next_tick = add_hihat_snare_compas(drum_track, next_tick)  # Batería en canal 9, 8 segundos
   for _ in range(2):
       next_tick = add_triplet_compas(drum_track, next_tick)  # Batería en canal 9, 16 segundos en total
   next_tick = add_hihat_snare_compas(drum_track, next_tick)  # Batería en canal 9, 8 segundos
   next_tick = add_silence_final_compas(drum_track, next_tick)  # Silencio final de 8 segundos para la batería




# Reproducir la secuencia
sequencer = MidiSystem.getSequencer()
sequencer.open()
sequencer.setSequence(sequence)
sequencer.start()

while sequencer.isRunning():
    pass

sequencer.close()

# Guardar la secuencia en un archivo MIDI
output_file = 'seven_nation_army_compas.mid'
MidiSystem.write(sequence, 1, File(output_file))
print("Archivo MIDI guardado como {}".format(output_file))
