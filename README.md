# QR Code Generator

A simple and intuitive QR code generator built with Python. Generate QR codes from URLs and customize them with different box sizes, borders, and colors.

## Features

- ✨ Generate QR codes from any text/URL
- 🎨 Customize QR code appearance (size, border, colors)
- 🌐 Web-based interface using Streamlit
- 📥 Download generated QR codes as PNG images
- ⚡ Fast and lightweight

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. Clone or download this repository:
```bash
cd qr_generator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Application (Recommended)

Run the Streamlit web interface:
```bash
streamlit run streamlit_app.py
```

This will open a local web server (usually at `http://localhost:8501`) where you can:
- Enter a URL to encode
- Add a title for your QR code
- Customize box size and border width
- Choose QR code and background colors
- Generate and display the QR code

### Command Line

Use the `app.py` module directly in your Python code:
```python
from app import generate_qr

# Generate and save QR code
generate_qr("https://example.com", filename="my_qrcode.png")

# Generate without saving (returns PIL Image)
qr_image = generate_qr("https://example.com", save=False)
```

## Project Structure

```
qr_generator/
├── app.py              # Core QR code generation logic
├── streamlit_app.py    # Web interface
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Requirements

- **streamlit** - Web framework for the UI
- **qrcode** - QR code generation library
- **Pillow** - Image processing library

See `requirements.txt` for more details.

## Function Documentation

### `generate_qr(data, filename="qrcode.png", version=1, box_size=10, border=4, fill_color="black", back_color="white", save=True)`

Generates a QR code from the provided data.

**Parameters:**
- `data` (str): The text/URL to encode
- `filename` (str): Output filename (default: "qrcode.png")
- `version` (int): QR code version, affects size (default: 1)
- `box_size` (int): Size of each box in pixels (default: 10)
- `border` (int): Border width in boxes (default: 4)
- `fill_color` (str): QR code color in hex format (default: "black")
- `back_color` (str): Background color in hex format (default: "white")
- `save` (bool): If True, saves to file; if False, returns PIL Image (default: True)

**Returns:**
- If `save=True`: filename (str)
- If `save=False`: PIL Image object

## Example

```python
from app import generate_qr

# Create a custom QR code
qr = generate_qr(
    "https://www.youtube.com/@CodeWithSky-w2m",
    filename="channel_qr.png",
    box_size=12,
    border=5,
    fill_color="#1f77b4",
    back_color="#ffffff"
)
print(f"QR code saved as {qr}")
```

## License

This project is free to use and modify.

## Author

Created with ❤️ from CodeWithSKy
