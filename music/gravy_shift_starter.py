# gravy_shift_starter.py — Stage 1: drums + bass MIDI, 118 BPM, F minor, 8 bars
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

TPB = 480
STEP = TPB // 4   # one 16th note
BARS = 8

def save(name, notes, channel):
    mid = MidiFile(ticks_per_beat=TPB)
    track = MidiTrack(); mid.tracks.append(track)
    track.append(MetaMessage("track_name", name=name))
    track.append(MetaMessage("set_tempo", tempo=bpm2tempo(118)))
    events = []
    for start, length, pitch, vel in notes:
        events.append((start, Message("note_on", note=pitch, velocity=vel, channel=channel)))
        events.append((start + length, Message("note_off", note=pitch, velocity=0, channel=channel)))
    events.sort(key=lambda e: (e[0], e[1].type == "note_on"))
    now = 0
    for t, msg in events:
        msg.time = t - now; now = t
        track.append(msg)
    mid.save(name + ".mid")

# Drums: kick, clap on 2 and 4, hats, open hat lift at the end of each bar
drums = []
for bar in range(BARS):
    b = bar * 16 * STEP
    for s in (0, 7, 10):       drums.append((b + s*STEP, STEP, 36, 115))  # kick
    for s in (4, 12):          drums.append((b + s*STEP, STEP, 39, 110))  # clap
    for s in range(0, 14, 2):  drums.append((b + s*STEP, STEP, 42, 80))   # closed hat
    drums.append((b + 14*STEP, STEP, 46, 90))                             # open hat
save("Drums - Verse", drums, 9)

# Bass: F, Db, Eb, C — bouncy root/octave funk pattern
roots = [41, 37, 39, 36]
bass = []
for bar in range(BARS):
    b = bar * 16 * STEP
    r = roots[bar % 4]
    for s, length, p in [(0,3,r), (3,1,r), (6,2,r+12), (8,2,r), (11,1,r+7), (14,2,r+12)]:
        bass.append((b + s*STEP, length*STEP, p, 105))
save("Bass - Verse", bass, 0)

print("Done: 'Drums - Verse.mid' and 'Bass - Verse.mid'")
