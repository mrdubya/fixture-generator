#! /usr/local/bin/python

# Generate team fixture list using a Berger table

def rotate(arr, dist):
    # Rotate n-1 elements clockwise (right to left) dist places
    assert dist > 0 and dist < len(arr)
    return arr[dist:-1] + arr[:dist] + arr[-1:]

def generate(number=6):
    # Ensure even number of teams
    if number % 1:
        number += 1
    # Generate pairings - 1 less than number of teams
    ids = range(number)
    mid_point = number/2
    pairings = []
    for i in range(number - 1):
        home = ids[:mid_point]
        away = ids[mid_point:]
        away.reverse()
        pairings.append(zip(home, away))
        ids = rotate(ids, 1)
    # Interleave
    interleaved = []
    for i in range(mid_point - 1):
        interleaved.append(pairings[i])
        interleaved.append(pairings[mid_point + i])
    interleaved.append(pairings[mid_point - 1])
    # Fix up last team home and aways - swap teams every other match
    for i in range(1, number - 1, 2):
        i = interleaved[i]
        i[0] = i[0][1], i[0][0]
    return interleaved

for f in generate(10):
    print f
