import streamlit as st
import pandas as pd
#%%
# 页面要最宽显示
st.set_page_config(layout="wide")
#大标题“ES-SCLC治疗周期综合管理平台”
st.title('ES-SCLC免疫治疗综合管理平台')
# 将streamlit的页面分成两列
left_column, right_column = st.columns(2)

#%%
# 左侧显示副标题“患者数据输入“
left_column.subheader('患者数据输入')
# 文本输入框，label=”患者年龄“
age = left_column.text_input(label='患者年龄')
# 下拉框，label=”患者性别“，options=[‘男’，‘女’]
gender = left_column.selectbox(label='患者性别', options=['男', '女'])
# 免疫治疗药物，下拉选择，label=”免疫治疗药物“，options=[‘Atezolizumab’，‘Durvalumab’，‘Nivolumab’，‘Pembrolizumab’]
drug = left_column.selectbox(label='免疫治疗药物', options=['Atezolizumab', 'Durvalumab', 'Nivolumab', 'Pembrolizumab'])
# 剂量，下拉选择，label=”剂量“，options=[‘1200mg’，‘1500mg’，‘其他’]
dose = left_column.selectbox(label='剂量', options=['1200mg', '1500mg', '其他'])
# 转移情况，下拉选择，label=”转移情况“，options=[‘无转移’，‘有转移’]
metastasis = left_column.selectbox(label='转移情况', options=['无转移', '有转移'])
# 合并疗法，下拉选择，label=”合并疗法“，options=[‘无合并疗法’，‘化疗’，‘放疗’，‘化疗+放疗’]
combined_therapy = left_column.selectbox(label='合并疗法', options=['无合并疗法', '化疗', '放疗', '化疗+放疗'])
# 化疗方案，下拉选择，label=”化疗方案“，options=[‘EP’，‘EC’，‘IP’，‘IC’]
chemotherapy = left_column.selectbox(label='化疗方案', options=['EP', 'EC', '其它'])
# 目前周期，下拉选择，label=”目前周期“，options=[‘1’，‘2’，‘3’，]
cycle = left_column.selectbox(label='目前周期', options=['1', '2', '3'])
#%%
# 右侧显示副标题“患者管理信息”
right_column.subheader('患者综合风险预测')

# 显示文字：患者风险评估
right_column.write('死亡风险评估：')

# 显示文字：30天死亡风险：0.1%；90天死亡风险：0.2%；180天死亡风险：0.3%
right_column.write('30天死亡风险：0.1%；90天死亡风险：0.2%；180天死亡风险：0.3%')
right_column.markdown('---')
# 显示文字：不良事件风险风险评估：
right_column.write('不良事件风险风险评估：')

# 显示文字：免疫相关不良事件风险：0.1%；非免疫相关不良事件风险：0.2%
right_column.write('免疫相关不良事件风险：0.1%；非免疫相关不良事件风险：0.2%')
right_column.markdown('---')
# 显示文字：转移风险评估：
right_column.write('复发和转移风险评估：')

# 显示文字：转移风险：0.1%
right_column.write('转移风险：0.1%')
right_column.write('转移风险：0.2%')

# 添加分割线
right_column.markdown('---')


