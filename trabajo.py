def get_parity_bit(message):
    # Verified que el mensaje contenga solo 0s y 1s
    if not all(bit in '01' for bit in message):
        return "Error: El mensaje debe contener solo 0s y 1s"
    
    number_of_ones = message.count("1")
    # Agrega bit de paridad: 0 si el número de 1s es par, 1 si es impar
    if number_of_ones % 2 == 0:
        return message + "0"
    return message + "1"

def send_message():
    valid_message = "01010101"
    invalid_message = "00010101"
    # Prueba ambos mensajes
    print("Probando mensaje válido:")
    receive_message(get_parity_bit(valid_message))
    print("\nProbando mensaje inválido:")
    receive_message(get_parity_bit(invalid_message))

def receive_message(message_with_parity_bit):
    # Verifica que el mensaje no esté vacío
    if not message_with_parity_bit:
        print("Error: Mensaje vacío")
        return
    
    # Obtiene el mensaje sin el bit de paridad
    message = message_with_parity_bit[:-1]
    parity_bit = message_with_parity_bit[-1]
    
    # Calcula el número de 1s en el mensaje completo
    number_of_ones = message_with_parity_bit.count("1")
    
    # Verifica la paridad
    if number_of_ones % 2 == 0:
        print("El mensaje llegó correctamente")
        print("Mensaje: " + message)
        print(f"Bit de paridad: {parity_bit}")
    else:
        print("Retransmitir el mensaje")
        print("Mensaje: " + message)
        print(f"Bit de paridad: {parity_bit}")

def test():
    message = input("Ingrese el mensaje: ")
    message_with_parity_bit = get_parity_bit(message)
    print("El mensaje con bit de paridad es: " + message_with_parity_bit)
    # Verifica el mensaje recibido
    receive_message(message_with_parity_bit)

# Llama a la función test para probar
test()
