import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("데이터 시각화 웹앱 (Plotly + Streamlit)")

# 데이터 불러오기
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(url)

# 데이터 확인
st.subheader("데이터 미리보기")
st.write(df.head())

# 컬럼 선택
x_col = st.selectbox("X축 컬럼 선택", df.columns)
y_col = st.selectbox("Y축 컬럼 선택", df.columns)

# Plotly 시각화
fig = px.line(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
st.plotly_chart(fig)
