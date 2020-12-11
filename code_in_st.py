import streamlit as st
import os
import runpy
st.write('Better use with [Cheat Sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/master/app.py)')
input_=st.text_area('Area for Python+Streamlit code. Try: st.balloons()')
#st.write(input_)


with open('test.py', 'w') as f: # opción "a" append
  if os.stat('test.py').st_size > 0:
    pass
  else:
    f.write('import streamlit as st\n')
  f.write(input_+'\n')


runpy.run_path('test.py')
