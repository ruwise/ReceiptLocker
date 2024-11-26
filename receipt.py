class Receipt:

    def __init__(self, r_id, receipt_no, vendor_nm, user_name, date, amount, category, image_path):
        self.r_id = r_id
        self.receipt_no = receipt_no
        self.vendor_nm = vendor_nm
        self.user_name = user_name
        self.date = date
        self.amount = amount
        self.category = category
        self.image_path = image_path

    def to_dict(self):
        return {
                self.r_id: self.__dict__
                }

