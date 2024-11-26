# Receipt Locker
#### Video Demo:  https://youtu.be/
#### Description:
This is an application which can be used for storing and retrieving receipts. 

UI of this application is built with Tkinter. 
I designed pages using figma and used the tool to create the frames from the design. 
Each frames created kept in different classes and objects of the fame classes are created in main project file. This helped me with changing pages from one to another and loading details to each page.

This application has four pages or frames.
Home fame, upload receipt frame, view all frame and receipt details frame.

Home-frame have two buttons which are used for navigating to upload page and Saved receipts page.

Upload receipt frame have the input fields for entering receipt details to save into storage.
Validation done are,
1. No fields can be empty. 
2. Date field should contain a valid date in dd-mm-yyyy format 
3. Name should contain only alphabets, no numbers or special characters allowed, except comma and space 
4. Amount should be a valid number. Decimal point is allowed.

View all frame is where we can see all the saved receipts. There we can filter saved receipts based on category. Also, we can sort the listed receipt based on the column names such as Receipt Id, Name, Vendor/Shop name, Date or Amount.
Details button will open the selected receipt in receipt details frame. Delete button is for deleting the receipts from storage.

On details frame we can see the selected receipt details. On the same frame we have an open image button. If image is available, we can open the image using that button.

Project.py file is where all the frames are created and linked together. Also, this is where we have the validation methods and file operations for saving and retrieving receipt details.
Project_test.py file contains test cases for the validation functions.

Storage used: Receipt details are stored in a JSON file name receipts.json. Receipt images are stored in the folders under project directory with respective dates as names. 
If we just want the image, we can browse the folders and find the receipt images under each date folders. 
