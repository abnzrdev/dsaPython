from collections import Counter
def towers(bar_len):
    freq = Counter(bar_len)
    tallest = max(freq.values())  
    amt = len(freq)              
    return tallest, amt
    
if __name__ == "__main__":
    num = int(input(""))
    nums = list(map(int, input("").split()))
    result = towers(nums)
    print(result[0], result[1], end=" ")
