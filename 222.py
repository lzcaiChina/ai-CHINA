import streamlit as st

st.title("鸡兔同笼计算器")
st.subheader("输入头和脚的数量，一键计算！")

# 初始化会话状态，记录是否继续计算
if "continue_calc" not in st.session_state:
    st.session_state.continue_calc = True

if st.session_state.continue_calc:
    try:
        # 输入框，限制为整数
        n = st.number_input("请输入几个头", min_value=1, step=1, key="n")
        m = st.number_input("请输入几个脚", min_value=2, step=2, key="m")
        
        if st.button("开始算！"):
            n = int(n)
            m = int(m)
            x = m/2 - n
            y = n*2 - m/2
            # 保留你的判断逻辑和吐槽文案
            if x>=0 and y>=0 and x%1==0 and y%1==0 and m%2==0:
                st.success(f"兔子{int(x)}只，鸡{int(y)}只")
            else:
                st.error("你是个潮霸，连题都不会出")
            
            # 继续/退出选择
            choice = st.radio("笨蛋是否要继续计算？？！（输入y继续，随便一按就滚蛋了哦：）", 
                              options=["y", "滚蛋"], key="choice")
            if choice != "y":
                st.session_state.continue_calc = False
                st.warning("你滚蛋了")
    except ValueError:
        st.error("输入的不是数字！重新输入！")
else:
    # 重新计算按钮，重置状态
    if st.button("再算一次！"):
        st.session_state.continue_calc = True
        st.experimental_rerun()
