from Usuario import Usuario

adrien = Usuario ("Adrien")
nibbles =Usuario ("Mr Nibbles")
bennyBob =Usuario ("Benny Bob")

adrien.hacer_deposito (100)
adrien.hacer_deposito (150)
adrien.hacer_deposito (100)
adrien.hacer_retiro (45)
adrien.mostrar_balance_usuario()



nibbles.hacer_deposito (1500)
nibbles.hacer_deposito(1000)
nibbles.hacer_retiro (500)
nibbles.hacer_retiro(800)
nibbles.mostrar_balance_usuario()


bennyBob.hacer_deposito(1000)
bennyBob.hacer_retiro(1000)
bennyBob.hacer_retiro(3000)
bennyBob.hacer_retiro(4500)
bennyBob.mostrar_balance_usuario()


adrien.hacerTransferencia(100, bennyBob)