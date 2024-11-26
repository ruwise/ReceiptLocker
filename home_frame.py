from pathlib import Path
from tkinter import Tk, Frame, Canvas, PhotoImage, Button


class HomeFrame(Frame):
    ASSETS_PATH = Path(r"assets/frame0")

    def __init__(self, window: Tk):
        super().__init__(window)
        self.canvas = Canvas(
            self,
            bg="#90E7C8",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(
            267.0,
            300.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            542.0,
            118.0,
            anchor="nw",
            text="Receipt Locker",
            fill="#38759F",
            font=("Inter BlackItalic", 48 * -1)
        )
        self.canvas.pack()
        self.btn_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.upload_btn = Button(
            self,
            image=self.btn_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.upload_btn.place(
            x=623.0,
            y=306.0,
            width=203.0,
            height=53.0
        )

        self.btn_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.view_all_btn = Button(
            self,
            image=self.btn_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.view_all_btn.place(
            x=623.0,
            y=398.0,
            width=203.0,
            height=52.0
        )

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)



