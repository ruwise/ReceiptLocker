import os
import json
import shutil
from pathlib import Path
import random
import string
from tkinter import Frame, Tk, messagebox, END
from home_frame import HomeFrame
from upload_receipt_frame import UploadReceiptFrame
from view_all_frame import ViewAllFrame
from receipt_details_frame import ReceiptDetailsFrame
from receipt import Receipt
from datetime import datetime

window = Tk()
window.geometry("1000x800")
window.configure(bg="#90E7C8")
window.title("Receipt Locker")
home_frame = HomeFrame(window)
upload_frame = UploadReceiptFrame(window)
rcpt_dtls_frame = ReceiptDetailsFrame(window)
view_all_frame = ViewAllFrame(window)
receipts_ids = []
receipts = []
JSON_FILE_PATH = "receipt_details/receipts.json"


def main():
    global receipts
    load_receipts()
    home_frame.upload_btn.config(command=lambda: change_frame(home_frame, upload_frame))
    home_frame.view_all_btn.config(command=lambda: change_view_all_receipt(home_frame))

    upload_frame.home_btn.config(command=lambda: change_frame(upload_frame, home_frame))
    upload_frame.view_all_btn.config(command=lambda: change_view_all_receipt(upload_frame))
    upload_frame.btn_save.config(command=lambda: save_receipt(upload_frame))

    view_all_frame.home_btn.config(command=lambda: change_frame(view_all_frame, home_frame))
    view_all_frame.upload_btn.config(command=lambda: change_frame(view_all_frame, upload_frame))

    rcpt_dtls_frame.btn_close.config(command=lambda: change_view_all_receipt(rcpt_dtls_frame))

    home_frame.pack()
    home_frame.tkraise()

    window.resizable(True, True)
    window.mainloop()


def change_frame(current_frame: Frame, new_frame: Frame):
    current_frame.pack_forget()
    new_frame.pack()
    new_frame.tkraise()


def validate_fields(receipt_frame: UploadReceiptFrame):
    message = ""
    status = True
    if len(receipt_frame.entry_rcpt_id.get()) == 0:
        message += "Receipt Id, "
        status = False
    if len(receipt_frame.entry_vendor_nm.get()) == 0:
        message += "Vendor/Store name, "
        status = False
    if len(receipt_frame.entry_nm_on_rcpt.get()) == 0:
        message += "Name on receipt, "
        status = False
    if len(receipt_frame.entry_date.get()) == 0:
        message += "Date, "
        status = False
    if len(receipt_frame.entry_amount.get()) == 0:
        message += "Amount, "
        status = False
    if len(receipt_frame.selected_category.get()) == 0 or receipt_frame.selected_category.get() == "Select category":
        message += "Category, "
        status = False
    if not status:
        messagebox.showerror(title="Empty Field", message=f"Field/s {message} cannot be empty!")
        return False
    if not validate_date(receipt_frame.entry_date.get()):
        messagebox.showerror(title="Invalid", message="Please enter a valid date!")
        return False
    if not validate_name(receipt_frame.entry_nm_on_rcpt.get().strip()):
        messagebox.showerror(title="Invalid",
                             message="Please enter a valid name!\n (No numbers or special characters except commas and spaces are allowed.)")
        return False
    if not validate_amount(receipt_frame.entry_amount.get().strip()):
        messagebox.showerror(title="Invalid", message="Please enter a valid amount value!")
        return False
    return True


def validate_date(date: str):
    date_format = "%d-%m-%Y"
    try:
        bool(datetime.strptime(date, date_format))
    except ValueError:
        return False
    return True


def validate_amount(amount: str):
    if amount.count(".") > 1:
        return False
    if not (amount.replace(".", "")).isdecimal():
        return False
    return True


def validate_name(name: str):
    if name.replace(",", "").replace(" ", "").isalpha():
        return True
    else:
        return False


def save_receipt(frame: UploadReceiptFrame):
    global receipts, receipts_ids
    if validate_fields(frame):
        while True:
            uid = ''.join(
                random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
            if uid in receipts_ids:
                continue
            else:
                break
        receipts_ids.append(uid)
        receipt = Receipt(receipt_no=frame.entry_rcpt_id.get(), date=frame.entry_date.get(),
                          vendor_nm=frame.entry_vendor_nm.get(),
                          user_name=frame.entry_nm_on_rcpt.get(), amount=frame.entry_amount.get(),
                          category=frame.selected_category.get(),
                          image_path=frame.image_path, r_id=uid)
        if not frame.image_path == "Image not available":
            new_path = f"images{os.sep}{frame.entry_date.get()}"
            parent, file_name = os.path.split(frame.image_path)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            new_file_path = f"{new_path}{os.sep}{uid}_{file_name}"
            shutil.copy(frame.image_path, new_file_path)
            receipt.image_path = new_file_path
        receipts.append(receipt)
        try:
            if os.path.getsize(JSON_FILE_PATH) == 0:
                raise FileNotFoundError
            with open(file=JSON_FILE_PATH, mode="r") as file:
                receipt_file = json.load(file)
        except FileNotFoundError:
            with open(file=JSON_FILE_PATH, mode="w") as file:
                json.dump(receipt.to_dict(), file, indent=4)
        else:
            receipt_file.update(receipt.to_dict())
            with open(file=JSON_FILE_PATH, mode="w") as file:
                json.dump(receipt_file, file, indent=4)
        change_view_all_receipt(frame)
        reset_upload_frame(frame)
    else:
        print("Empty fields. Please try again.")


def reset_upload_frame(frame: UploadReceiptFrame):
    frame.entry_rcpt_id.delete(0, END)
    frame.entry_date.delete(0, END)
    frame.entry_date.set_date(datetime.today())
    frame.entry_vendor_nm.delete(0, END)
    frame.entry_nm_on_rcpt.delete(0, END)
    frame.entry_amount.delete(0, END)
    frame.selected_category.set("Select category")
    frame.image_path = "Image not available"
    frame.canvas.itemconfig(frame.txt_img_path, text=frame.image_path)


def load_receipts():
    global receipts, receipts_ids
    try:
        if os.path.getsize(JSON_FILE_PATH) == 0:
            return False
        with open(file=JSON_FILE_PATH, mode="r") as file:
            receipt_file = json.load(file)
    except FileNotFoundError:
        receipts_path = Path(JSON_FILE_PATH)
        receipts_path.parent.mkdir(exist_ok=True, parents=True)
        receipts_path.write_text("")
        return False
    else:
        receipts_ids = [r_id for r_id, item in receipt_file.items()]
        receipts = [Receipt(**json.loads(json.dumps(rcpt))) for r_id, rcpt in receipt_file.items()]
        return True


def change_view_all_receipt(current_frame: Frame):
    global receipts, view_all_frame
    load_receipts()
    current_frame.forget()
    view_all_frame.receipts = receipts[:]
    view_all_frame.filtered_receipts = receipts[:]
    view_all_frame.detail_frame = rcpt_dtls_frame
    view_all_frame.load_details()
    view_all_frame.tkraise()


if __name__ == '__main__':
    main()
