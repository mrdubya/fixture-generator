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

"""Generate a fixture list.

usage: fixgen [-d] [-h] [-p number] number

-d generate double round-robin (second half matches reversed).
-h display this help.
-p phase shift for fixture list.
number of teams (odd values rounded up 1).
"""

import getopt
import re
import sys

from fixture_generator import generate_fixtures, berger_table, print_lists, print_grid

# Utility product information
__product__ = 'Fixture generator'
__copyright__ = 'Copyright 2010 Mike Williams. All rights reserved.'
version_info = (0, 1, 0, 'beta', 0)
__version__ = '%d.%d.%d' % version_info[:3]
if version_info[3] != 'final':
    __version__ += ' %s.%d' % version_info[3:]

__description__ = '%s %s.\n%s' % (__product__, __version__, __copyright__)

USAGE = re.search('^usage:.*', __doc__, re.MULTILINE).group()

def usage(mesg):
    sys.exit('%s\n%s' % (mesg, USAGE))

# Parse the command line options
try:
    opts, pargs = getopt.getopt(sys.argv[1:], 'dhp:')
except getopt.GetoptError, e:
    usage(e)

double = False
offset = 0
for option, value in opts:
    if option == '-h':  # Display help
        sys.exit(__doc__)

    elif option == '-d':  # Double round robin
        double = True

    elif option == '-p':  # Offset starting fixture
        try:
            offset = int(value)
        except:
            usage('Invalid start fixture shift.')

if len(pargs) != 1:
    usage('Wrong number of arguments given.')
try:
    number = int(pargs[0])
except:
    usage('Invalid number of teams')

fl = generate_fixtures(number, berger_table, double, offset)
print_lists(fl)
print_grid(fl)

#eof fixgen.py
