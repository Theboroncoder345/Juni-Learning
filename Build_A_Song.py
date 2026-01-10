import pysynth

# example:
potter = [('b3', 4), ('e', -4), ('g', 8), ('f#', 4),
          ('e', 2), ('b', 4), ('a', -2), ('f#', 2)]
pysynth.make_wav(potter, fn= 'potter.wav')

# write the code to build your own song below:
DSB = [("e1", 2), ("e1",8), ("f#1", 8), ("g#1", 8), ("b1", 2),
       ("b1", 8), ("c#2", 8), ("d#2", 8), ("c#2", 2), ("c#2", 8),
       ("d#2", 8), ("e2", 8), ("a1", -4), ("a1", -4), ("d#2", 8),
       ("e2", 8), ("e1", 2), ("e1",8), ("f#1", 8), ("g#1", 8),
       ("b1", -4), ("b1", 4), ("b1", 8), ("c#2", 8), ("d#2", 8),
       ("g#1", -4), ("g#1", -4), ("g#2", 8), ("g#1", 8), ("a1", 4),
       ("a1", 8), ("a1", 2), ("d#2", 8), ("e2", 8), ("e1", 8), ("e1", 1)]
pysynth.make_wav(DSB, fn= 'Dontstopbelieving.wav')
