def main():
    a = int(input('enter a  : '))
    n = int(input('enter n: '))
    cal(a, n)

def cal(a, n):
    mod = n
    p = []
    p.append(0)
    p.append(1)
    quotient = []
    remainer =[]
    while (n % a != 0):
        q = n//a
        r = n - a*q
        n = a
        a = r
        quotient.append(q)
        remainer.append(r)
    print('p 0 = 0')
    print('p 1 = 1')
    for i in range(len(quotient)):

        # # p[i+2] = p[i]-p[i+1]*quotient[i]
        p.append(p[i+2-2]-p[i+2-1]*quotient[i])
        while p[i+2] < 0:
            p[i+2] =p[i+2] + mod
        while p[i+2] > mod:
            p[i+2] = p[i+2]-mod
        print('p',i+2,'=', p[i+2-2], '- (',p[i+2-1],') *', quotient[i], 'mod 26','=',p[i+2])
    print('t = ', p[len(p)-1])
    print('______________________________________')

main()







