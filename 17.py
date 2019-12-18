from intcode import IntCode
from utility import draw
from collections import defaultdict, Counter

def add(p, p2):
    return (p[0]+p2[0], p[1]+p2[1])

def score(p, f):
    if f[p] == 35 and f[add(p,(1,0))] == f[add(p,(-1,0))] == f[add(p,(0,1))] == f[add(p,(0,-1))] == 35:
        return p[0]*p[1]
    return 0


def find_sublists():
    l = 'R8R8R4R4R8L6L2R4R4R8R8R8L6L2'

    #for i in range(0, len(l), 2):
    for i in range(1):
        l2 = l[:]
        a = l2[:i]

        a = "R8R8"

        if a == "":
            continue



        #print("a = {}".format(a))
        l2 = l2.replace(a, "A")



        for j in range(0, len(l2), 2):
            l3 = l2[:]

            while len(l3) > 0 and l3[0] in "ABC":
                l3 = l3[1:]

            print(l3)

            b = l3[:j]
            if "-" in b:
                break
            if b == "":
                continue

            print("  b = {}".format(b))
            l3 = l3.replace(b, "B")
            for k in range(0, len(l3), 2):
                l4 = l3[:]

                while len(l4) > 0 and l4[0] in "ABC":
                    l4 = l4[1:]

                c = l4[:k]
                if "-" in c:
                    break
                if c == "":
                    continue
                print("    c = {}".format(c))
                l4 = l4.replace(c, "C")

                print("      ", l4)

                if all(list(map(lambda x: x in "ABC", l4))):
                    print("FOUND: a = {}, b = {}, c = {}".format(a,b,c))
                    print("  --> {}".format(l[:].replace(a, "A").replace(b, "B").replace(c, "C")))




def combinations(l):
    out = []
    for n in range(2, len(l)+1, 2):
        for i in range(0, len(l), 2):
            a = l[i:i+n]
            if len(a) == n:
                out.append(a)
    return out

def filter_invalid(l):
    return list(filter(lambda x: all(e not in x for e in "-ABC"), l))


def check_sublists(l, c, sublists):

    if c > 4:
        return False, []

    if all(list(map(lambda x: x in "-ABC", l))):

        if len(l) <= 20 and all(map(lambda x: len(x) <= 10, sublists)):
            #print("found: {} - {}".format(sublists, l))
            return True, sublists

        return False, []

    for p in filter_invalid(combinations(l)):
        l2 = l[:]
        l2 = l2.replace(p, "-A" if c == 1 else "-B" if c == 2 else "-C")

        b, sl = check_sublists(l2, c+1, sublists + [p])
        if b:
            return True, sl
    return False, []

if __name__ == "__main__":

    data = [1,330,331,332,109,3080,1101,0,1182,15,1101,0,1403,24,1001,0,0,570,1006,570,36,1002,571,1,0,1001,570,-1,570,1001,24,1,24,1105,1,18,1008,571,0,571,1001,15,1,15,1008,15,1403,570,1006,570,14,21101,58,0,0,1105,1,786,1006,332,62,99,21102,333,1,1,21101,0,73,0,1105,1,579,1102,0,1,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,101,0,574,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1106,0,81,21102,1,340,1,1105,1,177,21102,477,1,1,1105,1,177,21102,1,514,1,21102,1,176,0,1106,0,579,99,21101,184,0,0,1105,1,579,4,574,104,10,99,1007,573,22,570,1006,570,165,1002,572,1,1182,21101,0,375,1,21102,211,1,0,1105,1,579,21101,1182,11,1,21102,1,222,0,1106,0,979,21101,0,388,1,21102,233,1,0,1105,1,579,21101,1182,22,1,21101,244,0,0,1105,1,979,21101,0,401,1,21101,255,0,0,1106,0,579,21101,1182,33,1,21101,266,0,0,1106,0,979,21101,0,414,1,21102,1,277,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21101,313,0,0,1105,1,622,1005,575,327,1101,1,0,575,21101,327,0,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,20,26,0,109,4,1202,-3,1,587,20102,1,0,-1,22101,1,-3,-3,21101,0,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1106,0,597,109,-4,2106,0,0,109,5,1202,-4,1,630,20101,0,0,-2,22101,1,-4,-4,21102,0,1,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20102,1,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21101,0,702,0,1105,1,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,1,731,0,1106,0,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,756,0,0,1105,1,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21101,774,0,0,1105,1,622,21201,-3,1,-3,1106,0,640,109,-5,2105,1,0,109,7,1005,575,802,20101,0,576,-6,21002,577,1,-5,1106,0,814,21102,0,1,-1,21101,0,0,-5,21101,0,0,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,43,-3,22201,-6,-3,-3,22101,1403,-3,-3,2102,1,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21101,0,1,-1,1106,0,924,1205,-2,873,21101,35,0,-4,1106,0,924,1201,-3,0,878,1008,0,1,570,1006,570,916,1001,374,1,374,1201,-3,0,895,1101,2,0,0,1201,-3,0,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20102,1,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,43,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,39,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21101,0,973,0,1105,1,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21101,0,0,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21102,1,-4,-2,1106,0,1041,21102,1,-5,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,1201,-2,0,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,2101,0,-2,0,1106,0,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1105,1,989,21101,0,439,1,1106,0,1150,21102,1,477,1,1106,0,1150,21101,514,0,1,21101,1149,0,0,1106,0,579,99,21101,1157,0,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,1201,-5,0,1176,2101,0,-4,0,109,-6,2105,1,0,28,5,38,1,3,1,38,1,3,1,38,1,3,1,38,1,3,1,38,1,3,1,34,9,34,1,3,1,38,1,3,1,38,1,3,1,34,9,34,1,3,1,38,1,3,1,38,1,3,1,34,5,3,5,30,1,11,1,30,1,11,1,30,1,11,1,22,9,11,5,18,1,23,1,18,1,23,1,18,1,23,1,10,7,1,1,19,9,6,1,5,1,1,1,19,1,3,1,3,1,6,1,5,1,1,5,15,1,3,1,3,1,6,1,5,1,5,1,15,1,3,1,3,1,6,11,1,1,1,7,3,5,3,11,6,1,3,1,1,1,1,1,9,1,11,1,5,1,6,1,1,9,7,1,11,1,5,1,6,1,1,1,1,1,1,1,1,1,9,1,11,1,5,1,6,9,1,9,11,7,8,1,1,1,1,1,3,1,30,9,3,1,30,1,3,1,1,1,5,1,30,1,3,1,1,7,30,1,3,1,38,1,3,1,38,1,3,1,38,5,34]

    machine = IntCode(data)

    f = machine.get_outputs()
    field = defaultdict(int)

    x = 0
    y = 0
    for c in f:
        if c == 10:
            y += 1
            x = 0
            continue

        field[(x,y)] = c
        x += 1

    #draw(field, {35: "█", 46: " "})

    # solution for puzzle 1:
    print(sum(score(x, field) for x in list(field)))

    data[0] = 2

    #find_sublists()

    l = 'R8R8R4R4R8L6L2R4R4R8R8R8L6L2'
    b, sl = check_sublists(l, 1, [])

    print(sl)

    mapping = {0:"A", 1:"B", 2:"C"}

    for i, s in enumerate(sl):
        l = l.replace(s, mapping[i])
    print(l)



# solution for 15.01: 244
# solution for 15.02: 278
