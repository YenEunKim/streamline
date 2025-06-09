import streamlit as st

st.set_page_config(page_title="Ye Eun Kim", layout="wide")

# 페이지 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to(page_name):
    st.session_state.page = page_name

# 메인 페이지
if st.session_state.page == "main":
    st.markdown("<div style='text-align:center; font-size: 24px; font-weight: bold;'>Ye Eun.</div><hr>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    # 한 줄로 반복문 처리
    for i, (col, label, img_path, target) in enumerate(zip(
        [col1, col2, col3, col4],
        ["Photography", "Video", "Typography", "Branding"],
        ["data/1.png", "data/2.png", "data/3.png", "data/4.png"],
        ["photo1", "photo2", "photo3", "photo4"]
    )):
        with col:
            # 이미지 표시
            st.image(img_path, use_container_width=True)

            # HTML 버튼 가운데 정렬
            st.markdown(f"""
                <div style='text-align: center; margin-top: 0.5em;'>
                    <form action="" method="post">
                        <button name="btn_{i}" style="
                            background-color: #333;
                            color: white;
                            padding: 8px 18px;
                            font-size: 14px;
                            border: none;
                            border-radius: 10px;
                            cursor: pointer;">
                            {label}
                        </button>
                    </form>
                </div>
            """, unsafe_allow_html=True)

            # 버튼 클릭 처리
            if st.session_state.get(f"btn_{i}"):
                go_to(target)

    st.markdown("<hr>", unsafe_allow_html=True)

    # 자기소개
    st.markdown("""
        <h2 style='text-align: center;'>Ye Eun Kim.</h2>
        <p style='text-align: center;'>
        Yeeun Kim is a designer based in Seoul, Korea. Interested in photography, video, typography, and branding.<br>
        Majoring visual communication design at Hongik University.
        </p>
    """, unsafe_allow_html=True)

# 상세 페이지 1
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
    st.write("instagram")
    if st.button("Back", key="back1"):
        go_to("main")

# 상세 페이지 2
elif st.session_state.page == "photo2":
    st.markdown("## Ye Eun.")
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
    st.write("instagram")
    if st.button("Back", key="back2"):
        go_to("main")

# 상세 페이지 3
elif st.session_state.page == "photo3":
    st.markdown("## Ye Eun.")
    st.image("data/3-1.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram")
    if st.button("Back", key="back3"):
        go_to("main")

# 상세 페이지 4
elif st.session_state.page == "photo4":
    st.markdown("## Ye Eun.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/4-1.png", use_container_width=True)
    with col2:
        st.image("data/4-2.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram")
    if st.button("Back", key="back4"):
        go_to("main")