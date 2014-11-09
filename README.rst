Competition Fixture Generator
-----------------------------

A command line tool to generate round-robin and full home-away double
round-robin fixture lists for a competition using a Berger table.
In a full home-away fixture list no team will have more than 2 home or away
fixtures in a row during for the competition (apart from a full home-away
fixture list for 3/4 teams).

::

    $ fixgen -h
    Generate a fixture list.

    usage: fixgen [-h] [-d] [-p number] [-f file | [-l] number]

    -d generate double round-robin (second half matches reversed).
    -f get team names from a file
    -h display this help.
    -l use letters for team names (default is numbers)
    -p phase shift for fixture list.
    number of teams (odd values rounded up 1).

The output is a simple list of 0 v 1, 2 v 3 and so on for each round of the
competition.
Specify ``-l`` to use letters instead of numbers.
With ``-f`` team names will be read from a file (one team name per line).
The competition round fixture lists are followed by a per team list of matches
where they are first named (usually home matches).
For a competition with 6 teams the output is the following::

    $ fixgen 6
    [0 v 5, 1 v 4, 2 v 3]
    [5 v 3, 4 v 2, 0 v 1]
    [1 v 5, 2 v 0, 3 v 4]
    [5 v 4, 0 v 3, 1 v 2]
    [2 v 5, 3 v 1, 4 v 0]
    0 [5, 1, ' ', 3, ' ']
    1 [4, ' ', 5, 2, ' ']
    2 [3, ' ', 0, ' ', 5]
    3 [' ', ' ', 4, ' ', 1]
    4 [' ', 2, ' ', ' ', 0]
    5 [' ', 3, ' ', 4, ' ']

An odd number of teams is rounded up to the next even number to generate the
competition fixtures.
If team names are supplied and there are an odd number of teams then a team with
the name No game is added - the team playing them will have a bye for that
competition round.
A file with the team names Bulls, Tigers, and Eagles produces the following
output::

    $ fixgen -f teams
    [Bulls v No game, Tigers v Eagles]
    [No game v Eagles, Bulls v Tigers]
    [Tigers v No game, Eagles v Bulls]
    Bulls ['No game', 'Tigers', ' ']
    Eagles [' ', ' ', 'Bulls']
    No game [' ', 'Eagles', ' ']
    Tigers ['Eagles', ' ', 'No game']

The phase argument allows generation of a simple variation of the generated
fixtures for the same number of teams.
For example if the teams do not change from competition to competition, the
order of fixtures played in the following competition can be changed using a
phase number between 1 and one less than the number of fixtures in a single
round-robin.
(A phase of 0 is the same as specifying no phase.)
So using the same file of team names as above with a phase of 2 results in the
following::

    $ fixgen -p 2 -f teams
    [Tigers v No game, Eagles v Bulls]
    [Bulls v No game, Tigers v Eagles]
    [No game v Eagles, Bulls v Tigers]
    Bulls [' ', 'No game', 'Tigers']
    Eagles ['Bulls', ' ', ' ']
    No game [' ', ' ', 'Eagles']
    Tigers ['No game', 'Eagles', ' ']

