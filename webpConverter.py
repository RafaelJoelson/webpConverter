from PIL import Image
import os

def convert_images_to_webp(input_folder, output_folder):
    # Verifica se a pasta de saída existe, se não, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Percorre todas as imagens na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):  # Verifica os formatos suportados
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Remove a extensão do arquivo original e adiciona o prefixo "converted_"
            output_file = "converted_" + os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_folder, output_file)
            
            # Salva a imagem no formato WebP
            img.save(output_path, "WEBP")
            print(f"Imagem {filename} convertida para {output_file}")

# Exemplo de uso:
input_folder = "./"  # Pasta de entrada com as imagens originais
output_folder = "./converted"   # Pasta onde serão salvas as imagens convertidas

convert_images_to_webp(input_folder, output_folder)