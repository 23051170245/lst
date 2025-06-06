import streamlit as  st
import pandas as pd
import numpy as np


st.subheader('🧭南宁美食图')
st.map( pd.DataFrame({
                'latitude':[22.853986,22.826429,22.843103,22.772474,22.754556],
                'longitude':[108.222308,108.289355,108.267250,108.267086,108.266534]
}))

st.header("🍉用餐高峰时段")
# 定义数据,以便创建数据框
data = {
    '时段':[11, 12, 13],
    '粤味炒面':[10, 20, 9],
    '陕西凉面':[11, 16, 12],
    '隆江猪脚饭':[11, 10, 16],
    '小耳朵自助':[13,14,18],
    '麦当劳(华成都市店)':[14,19,17]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,], name='序号')
# 将新索引应用到数据框上
df.index = index
st.area_chart(df, x='时段')


# 定义数据,以便创建数据框
data = {
    '美食':['粤味炒面', '陕西凉面', '隆江猪脚饭','小耳朵自助','麦当劳（华成都市店）'],
    '评分':[6,7,5,10,8],

}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,4,5], name='序号')
# 将新索引应用到数据框上
df.index = index

st.header("🍟美食评分")
st.bar_chart(df, x='美食')
st.header("🍚不同食物类型价格")
# 定义数据,以便创建数据框
data = {
   '月份':['01月', '02月', '03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
    '粤味炒面':[20, 15, 18,12,13,14,15,17,12,13,11,12],
    '陕西凉面':[12, 16, 12,12,12,13,14,15,16,12,11,12],
    '隆江猪脚饭':[11, 10, 16,13,13,13,12,11,13,14,15,15],
    '麦当劳（华成都市店）':[38,39,60,68,92,75,24,75,93,54,12,57],
    '小耳朵自助':[12,43,65,126,242,72,78,12,56,23,89,65]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,4,5,6,7,8,9,10,11,12], name='月份')
# 将新索引应用到数据框上
df.index = index
st.line_chart(df, x='月份')

st.title('🍽餐厅详情')
with st.expander("陕西凉面"):
        c1, c2= st.columns(2)
        c1.markdown('## 凉面')
        c1.markdown('##### 评分')
        c1.markdown('# 4.9/5.0')
        c1.markdown('#### 人均消费')
        c1.markdown('# 8元')

        c2.markdown('**推荐菜品：**')
        c2.markdown(' • &#8194;凉面')
        c2.markdown(' • &#8194;凉皮')
        c2.markdown(' • &#8194;牛筋面')


st.subheader('当前拥挤程度')
st.progress(10,text="10%拥挤")

st.title('😍今日推荐')
st.markdown("<span style='color:red; border:2px solid red; border-radius:8px; padding:4px;'>干饭首选👍</span>", unsafe_allow_html=True)

# 初始化会话状态
if 'count' not in st.session_state:
    st.session_state.count = 0

count = 0;
if st.button(' :red[今天吃什么]'):
    st.session_state.count += 1
if st.session_state.count % 6 == 1:
    st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：陕西凉面</span>", unsafe_allow_html=True)
    st.markdown("![凉面](https://ts1.tc.mm.bing.net/th/id/R-C.c4f9d2804de17a426bbbfe01f845bee0?rik=A%2fUr1w9HWql3zQ&riu=http%3a%2f%2fcp2.douguo.net%2fupload%2fcaiku%2f6%2f4%2f4%2fyuan_644c75deaa57dec86c9a1466bf4e9b24.jpeg&ehk=3tIXMW8ygcrovrBpyeXpQVKYI2TMDTXZsn6j1UEkxCk%3d&risl=&pid=ImgRaw&r=0)")
if st.session_state.count % 6 == 2:
    st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：隆江猪脚饭</span>", unsafe_allow_html=True)
    st.markdown("![隆江猪脚饭](https://tse4-mm.cn.bing.net/th/id/OIP-C.-k_asvs8q7pV6L0SErCCDwHaE8?rs=1&pid=ImgDetMain)")
if st.session_state.count % 6 == 3:
    st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：粤味炒面</span>", unsafe_allow_html=True)
    st.markdown("![炒面](https://tse4-mm.cn.bing.net/th/id/OIP-C.n8IVnjGT4gKae0ePpsFaywHaE8?rs=1&pid=ImgDetMain)")
if st.session_state.count % 6 == 4:
    st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：麦当劳(华成都市店)</span>", unsafe_allow_html=True)
    st.markdown("![麦当劳](https://ts1.tc.mm.bing.net/th/id/R-C.176e0c004b334b40a095e616ec24a1e1?rik=TVEMBdkSJyRxnQ&riu=http%3a%2f%2fimg.qqjm.com%2f2019%2f05%2f596282113YYi.jpg&ehk=iUw0USvxB8xgmxvtQOnoKpyHcsCJD0uhwAL4YKS%2b980%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1)")
if st.session_state.count % 6 == 5:
    st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：小耳朵自助</span>", unsafe_allow_html=True)
    st.markdown("![小耳朵自助](https://img95.699pic.com/photo/60001/9810.jpg_wh300.jpg!/fh/300/quality/90)")

