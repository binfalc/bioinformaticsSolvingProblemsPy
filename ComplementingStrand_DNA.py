"""The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC")."""

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s

my_sequence = input("input your strand here")
# start with an empty list
answer = []
# set the complement for each nucleotide
complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

# for each nucleotide in my sequence
for nucleotide in my_sequence:
    # append the complementary nucleotide in the answer list
    answer.append(complement[nucleotide])

# the output is the reversed list without spaces between characters
print(''.join(answer[::-1]))
