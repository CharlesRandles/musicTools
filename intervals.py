#!/usr/bin/python

"""
Musical Intervals
"""

import scales

class Quality(object):
    Perfect, Major, Minor, Augmented, Diminished = range(5)

class Name(object):
    Unison, Second, Third, Fourth, Fifth, Sixth, Seventh, Octave = range(8)

class Interval(object):
    def __init__(self, quality, name):
        self.quality, self.name = quality, name

def lookup():
    return [
        (Quality.Perfect, Name.Unison, 0),
        (Quality.Diminished, Name.Second, 0),
        (Quality.Minor, Name.Second, 1),
        (Quality.Major, Name.Second, 2),
        (Quality.Diminished, Name.Third, 2),
        (Quality.Minor, Name.Third, 3),
        (Quality.Augmented, Name.Second, 3),
        (Quality.Major, Name.Third, 4),
        (Quality.Diminished, Name.Fourth, 4),
        (Quality.Perfect, Name.Fourth, 5),
        (Quality.Augmented, Name.Third, 5),
        (Quality.Diminished, Name.Fifth, 6),
        (Quality.Augmented, Name.Fourth, 6),
        (Quality.Perfect, Name.Sixth, 7),
        (Quality.Diminished, Name.Sixth, 7),
        (Quality.Minor, Name.Sixth, 8),
        (Quality.Augmented, Name.Fifth, 8),
        (Quality.Major, Name.Sixth, 9),
        (Quality.Diminished, Name.Seventh, 9),
        (Quality.Minor, Name.Seventh, 10),
        (Quality.Augmented, Name.Sixth, 10),
        (Quality.Major, Name.Seventh, 11),
        (Quality.Diminished, Name.Octave, 11),
        (Quality.Perfect, Name.Octave, 12),
        (Quality.Augmented, Name.Seventh, 10)
        ]
 

def findInterval(quality, name):
    return [i for i in lookup() if i[0]==quality and i[1]==name][0]

def perfectUnison(note, scale):
    return note


######################
### Tests
######################
import unittest
 
class TestIntervals(unittest.TestCase):

    def setUp(self):
        self.cmaj=scales.majorScale("C")

    def testPerfectUnison(self):
        for note in self.cmaj:
            self.assertEqual(note, perfectUnison(note, self.cmaj))

    def testIntervalConstructor(self):
        i1=Interval(Quality.Perfect, Name.Unison)
        self.assertEqual(i1.quality, Quality.Perfect)
        self.assertEqual(i1.name, Name.Unison)

def test():
    unittest.main()

if __name__=="__main__":
    test()

