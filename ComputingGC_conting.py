def readFastaEntry( fp ):
    string = ""
    while True:
        line = string or f.readline()
        if not line:
            break
        seq = []
        while True:
            string = f.readline()
            if not string or string.startswith(">"):
                break
            else:
                seq.append(string)
        yield (line, "".join(seq))


with readFastaEntry() as data:
    for line in data:
        if '>' in line:
            continue
        myDNAstring += line.strip()

def gc_count(s):
    num_gc = 0
    for char in s:
        if char in "gcGC":
            num_gc = num_gc + 1
    return num_gc


print(gc_count(myDNAstring))

