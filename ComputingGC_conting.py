with open(myFasta.txt) as data:
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

