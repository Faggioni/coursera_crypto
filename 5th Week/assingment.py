import numtools as nt
import math
import numbthy as nb
import time as t

p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
B = int(math.pow(2,20))

#Creating Hash Table
def genhash():
    start = t.time()
    hash_table = []
    for i in range(int(B + 1)):
        hash_table.append(h * nb.inverse_mod(nb.power_mod(g,i,p),p))
    print 'Execution Time:' + str((t.time() - start))
    return hash_table


#Searching for the values
def comparison(table):
    start = t.time()
    for i in range(int(B + 1)):
        a = nb.power_mod(g,B*i,p)
        for j in table:
            if(j == a):
                x0 = table.index(j)
                x1 = j
                print 'x0'
                print x0
                print 'x1'
                print x1
                print 'Execution Time:' + str((t.time() - start))
                return x0,x1

#Calculates x0 and x1
def calx(x0,x1):
    start = t.time()
    print 'Execution Time:' + str((t.time() - start))
    return x0 * B + x1


#main function
def main():
    print 'Process Begin'
    start = t.time()
    table = genhash()
    print 'Hash Table Generated'
    x0 , x1 = comparison(table)
    x = calx(x0,x1)
    print x
    print 'Process Finished'
    print 'Execution Time:' + str((t.time() - start))
