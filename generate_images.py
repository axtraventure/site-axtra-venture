import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from PIL import Image, ImageDraw
except ImportError:
    install('Pillow')
    from PIL import Image, ImageDraw

img_dir = "build/assets/img"
os.makedirs(img_dir, exist_ok=True)

def create_image(filename, size, text, bg_color="#E9E9E9", text_color="#353738"):
    img = Image.new('RGB', size, color=bg_color)
    d = ImageDraw.Draw(img)
    # just put some text
    d.text((size[0]//4, size[1]//2), text, fill=text_color)
    img.save(os.path.join(img_dir, filename))

# Favicons
create_image("favicon-32x32.png", (32, 32), "AV")
create_image("favicon-16x16.png", (16, 16), "A")
create_image("apple-touch-icon.png", (180, 180), "AV")
# Open Graph
create_image("og-image.jpg", (1200, 630), "Axtra Venture - Especialista em Google Meu Negocio")

# Placeholders
create_image("hero-bg.webp", (1920, 800), "Hero Background")
create_image("hero-bg-2.webp", (1920, 800), "Hero Background 2")
create_image("hero-bg-3.webp", (1920, 800), "Hero Background 3")
create_image("about.webp", (800, 800), "Sobre a Empresa")
create_image("benefits-bg.webp", (1920, 1080), "Beneficios Background")
create_image("benefits.webp", (800, 800), "Beneficios Imagem")
create_image("service-1.webp", (600, 400), "Posicionamento GMN")
create_image("service-2.webp", (600, 400), "Fotos 360")
create_image("service-3.webp", (600, 400), "Tour Virtual")
create_image("service-4.webp", (600, 400), "Marketing Local")
create_image("service-5.webp", (600, 400), "Serviço Adicional 1")
create_image("service-6.webp", (600, 400), "Serviço Adicional 2")
create_image("logo.png", (200, 60), "Logo Axtra")
create_image("logo-footer.png", (200, 60), "Logo Axtra")
create_image("avatar-1.webp", (100, 100), "Avatar")
create_image("avatar-2.webp", (100, 100), "Avatar")
create_image("avatar-3.webp", (100, 100), "Avatar")
create_image("cta-bg.webp", (1920, 600), "CTA Final Background")

print("Imagens criadas com sucesso.")
