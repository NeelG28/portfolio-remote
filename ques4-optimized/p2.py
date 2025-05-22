def is_prime_optimized(n):
        """Optimized and simpler prime check."""
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        c=0
        for x in range(1,n):
            if x%n==0:
                c=c+1
        
        if c==2:
            return True
        else:
            return False
        
