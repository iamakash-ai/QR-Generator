import qrcode
from PIL import Image
import io


def generate_qr(data, filename="qrcode.png", version=1, box_size=10, border=4, fill_color="black", back_color="white", save=True):
    """Generate a QR code from `data`.

    If `save` is True (default) the image is saved to `filename` and the
    filename is returned. If `save` is False, a PIL `Image` object is returned.
    """
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")

    if save:
        img.save(filename)
        return filename
    else:
        return img


if __name__ == "__main__":
    data = "https://www.youtube.com/@CodeWithSky-w2m"
    out = generate_qr(data)
    print(f"QR code generated and saved as {out}")