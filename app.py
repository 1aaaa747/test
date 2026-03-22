import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. 网页的标题和文字说明
st.title("🌊 验潮站海平面模拟系统")
st.write("欢迎来到我的第一个科研交互网站！你可以拖动下方的滑块来改变图表。")

# 2. 魔法交互：加一个双向滑块，让用户选择年份区间！
year_range = st.slider("请选择你想查看的年份区间", 2016, 2036, (2016, 2026))

# 3. 核心数据生成（根据滑块的值动态生成数据）
np.random.seed(42)
# year_range[0] 是起始年份，year_range[1] 是结束年份
t = np.linspace(year_range[0], year_range[1], 500)
data = 100 * np.sin(t) + 20 * np.random.normal(size=500) + (t - 2016) * 10

# 4. 绘图代码（和你在 Jupyter 里写的一模一样）
fig = plt.figure(figsize=(10, 5))
plt.plot(t, data, color='#1f77b4', linewidth=1)
plt.title(f"Tidal Station Simulation ({year_range[0]} - {year_range[1]})")
plt.xlabel("Year")
plt.ylabel("Water Level")
plt.grid(True, alpha=0.3)

# 5. 见证奇迹：把画好的图表展示在网页上！
st.pyplot(fig)