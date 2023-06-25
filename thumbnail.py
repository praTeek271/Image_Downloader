import os
from PIL import Image

def thumb_maker(image_path, ods=0):
    if ods != 1 and not image_path.startswith("images"):
        image_path = os.path.join("images", image_path)

    c = 0
    try:
        with Image.open(image_path) as image:
            image.thumbnail((500, 500), Image.ANTIALIAS)  # Resize image to 500x500 (max size)
            image = image.convert("RGB")  # Convert to RGB color mode
            s = os.path.splitext(os.path.basename(image_path))[0]
            thumb_dir = "static/_thumb"
            os.makedirs(thumb_dir, exist_ok=True)
            thumb_path = os.path.join(thumb_dir, f"{s}_thumb.jpg")
            image.save(thumb_path)

    except Exception or Warning as e:
        # print("ERROR :: -->", e, "<-- ::")
        # try it for 3 times then pass
        if c < 3:
            thumb_maker(image_path, ods)
            c += 1
        else:
            pass
    return thumb_path

if __name__ == "__main__":
    print(thumb_maker(r"D:\Lucifer-Drive\Programs\Django-programs\image_downloader\static\images\2412219.png", 1))
