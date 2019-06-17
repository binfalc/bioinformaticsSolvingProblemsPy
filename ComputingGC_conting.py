from Bio import SeqIO

GC = 0

records = open("firstSample1.fasta", "r")
for record in SeqIO.parse(records, 'fasta'):
    count = 0
    totalcount = 0
    for nt in record.seq:
        totalcount = totalcount + 1
        if nt in "gcGC":
            count = count + 1
    percent = count / totalcount * 100
    if percent > GC:
        GC = percent
        ID = record.id

print(ID)
print(GC)
records.close()

