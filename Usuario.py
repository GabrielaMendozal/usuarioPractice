class Usuario:
    def __init__(self,name):
        self.name = name
        self.amount =0
        
    def hacer_deposito(self, amount):
        self.amount += amount
    def hacer_retiro(self, amount):
        self.amount -= amount

    def mostrar_balance_usuario(self):
        print (f"Usuario: {self.name},Balance : {self.amount}" )

        
    def hacerTransferencia(self,amount,usuario):
        self.amount -= amount
        usuario.amount += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()