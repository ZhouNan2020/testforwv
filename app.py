import streamlit as st
import pandas as pd
#%%
#大标题“ES-SCLC治疗周期综合管理平台”
st.title('ES-SCLC治疗周期综合管理平台')
# 将streamlit的页面分成两列
left_column, right_column = st.columns(2)

#%%
# 左侧显示副标题“患者数据输入“
left_column.subheader('患者数据输入')
# 文本输入框，label=”患者年龄“
age = left_column.text_input(label='患者年龄')
# 下拉框，label=”患者性别“，options=[‘男’，‘女’]
gender = left_column.selectbox(label='患者性别', options=['男', '女'])
# 