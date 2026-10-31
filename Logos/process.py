import os
import shutil
from PIL import Image

def process_image(input_path, output_path, format_str="WEBP"):
    print(f"Processando {os.path.basename(input_path)} para {format_str}...")
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()
    
    new_data = []
    for item in datas:
        r, g, b, a = item
        # Calcular brilho medio
        brightness = (r + g + b) / 3.0
        
        # Verificar se e muito proximo do branco
        if r > 220 and g > 220 and b > 220:
            # Verificar se e uma sombra cinza neutra (valores R, G, B proximos entre si)
            diff_rg = abs(r - g)
            diff_gb = abs(g - b)
            diff_rb = abs(r - b)
            
            if diff_rg < 10 and diff_gb < 10 and diff_rb < 10:
                # E uma sombra neutra
                # Mapeamos o alpha baseado no brilho: quanto mais proximo do branco, mais transparente
                if brightness >= 253:
                    alpha = 0
                else:
                    # Suave transicao de alpha
                    alpha = int(255 * (1.0 - (brightness - 220) / (255.0 - 220.0)))
                    alpha = max(0, min(255, alpha))
                # Sombra projetada: usa cor preta/cinza escuro com o alpha correspondente
                new_data.append((30, 30, 30, alpha))
            else:
                # E um detalhe colorido da logo que e bem claro
                if brightness >= 253:
                    alpha = 0
                else:
                    # Suave transicao de alpha
                    alpha = int(255 * (1.0 - (brightness - 240) / (255.0 - 240.0)))
                    alpha = max(0, min(255, alpha))
                new_data.append((r, g, b, alpha))
        else:
            # Mantem pixel original totalmente opaco
            new_data.append((r, g, b, 255))
            
    img.putdata(new_data)
    if format_str == "WEBP":
        img.save(output_path, "WEBP", quality=90)
    else:
        img.save(output_path, "PNG")
    print(f"Salvo em {output_path}")

def generate_favicons(icon_path, public_dir):
    print("Processando e redimensionando favicons...")
    img = Image.open(icon_path).convert("RGBA")
    
    # Gerar favicon.png (32x32 pixels, super leve)
    favicon_png_path = os.path.join(public_dir, "favicon.png")
    img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    img_32.save(favicon_png_path, "PNG")
    print(f"Favicon PNG 32x32 salvo: {favicon_png_path}")
    
    # Gerar favicon.ico (multi-tamanhos: 16x16, 32x32, 48x48)
    favicon_ico_path = os.path.join(public_dir, "favicon.ico")
    img.save(favicon_ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"Favicon ICO multi-tamanho salvo: {favicon_ico_path}")
    
    # Gerar favicon.webp (32x32)
    favicon_webp_path = os.path.join(public_dir, "favicon.webp")
    img_32.save(favicon_webp_path, "WEBP", quality=90)
    print(f"Favicon WebP 32x32 salvo: {favicon_webp_path}")

def main():
    logos_dir = r"d:\Projetos\SRTecnoCIA\AI-MaximusPericias\Logos"
    public_dir = r"d:\Projetos\SRTecnoCIA\AI-MaximusPericias\apps\web\public"
    
    # Garantir que a pasta public exista
    os.makedirs(public_dir, exist_ok=True)
    
    # Inputs
    icon_in = os.path.join(logos_dir, "ChatGPT Image 19 de jul. de 2026, 10_17_54.png")
    vertical_in = os.path.join(logos_dir, "ChatGPT Image 19 de jul. de 2026, 10_18_25.png")
    horizontal_in = os.path.join(logos_dir, "ChatGPT Image 19 de jul. de 2026, 10_19_08.png")
    
    # Outputs WebP
    icon_webp = os.path.join(public_dir, "logo-icon.webp")
    vertical_webp = os.path.join(public_dir, "logo-vertical.webp")
    horizontal_webp = os.path.join(public_dir, "logo-horizontal.webp")
    
    # Outputs PNG (para fallback)
    icon_png = os.path.join(public_dir, "logo-icon.png")
    vertical_png = os.path.join(public_dir, "logo-vertical.png")
    horizontal_png = os.path.join(public_dir, "logo-horizontal.png")
    
    # Processar imagens de logo
    process_image(icon_in, icon_webp, "WEBP")
    process_image(icon_in, icon_png, "PNG")
    
    process_image(vertical_in, vertical_webp, "WEBP")
    process_image(vertical_in, vertical_png, "PNG")
    
    process_image(horizontal_in, horizontal_webp, "WEBP")
    process_image(horizontal_in, horizontal_png, "PNG")
    
    # Gerar os favicons leves redimensionados
    generate_favicons(icon_png, public_dir)

if __name__ == "__main__":
    main()
