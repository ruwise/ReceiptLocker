from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, StringVar, OptionMenu, Label, messagebox
from receipt_details_frame import ReceiptDetailsFrame
from datetime import datetime
import json
import os
from idlelib.tooltip import Hovertip


class ViewAllFrame(Frame):

    ASSETS_PATH = Path(r"assets/frame2")
    OPTIONS = [
        "Show All",
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
    JSON_FILE_PATH = "receipt_details/receipts.json"

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, window: Tk):
        super().__init__(window)
        self.canvas = Canvas(
            self,
            bg="#96E8CA",
            height=400,
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
        self.upload_btn = Button(
            self,
            image=self.btn_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.upload_btn.place(
            x=208.0,
            y=39.0,
            width=171.0,
            height=48.0
        )

        self.canvas.create_text(
            54.0,
            115.0,
            anchor="nw",
            text="Saved Receipts",
            fill="#38759F",
            font=("Inter Bold", 24 * -1)
        )

        self.canvas.create_text(
            65.0,
            173.0,
            anchor="nw",
            text="Category:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.selected_category = StringVar(self)
        self.selected_category.set("Show All")
        self.receipts = []
        self.filtered_receipts = []
        self.detail_frame: ReceiptDetailsFrame | None = None
        self.entry_category = OptionMenu(
            self,
            self.selected_category,
            *self.OPTIONS,
            command=self.filter_receipts
        )
        self.entry_category.configure(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0)
        self.entry_category.place(
            x=65.0,
            y=198.0,
            width=185.0,
            height=30.0
        )
        self.receipt_id_order = False
        self.btn_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.header_btn_rcpt_id = Button(
            self,
            image=self.btn_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sort_receipts("receipt_id"),
            relief="flat"
        )
        self.header_btn_rcpt_id.place(
            x=63.0,
            y=248.0,
            width=120.0,
            height=31.0
        )
        self.nm_on_rcpt_order = False
        self.btn_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.header_btn_nm_on_rcpt = Button(
            self,
            image=self.btn_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sort_receipts("nm_on_rcpt"),
            relief="flat"
        )
        self.header_btn_nm_on_rcpt.place(
            x=182.0,
            y=248.0,
            width=207.0,
            height=31.0
        )
        self.vendor_nm_order = False
        self.btn_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.header_btn_vendor_nm = Button(
            self,
            image=self.btn_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sort_receipts("vendor_nm"),
            relief="flat"
        )
        self.header_btn_vendor_nm.place(
            x=388.0,
            y=248.0,
            width=255.88743591308594,
            height=31.0
        )
        self.date_order = False
        self.btn_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.header_btn_date = Button(
            self,
            image=self.btn_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sort_receipts("date"),
            relief="flat"
        )
        self.header_btn_date.place(
            x=643.0,
            y=248.0,
            width=120.0,
            height=31.0
        )
        self.amount_order = False
        self.btn_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.header_btn_amount = Button(
            self,
            image=self.btn_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sort_receipts("amount"),
            relief="flat"
        )
        self.header_btn_amount.place(
            x=762.0,
            y=248.0,
            width=120.0,
            height=31.0
        )
        self.receipt_rows = []
        self.receipt_buttons = []
        self.delete_buttons = []
        self.total_val = ""
        self.total_txt = ""
        self.canvas.pack()

    def filter_receipts(self, *args):
        category = args[0]
        if category == "Show All":
            self.filtered_receipts = self.receipts
        elif self.receipts is not None and len(self.receipts) > 0:
            temp = []
            for receipt in self.receipts:
                if receipt.category == category:
                    temp.append(receipt)
            self.filtered_receipts = temp[:]
        self.load_details()

    def load_details(self):
        y_value = 290.0
        if len(self.receipt_buttons) > 0:
            for button in self.receipt_buttons:
                button.destroy()
        if len(self.delete_buttons) > 0:
            for button in self.delete_buttons:
                button.destroy()
        if len(self.receipt_rows) > 0:
            for row in self.receipt_rows:
                self.canvas.delete(row)
        self.canvas.delete(self.total_txt)
        self.canvas.delete(self.total_val)
        self.receipt_buttons = []
        self.delete_buttons = []
        self.receipt_rows = []

        print(f"total items: {len(self.filtered_receipts)}")
        size = 400
        total = 0
        for receipt in self.filtered_receipts:
            total += float(receipt.amount)
            self.receipt_rows.append(self.canvas.create_text(
                63.0,
                y_value,
                anchor="nw",
                text=receipt.receipt_no,
                fill="#000000",
                font=("Inter", 16 * -1)
            ))

            self.receipt_rows.append(self.canvas.create_text(
                186.0,
                y_value,
                anchor="nw",
                text=receipt.user_name,
                fill="#000000",
                font=("Inter", 16 * -1)
            ))

            self.receipt_rows.append(self.canvas.create_text(
                391.0,
                y_value,
                anchor="nw",
                text=receipt.vendor_nm,
                fill="#000000",
                font=("Inter", 16 * -1)
            ))

            self.receipt_rows.append(self.canvas.create_text(
                644.0,
                y_value,
                anchor="nw",
                text=receipt.date,
                fill="#000000",
                font=("Inter", 16 * -1)
            ))

            self.receipt_rows.append(self.canvas.create_text(
                762.0,
                y_value,
                anchor="nw",
                text=f"${receipt.amount}",
                fill="#000000",
                font=("Inter", 16 * -1)
            ))
            btn_image_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
            label = Label(image=btn_image_8)
            label.image = btn_image_8  # keep a reference!
            btn_open_rcpt = Button(
                self,
                image=btn_image_8,
                borderwidth=0,
                highlightthickness=0,
                command=lambda receipt=receipt: self.show_details_frame(receipt),
                relief="flat"
            )
            btn_open_rcpt.place(
                x=884.0,
                y=y_value,
                width=30.0,
                height=27.0
            )
            open_dtl_tip = Hovertip(btn_open_rcpt, "Show details.")
            btn_image_9 = PhotoImage(file=self.relative_to_assets("button_9.png"))
            label_1 = Label(image=btn_image_9)
            label_1.image = btn_image_9  # keep a reference!
            btn_delete_rcpt = Button(
                self,
                image=btn_image_9,
                borderwidth=0,
                highlightthickness=0,
                command=lambda receipt=receipt: self.delete_receipt(receipt),
                relief="flat"
            )
            btn_delete_rcpt.place(
                x=924.0,
                y=y_value,
                width=30.0,
                height=27.0
            )
            open_dtl_tip = Hovertip(btn_delete_rcpt, "Delete receipt.")
            self.receipt_buttons.append(btn_open_rcpt)
            self.delete_buttons.append(btn_delete_rcpt)
            y_value += 40
            size += 40
            self.canvas.configure(height=size+40)
        self.total_txt = self.canvas.create_text(
            644.0,
            y_value,
            anchor="nw",
            text="Total:",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )
        self.total_val = self.canvas.create_text(
            762.0,
            y_value,
            anchor="nw",
            text=f"${total}",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )
        self.pack()
        # self.tkraise()

    def show_details_frame(self, receipt):
        print(receipt.r_id)
        self.forget()
        self.detail_frame.canvas.itemconfig(self.detail_frame.txt_rcpt_num, text=receipt.receipt_no)
        self.detail_frame.canvas.itemconfig(self.detail_frame.txt_date, text=receipt.date)
        self.detail_frame.canvas.itemconfig(self.detail_frame.txt_vendor_nm, text=receipt.vendor_nm)
        self.detail_frame.canvas.itemconfig(self.detail_frame.txt_nm_on_rcpt, text=receipt.user_name)
        self.detail_frame.canvas.itemconfig(self.detail_frame.txt_amount, text=receipt.amount)
        self.detail_frame.canvas.itemconfig(self.detail_frame.txt_category, text=receipt.category)
        self.detail_frame.canvas.itemconfig(self.detail_frame.txt_rcpt_img_path, text=receipt.image_path)
        self.detail_frame.image_path = receipt.image_path
        self.detail_frame.pack()
        self.detail_frame.tkraise()

    def delete_receipt(self, receipt):
        print(f"Deleting receipt {receipt.r_id}")
        answer = messagebox.askokcancel(
            title="Confirmation",
            message="Deleting selected receipt permanently, You won't be able to undo it!",
            icon=messagebox.WARNING)
        if not answer:
            return
        if answer:
            messagebox.showinfo(
                title="Deletion Status",
                message="The data is deleted successfully.")

        i = self.receipts.index(receipt)
        j = self.filtered_receipts.index(receipt)
        print(i , j)
        self.receipts.pop(i)
        self.filtered_receipts.pop(j)

        with open(self.JSON_FILE_PATH, 'r') as file:
            data = json.load(file)
        if receipt.r_id in data:
            removed_value = data.pop(receipt.r_id)
            print(removed_value)
        with open(file=self.JSON_FILE_PATH, mode="w") as file:
            json.dump(data, file, indent=4)
        if not receipt.image_path == "Image not available":
            os.remove(receipt.image_path)
        self.load_details()

    def sort_receipts(self, column: str):
        if column == "receipt_id":
            self.filtered_receipts.sort(key=lambda rec: rec.receipt_no, reverse=self.receipt_id_order)
            if self.receipt_id_order:
                self.receipt_id_order = False
            else:
                self.receipt_id_order = True
        elif column == "nm_on_rcpt":
            self.filtered_receipts.sort(key=lambda rec: rec.user_name, reverse=self.nm_on_rcpt_order)
            if self.nm_on_rcpt_order:
                self.nm_on_rcpt_order = False
            else:
                self.nm_on_rcpt_order = True
        elif column == "vendor_nm":
            self.filtered_receipts.sort(key=lambda rec: rec.vendor_nm, reverse=self.vendor_nm_order)
            if self.vendor_nm_order:
                self.vendor_nm_order = False
            else:
                self.vendor_nm_order = True
        elif column == "date":
            self.filtered_receipts.sort(key=lambda rec: datetime.strptime(rec.date, "%d-%m-%Y"), reverse=self.date_order)
            if self.date_order:
                self.date_order = False
            else:
                self.date_order = True
        elif column == "amount":
            self.filtered_receipts.sort(key=lambda rec: rec.amount, reverse=self.amount_order)
            if self.amount_order:
                self.amount_order = False
            else:
                self.amount_order = True
        else:
            pass
        self.load_details()


