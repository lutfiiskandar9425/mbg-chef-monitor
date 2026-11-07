from PIL import Image, ImageDraw
import numpy as np
import os

img_path = r'C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/.user_uploaded/media_1793831154183_d2267df1.jpg'
im = Image.open(img_path).convert('RGBA')
w, h = im.size
print(f'Original size: {w}x{h}')

arr = np.array(im)
center_x = w / 2.0
center_y = h / 2.0

# Find radius by looking at where the checkerboard turns into the outer gold rim.
# Checkerboard is neutral gray checker: RGB values are close to each other: abs(r-g)<15 and abs(g-b)<15 and r>170
# The outer circle rim is gold/bronze: e.g. R=100..180, G=80..140, B=20..70 (saturation is noticeable, B is significantly lower than R)
print('Sample checkerboard at (20, 20):', arr[20, 20][:3])

# Let's inspect along radius from center to edge at various angles
distances = []
for deg in range(0, 360, 5):
    rad = np.radians(deg)
    # search from edge towards center
    for r in range(int(w * 0.49), int(w * 0.30), -1):
        x = int(center_x + r * np.cos(rad))
        y = int(center_y + r * np.sin(rad))
        if 0 <= x < w and 0 <= y < h:
            pix = arr[y, x][:3]
            # check if not checkerboard
            # checkerboard has (r,g,b) where max-min <= 10 and min >= 180
            diff = int(np.max(pix)) - int(np.min(pix))
            if diff > 20 or np.mean(pix) < 160: # hit the gold/dark rim!
                distances.append(r)
                break

median_radius = np.median(distances)
print(f'Detected radius: {median_radius} px')

# Let's create an anti-aliased circular crop
# Super-sample 4x for smooth anti-aliased circle edge
scale = 4
mask = Image.new('L', (w * scale, h * scale), 0)
draw = ImageDraw.Draw(mask)
r_super = (median_radius + 0.5) * scale
draw.ellipse([
    (center_x * scale - r_super, center_y * scale - r_super),
    (center_x * scale + r_super, center_y * scale + r_super)
], fill=255)
mask = mask.resize((w, h), Image.Resampling.LANCZOS)

# Apply mask as alpha
im.putalpha(mask)

# Crop to the circle bounding box with a small comfortable padding or square
crop_box = (
    int(center_x - median_radius - 2),
    int(center_y - median_radius - 2),
    int(center_x + median_radius + 2),
    int(center_y + median_radius + 2)
)
cropped = im.crop(crop_box)
print(f'Cropped size: {cropped.size}')

# Save transparent PNG master
master_png = r'C:/Users/HP/Projects/APlikasi MBG/bgn_logo_master.png'
cropped.save(master_png, 'PNG')
print(f'Saved master transparent PNG to: {master_png}')

arr_c = np.array(cropped)
print('Corner alpha values:', arr_c[0,0,3], arr_c[0,-1,3], arr_c[-1,0,3], arr_c[-1,-1,3])
print('Center pixel RGBA:', arr_c[arr_c.shape[0]//2, arr_c.shape[1]//2])


