#! /usr/local/bin/python

# Generate team fixture list using a Berger table.
#
# One property of Berger table is that teams offset by half number of teams are
# never away or home at the same time (e.g. for 10 teams, 1 & 6, 2 & 7, etc.)
#
# To generate full home-away season need to reverse last two fixture lists
# before reversing fixtures, else some teams have 3 away or home matches in a
# row.

def rotate(arr, dist):
    # Rotate n-1 elements clockwise (right to left) dist places
    dist = dist % len(arr)
    return arr[dist:-1] + arr[:dist] + arr[-1:]

def generate(number=6, full=True, offset=0):
    assert number > 3
    # Ensure even number of teams
    if number % 1:
        number += 1
    # Generate initial team id sequence
    ids = [chr(ord('A') + i) for i in range(number)]
    if offset:
        ids = rotate(ids, offset)
    # Generate pairings - 1 less than number of teams
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
    # Generate full home-away season
    if full:
        interleaved[-2], interleaved[-1] = interleaved[-1], interleaved[-2]
        t = []
        for f in interleaved:
            t.append([(a, h) for (h, a) in f])
        interleaved.extend(t)
    return interleaved

for f in generate():
    print f
