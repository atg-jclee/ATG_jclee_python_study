#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time
import asyncio


# In[7]:


def print_current_time() :
    print(f"Now : {time.strftime('%X')}")
    time.sleep(1)


# In[8]:


def main():
    print('print_current_time')
    while True:
        print_current_time()


# In[9]:


if __name__ == '__main__':
    print('main')
    main()

