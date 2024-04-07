import math

def fft(a, inv):
    n = len(a)
    
    if n == 1:
        return
    
    a0 = a[::2]
    a1 = a[1::2]
    
    fft(a0, inv)
    fft(a1, inv)
    
    ang = 2 * math.pi / n * (-1 if inv else 1)
    wn = complex(math.cos(ang), math.sin(ang))
    
    w = 1
    for i in range(n // 2):
        t = w * a1[i]
        a[i] = a0[i] + t
        a[i + n // 2] = a0[i] - t
        
        if inv:
            a[i] /= 2
            a[i + n // 2] /= 2
        
        w *= wn

def main():
    N = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    Q = int(input())
    Y = list(map(int, input().split()))

    MAX = 2 ** 18
    x_a = [0] * MAX
    x_b = [0] * MAX
    x_c = [0] * MAX

    for val in a:
        x_a[val] += 1
    for val in b:
        x_b[val] += 1
    for val in c:
        x_c[val] += 1

    fft(x_a, False)
    fft(x_b, False)
    fft(x_c, False)

    for i in range(MAX):
        x_a[i] *= x_b[i] * x_c[i]

    fft(x_a, True)

    c = [int(val.real + 0.1) for val in x_a]

    for yi in Y:
        print(c[yi])

if __name__ == "__main__":
    main()
