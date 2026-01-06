from pathlib import Path
import shutil

def gerar_nome_unico(destino: Path, nome_arquivo: str) -> Path:
    novo_caminho = destino / nome_arquivo

    if not novo_caminho.exists():
        return novo_caminho

    stem = novo_caminho.stem
    suffix = novo_caminho.suffix

    contador = 1
    while True:
        candidato = destino / f"{stem}_{contador}{suffix}"
        if not candidato.exists():
            return candidato
        contador += 1


def mover_videos_para_pictures():
    origens = [
        Path(r""),
        Path(r""),
        Path(r"")
    ]

    destino = Path(r"")

    extensoes_imagem = {
        ".mp4", ".mkv", ".avi", ".mov", ".wmv",
        ".flv", ".webm", ".mpeg", ".mpg", ".3gp",
        ".m4v", ".ts"
    }

    destino.mkdir(parents=True, exist_ok=True)

    for origem in origens:
        for arquivo in origem.rglob("*"):
            if arquivo.is_file() and arquivo.suffix.lower() in extensoes_imagem:
                try:
                    if destino not in arquivo.parents:
                        destino_final = gerar_nome_unico(destino, arquivo.name)
                        shutil.move(str(arquivo), destino_final)
                        print(f"MOVIDO: {arquivo} → {destino_final.name}")
                except Exception as e:
                    print(f"Erro ao mover {arquivo}: {e}")

def mover_whatsapp():
    origem = Path(r"C:\Users\gblgo\OneDrive")
    destino = Path(r"C:\Users\gblgo\Pictures\wpp imagens")

    # Cria a pasta WhatsApp se não existir
    destino.mkdir(exist_ok=True)

    for arquivo in origem.rglob("*"):
        if arquivo.is_file():
            try:
                # Verifica se "whatsapp" está no nome do arquivo (ignora maiúsculas)
                if "whatsapp" in arquivo.name.lower():
                    
                    # Evita mover arquivos que já estão na pasta destino
                    if destino not in arquivo.parents:
                        shutil.move(str(arquivo), destino / arquivo.name)
                        print(f"Movido: {arquivo}")

            except Exception as e:
                print(f"Erro ao mover {arquivo}: {e}")

def excluir_arquivos():
    origem = Path(r"C:\Users\gblgo\OneDrive")
    extensoes = {".txt", ".doc", ".docx", ".xlsx", ".xls", ".json", ".xml", ".lnk"}

    for arquivo in origem.rglob("*"):
        if arquivo.is_file() and arquivo.suffix.lower() in extensoes:
            try:
                arquivo.unlink()
                print(f"EXCLUÍDO: {arquivo}")
            except Exception as e:
                print(f"Erro ao excluir {arquivo}: {e}")


def mover_imagens_para_pictures():
    origens = [
        Path(r""),
        Path(r"")
    ]

    destino = Path(r"")

    extensoes_imagem = {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".tiff", ".webp", ".heic", ".heif"
    }

    destino.mkdir(parents=True, exist_ok=True)

    for origem in origens:
        for arquivo in origem.rglob("*"):
            if arquivo.is_file() and arquivo.suffix.lower() in extensoes_imagem:
                try:
                    if destino not in arquivo.parents:
                        destino_final = gerar_nome_unico(destino, arquivo.name)
                        shutil.move(str(arquivo), destino_final)
                        print(f"MOVIDO: {arquivo} → {destino_final.name}")
                except Exception as e:
                    print(f"Erro ao mover {arquivo}: {e}")

if __name__ == "__main__":
    mover_videos_para_pictures()
    mover_whatsapp()
    excluir_arquivos()
    mover_imagens_para_pictures()

