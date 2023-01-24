class Solution: 
    def romanToInt(self, input):
        values = {"I":1, "V":5, "X":10, "L":50,"C":100, "D":500,"M":1000}
        total = 0
        for i in range(len(input)):
            numeral = input[i]

            # last iteration
            if i == len(input)-1:
                total += values[numeral]
            
            # all other iterations
            else:
                next_num = input[i+1]

                # normal case, current is > next
                if values.get(numeral) >= values.get(next_num):
                    total += values.get(numeral)
                
                # other case, current is < next
                else: 
                    total -= values.get(numeral)

        return total

