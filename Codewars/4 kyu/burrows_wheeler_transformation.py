raw_str = "Humble Bumble"
bwt_matrix = []
for letter_index in range(len(raw_str)):
    tmp_lst = []
    for letter in raw_str[letter_index:]:
        tmp_lst.append(letter)
    for letter in raw_str[0:letter_index]:
        tmp_lst.append(letter)
    bwt_matrix.append(tmp_lst)
tmp_lst = bwt_matrix[0].copy()
bwt_matrix.sort()
n = bwt_matrix.index(tmp_lst)
enc_str = ''
for word_lst in bwt_matrix:
    enc_str += word_lst[-1]
for i in bwt_matrix:
    print(i)
print(enc_str, n)

last_str = [i for i in enc_str]
first_str = sorted(enc_str)
print(first_str)
print(last_str)
dec_str = first_str[n]
first_str.pop(n)
last_str.pop(n)
# while len(dec_str) != len(enc_str):

# TODO...