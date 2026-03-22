import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. 网页全局设置：开启宽屏模式，自定义网页标题
st.set_page_config(layout="wide", page_title="数据模拟系统")

# 2. 颜值升级：使用侧边栏 (Sidebar) 存放控制组件
with st.sidebar:
    st.header("⚙️ 参数控制面板")
    st.write("请在下方调整模型参数：")
    year_range = st.slider("滑动选择年份区间", 2016, 2036, (2016, 2026))

st.title("🌊 验潮站海平面动态模拟系统")
st.markdown("---") # 加一条华丽的分割线

# 3. 性能升级：使用缓存魔法！(注意这个装饰器)
@st.cache_data
def get_simulation_data(start_year, end_year):
    # 把原本耗时的数据生成步骤放进函数里
    np.random.seed(42)
    t = np.linspace(start_year, end_year, 500)
    data = 100 * np.sin(t) + 20 * np.random.normal(size=500) + (t - 2016) * 10
    return t, data

# 调用函数获取数据
t, data = get_simulation_data(year_range[0], year_range[1])

# 4. 绘图展示
fig = plt.figure(figsize=(12, 4)) # 把图表拉长一点，更好看
plt.plot(t, data, color='#1f77b4', linewidth=1.5)
plt.title(f"Tidal Station Simulation ({year_range[0]} - {year_range[1]})")
plt.xlabel("Year")
plt.ylabel("Water Level")
plt.grid(True, alpha=0.3)

# 展示图表
st.pyplot(fig)
