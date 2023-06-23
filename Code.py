from Bio.Seq import Seq

k1 = Seq('CATAAGA')
k2 = Seq('AAACAGA')

# Calculate the Hamming distance
hamming_distance = sum(a != b for a, b in zip(k1, k2))

print(hamming_distance)

#or

def hamming_distance(string1, string2):
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance

string1 = input("Please enter the first sequence: ")
string2 = input("Please enter the second sequence: ")

distance = hamming_distance(string1, string2)
print("Hamming distance:", distance)
