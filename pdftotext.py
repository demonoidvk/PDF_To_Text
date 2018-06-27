
# coding: utf-8

# In[1]:


import subprocess, os
import glob


# In[ ]:


pdf_files =glob.glob("./data1/*.pdf")
for p in pdf_files:
    cmd= "pdftotext " + p 
    p=subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
    p.wait()
    

