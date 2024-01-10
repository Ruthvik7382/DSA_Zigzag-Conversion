#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # Checks for cases where numRows ==1 or greater than len(s) because in both cases the string is in a zigzag pattern and no conversion is needed
        if numRows == 1 or numRows >= len(s):
            return s

        # EMPTY STRING TO STORE RESULT
        result = ""

        # Calculate the step size for each row
        # Since there are two movements i.e up and down 
        step = 2 * numRows - 2

        # Iterate through each row
        for i in range(numRows):
            j = i
            # Handle the first and last rows separately
            if i == 0 or i == numRows - 1:
                while j < len(s):
                    result += s[j]
                    j += step
            else:
                # For other rows, add both characters in a zigzag pattern
                while j < len(s):
                    result += s[j]
                    j += 2 * (numRows - 1 - i)
                    if j < len(s):
                        result += s[j]
                        j += 2 * i

        return result


# In[17]:


solution = Solution()
input_string = "COLUMBIA"
numRows = 4
result = solution.convert(input_string, numRows)
print(result)


# In[ ]:




