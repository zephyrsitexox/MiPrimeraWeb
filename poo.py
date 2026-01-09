class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial # El dinero que tiene la cuenta

    # Acción de DEPOSITAR (Meter dinero)
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print(f"✅ {self.titular} depositó ${cantidad}. Saldo nuevo: ${self.saldo}")

    # --- TU MISIÓN: COMPLETA ESTA FUNCIÓN ---
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente")
        else:    
            self.saldo = self.saldo - cantidad
            print(f"Retiro exitoso de ${cantidad}. Saldo restante: ${self.saldo}")

# --- PRUEBAS ---
mi_cuenta = CuentaBancaria("Daniel", 1000) # Empiezas con $1000

mi_cuenta.depositar(500) # Ahora deberías tener $1500
mi_cuenta.retirar(200)   # Deberías bajar a $1300
mi_cuenta.retirar(5000)  # Debería dar error de saldo insuficiente