#! /usr/local/bin/python

# Copyright (c) 2010-2012 Michael Williams <mrw@eandem.co.uk>
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


class Fixture(object):

    def __init__(self, (home, away)):
        self.home = home
        self.away = away

    def __str__(self):
        return '%s v %s' % (self.home, self.away)

    def __repr__(self):
        return self.__str__()


def generate_fixtures(teams, generator_, double=False, offset=0):
    # Generate the fixture list
    rounds = generator_(teams, double)
    fixtures = [map(Fixture, round) for round in rounds]
    # Shift starting fixture
    offset = offset % len(teams)
    fixtures = fixtures[offset:] + fixtures[:offset]
    return fixtures

def print_lists(fixture_list):
    for f in fixture_list:
        print f

def print_grid(fixture_list):
    away = {}
    for fixtures in fixture_list:
        for match in fixtures:
            hm = away.get(match.home, [])
            hm.append(match.away)
            away[match.home] = hm
            am = away.get(match.away, [])
            am.append(' ')
            away[match.away] = am

    home = away.keys()
    home.sort()
    for team in home:
        print team, away[team]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# eof generator.py
