import streamlit as st
from PIL import Image
import io

# --- Page Config ---
st.set_page_config(page_title="Image Compressor", page_icon="🖼️", layout="centered")


# --- CSS Styling ---
css = """
<style>
body, .main { background: linear-gradient(135deg, #ffffff, #e3f2fd); color: #000000; }
.stButton>button { background: #2196f3; color: white; border-radius: 10px; padding: 0.6rem 1.2rem; font-size: 16px; transition: all 0.3s ease; }
.stButton>button:hover { background: #64b5f6; }
.block-container { padding-top: 2rem; }
.header, .footer {visibility: hidden;}
.container-card {background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); padding: 2rem; border-radius: 20px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); max-width: 800px; margin: auto;}
h1, h2, h3 {text-align: center; font-family: 'Poppins', sans-serif;}
img {border-radius: 12px; margin-top: 1rem;}
</style>
"""

st.markdown(css, unsafe_allow_html=True)


st.markdown('<div class="container-card">', unsafe_allow_html=True)

st.markdown("""
<h1>🖼️ Image Compression App</h1>
<h3>Effortlessly reduce image size without losing quality</h3>
<hr style='border: 0.5px solid #555;'>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    with st.spinner('Processing Image...'):
        image = Image.open(uploaded_file)

        st.subheader("Original Image Preview")
        st.image(image, use_column_width=True)

        st.subheader("Compression Settings")
        quality = st.slider("Select Compression Quality", 10, 95, 70)

        if image.mode == "RGBA":
            image = image.convert("RGB")

        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=quality)
        compressed_data = buffer.getvalue()

        compressed_image = Image.open(io.BytesIO(compressed_data))

        st.success(f"\u2705 Image compressed to ~{round(len(compressed_data)/1024, 2)} KB")

        st.subheader("Compressed Image Preview")
        st.image(compressed_image, use_column_width=True)

        # Add this line for the download button
        compressed_image_bytes = io.BytesIO(compressed_data)

        st.download_button(
            label="Download Compressed Image",
            data=compressed_image_bytes,
            file_name="compressed_image.jpg",
            mime="image/jpeg",
        )

st.markdown('</div>', unsafe_allow_html=True)
