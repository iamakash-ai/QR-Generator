import streamlit as st
import streamlit as st
from app import generate_qr
from PIL import Image
import io, base64

st.set_page_config(page_title="QR Code Generator", layout="centered")

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

# Inject CSS
st.markdown(page_bg_img, unsafe_allow_html=True)