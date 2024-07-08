#python expression

#1.tuliskan hasil dari ekspresi berikut 

print ("a", 15%5)
print ("b", 12 +3*5==75)
print ("c", "PML" + "15523")
print ("d", "100" + str(234))
print ("e", ((11%3)+2) != 8/2)
print('')

#2.diberikan 3 buah variabel p=11,q=5,dan r=4 tentukanlah ekspresi boolean berikut :

p=11
q=5
r=4

print ("a", ((p-r) == (r+q) ))
print ("b",(((p%3)+q)!=(r%2)))
print ("c", ((q-3)==(p%2+q)))
print ("d", ((r+q)!=((p*2)%2)))
print ("e", ((((q%3)+p)>(r%2))))
print ("f", (((r+p))<=(q*5)))

#apakah  hasil dari cuplikan kode berikut :

print ("Honey" + "Boo"*3)

capitals = {}
capitals['Murica']='Washington'
capitals['Germany']='Bonn'
capitals['France']='Paris'
capitals['England']='London'
capitals['Germany']='Berlin'
print (capitals['Germany'])

print('3.Hasil dari potongan Kode')
a = "23"
b=9
print (a+str(b))
print('')

print (4.)
letters = ["a","b","o","c","p"]

print (letters[1])
print (letters[len(letters)-2])
print (letters+["x"])
print (letters)
print ('')
 
print ("5.Apa hasil dari kode berikut")
hasil= ' '.join('h a n d s'.split())
print (hasil)
print(' ')

print (7.)
def pembagi_indeks(nums,divisor):
    for i in range(len(nums)):
        if nums[i] % divisor ==0:
            return i
        return -1
vals = [100,66,55,64,41,35,18,64]
hasil = pembagi_indeks(vals,5)
print(' ')

def mystery(n,m):
    p=0
    e=0
    while p < n :
        p= p + 1
        e= 0
    return p

print(mystery(4,3))