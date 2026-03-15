def largest_prime(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False

    for p in range(2, int(n**0.5)+1):
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i] = False
    
    for i in range(n,1,-1):
        if prime[i]:
            print("Largest prime <=",n, "is",i)
            break

n = int(input("Enter number :"))
largest_prime(n)