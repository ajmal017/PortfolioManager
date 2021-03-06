from pyetf.functions import *
from tkinter import *
from tkinter import ttk


class SellEtf(ttk.Frame):
    """Class representing a Frame responsable for the selling of an ETF"""

    def __init__(self, root):
        """
        Given the master instaciate a class handling the selling function
        :param root: ttk.Frame
        """
        super().__init__(root)
        self.root = root
        self.p = root.p
        ttk.Label(self, text='VENDI ETF').grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self, text='Ticker', anchor='w', justify='left').grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self, text='Data Vendita', anchor='w', justify='left').grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(self, text='Numero di Azioni', anchor='w', justify='left').grid(row=3, column=0, padx=5, pady=5)
        ttk.Label(self, text="Prezzo di Vendita", anchor='w', justify='left').grid(row=4, column=0, padx=5, pady=5)
        ttk.Label(self, text='Commissioni', anchor='w', justify='left').grid(row=5, column=0, padx=5, pady=5)
        self.tickerVar = StringVar()
        self.dateVar = StringVar(value='Es. 10-12-2020')
        self.nVar = IntVar()
        self.priceVar = DoubleVar()
        self.commVar = DoubleVar()
        ttk.Entry(self, textvariable=self.tickerVar, width=13).grid(row=1, column=1)  
        self.tickerVar.trace_add('write', lambda *args: self.tickerVar.set(self.tickerVar.get().upper()))
        self.e = ttk.Entry(self, textvariable=self.dateVar, width=13)
        self.e.grid(row=2, column=1)   
        ttk.Entry(self, textvariable=self.nVar, width=13).grid(row=3, column=1)           
        ttk.Entry(self, textvariable=self.priceVar, width=13).grid(row=4, column=1)           
        ttk.Entry(self, textvariable=self.commVar, width=13).grid(row=5, column=1) 
        self.result = ttk.Label(self, text='')
        self.result.grid(row=6, column=1) 
        ttk.Button(self, text='Vendi', command=self.sell_etf).grid(row=6, column=0, pady=10)

    def sell_etf(self):
        """
        When the Add button is clicked try selling the ETF. Display the result on the adjacent label.
        :return None
        """
        #try:
        self.p.sell_etf(self.tickerVar.get(), date_from_text(self.e.get()), self.priceVar.get(), self.commVar.get(), self.nVar.get())       
        self.tickerVar.set('')
        self.dateVar.set('')
        self.priceVar.set('')
        self.commVar.set('')
        self.nVar.set('')
        self.result.configure(text='ETF sold !')
        self.root.app.leftFrame.last_day()
        #except:
            #self.result.configure(text='Errore !')