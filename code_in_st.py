import streamlit as st
import os
import runpy

input_=st.text_area('Area for textual entry')
#st.write(input_)


with open('test.py', 'w') as f: # opción "a" append
  if os.stat('test.py').st_size > 0:
    pass
  else:
    f.write('import streamlit as st\n')
  f.write(input_+'\n')


runpy.run_path('test.py')
