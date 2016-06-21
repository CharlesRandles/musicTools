module Scales where

import Data.Maybe (fromJust)

type Note = String
noteNames :: [Note]
noteNames = ["C","D","E","F","G","A","B"]

chromaticScale :: [Note]
chromaticScale=["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

semitones:: [(Int, [Note])]
semitones =  [(0,["C", "B#"]),
             (1,["C#", "Db"]),
             (2,["D", "C##"]),
             (3,["D#", "Eb"]),
             (4,["E", "Fb"]),
             (5,["F", "E#"]),
             (6,["F#", "Gb"]),
             (7,["G", "F##"]),
             (8,["G#", "Ab"]),
             (9,["A", "Bbb"]),
             (10,["A#", "Bb"]),
             (11,["B", "Cb"])]

modes :: [(String, [Int])]
modes = [("Ionian", [2,2,1,2,2,2,1]),
         ("Dorian", [2,1,2,2,2,1,2]),
         ("Phrygian", [1,2,2,2,1,2,2]),
         ("Lydian", [2,2,2,1,2,2,1]),
         ("Mixolydian", [2,2,1,2,2,1,2]),
         ("Aeolian", [2,1,2,2,1,2,2]),
         ("Locrian", [1,2,2,1,2,2,2])]

modeFromName :: String -> [Int] 
modeFromName mode = fromJust $ lookup mode modes

intToNote :: Int -> [Note]
intToNote n 
          | (n < 0) || (n > 11) = error $ "Semitones are numbered from 0-11. " ++ (show n) ++ " is not valid."
          | otherwise = fromJust $ lookup n semitones

noteToInt :: Note -> Int
noteToInt note = noteToInt' semitones note
noteToInt' [] note = error $ note ++ " is not a note"
noteToInt' ((n, notes):ns) note = 
          if note `elem` notes 
          then n
          else noteToInt' ns note

addMod12 :: Int -> Int -> Int
addMod12 note semitones = (note + semitones) `mod` 12

addNote :: Note -> Int -> [Note]
addNote note semitones = intToNote $ addMod12 (noteToInt note) semitones

indexOf :: (Eq a, Show a) => a -> [a] -> Int
indexOf x [] = error "indexOf: not in list"
indexOf x (a:as)
        | x == a = 0
        | otherwise = 1 + (indexOf x as)

nextNoteName :: Note -> Note
nextNoteName note = noteNames !! (((indexOf note noteNames) + 1) `mod` 7)

noteFromNotes::Note->[Note]->Note
noteFromNotes note notes = head $ filter (\n -> (head n) == (head note)) notes

scale tonic mode = reverse $ scale' [tonic] mode
scale' notes [] = notes
scale' notes@(n:ns) (s:ss) = scale' (nextNote:notes) ss
       where nextNote = noteFromNotes (nextNoteName n) (addNote n s)