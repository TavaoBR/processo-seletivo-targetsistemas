seq_a = [1,3,5,7]
next_a = seq_a[-1] + 2
print(f"a) {next_a}") # 9

seq_b = [2, 4, 8, 16, 32, 64]
next_b = seq_b[-1] * 2
print(f"b) {next_b}") # 128

seq_c = [0, 1, 4, 9, 16, 25, 36]
next_c = (len(seq_c))**2
print(f"c) {next_c}") # 49

seq_d = [4, 16, 36, 64]
next_d = (len(seq_d)*2)**2
print(f"d) {next_d}") # 100

seq_e = [1, 1, 2, 3, 5, 8]
next_e = seq_e[-1] + seq_e[-2]
print(f"e) {next_e}") # 13

seq_f = [2, 10, 12, 16, 17, 18, 19]
next_f = 20
while next_f % 5 == 0:
    next_f += 1
print(f"f) {next_f}") # 21


#Resultados 
# a) 9
# b) 128
# c) 49
# d) 100
# e) 13
# f)  21