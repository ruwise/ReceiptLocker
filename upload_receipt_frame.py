from datetime import date
from pathlib import Path
from tkinter import Tk, Frame, Canvas, Button, Entry, PhotoImage, OptionMenu, StringVar, filedialog
from tkcalendar import DateEntry


class UploadReceiptFrame(Frame):

    ASSETS_PATH = Path(r"assets/frame1")
    OPTIONS = [
        "Electricity",
        "Fees",
        "Fuel",
        "Grocery",
        "Pets",
        "Medical",
        "Telephone/Internet",
        "Vehicle related",
        "Water",
        "Others"
    ]

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, window: Tk):
        super().__init__(window)
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
        self.btn_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.home_btn = Button(
            self,
            image=self.btn_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.home_btn.place(
            x=43.0,
            y=39.0,
            width=143.0,
            height=48.0
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
            x=207.0,
            y=39.0,
            width=171.0,
            height=48.0
        )

        self.canvas.create_text(
            122.0,
            126.0,
            anchor="nw",
            text="Upload Receipt",
            fill="#38759F",
            font=("Inter Bold", 24 * -1)
        )

        self.canvas.create_text(
            138.0,
            200.0,
            anchor="nw",
            text="Receipt id:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(
            331.5,
            241.0,
            image=self.entry_image_1
        )
        self.entry_rcpt_id = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_rcpt_id.place(
            x=138.0,
            y=225.0,
            width=387.0,
            height=30.0
        )

        self.canvas.create_text(
            651.0,
            200.0,
            anchor="nw",
            text="Date:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(
            743.5,
            241.0,
            image=self.entry_image_2
        )
        today = date.today()
        self.entry_date = DateEntry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            maxdate=today,
            date_pattern="dd-mm-yyyy"
        )
        self.entry_date.place(
            x=651.0,
            y=225.0,
            width=185.0,
            height=30.0
        )

        self.canvas.create_text(
            138.0,
            265.0,
            anchor="nw",
            text="Vendor/shop name:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.canvas.create_image(
            487.0,
            306.0,
            image=self.entry_image_3
        )
        self.entry_vendor_nm = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_vendor_nm.place(
            x=138.0,
            y=290.0,
            width=698.0,
            height=30.0
        )

        self.canvas.create_text(
            138.0,
            336.0,
            anchor="nw",
            text="Name on receipt:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.canvas.create_image(
            487.0,
            377.0,
            image=self.entry_image_4
        )
        self.entry_nm_on_rcpt = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_nm_on_rcpt.place(
            x=138.0,
            y=361.0,
            width=698.0,
            height=30.0
        )

        self.canvas.create_text(
            138.0,
            406.0,
            anchor="nw",
            text="Amount:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.canvas.create_image(
            331.5000037252894,
            451.0000009536742,
            image=self.entry_image_5
        )
        self.entry_amount = Entry(
            self,

            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_amount.place(
            x=138.0,
            y=435.0,
            width=387.0000074505788,
            height=30.000001907348405
        )

        self.canvas.create_text(
            138.0,
            478.0,
            anchor="nw",
            text="Imgae file:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.btn_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.image_path = "Image not available"
        self.btn_upload_img = Button(
            self,
            image=self.btn_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.image_uploader,
            relief="flat"
        )
        self.btn_upload_img.place(
            x=138.0,
            y=507.0,
            width=173.0,
            height=32.0
        )
        self.txt_img_path = self.canvas.create_text(
            262.0,
            478.0,
            anchor="nw",
            text=self.image_path,
            fill="#000000",
            font=("Inter", 14)
        )
        self.canvas.create_text(
            651.0,
            410.0,
            anchor="nw",
            text="Category:",
            fill="#000000",
            font=("Inter", -16)
        )

        self.selected_category = StringVar(self)
        self.selected_category.set("Select category")
        self.entry_category = OptionMenu(
            self,
            self.selected_category,
            *self.OPTIONS
        )
        self.entry_category.configure(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0)
        self.entry_category.place(
            x=651.0,
            y=435.0,
            width=185.0,
            height=30.0
        )

        self.btn_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.btn_reset = Button(
            self,
            image=self.btn_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.reset_values(),
            relief="flat"
        )
        self.btn_reset.place(
            x=572.0,
            y=520.0,
            width=121.0,
            height=38.0
        )

        self.btn_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.btn_save = Button(
            self,
            image=self.btn_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.btn_save.place(
            x=715.0,
            y=520.0,
            width=121.0,
            height=38.0
        )
        self.canvas.pack()

    def reset_values(self):
        self.entry_rcpt_id.delete(0, "end")
        today = date.today()
        self.entry_date.set_date(today)
        self.entry_vendor_nm.delete(0, "end")
        self.entry_nm_on_rcpt.delete(0, "end")
        self.entry_amount.delete(0, "end")
        self.selected_category.set("Select Category")
        self.image_path = "Image not available"
        self.canvas.itemconfig(self.txt_img_path, text=self.image_path)

    def image_uploader(self):
        file_types = [("Image files", "*.png;*.jpg;*.jpeg")]
        self.image_path = filedialog.askopenfilename(filetypes=file_types)
        if len(self.image_path) > 0:
            self.canvas.itemconfig(self.txt_img_path, text=self.image_path)
