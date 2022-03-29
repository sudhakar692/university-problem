class Solution:
    def solve(self, n):
        ab = 4

        invalid_ways = [0]*(n+1)

        if n >= ab:
            invalid_ways[ab] = 1

        for i in range(ab+1, n+1):
            invalid_ways[i] = invalid_ways[i-1] + invalid_ways[i-2] + \
                invalid_ways[i-3] + invalid_ways[i-4]+(2**(i-ab))

        no_of_valid_ways_to_attend = (2 ** n) - invalid_ways[n]

        # Total no. of combinations in which I'll miss the ceremony because not present at last day
        not_able_to_attend = (2 ** n) // 2 - \
            (invalid_ways[n] - invalid_ways[n-1])

        # The probability that you will miss your graduation ceremony.
        result = f"{not_able_to_attend}/{no_of_valid_ways_to_attend}"
        return result


if __name__ == '__main__':
    print("Started running test cases...")
    s = Solution()
    assert s.solve(5) == '14/29'
    assert s.solve(10) == '372/773'
    print("All test cases passed!")
