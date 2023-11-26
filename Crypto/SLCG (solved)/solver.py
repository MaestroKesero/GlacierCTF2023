from Crypto.Util.number import GCD


#gtfd{ 01100111 01100011 01110100 01100110 01111011
#g = 01100111 (valores 1)

s0 = 114293481651692805418121538415147589604
s1 = 54633022358060826155954146262572096344
s2 = 125313023815946519926697407430683658442
s3 = 162960109688532363602735593403961340669
s4 = 169104787290291550198916185039818769417




''' Valores antiguos
s0 = 54633022358060826155954146262572096344
s1 = 39246964755280114087344695441503859529
s2 = 162960109688532363602735593403961340669
s3 = 169104787290291550198916185039818769417
s4 = 13372371689034608934042109259651932913
'''


n1 = -((s3 - s2) * (s1 - s0)) + pow((s2-s1), 2)
n2 = -((s4 - s3) * (s2 - s1)) + pow((s3 - s2), 2) 

n = GCD (n1,n2)
print(n1)
print(n2)
print ("N es : ",n)

m = (s3 - s2) * pow(s2 - s1, -1, n2) % n2
print (m)

c = (s1 - s0*m) % n2
print (c)






'''
s0 = (m * seed) mod n
s1 = (m * s0) mod n
s2 = (m * s1) mod n
s3 = (m * s2) mod n
s4 = (m * s3) mod n

s2 - s1 = (s1 - seed) * m mod n
s3 - s2 = (s2 - s1) * m mod n
s4 - s3 = (s3 - s2) * m mod n


m = (s2 - s1) * (s1 - seed)⁻1 mod n
m = (s3 - s2) * (s2 - s1)⁻1 mod n
m = (s4 - s3) * (s3 - s2)⁻1 mod n

(s2 - s1) * (s1 - seed)⁻1 mod n = (s3 - s2) * (s2 - s1)⁻1 mod n
(s2 - s1)² = (s3 - s2) * (s1 - seed) mod n

(s2 - s1)² = (s3 - s2) * (s1 - seed)




(s3 - s2) * (s2 - s1)⁻1 mod n = (s4 - s3) * (s3 - s2)⁻1 mod n
(s3 - s2)² = (s4 - s3) * (s2 - s1) mod n

(s3 - s2)² = (s4 - s3) * (s2 - s1)





(s2 - s1)² = (s3 - s2) * (s1 - seed)
(s3 - s2)² = (s4 - s3) * (s2 - s1)

t0 = s1 - seed
t1 = s2 - s1
t2 = s3 - s2
t3 = s4 - s3
t4 = s5 - s4
t5 = s6 - s5

multiple1 = (s1 - seed * s3 - s2) - (s2 - s1)²
multiple2 = (t1 * t3) - pow(t2, 2)
multiple3 = (t2 * t4) - pow(t3, 2)
'''



'''
 En realidad el programa se traga 7 bits en binario y no 8, es por tanto que la lista entera de ct tiene valor
de 364, que es divisible entre 7 = 52 caracteres. Por tanto sabemos que la flag va a tener 46 caracteres
364 - (6 caracteres conocidos x 7 bits) = 322 / 7 = 46 caracteres de flag que no conocemos. Los resultados son enteros.
Tambien nos damos cuenta de que el primer cero a la izquierda no sirve por que toda representacion de caracteres en binario tiene ese 0 (quitando ñ).
'''