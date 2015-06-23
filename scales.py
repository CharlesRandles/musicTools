#!/usr/bin/python
"""
Generate and manipulate musical scales
"""

import unittest

class InvalidNoteException(Exception):
    pass

def notes():
    return {0:["C", "B#"],
            1:["C#", "Db"],
            2:["D", "C##"],
            3:["D#", "Eb"],
            4:["E", "Fb"],
            5:["F", "E#"],
            6:["F#", "Gb"],
            7:["G", "F##"],
            8:["G#", "Ab"],
            9:["A", "Bbb"],
            10:["A#", "Bb"],
            11:["B", "Cb"]}

def nextNoteName(note):
    return chr(((ord(note[0]) - ord("A") + 1)%7)+ord("A"))

def findIndex(note):
    for key in notes().keys():
        if note in notes()[key]:
            return key

def nextNote(note, step):
    noteName = nextNoteName(note)
    index = (findIndex(note) + step) % 12
    for candidate in notes()[index]:
        if candidate[0] == noteName[0]:
            return candidate
    raise InvalidNoteException("Unable to raise {} by {} steps.".format(note,step))
    
def buildScale(tonic, steps):
    scale = [tonic]
    note = tonic
    for step in steps:
        note = nextNote(note, step)
        scale.append(note)
    return scale

def majorScale(tonic):
    steps=[2,2,1,2,2,2,1]
    return buildScale(tonic, steps)

def naturalMinorScale(tonic):
    steps=[2,1,2,2,1,2,2]
    return buildScale(tonic, steps)

def harmonicMinorScale(tonic):
    steps=[2,1,2,2,1,3,1]
    return buildScale(tonic, steps)


#################
## Tests
################
class TestMajor(unittest.TestCase):
    def setUp(self):
        self.cmaj=["C", "D", "E", "F", "G", "A", "B", "C"]
        self.majSteps=[2,2,1,2,2,2,1]
        self.semitones=[
            "C","C#","D","Eb",
            "E","F","F#","G",
            "Ab","A","Bb","B",
        ]
    def testFindIndex(self):
        self.assertEqual(findIndex("C"), 0)
        self.assertEqual(findIndex("B"), 11)
    def testNextNoteName(self):
        self.assertEqual(nextNoteName("C"), "D")
        self.assertEqual(nextNoteName("C#"), "D")
        self.assertEqual(nextNoteName("Db"), "E")
        self.assertEqual(nextNoteName("G"), "A")
        
    def testNextNote(self):
        self.assertEqual(nextNote("C", 2), "D")
        self.assertEqual(nextNote("G", 2), "A")
        
    def testBuildScale(self):
        self.assertEqual(buildScale("C", self.majSteps), self.cmaj)
                         
    def testCMaj(self):
        scale = majorScale("C")
        self.assertEqual(scale, self.cmaj)
        
    def testMajorScales(self):
        print("Major Scales")
        for semitone in self.semitones:
            print("{}:\t{}".format(
                semitone, "-".join(majorScale(semitone))))

    def testNaturalMinorScales(self):
        print("Natural Minor Scales")
        for semitone in self.semitones:
            print("{}:\t{}".format(
                semitone, "-".join(naturalMinorScale(semitone))))

    def testHarmonicMinorScales(self):
        print("Harmonic Minor Scales")
        for semitone in self.semitones:
            print("{}:\t{}".format(
                semitone, "-".join(harmonicMinorScale(semitone))))

            
def test():
    unittest.main()

if __name__=="__main__":
    test()
