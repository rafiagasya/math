import tkinter as tk
from tkinter import messagebox
import math

class TabungCalculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f0f0f0")
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(self, text="Kalkulator Tabung", bg="#f0f0f0", fg="#2c3e50",
                        font=("Arial", 18, "bold"))
        title.pack(pady=20)
        
        # Form frame
        form_frame = tk.Frame(self, bg="#f0f0f0")
        form_frame.pack(padx=20, pady=10)
        
        # Jari-jari
        tk.Label(form_frame, text="Jari-jari (cm):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.radius = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.radius.grid(row=0, column=1, pady=5, padx=10)
        
        # Tinggi
        tk.Label(form_frame, text="Tinggi (cm):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.tinggi = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.tinggi.grid(row=1, column=1, pady=5, padx=10)
        
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
            r = float(self.radius.get())
            t = float(self.tinggi.get())
            
            volume = math.pi * (r ** 2) * t
            luas_alas = math.pi * (r ** 2)
            luas_selimut = 2 * math.pi * r * t
            luas_permukaan = 2 * luas_alas + luas_selimut
            
            result_text = f"""HASIL PERHITUNGAN TABUNG
{'─'*40}
Jari-jari: {r} cm
Tinggi: {t} cm

Volume: {volume:.2f} cm³
Luas Alas: {luas_alas:.2f} cm²
Luas Selimut: {luas_selimut:.2f} cm²
Luas Permukaan: {luas_permukaan:.2f} cm²"""
            
            self.result.delete(1.0, tk.END)
            self.result.insert(1.0, result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
    
    def reset(self):
        self.radius.delete(0, tk.END)
        self.tinggi.delete(0, tk.END)
        self.result.delete(1.0, tk.END)
