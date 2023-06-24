import os
from PIL import Image

def thumb_maker(image_path):
    c = 0
    try:
        image = Image.open(image_path)
        # image.thumbnail((500, 500), Image.LANCZOS) 
        image.thumbnail((500, 500), Image.ANTIALIAS)  # Resize image to 500x500 (max size)

    #-------------------------------------------------------------------------------------------------------------,
                                                    # Resize image to 500x500 (max size) using LANCZOS filter     |
        #because  "DeprecationWarning: ANTIALIAS is deprecated and will be removed in Pillow 10 (2023-07-01).     |
        # Use LANCZOS or Resampling.LANCZOS instead."                                                             |       
    #-------------------------------------------------------------------------------------------------------------'
       
        image.thumbnail((500,500), Image.ANTIALIAS)  # Resize image to 500x500 (max size)
        image = image.convert("RGB")  # Convert to RGB color mode
        s = os.path.splitext(os.path.basename(image_path))[0]
        thumb_dir = "_thumb"
        os.makedirs(thumb_dir, exist_ok=True)
        thumb_path = os.path.join(thumb_dir, f"{s}_thumb.jpg")
        image.save(thumb_path)
    except  Exception as e:
        print(e)
        # try it for 3 times then pass
        if c < 3:
            thumb_maker(image_path)
            c += 1
        else:
            pass

if __name__ == "__main__":
    thumb_maker(r"D:\Lucifer-Drive\Programs\Django-programs\image_downloader\static\images\2412219.png")
