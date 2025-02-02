class Solution:

    # 2429. Minimum XOR Value of Two Numbers in an Array
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        num1_list = format(num1, '032b')
        num2_list = format(num2, '032b')
        x = ['0'] * 32
        num2_bits = num2_list.count('1')
        num1_bits = num1_list.count('1')
        
        for i,b in enumerate(num1_list):
            if b == '1' and num2_bits > 0:
                x[i] = '1'
                num2_bits -= 1

        for i in range(len(x)-1, -1, -1):
            if x[i] == '0' and num2_bits > 0:
                x[i] = '1'
                num2_bits -= 1

        binx = "".join(x)

        return int(binx,2)
        