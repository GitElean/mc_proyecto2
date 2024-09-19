import threading
from javax.sound.midi import MidiSystem, Sequence, MidiEvent, ShortMessage
from java.io import File

# Create a new MIDI sequence
sequence = Sequence(Sequence.PPQ, 24)
track = sequence.createTrack()

# Function to add note on and off events
def add_note_on_event(track, channel, note, tick, volume=93):
    msg_on = ShortMessage()
    msg_on.setMessage(ShortMessage.NOTE_ON, channel, note, volume)
    event_on = MidiEvent(msg_on, int(tick))  # Cast tick to int
    track.add(event_on)

def add_note_off_event(track, channel, note, tick, volume=93):
    msg_off = ShortMessage()
    msg_off.setMessage(ShortMessage.NOTE_OFF, channel, note, volume)
    event_off = MidiEvent(msg_off, int(tick))  # Cast tick to int
    track.add(event_off)

# Bass function that writes MIDI events
def bass_midi(start_tick):
    tick_per_beat = 24  # Based on the BPM setup

    # Define the notes with their durations (tick_per_beat multipliers for time)
    def play_bass_note_midi(channel, note, duration):
        add_note_on_event(track, channel, note, start_tick[0], 93)  # Default volume = 93
        add_note_off_event(track, channel, note, start_tick[0] + int(tick_per_beat * duration), 93)
        start_tick[0] += int(tick_per_beat * duration)  # Increment start_tick for each note

    # Loop the bass pattern twice
    for _ in range(2):
        for _ in range(12):
            play_bass_note_midi(1, 40, 1.5)  # E2
            play_bass_note_midi(1, 40, 0.5)  # E2
            play_bass_note_midi(1, 43, 0.8)  # G2
            play_bass_note_midi(1, 40, 0.7)  # E2 (ligado)
            play_bass_note_midi(1, 38, 0.5)  # D2

            play_bass_note_midi(1, 36, 2.0)  # C2
            play_bass_note_midi(1, 35, 2.0)  # B1

        for _ in range(8):
            play_bass_note_midi(1, 31, 0.5)

        for _ in range(8):
            play_bass_note_midi(1, 28, 0.5)

        for _ in range(4):
            play_bass_note_midi(1, 40, 1.5)  # E2
            play_bass_note_midi(1, 40, 0.5)  # E2
            play_bass_note_midi(1, 43, 0.8)  # G2
            play_bass_note_midi(1, 40, 0.7)  # E2 (ligado)
            play_bass_note_midi(1, 38, 0.5)  # D2

            play_bass_note_midi(1, 36, 2.0)  # C2
            play_bass_note_midi(1, 35, 2.0)  # B1

        for _ in range(8):
            play_bass_note_midi(1, 31, 0.5)

        for _ in range(8):
            play_bass_note_midi(1, 28, 0.5)

    # Final segment of the bass
    play_bass_note_midi(1, 36, 2.0)  # C2
    play_bass_note_midi(1, 35, 2.0)  # B1

    for _ in range(8):
        play_bass_note_midi(1, 40, 1.5)  # E2
        play_bass_note_midi(1, 40, 0.5)  # E2
        play_bass_note_midi(1, 43, 0.8)  # G2
        play_bass_note_midi(1, 40, 0.7)  # E2 (ligado)
        play_bass_note_midi(1, 38, 0.5)  # D2

        play_bass_note_midi(1, 36, 2.0)  # C2
        play_bass_note_midi(1, 35, 2.0)  # B1

    for _ in range(8):
        play_bass_note_midi(1, 31, 0.5)

    for _ in range(8):
        play_bass_note_midi(1, 28, 0.5)

    # B1 bend and slide down sequence
    play_bass_note_midi(1, 35, 1)  # B1
    play_bass_note_midi(1, 35, 0.5)  # B1 bend
    play_bass_note_midi(1, 34, 0.5)  # Slight bend release
    play_bass_note_midi(1, 35, 1)  # B1 (start of slide)
    play_bass_note_midi(1, 33, 1)  # Slide down to A1
    play_bass_note_midi(1, 31, 1)  # Continue slide to G1


####################################################################
# Voice function that writes MIDI events
def voice_midi(start_tick):
    tick_per_beat = 24  # Based on the BPM setup

    # Define the notes with their durations (tick_per_beat multipliers for time)
    def play_voice_note_midi(channel, note, duration):
        add_note_on_event(track, channel, note, start_tick[0], 93)  # Default volume = 93
        add_note_off_event(track, channel, note, start_tick[0] + int(tick_per_beat * duration), 93)
        start_tick[0] += int(tick_per_beat * duration)  # Increment start_tick for each note

    # Simulating sleep in MIDI (move start_tick forward by sleep amount)
    def sleep_midi(beats):
        start_tick[0] += int(tick_per_beat * beats)

    # Add notes and rests for the voice part
    sleep_midi(15.25)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 67, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 1)
    sleep_midi(1.75)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 1.5)
    sleep_midi(0.75)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 71, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    sleep_midi(2)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 1.5)
    sleep_midi(1)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 69, 0.5)
    play_voice_note_midi(10, 71, 0.5)
    play_voice_note_midi(10, 69, 0.5)
    play_voice_note_midi(10, 69, 0.5)
    play_voice_note_midi(10, 67, 0.75)
    play_voice_note_midi(10, 67, 0.75)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 63, 0.75)
    play_voice_note_midi(10, 63, 0.75)
    play_voice_note_midi(10, 64, 1.5)
    sleep_midi(3)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 1.5)
    sleep_midi(3)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 1.5)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 1)
    sleep_midi(16)
    sleep_midi(3)
    sleep_midi(15.25)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 67, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    sleep_midi(2)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 1)
    sleep_midi(0.75)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 71, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    sleep_midi(2)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.75)
    sleep_midi(0.75)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 69, 0.5)
    play_voice_note_midi(10, 71, 0.5)
    play_voice_note_midi(10, 69, 0.5)
    play_voice_note_midi(10, 69, 0.5)
    play_voice_note_midi(10, 67, 0.75)
    play_voice_note_midi(10, 67, 0.75)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 63, 0.75)
    play_voice_note_midi(10, 63, 0.75)
    play_voice_note_midi(10, 64, 1.5)
    sleep_midi(6.25)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 62, 0.5)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 1.0)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.75)
    play_voice_note_midi(10, 64, 0.5)
    sleep_midi(6)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 1.5)
    play_voice_note_midi(10, 64, 1)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 0.5)
    play_voice_note_midi(10, 64, 1)
    sleep_midi(1.5)
    sleep_midi(48)
    sleep_midi(1.25)

# Define the starting tick as a list to modify within the function
start_tick = [0]

# Call the bass function to write to the MIDI
bass_midi(start_tick)
voice_midi(stat_tick)
# Save the MIDI file
midi_file = File("bass_midi_output_fixed.mid")
MidiSystem.write(sequence, 1, midi_file)

print("MIDI file saved as bass_midi_output_fixed.mid")

