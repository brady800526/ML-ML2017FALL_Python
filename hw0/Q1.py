#!/usr/bin/env python
# coding: utf-8

# ## Proprocess the text to list

# In[66]:


import sys


# In[67]:


words = open(sys.argv[1], 'r')
words_list = list(map(str.strip,words.read().split(' '))) # remove the leading and trailing space


# ## Add each word into dictionary and keey the order

# In[25]:


from collections import OrderedDict
words_count_dict = OrderedDict()

for word in words_list:
    if word not in words_count_dict:
        words_count_dict[word] = 1
    else:
        words_count_dict[word] += 1
words_count_dict


# ## Output the words count to txt file

# In[65]:


output_file = open('Q1.txt', 'w')
for index, (word, count) in enumerate(words_count_dict.items()):
    if index != len(words_count_dict)-1:
        output_file.writelines(f'{word} {index} {count}\n')
    else:
        output_file.writelines(f'{word} {index} {count}')
output_file.close()

