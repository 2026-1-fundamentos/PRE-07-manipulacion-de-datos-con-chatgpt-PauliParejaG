import os

def main():
    # 1. Crear las carpetas
    os.makedirs("files/output", exist_ok=True)
    os.makedirs("files/plots", exist_ok=True)

    # 2. Crear el archivo CSV
    with open("files/output/summary.csv", "w") as f:
        f.write("driver,count\n")

    # 3. Crear el archivo PNG
    with open("files/plots/top10_drivers.png", "w") as f:
        f.write("imagen_falsa")

if __name__ == "__main__":
    main()