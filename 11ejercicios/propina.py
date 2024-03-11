def calcular_propina(total_cuenta):
    propina_18 = total_cuenta * 0.18
    total_18 = total_cuenta + propina_18

    propina_20 = total_cuenta * 0.20
    total_20 = total_cuenta + propina_20

    propina_25 = total_cuenta * 0.25
    total_25 = total_cuenta + propina_25

    return propina_18, total_18, propina_20, total_20, propina_25, total_25

def main():
    total_cuenta = float(input("¿Cuál es el total de la cuenta para hoy, por favor? $"))
    propina_18, total_18, propina_20, total_20, propina_25, total_25 = calcular_propina(total_cuenta)

    print(f"La propina del 18% es de ${propina_18:.2f}, lo que hace un total de ${total_18:.2f}.")
    print(f"La propina del 20% es de ${propina_20:.2f}, lo que hace un total de ${total_20:.2f}.")
    print(f"La propina del 25% es de ${propina_25:.2f}, lo que hace un total de ${total_25:.2f}.")

if __name__ == "__main__":
    main()
