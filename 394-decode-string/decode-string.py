class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num=0
        stack=[]
        curr_str=""
        for x in s:
            if x.isdigit():
                num=num*10+int(x)
            elif x=='[':
                stack.append((num,curr_str))
                num=0
                curr_str=""
            elif x==']':
                num,prev_str=stack.pop()
                curr_str=prev_str+num*curr_str
                num=0
            else:
                curr_str=curr_str+x
                
        return curr_str