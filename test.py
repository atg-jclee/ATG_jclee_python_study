#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[2]:


def print_current_time() :
    print(f"Now : {time.strftime('%X')}")
    print('jenkins CI test4444')
    time.sleep(1)


# In[3]:


def main():
    print('print_current_time')
    while True:
        print_current_time()


# In[4]:


if __name__ == '__main__':
    print('main')
    main()

