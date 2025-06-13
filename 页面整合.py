import streamlit as st
import pandas as pd   # 导入Pandas并用pd代替
st.image('https://www.gxvnu.edu.cn/images/QQtupian20240701090920_fuben.png')
# 创建选项卡
st.markdown("""
    <style>
        .main > div {
            padding: 10rem 10rem;
        }
        .block-container {
            padding: 10rem 10rem;
            max-width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["数字档案", "南宁美食数据", "个人简历生成器"])
# 在第一个选项卡中添加内容
with tab1:
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
    
# 在第二个选项卡中添加内容
with tab2:
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



# 在第三个选项卡中添加内容
with tab3:
    st.title('🎨个人简历生成器')
    st.text('使用Streamlit创建您的个性化简历')
    c1,c2=st.columns([1,2])
    with c1:
        st.header('个人信息表单')
        st.markdown('***')
        st.session_state['name']=st.text_input('姓名')
        st.session_state['position']=st.text_input('职位')
        st.session_state['telephone']=st.text_input('电话')
        st.session_state['email']=st.text_input('邮箱')
        st.session_state['birthday']=st.text_input('出生日期')
        st.write('性别')
# 设置标签为“hidden”
# 设置水平排列
        xbie = st.radio(
            '你的性别是什么',
            ['男', '女', '其他'],
            horizontal=True,
           label_visibility='hidden'
    )
        st.write('学历')
        size = st.selectbox(
            '选择学历',
            ['小学', '初中', '高中','大学'],
            label_visibility='collapsed'
    )
        options_2 = st.multiselect(
        '语言能力(可多选)',
        ['中文', '英语', '日语', '德语', '意大利语'],
    ) 
        options_3 = st.multiselect(
        '技能(可多选)',
        ['C++', 'Java', 'Python', '机器学习', '人工智能'],
    )   

        from datetime import datetime, time

        st.subheader("工作经验（年）")
        age = st.slider('', 0, 30)
        st.write(" ", age, '年')

        st.subheader("期望工资范围")
        values = st.slider(
            '',
            1000.0, 30000.0, (1000.0,30000.0))
        jianjie=st.text_area(label='个人简介：',placeholder='请简要介绍您的专业背景、职业目标和个人特点...')

        st.write('最佳联系时间')
        size1 = st.selectbox(
                '语言能力',
                ['7:00', '8:30', '12:00','15:00'],
                label_visibility='collapsed'
    )

        uploaded_file=st.file_uploader("上传个人照片",type=['jpg', 'jpeg', 'png'])
    with c2:
        st.header('简历实时预览')
        st.markdown('***')
        if uploaded_file is None:
            st.warning('未上传图片')
        else:
            st.image(uploaded_file, caption='上传的图片',width=200)
        st.write('**姓名**：',st.session_state['name'])
        st.write('**职位**：',st.session_state['position'])
        st.write('**电话**：',st.session_state['telephone'])
        st.write('**邮箱**：',st.session_state['email'])
        st.write('**出生日期**：',st.session_state['birthday'])
        st.write('**性别**：',xbie)
        st.write('**学历**：',size)
        st.write('**语言能力**：',options_2)
        st.write('**技能**：',options_3)
        st.write('**工作经验(年)**：',age)
        st.write('**期望薪资范围**：',values)
        st.write('<span style="font-size:50px;">个人简介</span>:',jianjie,unsafe_allow_html=True)
        st.write('**最佳联系时间**：',size1)


