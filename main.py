import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('steamlit 超入門編')

st.write('dataFrame')

df = pd.DataFrame({
    '1列目' : [1,2,3,4,5,6],
    '2列目' : [12,2,53,4,45,6]
})
st.dataframe(df)

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)
st.line_chart(df2)
df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns = ['lat','lon']
)
st.map(df3)

st.write('display Image')
img = Image.open('sample.jpg')
st.image(img, caption='test', use_column_width=True)

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='test', use_column_width=True)


option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は、',option,'です。'


st.write('Interactive widgets')

text = st.sidebar.text_input('あなたの好きな趣味を教えてください。')
'あなたの好きな趣味：',option

condision = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'あなたの調子は：',condision

expander = st.expander('お問い合わせ')
expander.write('お問い合わせを書く')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'done!!'