import tkinter as tk
from tkinter import messagebox, Listbox,ttk
from tkintertable import TableCanvas
import datetime
import pandas as pd

class StockScraperApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.username = ""
        self.password = ""

        self.title("Login to the App")
        self.geometry("300x200")

        self.username_label = tk.Label(self, text="Username: ")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password: ")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.validate_credentials)
        self.login_button.pack()

    def validate_credentials(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        if self.username == "" and self.password == "":
            messagebox.showinfo("Info", "Login Successful!")
            self.geometry("200x100")
            self.create_stock_select_window()
        else:
            messagebox.showerror("Error", "Invalid credentials, please try again.")

    def create_stock_select_window(self):
        self.stock_select_window = tk.Toplevel(self)
        self.stock_select_window.title("Stock Scraper App")
        self.stock_select_window.geometry("700x500")

        # #Top Frame for the title
        # top_frame= ttk.Frame(self.stock_select_window)
        # top_frame.grid(column = 0, row=0)
        #
        # header_label = ttk.Label(top_frame, text="Fetch stock data from yahoo finance website !")
        # header_label.grid(column = 0, row=0)
        #
        # #Mid frame to get inputs from users
        # mid_frame = ttk.Frame(self.stock_select_window)
        # mid_frame.grid(column=0, row=1)
        #
        # self.stock_list = Listbox(self.mid_frame)
        # self.stock_list.insert(1, "Stock 1")
        # self.stock_list.insert(2, "Stock 2")
        # self.stock_list.insert(3, "Stock 3")
        # self.stock_list.pack()
        #
        # self.scrape_button = tk.Button(self.stock_select_window, text="Scrape", command=self.scrape_data)
        # self.scrape_button.pack()
        # Create the first frame

        self.stock_select_window.columnconfigure(0, weight=1)
        self.stock_select_window.rowconfigure(0, weight=1)
        self.stock_select_window.rowconfigure(1, weight=2)
        self.stock_select_window.rowconfigure(2, weight=3)

        top_frame = ttk.Frame(self.stock_select_window,borderwidth=5, relief="solid")
        top_frame.grid(row=0, column=0, sticky="nsew")

        # Create the second frame
        mid_frame = ttk.Frame(self.stock_select_window,borderwidth=5, relief="solid")
        mid_frame.grid(row=1, column=0, sticky="nsew")

        # Create the third frame
        bottom_frame = ttk.Frame(self.stock_select_window,borderwidth=5, relief="solid")
        bottom_frame.grid(row=2, column=0, sticky="nsew")

        # Add widgets to the frames
        label1 = ttk.Label(top_frame, text="Fetch stock data from Yahoo finance website !")
        label1.pack()

        label2 = ttk.Label(mid_frame, text="Select the stock code to get data.")
        label2.pack()

        self.stock_list = Listbox(mid_frame)
        self.stock_list.insert(1, "SPY")
        self.stock_list.insert(2, "Stock 2")
        self.stock_list.insert(3, "Stock 3")
        self.stock_list.pack()

        self.scrape_button = tk.Button(mid_frame, text="Scrape", command=self.scrape_data)
        self.scrape_button.pack()


        self.label3 = ttk.Label(bottom_frame, text="This is the third frame")
        self.label3.pack()

        self.table = TableCanvas(bottom_frame, data=self.stock_data)
        self.table.show()

        # # Create the Treeview widget
        # tree = ttk.Treeview(bottom_frame, columns=self.stock_data.columns, show='headings')
        # tree.pack()
        #
        # # Set the column headings
        # for col in self.stock_data.columns:
        #     tree.heading(col, text=col)
        #     tree.column(col, width=100, anchor='center')
        #
        # # Insert the data into the Treeview
        # for index, row in self.stock_data.iterrows():
        #     tree.insert('', 'end', values=list(row))

    def scrape_data(self):
        selected_stock = self.stock_list.get(self.stock_list.curselection())
        messagebox.showinfo("Info", f"Scraping data for {selected_stock}")

        stockcode = selected_stock

        ts1 = str(int(datetime.datetime(2023, 1, 15).timestamp()))
        ts2 = str(int(datetime.datetime(2023, 1, 25).timestamp()))

        interval = '1d'
        # interval='1wk'
        # interval='1mo'

        event = 'history'
        # events= 'div'
        # events= 'splits'

        url = 'https://query1.finance.yahoo.com/v7/finance/download/' \
              + stockcode + '?period1=' + ts1 + '&period2=' + ts2 + '&interval=' \
              + interval + '&events=' + event + '&includeAdjustedClose=true'

        print(url)
        print(ts1)
        print(ts2)

        self.stock_data = pd.read_csv(url)

        # Scrape data for the selected stock and save to the database

if __name__ == "__main__":
    app = StockScraperApp()
    app.mainloop()