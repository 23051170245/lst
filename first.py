import streamlit as st  # 导入Streamlit并用st代表它
import pandas as pd   # 导入Pandas并用pd代替
st.title("🕶学生小李-数字档案")
st.header("🔑基础信息")
st.subheader("学生ID:`32576126`")
st.subheader("注册时间:`2023-10-31` ")
st.subheader("所在学院：`计算机与信息工程学院`")
st.subheader('📊技能矩阵')
c1, c2, c3 = st.columns(3)
c1.metric(label="c语言", value="95%", delta="2%")
c2.metric(label="python", value="67%", delta="1%")
c3.metric(label="java", value="58%", delta="3%")

data = {
    '日期':["01-02"," 06-14", "07-06"],
    '任务':["打扫卫生", "四级考试", "期末考试"],
    '难度':["★☆☆☆☆", "★★★★★", "★★★☆☆"],
}
# 定义数据框所用的索引
index = pd.Series([1, 2, 3], name='你好')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.subheader('任务日志')
st.dataframe(df)

st.subheader('🔐 最新代码成果')
# 创建要显示的Python代码块的内容
python_code = '''def matrix_():
    print("你好，Streamlit！")
'''
# 创建一个代码块，用于展示python_code的内容
# 并设置language为None，即该代码块无语法高亮
st.code(python_code, language=None)
# 创建一个代码块，用于展示python_code的内容
# language为默认，即该代码块以Python语法高亮
st.code(python_code)
# 创建一个代码块，用于展示python_code的内容
# language为默认，即该代码块以Python语法高亮
# 并设置line_numbers为True，即该代码块有行号
st.code(python_code, line_numbers=True)
st.markdown('***')
st.markdown(':green[`>>SYSTEM MESSAGE`:]等待指令')
st.markdown(':green[`>>TARGET`:]教务系统')
st.markdown(':green[`>>CUNTDOWN`:]2025-6-4')

