import os
from pathlib import Path
from tkinter import Tk, Canvas, Frame, Button, PhotoImage


class ReceiptDetailsFrame(Frame):

    ASSETS_PATH = Path(r"assets/frame3")

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, window: Tk):
        super().__init__(window)
        self.image_path = ""
        self.canvas = Canvas(
            self,
            bg="#96E8CA",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            120.0,
            82.0,
            anchor="nw",
            text="Receipt Details:",
            fill="#38759F",
            font=("Inter Bold", 24 * -1)
        )

        self.canvas.create_text(
            136.0,
            156.0,
            anchor="nw",
            text="Receipt id:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            649.0,
            156.0,
            anchor="nw",
            text="Date:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            136.0,
            221.0,
            anchor="nw",
            text="Vendor/shop name:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            136.0,
            292.0,
            anchor="nw",
            text="Name on receipt:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            136.0,
            362.0,
            anchor="nw",
            text="Amount:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            136.0,
            434.0,
            anchor="nw",
            text="Image file:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.btn_open_img = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_image(),
            relief="flat"
        )
        self.btn_open_img.place(
            x=136.0,
            y=462.0,
            width=123.0,
            height=32.0
        )

        self.canvas.create_text(
            649.0,
            366.0,
            anchor="nw",
            text="Category:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )
        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.btn_close = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.btn_close.place(
            x=713.0,
            y=476.0,
            width=121.0,
            height=38.0
        )

        self.txt_rcpt_img_path = self.canvas.create_text(
            260.0,
            434.0,
            anchor="nw",
            text="image file path val",
            fill="#000000",
            font=("Inter Bold", 14 * -1)
        )

        self.txt_rcpt_num = self.canvas.create_text(
            136.0,
            187.0,
            anchor="nw",
            text="Receipt Number  val",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.txt_vendor_nm = self.canvas.create_text(
            136.0,
            256.0,
            anchor="nw",
            text="Vendor/Shop Name  val",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.txt_nm_on_rcpt = self.canvas.create_text(
            136.0,
            323.0,
            anchor="nw",
            text="Name on receipt  val",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.txt_amount = self.canvas.create_text(
            136.0,
            394.0,
            anchor="nw",
            text="Amount  val",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.txt_date = self.canvas.create_text(
            649.0,
            187.0,
            anchor="nw",
            text="Date val",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.txt_category = self.canvas.create_text(
            649.0,
            394.0,
            anchor="nw",
            text="Category val",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )
        self.canvas.pack()

    def open_image(self):
        if not (len(self.image_path.strip()) == 0 or self.image_path.strip() == "Image not available"):
            os.popen(self.image_path)



