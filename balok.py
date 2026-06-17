import tkinter as tk
from tkinter import messagebox

class BalokCalculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f0f0f0")
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(self, text="Kalkulator Balok", bg="#f0f0f0", fg="#2c3e50",
                        font=("Arial", 18, "bold"))
        title.pack(pady=20)
        
        # Form frame
        form_frame = tk.Frame(self, bg="#f0f0f0")
        form_frame.pack(padx=20, pady=10)
        
        # Panjang
        tk.Label(form_frame, text="Panjang (cm):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.panjang = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.panjang.grid(row=0, column=1, pady=5, padx=10)
        
        # Lebar
        tk.Label(form_frame, text="Lebar (cm):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.lebar = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.lebar.grid(row=1, column=1, pady=5, padx=10)
        
        # Tinggi
        tk.Label(form_frame, text="Tinggi (cm):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.tinggi = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.tinggi.grid(row=2, column=1, pady=5, padx=10)
        
        # Button frame
        btn_frame = tk.Frame(self, bg="#f0f0f0")
        btn_frame.pack(pady=20)
        
        calc_btn = tk.Button(btn_frame, text="Hitung", bg="#3498db", fg="white",
                            font=("Arial", 11, "bold"), padx=20, pady=10,
                            command=self.calculate, activebackground="#2980b9",
                            relief=tk.FLAT, border=0)
        calc_btn.pack(side=tk.LEFT, padx=10)
        
        reset_btn = tk.Button(btn_frame, text="Reset", bg="#95a5a6", fg="white",
                             font=("Arial", 11, "bold"), padx=20, pady=10,
                             command=self.reset, activebackground="#7f8c8d",
                             relief=tk.FLAT, border=0)
        reset_btn.pack(side=tk.LEFT, padx=10)
        
        # Result frame
        result_label = tk.Label(self, text="Hasil:", bg="#f0f0f0", fg="#333",
                              font=("Arial", 11, "bold"))
        result_label.pack(anchor=tk.W, padx=20, pady=(20, 5))
        
        self.result = tk.Text(self, height=8, width=50, font=("Arial", 10),
                             bg="#ecf0f1", fg="#333", relief=tk.SOLID, border=1)
        self.result.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
    
    def calculate(self):
        try:
            p = float(self.panjang.get())
            l = float(self.lebar.get())
            t = float(self.tinggi.get())
            
            volume = p * l * t
            luas_permukaan = 2 * (p*l + l*t + p*t)
            
            result_text = f"""HASIL PERHITUNGAN BALOK
{'─'*40}
Panjang: {p} cm
Lebar: {l} cm
Tinggi: {t} cm

Volume: {volume:.2f} cm³
Luas Permukaan: {luas_permukaan:.2f} cm²"""
            
            self.result.delete(1.0, tk.END)
            self.result.insert(1.0, result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
    
    def reset(self):
        self.panjang.delete(0, tk.END)
        self.lebar.delete(0, tk.END)
        self.tinggi.delete(0, tk.END)
        self.result.delete(1.0, tk.END)
