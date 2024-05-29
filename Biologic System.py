from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import json
import traceback

root = Tk()

class PatientRecord:
    def __init__(self, name, URN, date,  mobile, medicine, doctor, status, ordered):
        self.name = name
        self.URN = URN
        self.date = date
        self.mobile = mobile
        self.medicine = medicine
        self.doctor = doctor
        self.status = status
        self.ordered = ordered

    def update_name(self, name):
        self.name = name

    def update_URN(self, URN):
        self.URN = URN

    def update_mobile(self, mobile):
        self.mobile = mobile

    def update_medicine(self, medicine):
        self.medicine = medicine

    def update_doctor(self, doctor):
        self.doctor = doctor

    def update_status(self, status):
        self.status = status

    def update_ordered(self, ordered):
        self.ordered = ordered

    def display_status(self):
        return f"Patient: {self.name}, URN: {self.URN}, Mobile: {self.mobile}, Medicine: {self.medicine}, Doctor: {self.doctor}, Status: {self.status}, Ordered: {self.ordered}"


    def to_dict(self):
        return {
            "name": self.name,
            "URN": self.URN,
            "date": self.date,
            "mobile": self.mobile,
            "medicine": self.medicine,
            "doctor": self.doctor,
            "status": self.status,
            "ordered": self.ordered
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["URN"],
            data["date"],
            data["mobile"],
            data["medicine"],
            data["doctor"],
            data["status"],
            data["ordered"]
        )


    @classmethod
    def load_from_file(cls, filename):
        try:
            with open("Records/"+filename, 'r') as file:
                data = json.load(file)
                return cls.from_dict(data)
        except IOError as e:
            print(f"Failed to load patient record: {e}")
            messagebox.showerror("Error", f"Failed to load patient record: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            messagebox.showerror("Error", f"Error decoding JSON: {e}")


def opensearched():
    number = t.get() + ".txt"
    try:
        load = PatientRecord.load_from_file(number)
    except Exception:
        traceback.print_exc()
        print("returned")
        return
    global name_e
    global urn_e
    global mobile_num_e
    global date_e
    global med_e
    global doc_e
    global status_e
    global order_e

    op = Toplevel(root)
    op.geometry("500x600")
    op.resizable(False, False)
    op.title("Edit patient record")
    op.configure(bg="grey")

    Label(op, text="Name:", foreground="black", bg="grey", font=("Arial", 20)).grid(row=0, column=0, padx=5, pady=5)
    Label(op, text="URN:", foreground="black", bg="grey", font=("Arial", 20)).grid(row=1, column=0, padx=5, pady=5)
    Label(op, text="Date:", foreground="black", bg="grey", font=("Arial", 20)).grid(row=2, column=0, padx=5, pady=5)
    Label(op, text="Mobile:", foreground="black", bg="grey", font=("Arial", 20)).grid(row=3, column=0, padx=5, pady=5)
    Label(op, text="Medicine:", foreground="black", bg="grey", font=("Arial", 20)).grid(row=4, column=0, padx=5, pady=5)
    Label(op, text="Doctor:", foreground="black", bg="grey", font=("Arial", 20)).grid(row=5, column=0, padx=5, pady=5)
    Label(op, text="Status:", foreground="black", bg="grey", font=("Arial", 20)).grid(row=6, column=0, padx=5, pady=5)
    Label(op, text="Ordered:", foreground="black", bg="grey", font=("Arial", 20)).grid(row=8, column=0, padx=5, pady=5)

    name_e = Entry(op, font=("Arial", 20), foreground="black", background="white")
    name_e.insert(0, load.name)
    urn_e = Entry(op, font=("Arial", 20), foreground="black", background="white")
    urn_e.insert(0, load.URN)
    mobile_num_e = Entry(op, font=("Arial", 20), foreground="black", background="white")
    mobile_num_e.insert(0, load.mobile)
    date_e = Entry(op, font=("Arial", 20), foreground="black", background="white")
    date_e.insert(0, load.date)
    med_e = Entry(op, font=("Arial", 20), foreground="black", background="white")
    med_e.insert(0, load.medicine)
    doc_e = Entry(op, font=("Arial", 20), foreground="black", background="white")
    doc_e.insert(0, load.doctor)
    status_e = Text(op, font=("Arial", 15), foreground="black", background="white", width=30, height=5)
    status_e.insert('1.0', load.status)
    order_e = Entry(op, font=("Arial", 20), foreground="black", background="white")
    order_e.insert(0, load.ordered)

    name_e.grid(row=0, column=1, padx=5, pady=5)
    urn_e.grid(row=1, column=1, padx=5, pady=5)
    date_e.grid(row=2, column=1, padx=5, pady=5)
    mobile_num_e.grid(row=3, column=1, padx=5, pady=5)
    med_e.grid(row=4, column=1, padx=5, pady=5)
    doc_e.grid(row=5, column=1, padx=5, pady=5)
    status_e.grid(row=6, column=1, padx=5, pady=5)
    order_e.grid(row=8, column=1, padx=5, pady=5)

    Button(op, text="Save", foreground="black", font=("Arial", 20), command=edit_to_file).grid(row=9, column=1, padx=10, pady=10)


def addnew():
    global name_entry
    global URN_entry
    global mobile_entry
    global date_entry
    global medicine_entry
    global doctor_entry
    global status_entry
    global ordered_entry

    ad = Toplevel(root)
    ad.geometry("500x600")
    ad.resizable(False, False)
    ad.title("Add new patient to records")
    ad.configure(bg="grey")

    Label(ad, text="Name:", foreground="black", bg="grey", font= ("Arial", 20)).grid(row=0, column=0, padx=5, pady=5)
    Label(ad, text="URN:", foreground="black",bg="grey", font= ("Arial", 20)).grid(row=1, column=0, padx=5, pady=5)
    Label(ad, text="Date:", foreground="black", bg="grey",font= ("Arial", 20)).grid(row=2,column=0,padx=5,pady=5)
    Label(ad, text="Mobile:", foreground="black", bg="grey",font= ("Arial", 20)).grid(row=3, column=0, padx=5, pady=5)
    Label(ad, text="Medicine:", foreground="black", bg="grey",font= ("Arial", 20)).grid(row=4, column=0, padx=5, pady=5)
    Label(ad, text="Doctor:", foreground="black", bg="grey",font= ("Arial", 20)).grid(row=5, column=0, padx=5, pady=5)
    Label(ad, text="Status:", foreground="black", bg="grey",font= ("Arial", 20)).grid(row=6, column=0, padx=5, pady=5)
    Label(ad, text="Ordered:", foreground="black", bg="grey",font= ("Arial", 20)).grid(row=8, column=0, padx=5, pady=5)

    name_entry = Entry(ad, font=("Arial", 20), foreground="black", background="white")
    URN_entry = Entry(ad, font=("Arial", 20), foreground="black", background="white")
    mobile_entry = Entry(ad, font=("Arial", 20), foreground="black", background="white")
    date_entry = Entry(ad, font = ("Arial", 20), foreground="black", background="white")
    medicine_entry = Entry(ad, font=("Arial", 20), foreground="black", background="white")
    doctor_entry = Entry(ad, font=("Arial", 20), foreground="black", background="white")
    status_entry = Text(ad, font=("Arial", 15), foreground="black", background="white", width=30 , height= 5)
    ordered_entry = Entry(ad, font=("Arial", 20), foreground="black", background="white")

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    URN_entry.grid(row=1, column=1, padx=5, pady=5)
    date_entry.grid(row=2,column=1,padx=5,pady=5)
    mobile_entry.grid(row=3, column=1, padx=5, pady=5)
    medicine_entry.grid(row=4, column=1, padx=5, pady=5)
    doctor_entry.grid(row=5, column=1, padx=5, pady=5)
    status_entry.grid(row=6, column=1, padx=5, pady=5)
    ordered_entry.grid(row=8, column=1, padx=5, pady=5)

    Button(ad, text="Save", foreground="black", font = ("Arial", 20), command=save_to_file).grid(row=9, column=1, padx=10, pady=10)

def save_to_file():
    patient = {
        "name": name_entry.get(),
        "URN": URN_entry.get(),
        "date": date_entry.get(),
        "mobile": mobile_entry.get(),
        "medicine": medicine_entry.get(),
        "doctor": doctor_entry.get(),
        "status": status_entry.get('1.0', 'end-1c'),
        "ordered": ordered_entry.get()
    }
    try:
        with open("Records/"+mobile_entry.get()+".txt", 'w') as file:
            json.dump(patient, file)
        messagebox.showinfo("Info", "Patient record saved successfully.")
    except IOError as e:
        messagebox.showerror("Error", f"Failed to save patient record: {e}")

def edit_to_file():
    patient = {
        "name": name_e.get(),
        "URN": urn_e.get(),
        "date": date_e.get(),
        "mobile": mobile_num_e.get(),
        "medicine": med_e.get(),
        "doctor": doc_e.get(),
        "status": status_e.get('1.0', 'end-1c'),
        "ordered": order_e.get()
    }
    try:
        with open("Records/"+mobile_num_e.get()+".txt", 'w') as file:
            json.dump(patient, file)
        messagebox.showinfo("Info", "Patient record saved successfully.")
    except IOError as e:
        messagebox.showerror("Error", f"Failed to save patient record: {e}")

def quit():
    exit(0)

root.geometry("500x200")
root.title("Biologic System")
root.configure(bg = "grey")
root.resizable(False, False)

Label(root,background="grey",  foreground="black", text= "Mobile Number: ", font=("Arial", 16)).place(x=5,y=5)

t = Entry(root,foreground ="black", background="white", font = ("Arial", 17), width= 12)
t.place(x = 160, y = 5)

search = Button(root, text = "Search", foreground="black", background="grey", font = ("Arial", 17), width = 10, height=1, command=opensearched)
search.place(x = 340, y = 5)

add = Button(root, text = "Add New Patient", foreground="black", background="grey", font = ("Arial", 15), width = 15, height=1, command=addnew)
add.place(x = 320, y = 150)

q = Button(root, text = "Close", foreground="black", background="grey", font = ("Arial", 17), width = 10, height=1, command=quit)
q.place(x = 50, y=150)

mainloop()



