#!/usr/bin/python
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


T = int(raw_input())

for cas in range(1,T+1):
    goal = int(raw_input())
#    eprint("goal",goal)
    cas_done = False
#    eprint("CASE == ",cas)
    for r in xrange(5):
        for c in xrange(5):
            #eprint("START",r,c)
            if cas_done:
                break
            left = 9

            DONE = [[0 for x in range(3)] for y in range(3)]
            rr = 2+3*r
            cc = 2+3*c

            while left > 0:
                #eprint("{0} {1}".format(rr,cc))
                sys.stderr.flush()
                print("{0} {1}".format(rr,cc))
                sys.stdout.flush()
                rdone,cdone = map(int,raw_input().split())
                #eprint(rdone,cdone)
                if rdone == 0 and cdone == 0:
                    cas_done = True
                else:
                    r2 = (rdone-rr)+1
                    c2 = (cdone-cc)+1

                    #eprint(r2,c2)
                    if not DONE[r2][c2]:
                        left -= 1
                        DONE[r2][c2] = True
                    #eprint(DONE)
                    sys.stderr.flush()
