from PIL import Image
import os

master_path = r'C:/Users/HP/Projects/APlikasi MBG/bgn_logo_master.png'
im = Image.open(master_path).convert('RGBA')

# Target densities for Android
res_dir = r'C:/Users/HP/Projects/APlikasi MBG/mbg_chef_monitor/android/app/src/main/res'
densities = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192,
}

for folder, size in densities.items():
    folder_path = os.path.join(res_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    out_file = os.path.join(folder_path, 'ic_launcher.png')
    resized = im.resize((size, size), Image.Resampling.LANCZOS)
    resized.save(out_file, 'PNG')
    print(f'Generated {folder}/ic_launcher.png ({size}x{size})')

# In-app assets
assets_dir = r'C:/Users/HP/Projects/APlikasi MBG/mbg_chef_monitor/assets/images'
os.makedirs(assets_dir, exist_ok=True)
asset_logo = os.path.join(assets_dir, 'bgn_logo.png')
im.resize((512, 512), Image.Resampling.LANCZOS).save(asset_logo, 'PNG')
print(f'Saved in-app asset logo: {asset_logo}')

# Also save a 512x512 master in project root
root_logo = r'C:/Users/HP/Projects/APlikasi MBG/logo_bgn_512.png'
im.resize((512, 512), Image.Resampling.LANCZOS).save(root_logo, 'PNG')
print(f'Saved root master 512x512 logo: {root_logo}')

