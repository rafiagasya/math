import tkinter as tk
from tkinter import ttk
from balok import BalokCalculator
from bola import BolaCalculator
from kerucut import KerucutCalculator
from tabung import TabungCalculator
from prisma import PrismaCalculator
from lingkaran import LingkaranCalculator
from segitiga import SegitigaCalculator
from konversi_celcius import KonversiCelciusCalculator
from konversi_dollar import KonversiDollarCalculator

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Functional Calculator")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main frame
        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sidebar
        sidebar = tk.Frame(main_frame, bg="#2c3e50", width=180)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)
        
        # Title
        title_label = tk.Label(sidebar, text="KALKULATOR", bg="#2c3e50", fg="white", 
                              font=("Arial", 14, "bold"), pady=15)
        title_label.pack(fill=tk.X)
        
        # Section 1: Volume dan Luas Permukaan
        section1 = tk.Label(sidebar, text="📦 Volume & Luas Permukaan", bg="#2c3e50", 
                           fg="#ecf0f1", font=("Arial", 10, "bold"), pady=10)
        section1.pack(fill=tk.X, padx=5)
        
        buttons_data = [
            ("Balok", BalokCalculator),
            ("Bola", BolaCalculator),
            ("Kerucut", KerucutCalculator),
            ("Tabung", TabungCalculator),
            ("Prisma Segitiga", PrismaCalculator),
        ]
        
        self.pages = {}
        
        for text, widget_class in buttons_data:
            btn = tk.Button(sidebar, text=text, bg="#3498db", fg="white", 
                           font=("Arial", 10), padx=10, pady=10, 
                           command=lambda w=widget_class: self.show_page(w),
                           activebackground="#2980b9", relief=tk.FLAT, border=0)
            btn.pack(fill=tk.X, padx=5, pady=2)
            self.pages[widget_class] = widget_class
        
        # Section 2: Luas dan Keliling
        section2 = tk.Label(sidebar, text="📐 Luas & Keliling", bg="#2c3e50", 
                           fg="#ecf0f1", font=("Arial", 10, "bold"), pady=10)
        section2.pack(fill=tk.X, padx=5)
        
        buttons_data2 = [
            ("Lingkaran", LingkaranCalculator),
            ("Segitiga Siku-siku", SegitigaCalculator),
        ]
        
        for text, widget_class in buttons_data2:
            btn = tk.Button(sidebar, text=text, bg="#9b59b6", fg="white", 
                           font=("Arial", 10), padx=10, pady=10, 
                           command=lambda w=widget_class: self.show_page(w),
                           activebackground="#8e44ad", relief=tk.FLAT, border=0)
            btn.pack(fill=tk.X, padx=5, pady=2)
            self.pages[widget_class] = widget_class
        
        # Section 3: Konversi
        section3 = tk.Label(sidebar, text="🔄 Konversi Data", bg="#2c3e50", 
                           fg="#ecf0f1", font=("Arial", 10, "bold"), pady=10)
        section3.pack(fill=tk.X, padx=5)
        
        buttons_data3 = [
            ("Konversi Suhu", KonversiCelciusCalculator),
            ("Konversi Mata Uang", KonversiDollarCalculator),
        ]
        
        for text, widget_class in buttons_data3:
            btn = tk.Button(sidebar, text=text, bg="#e74c3c", fg="white", 
                           font=("Arial", 10), padx=10, pady=10, 
                           command=lambda w=widget_class: self.show_page(w),
                           activebackground="#c0392b", relief=tk.FLAT, border=0)
            btn.pack(fill=tk.X, padx=5, pady=2)
            self.pages[widget_class] = widget_class
        
        # Content area
        self.content_frame = tk.Frame(main_frame, bg="#f0f0f0")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Welcome page
        welcome_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        welcome_label = tk.Label(welcome_frame, 
                                text="Selamat datang di Multi-Functional Calculator!\n\nPilih fungsi kalkulator di sebelah kiri untuk memulai.",
                                bg="#f0f0f0", fg="#555", font=("Arial", 16))
        welcome_label.pack(expand=True)
        
        self.current_page = None
    
    def show_page(self, widget_class):
        if self.current_page is not None:
            self.current_page.pack_forget()
        
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.pack_forget()
        
        # Create and show new page
        page = widget_class(self.content_frame)
        page.pack(fill=tk.BOTH, expand=True)
        self.current_page = page

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
