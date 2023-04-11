import pickle


def main():
    class Vehiculo:
        MazdaRX7 = {
            'nombre': 'Mazda RX7',
            'color': 'Rojo',
            'esDeportivo': 'Es deportivo'
        }

    carro = open('carro.bin', 'wb')
    pickle.dump(Vehiculo.MazdaRX7, carro)
    carro.close()

    carroCargado = None

    def cargarCarro():
        abrir = open('carro.bin', 'rb')
        cargado = pickle.load(abrir)
        abrir.close()
        return cargado

    carroCargado = cargarCarro()
    print(carroCargado)


if __name__ == '__main__':
    main()
