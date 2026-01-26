class Solution(object):
    def maxProfit(self, prices):
        mi=float('inf')
        ma=0
        for p in prices:
            if p<mi:
                mi=p
            elif p-mi>ma:
                ma=p-mi
        return ma
