# debannerizer

A Python tool for scraping class schedules from the Mines _Self-Service Banner_
system into a database. Produced as a final project for CSCI-403 by Jack
Rosenthal, Ariel Shlosberg, and Nicholas Lantz (aka. _That Rubik's Cube Team_).

## Required Packages

Install these using `pip` (or however you like). You should install them for
Python 3.

    SQLAlchemy
    psycopg2
    beautifulsoup4
    lxml
    PyYAML

## Usage Instructions

You're going to need to setup `config.yaml` with the connection to the
database. There's a sample `config.yaml` to give you an idea how this looks.
You can even use a different database connector (SQLite for example).

To import data, use the `import_tool.py`, providing the term (as banner likes
it in its post requests) as the only argument, like so:

    $ python3 import_tool.py 201710

The `201710` is the way that banner represents terms, the format is relatively
trivial, the first four digits are the year, and then the month of the start of
the term follows as the next digit, followed by a zero to fill.

We included some cool examples of how to use the data with SQLAlchemy in
`examples.py`.

## Coding Style

[PEP-8](https://www.python.org/dev/peps/pep-0008/) is to be followed
__strictly__; however line lengths of up to 90 or 100 columns is OK if the
purpose of the line is still cleanly conveyed.
