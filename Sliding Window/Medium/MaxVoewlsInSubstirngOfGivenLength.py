'''
1456. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        checkV = 'aeiou'
        count = 0

        #Building the window size of k
        for i in range(k):
            if s[i] in checkV:
                count+=1
        
        ans = count

        #Applying Sliding Window
        for i in range(k,len(s)):
            print(i)
            count+= 1 if s[i] in checkV else 0
            count-=1 if s[i-k] in checkV else 0
            ans = max(ans,count)

        return ans




        