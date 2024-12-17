class Solution:
    def checkla( self,
                 s :str,
                 b :str ) -> bool:

        """
        to check string s and b
        """

        p_one = 0
        p_two = 0

        while p_two < len(b):
            if s[p_one] == b[p_two]:
                p_one += 1

            p_two+=1

        return p_one == len(s)

if __name__ == "__main__":

    s = Solution()
    print(s.checkla("abc", "ahbgdc"))
    print(s.checkla("axc", "ahbgdc"))


