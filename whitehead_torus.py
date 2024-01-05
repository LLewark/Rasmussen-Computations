#!/usr/bin/python3
# For Morse code format, see documentation at
# https://cbz20.raspberryip.com/code/khtpp/docs/Input.html

import subprocess, os

def morse2PD(m):
    result = subprocess.run(['./morse2pd.py', m], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')[:-1]

# Given morse code of a 1-1-tangle s, return morse code of the doubled tangle (with blackboard framing)
# The two strands are oriented according to updown1 and updown2 (1 for up, 0 for down)
def doublemorse(s,updown1,updown2):
    assert(s[-2:] == ',1')
    pieces = [[x[0],int(x[1:])] for x in s[:-2].split(".")]
    result = ""
    for x in pieces:
        if x[0] in ["l","r"]:
            y1 = "l" if (updown1 == 0) else "r"
            y2 = "l" if (updown2 == 0) else "r"
            result += y1 + str(2*x[1]) + "."
            result += y2 + str(2*x[1] + 1) + "."
        elif x[0] in ["u"]:
            result += x[0] + str(2*x[1] + 1) + "."
            result += x[0] + str(2*x[1]) + "."
        elif x[0] in ["x","y"]:
            result += x[0] + str(2*x[1] + 1) + "."
            result += x[0] + str(2*x[1]) + "."
            result += x[0] + str(2*x[1] + 2) + "."
            result += x[0] + str(2*x[1] + 1) + "."
    return result[:-1] + "," + str(updown1) + "," + str(updown2)


# Given the morse code a 2-2-tangle with downwards-upwards orientation,
# return the morse code of the link obtained by attaching a positive Whitehead clasp
def whitehead(s, twists):
    assert(s[-4:] == ',0,1')
    x = 'x' if twists < 0 else 'y'
    return "l0.r1." + s[:-4] + ("." + x + "0") * abs(2*twists) + ".l1.y0.y2.u1.u1.u0,"

# Returns Morse code for the braid (sigma_1 ... sigma_(strands-1))^twists
# All strands except one closed up, i.e. a 1-1-tangle, oriented upwards
def torusmorse(strands, twists):
    s = ".".join(["l" + str(s) for s in range(1, strands)])
    t = "." + ".".join(["y" + str(s) for s in range(strands - 1)])
    s += twists * t
    s += "." + ".".join(["u" + str(s) for s in reversed(range(1, strands))])
    return s + ",1"


# Print PD codes of the 3n-twisted positive Whitehead double of the T(2,2n+1) torus knot
# for 0 < n < 100.
for n in range(1,100):
    strands = 2
    twists = 2*n + 1
    framing = 3*n
    blackboardframing = framing - twists * (strands - 1)
    print(morse2PD(whitehead(doublemorse(torusmorse(strands, twists),0,1),blackboardframing)))
