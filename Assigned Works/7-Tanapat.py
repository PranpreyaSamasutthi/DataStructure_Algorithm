#!/usr/bin/env python
# coding: utf-8

# In[9]:


op = ["[","{","("]
cp = ["]","}",")"]

def check_Paranthesis(str):
    Stack = []
    for i in str:
        if i in op:
            Stack.append(i)
        elif i in cp:
            cp_pos = cp.index(i)
            if((len(Stack)>0)) and (op[cp_pos] == Stack[len(Stack)-1]):
                Stack.pop()
            else: return "not ok"
                  
    if len(Stack) == 0: return "ok"
    else: return "not ok"

string = "{[]{(Test)}}"
print(string,"-", check_Paranthesis(string))
string = "[{}{})(Test]"
print(string,"-", check_Paranthesis(string))
string = "(Test) Hello"
print(string,"-", check_Paranthesis(string))
string = "(Test) Hello(())"
print(string,"-", check_Paranthesis(string))
string = "123456((Test) Hello(())"
print(string,"-", check_Paranthesis(string))


# In[ ]:




