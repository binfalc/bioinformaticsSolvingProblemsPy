from Bio import SeqIO

records = list(SeqIO.parse("firstSample.fasta", "fasta"))
print(records[0].id)  # first record
print(records[-1].id)  # last record


myDNAstring = ""
def gc_count(s):
    num_gc = 0
    for char in s:
        if char in "gcGC":
            num_gc = num_gc + 1
    return num_gc


print(gc_count(myDNAstring))

