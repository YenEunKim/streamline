import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(page_title="Ye Eun Kim", layout="wide")

# ----------------- 상태 관리 -----------------
if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to(page):
    st.session_state.page = page

# ----------------- MAIN PAGE -----------------
if st.session_state.page == "main":
    st.markdown("<h2 style='text-align: center;'>Ye Eun.</h2><hr>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    for i, (col, label, img_path, page_name) in enumerate(zip(
        [col1, col2, col3, col4],
        ["Photography", "Video", "Typography", "Branding"],
        ["data/1.png", "data/2.png", "data/3.png", "data/4.png"],
        ["photo1", "photo2", "photo3", "photo4"]
    )):
        with col:
            st.image(img_path, use_container_width=True)

            # 버튼 중앙 정렬 + 작게
            button_clicked = st.markdown(f"""
                <div style='text-align:center; margin-top: 10px;'>
                    <form action="" method="post">
                        <button type="submit" name="page" value="{page_name}" style="
                            background-color: #333;
                            color: white;
                            padding: 5px 12px;
                            font-size: 11px;
                            border: none;
                            border-radius: 8px;
                            cursor: pointer;">
                            {label}
                        </button>
                    </form>
                </div>
            """, unsafe_allow_html=True)

    # 세션 변경 감지
    if "page" in st.experimental_get_query_params():
        go_to(st.experimental_get_query_params()["page"][0])

    st.markdown("<hr>", unsafe_allow_html=True)

    # ----------------- 소개 -----------------
    st.markdown("""
        <h2 style='text-align: center;'>Ye Eun Kim.</h2>
        <p style='text-align: center;'>
        Yeeun Kim is a designer based in Seoul, Korea. Interested in photography, video, typography, and branding.<br>
        Majoring visual communication design at Hongik University.
        </p>
    """, unsafe_allow_html=True)

    # ----------------- SKILL -----------------
    st.markdown("<h2 style='text-align: center;'>SKILL</h2>", unsafe_allow_html=True)

    skills = {
        "Adobe Photoshop": 90,
        "Adobe Illustration": 95,
        "Adobe After Effect": 30,
        "Adobe Premiere Pro": 60,
        "Adobe Indesign": 70,
        "Figma": 90
    }

    df = pd.DataFrame({
        "Tool": list(skills.keys()),
        "Skill": list(skills.values())
    })

    chart = alt.Chart(df).mark_bar(size=30).encode(
        x=alt.X("Tool", sort=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y("Skill", scale=alt.Scale(domain=[0, 100])),
        color=alt.value("black")
    ).properties(width=700, height=300)

    st.altair_chart(chart, use_container_width=True)

    # ----------------- Contact -----------------
    st.markdown("""
        <br><br>
        <h3 style='text-align: center;'>Contact.</h3>
        <p style='text-align: center;'>anna08060@gmail.com<br>instagram @yenni__s2</p>
    """, unsafe_allow_html=True)

# ----------------- 상세 페이지들 -----------------
elif st.session_state.page == "photo1":
    st.markdown("## Ye Eun.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/1-1.png", use_container_width=True)
    with col2:
        st.image("data/1-2.png", use_container_width=True)
    col3, col4 = st.columns(2)
    with col3:
        st.image("data/1-3.png", use_container_width=True)
    with col4:
        st.image("data/1-4.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram @yenni__s2")

    if st.button("Back"):
        go_to("main")

elif st.session_state.page == "photo2":
    st.markdown("## Ye Eun.")
    try:
        with open("data/video.mp4", "rb") as f:
            st.video(f.read())
    except:
        st.warning("비디오 파일이 없습니다.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("data/2-1.png", use_container_width=True)
    with col2:
        st.image("data/2-2.png", use_container_width=True)
    col3, col4 = st.columns(2)
    with col3:
        st.image("data/2-3.png", use_container_width=True)
    with col4:
        st.image("data/2-4.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram @yenni__s2")

    if st.button("Back"):
        go_to("main")

elif st.session_state.page == "photo3":
    st.markdown("## Ye Eun.")
    st.image("data/3-1.png", use_container_width=True)
    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram @yenni__s2")
    if st.button("Back"):
        go_to("main")

elif st.session_state.page == "photo4":
    st.markdown("## Ye Eun.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/4-1.png", use_container_width=True)
    with col2:
        st.image("data/4-2.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram @yenni__s2")

    if st.button("Back"):
        go_to("main")
