# basic_qrcode.py

import segno
from pathlib import Path

def generate_qr_code_txt(
        data: str = "Hello, World",
        filename: str = "hello_world_qr.png",
        scale: int = 1, border: int = 4,
        light: str = "white", dark: str = "black",
        quiet_zone: str = "white", data_dark: str = ""
    ) -> None:
    # default 5x5 pixels in size
    qr_code = segno.make_qr(data)
    if data_dark:
        qr_code.save(filename,
                     scale=scale,
                     border=border,
                     light=light,
                     dark=dark,
                     quiet_zone=quiet_zone,
                     data_dark=data_dark)
    else:
        qr_code.save(filename,
                     scale=scale,
                     border=border,
                     light=light,
                     dark=dark,
                     quiet_zone=quiet_zone)
    
def generate_GIF_qr_code(
        gif_loc: str,
        data: str = "Hello, World",
        filename: str = "hello_world_qr.png",
        scale: int = 1, border: int = 4,
        light: str = "white", dark: str = "black",
        quiet_zone: str = "white", data_dark: str = "",
        ) -> None:
    """
    Takes in a segno QR code and generates a GIF version of it.
    """
    qr_code = segno.make(data, error="h")
    qr_code.to_artistic(background=gif_loc,
                        target=filename,
                        scale=scale,
                        border=border,
                        light=light,
                        dark=dark,
                        quiet_zone=quiet_zone)

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    gif_path_1 = project_root / "IMGs" / "PyTexas_QR_Code_IMG_4.gif"
    gif_path_0 = project_root / "IMGs" / "PyTexas_QR_Code_IMG_5.gif"

    generate_qr_code_txt(scale=5, border=1, light="black", dark="hotpink",
                         data="https://pytexas.org/2026")

    generate_GIF_qr_code(scale=10, border=1, light="black", filename="contest-1.gif",
                         data="https://canva.link/PyTexas2026-TalkGame",
                         gif_loc=str(gif_path_1))

    generate_GIF_qr_code(scale=10, border=1, light="black", filename="deck-1.gif",
                         data="https://github.com/ProsperousHeart/mkdocs-jupyterlite-template-repo",
                         gif_loc=str(gif_path_0))

    generate_GIF_qr_code(scale=10, border=0, light="black", filename="contest-0.gif",
                         data="https://canva.link/PyTexas2026-TalkGame",
                         gif_loc=str(gif_path_0))

    generate_GIF_qr_code(scale=10, border=0, light="black", filename="deck-0.gif",
                         data="https://github.com/ProsperousHeart/mkdocs-jupyterlite-template-repo",
                         gif_loc=str(gif_path_0))

    generate_GIF_qr_code(scale=10, border=1, light="black", filename="form-1.gif",
                         data="https://forms.gle/xMbzVjo4iPQGf1QT8",
                         gif_loc=str(gif_path_1))

    generate_GIF_qr_code(scale=10, border=0, light="black", filename="form-0.gif",
                         data="https://forms.gle/xMbzVjo4iPQGf1QT8",
                         gif_loc=str(gif_path_0))
    
    generate_GIF_qr_code(scale=10, border=0, light="black", filename="repo-site-0.gif",
                         data="https://resume.prosperousheart.com/mkdocs-jupyterlite-template-repo/",
                         gif_loc=str(gif_path_0))