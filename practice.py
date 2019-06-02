import random
from time import sleep

major_chords = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
minor_chords = ['Cm', 'Dm', 'Em', 'Fm', 'Gm', 'Am', 'Bm']
all_chords = major_chords + minor_chords

strum_patterns = [' S-', ' Sand ', ' -and ']

print('The strum pattern is')
strum = ''
for i in range(4):
    strum += random.choice(strum_patterns)
print(strum)
sleep(5)
print("Now get ready to play some chords")
for i in range(4):
    print(random.choice(all_chords))
    sleep(4)


