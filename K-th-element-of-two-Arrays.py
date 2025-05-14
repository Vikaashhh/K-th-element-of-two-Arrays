class Solution:
    def kthElement(self, a, b, k):
        # Ensure array 'a' is smaller for easier binary search
        if len(a) > len(b):
            return self.kthElement(b, a, k)
        
        n, m = len(a), len(b)
        low, high = max(0, k - m), min(k, n)
        
        while low <= high:
            # Mid point in 'a' (kitne elements 'a' se lenge)
            cutA = (low + high) // 2
            # Baaki elements 'b' se lene padenge
            cutB = k - cutA
            
            # Agar cut 0 hai to left side -infinity
            leftA = float('-inf') if cutA == 0 else a[cutA - 1]
            leftB = float('-inf') if cutB == 0 else b[cutB - 1]
            
            # Agar cut array ke end tak hai to right side +infinity
            rightA = float('inf') if cutA == n else a[cutA]
            rightB = float('inf') if cutB == m else b[cutB]
            
            # Check karo kya partition sahi hai
            if leftA <= rightB and leftB <= rightA:
                # Sahi partition mila - max(leftA, leftB) hoga answer
                return max(leftA, leftB)
            elif leftA > rightB:
                # Zyada elements 'a' se liye, thoda kam karo
                high = cutA - 1
            else:
                # Kam elements 'a' se liye, thoda badhao
                low = cutA + 1
        
        return -1  # Edge case, ideally yahan nahi aana chahiye
