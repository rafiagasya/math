import tkinter as tk
from tkinter import messagebox

class KonversiCelciusCalculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f0f0f0")
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(self, text="Konversi Suhu dari Celsius", bg="#f0f0f0", fg="#2c3e50",
                        font=("Arial", 18, "bold"))
        title.pack(pady=20)
        
        # Form frame
        form_frame = tk.Frame(self, bg="#f0f0f0")
        form_frame.pack(padx=20, pady=10)
        
        # Celsius
        tk.Label(form_frame, text="Celcius (°C):", bg="#f0f0f0", fg="#333",
                font=("Arial", 11)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.celsius = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.celsius.grid(row=0, column=1, pady=5, padx=10)
        
        # Button frame
        btn_frame = tk.Frame(self, bg="#f0f0f0")
        btn_frame.pack(pady=20)
        
        calc_btn = tk.Button(btn_frame, text="Konversi", bg="#e74c3c", fg="white",
                            font=("Arial", 11, "bold"), padx=20, pady=10,
                            command=self.calculate, activebackground="#c0392b",
                            relief=tk.FLAT, border=0)
        calc_btn.pack(side=tk.LEFT, padx=10)
        
        reset_btn = tk.Button(btn_frame, text="Reset", bg="#95a5a6", fg="white",
                             font=("Arial", 11, "bold"), padx=20, pady=10,
                             command=self.reset, activebackground="#7f8c8d",
                             relief=tk.FLAT, border=0)
        reset_btn.pack(side=tk.LEFT, padx=10)
        
        # Result frame
        result_label = tk.Label(self, text="Hasil Konversi:", bg="#f0f0f0", fg="#333",
                              font=("Arial", 11, "bold"))
        result_label.pack(anchor=tk.W, padx=20, pady=(20, 5))
        
        self.result = tk.Text(self, height=8, width=50, font=("Arial", 10),
                             bg="#ecf0f1", fg="#333", relief=tk.SOLID, border=1)
        self.result.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
    
    def calculate(self):
        try:
            c = float(self.celsius.get())
            
            fahrenheit = (c * 9/5) + 32
            reamur = c * 4/5
            kelvin = c + 273.15
            
            result_text = f"""HASIL KONVERSI SUHU
{'─'*40}
Suhu Awal: {c}°C

Fahrenheit: {fahrenheit:.2f}°F
Reamur: {reamur:.2f}°R
Kelvin: {kelvin:.2f}K"""
            
            self.result.delete(1.0, tk.END)
            self.result.insert(1.0, result_text)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
    
    def reset(self):
        self.celsius.delete(0, tk.END)
        self.result.delete(1.0, tk.END)
