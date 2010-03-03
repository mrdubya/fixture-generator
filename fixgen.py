#! /usr/local/bin/python

# Copyright (c) 2010 Michael Williams <mrw@eandem.co.uk>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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
    # Generate pairings - 1 less than number of teams
    mid_point = number/2
    pairings = []
    for i in range(number - 1):
        home = ids[:mid_point]
        away = ids[mid_point:]
        away.reverse()
        pairings.append(zip(home, away))
        ids = rotate(ids, 1)
    # Interleave and fix up last team home and away (always first in pairings)
    fixtures = []
    for i in range(mid_point - 1):
        fixtures.append(pairings[i])
        p = pairings[mid_point + i]
        p[0] = p[0][1], p[0][0]
        fixtures.append(p)
    fixtures.append(pairings[mid_point - 1])
    if full:
        # Full season, swap last two fixture lists and then add reverse fixtures
        fixtures[-2], fixtures[-1] = fixtures[-1], fixtures[-2]
        fixtures.extend([[(away, home) for (home, away) in fixture]
                            for fixture in fixtures])
    # Shift starting point in fixtures
    offset = offset % number
    fixtures = fixtures[offset:] + fixtures[:offset]
    return fixtures

fixtures = generate(10, offset=5)
#for f in fixtures: print f

tm = {}
for f in fixtures:
    for h, a in f:
        hm = tm.get(h, [])
        hm.append(a)
        tm[h] = hm
        am = tm.get(a, [])
        am.append(' ')
        tm[a] = am

t = tm.keys()
t.sort()
for i in t:
    print i, tm[i]
