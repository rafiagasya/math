import tkinter as tk
from tkinter import messagebox

class PrismaCalculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f0f0f0")
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(self, text="Kalkulator Prisma Segitiga", bg="#f0f0f0", fg="#2c3e50",
                        font=("Arial", 18, "bold"))
        title.pack(pady=20)
        
        # Form frame
        form_frame = tk.Frame(self, bg="#f0f0f0")
        form_frame.pack(padx=20, pady=10)
        
        # Alas Segitiga
        tk.Label(form_frame, text="Alas Segitiga (cm):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.alas_seg = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.alas_seg.grid(row=0, column=1, pady=5, padx=10)
        
        # Tinggi Segitiga
        tk.Label(form_frame, text="Tinggi Segitiga (cm):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.tinggi_seg = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.tinggi_seg.grid(row=1, column=1, pady=5, padx=10)
        
        # Tinggi Prisma
        tk.Label(form_frame, text="Tinggi Prisma (cm):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.tinggi_prisma = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.tinggi_prisma.grid(row=2, column=1, pady=5, padx=10)
        
        # Sisi Miring Segitiga
        tk.Label(form_frame, text="Sisi Miring Segitiga (cm):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.sisi_miring = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.sisi_miring.grid(row=3, column=1, pady=5, padx=10)
        
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
            alas = float(self.alas_seg.get())
            tinggi_seg = float(self.tinggi_seg.get())
            tinggi_prisma = float(self.tinggi_prisma.get())
            sisi_miring = float(self.sisi_miring.get())
            
            luas_alas = 0.5 * alas * tinggi_seg
            volume = luas_alas * tinggi_prisma
            keliling_seg = alas + tinggi_seg + sisi_miring
            luas_permukaan = (2 * luas_alas) + (keliling_seg * tinggi_prisma)
            
            result_text = f"""HASIL PERHITUNGAN PRISMA SEGITIGA
{'─'*40}
Alas Segitiga: {alas} cm
Tinggi Segitiga: {tinggi_seg} cm
Tinggi Prisma: {tinggi_prisma} cm
Sisi Miring: {sisi_miring} cm

Luas Alas: {luas_alas:.2f} cm²
Volume: {volume:.2f} cm³
Luas Permukaan: {luas_permukaan:.2f} cm²"""
            
            self.result.delete(1.0, tk.END)
            self.result.insert(1.0, result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
    
    def reset(self):
        self.alas_seg.delete(0, tk.END)
        self.tinggi_seg.delete(0, tk.END)
        self.tinggi_prisma.delete(0, tk.END)
        self.sisi_miring.delete(0, tk.END)
        self.result.delete(1.0, tk.END)
