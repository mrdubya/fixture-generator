#! /usr/local/bin/python

# Copyright (c) 2012 Michael Williams <mrw@eandem.co.uk>
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


def berger_table(teams, double=True):
    """ Generate team fixture list using a Berger table.

    Team ids essentially start in two rows beginning at the bottom left
    and then moving in a counter clockwise direction, such that the first is
    is opposite the last, the second the penultimate and so on.  For example:

                  8 7 6 5
    Start here -> 1 2 3 4

    All the pairings are then generated by keeping 8 fixed and rotating the
    other ids clockwise, such that 8 is paired with 2, 3, 4, etc.  To get a
    good home and away alternation the last n - 1 pairings are interleaved
    with the first n pairings (where n is the number of matches and equal to
    one less than the number of teams).  And finally the matches for the last
    id (8 in the above example) in the interleaved pairings are reversed.

    >>> berger_table(range(4), False)
    [[(0, 3), (1, 2)], [(3, 2), (0, 1)], [(1, 3), (2, 0)]]

    One property of Berger table is that teams offset by half number of teams are
    never away or home at the same time (e.g. for 10 teams, 1 & 6, 2 & 7, etc.)

    To generate full home-away fixture list the last two fixture lists need to
    be reversed before adding the reversed fixtures, else some teams will have
    3 away or home matches in a row (only works for 6 or more teams).

    >>> berger_table(range(6))
    [[(0, 5), (1, 4), (2, 3)], [(5, 3), (4, 2), (0, 1)], [(1, 5), (2, 0), (3, 4)], [(2, 5), (3, 1), (4, 0)], [(5, 4), (0, 3), (1, 2)], [(5, 0), (4, 1), (3, 2)], [(3, 5), (2, 4), (1, 0)], [(5, 1), (0, 2), (4, 3)], [(5, 2), (1, 3), (0, 4)], [(4, 5), (3, 0), (2, 1)]]
    """
    def rotate(arr, dist):
        # Rotate n-1 elements clockwise (right to left) dist places
        dist = dist % len(arr)
        return arr[dist:-1] + arr[:dist] + arr[-1:]
    # Generate pairings - 1 less than number of teams
    number = len(teams)
    mid_point = number/2
    pairings = []
    for i in range(number - 1):
        home = teams[:mid_point]
        away = teams[mid_point:]
        away.reverse()
        pairings.append(zip(home, away))
        teams = rotate(teams, 1)
    # Interleave and fix up last team home and away (always first in pairings)
    fixtures = []
    for i in range(mid_point - 1):
        fixtures.append(pairings[i])
        p = pairings[mid_point + i]
        p[0] = (p[0][1], p[0][0])
        fixtures.append(p)
    fixtures.append(pairings[mid_point - 1])
    if double:
        # Double round robin, swap last two fixture lists and add reverse match fixtures
        fixtures[-2], fixtures[-1] = fixtures[-1], fixtures[-2]
        fixtures.extend([[(match[1], match[0]) for match in fixture]
                            for fixture in fixtures])
    return fixtures


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# eof bergertable.py
