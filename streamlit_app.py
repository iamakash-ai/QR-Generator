import streamlit as st
import streamlit as st
from app import generate_qr
from PIL import Image
import io, base64

st.set_page_config(page_title="QR Code Generator", layout="centered")

# Initialize session state for likes
if "likes" not in st.session_state:
    st.session_state.likes = 0

st.title("QR Code Generator")

# Main inputs
url = st.text_input("Enter URL to encode", value="https://www.youtube.com/@CodeWithSky-w2m")
qr_title = st.text_input("Enter QR Title", value="CodeWithSky YouTube Channel")

# Sidebar settings (moved here)
with st.sidebar:
  st.header("Settings")
  box_size = st.slider("Box size", 4, 40, 10)
  border = st.slider("Border", 1, 10, 4)
  fill_color = st.color_picker("QR color", "#000000")
  file_name = "qrcode.png"

# Apply single app background color (no helper functions)
st.markdown(f"""
<style>
.stApp {{
  background-color:  #80bfff;
}}
</style>
""", unsafe_allow_html=True)

if st.button("Generate QR"):
  if not url or not url.strip():
    st.error("Please enter a valid URL.")
  else:
    # Generate QR as PIL image (in-memory)
    qr_img = generate_qr(url.strip(), version=1, box_size=box_size, border=border, fill_color=fill_color, save=False)

    # Convert image to base64 and display centered (no functions)
    buf = io.BytesIO()
    qr_img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()
    html = f"""
    <div style="display:flex;justify-content:center">
      <div style="text-align:center">
      <img src="data:image/png;base64,{b64}" style="max-width:60%;height:auto;border:1px solid rgba(0,0,0,0.12);padding:8px;background:white" />
      <div style="font-size:14px;color:#000000;margin-top:8px">{qr_title}</div>
      </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

    # Provide download
    buf.seek(0)
    st.download_button("Download QR Code", data=buf, file_name=file_name, mime="image/png")
  
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Like button at bottom right with custom styling
st.markdown("""
<style>
.like-section {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: white;
    border-radius: 50px;
    padding: 12px 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    display: flex;
    align-items: center;
    gap: 10px;
    z-index: 999;
}
.like-text {
    font-size: 18px;
    font-weight: bold;
    color: #e74c3c;
}
</style>
""", unsafe_allow_html=True)

# Create a container for the like button at the bottom
col1, col2, col3 = st.columns([1, 1, 1])
with col3:
    st.markdown("---")
    like_col1, like_col2 = st.columns([1, 1])
    with like_col2:
        if st.button("❤️ Like"):
            st.session_state.likes += 1
            st.rerun()
        st.caption(f"Likes: {st.session_state.likes}")

footer="""<style>

a:hover,  a:active {
color: red;
background-color: transparent;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
color: white;
text-align: center;
}
</style>
<div class="footer">
  <p style="color: #000000; font-weight: bold;">Develop with <span style='color:red;'> ❤ </span> CodeWithSky </p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
# Inject CSS
