import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Blood Bank Manager")
root.geometry("750x600")
root.configure(bg="#fdf7fa")

# Fonts
FONT_HEADER = ("Georgia", 24, "bold")
FONT_LABEL = ("Segoe UI", 11)
FONT_BUTTON = ("Segoe UI", 10, "bold")

ages = list(range(18, 66))
genders = ["Male", "Female", "Other"]
blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

# Styles
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#fff3f7", font=FONT_LABEL)
style.configure("TEntry", padding=8, relief="flat")
style.configure("TCombobox", padding=8, relief="flat")

style.configure("Rounded.TButton",
                font=FONT_BUTTON,
                padding=10,
                background="#f4a6b5",
                foreground="white",
                borderwidth=0,
                relief="flat")

style.map("Rounded.TButton",
          background=[("active", "#f17394"), ("pressed", "#e94b6c")],
          foreground=[("pressed", "white")])

def drop_shadow(parent):
    shadow = tk.Frame(parent, bg="#e3dce1")
    shadow.pack(padx=35, pady=35, fill="both", expand=True)
    return shadow

def pretty_frame(parent):
    outer = drop_shadow(parent)
    frame = tk.Frame(outer, bg="#fff3f7", bd=0, highlightthickness=1, highlightbackground="#f0c2d4")
    frame.pack(padx=0, pady=0, fill="both", expand=True)
    return frame

def labeled_input(parent, label, row):
    ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", pady=6)
    entry = ttk.Entry(parent, width=30)
    entry.grid(row=row, column=1, pady=6)
    return entry

def add_donor_gui():
    win = tk.Toplevel(root)
    win.title("Add Donor")
    win.configure(bg="#fdf7fa")
    frame = pretty_frame(win)

    name = labeled_input(frame, "Donor Name", 0)

    ttk.Label(frame, text="Age").grid(row=1, column=0, sticky="w", pady=6)
    age = ttk.Combobox(frame, values=ages, state="readonly", width=28)
    age.grid(row=1, column=1, pady=6)

    ttk.Label(frame, text="Gender").grid(row=2, column=0, sticky="w", pady=6)
    gender = ttk.Combobox(frame, values=genders, state="readonly", width=28)
    gender.grid(row=2, column=1, pady=6)

    ttk.Label(frame, text="Blood Type").grid(row=3, column=0, sticky="w", pady=6)
    blood = ttk.Combobox(frame, values=blood_types, state="readonly", width=28)
    blood.grid(row=3, column=1, pady=6)

    weight = labeled_input(frame, "Weight (kg)", 4)
    disease = labeled_input(frame, "Disease (if any)", 5)

    def submit():
        try:
            BloodBank.donor_details(name.get(), int(age.get()), gender.get(), blood.get(),
                                    float(weight.get()), disease.get())
            messagebox.showinfo("Success", "Donor Added Successfully")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    ttk.Button(frame, text="➕ Add Donor", style="Rounded.TButton", command=submit).grid(row=6, column=0, columnspan=2, pady=20)

def request_blood_gui():
    win = tk.Toplevel(root)
    win.title("Request Blood")
    win.configure(bg="#fdf7fa")

    frame = pretty_frame(win)

    fields = {}
    def input_field(label, row):
        ttk.Label(frame, text=label).grid(row=row, column=0, sticky="w", pady=6)
        entry = ttk.Entry(frame, width=30)
        entry.grid(row=row, column=1, pady=6)
        fields[label] = entry

    input_field("Hospital Name", 0)
    input_field("Patient Name", 1)

    ttk.Label(frame, text="Patient Age").grid(row=2, column=0, sticky="w", pady=6)
    patient_age = ttk.Combobox(frame, values=ages, state="readonly", width=28)
    patient_age.grid(row=2, column=1, pady=6)

    ttk.Label(frame, text="Patient Gender").grid(row=3, column=0, sticky="w", pady=6)
    patient_gender = ttk.Combobox(frame, values=genders, state="readonly", width=28)
    patient_gender.grid(row=3, column=1, pady=6)

    ttk.Label(frame, text="Patient Blood Type").grid(row=4, column=0, sticky="w", pady=6)
    patient_blood = ttk.Combobox(frame, values=blood_types, state="readonly", width=28)
    patient_blood.grid(row=4, column=1, pady=6)

    input_field("Patient Weight", 5)
    input_field("Patient Disease", 6)
    input_field("Donor Name", 7)

    ttk.Label(frame, text="Donor Age").grid(row=8, column=0, sticky="w", pady=6)
    donor_age = ttk.Combobox(frame, values=ages, state="readonly", width=28)
    donor_age.grid(row=8, column=1, pady=6)

    ttk.Label(frame, text="Donor Gender").grid(row=9, column=0, sticky="w", pady=6)
    donor_gender = ttk.Combobox(frame, values=genders, state="readonly", width=28)
    donor_gender.grid(row=9, column=1, pady=6)

    ttk.Label(frame, text="Donor Blood Type").grid(row=10, column=0, sticky="w", pady=6)
    donor_blood = ttk.Combobox(frame, values=blood_types, state="readonly", width=28)
    donor_blood.grid(row=10, column=1, pady=6)

    def submit():
        try:
            BloodBank.request_blood(
                fields["Hospital Name"].get(),
                fields["Patient Name"].get(),
                int(patient_age.get()),
                patient_gender.get(),
                patient_blood.get(),
                float(fields["Patient Weight"].get()),
                fields["Patient Disease"].get(),
                fields["Donor Name"].get(),
                int(donor_age.get()),
                donor_gender.get(),
                donor_blood.get()
            )
            messagebox.showinfo("Success", "Blood Request Submitted")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    ttk.Button(frame, text="🩸 Request Blood", style="Rounded.TButton", command=submit).grid(row=11, column=0, columnspan=2, pady=20)

# ---- Main UI ----
tk.Label(root, text="💖 Blood Bank Manager 💖", font=FONT_HEADER, bg="#fdf7fa", fg="#d14f73").pack(pady=30)

btn_container = tk.Frame(root, bg="#fdf7fa")
btn_container.pack()

ttk.Button(btn_container, text="➕ Add Donor", style="Rounded.TButton", width=25, command=add_donor_gui).grid(row=0, column=0, padx=20, pady=10)
ttk.Button(btn_container, text="🩸 Request Blood", style="Rounded.TButton", width=25, command=request_blood_gui).grid(row=1, column=0, padx=20, pady=10)

root.mainloop()
