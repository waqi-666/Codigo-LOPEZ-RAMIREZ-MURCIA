def grafica_murcia():
    import numpy as np
    import matplotlib.pyplot as plt
    from pathlib import Path

    x = np.linspace(0, 10, 100)
    y = np.tan(x)
    y[np.abs(y) > 10] = np.nan  # Evita picos infinitos
    plt.plot(x, y, label="Tangente")
    plt.title("Gráfica de Murcia")
    plt.legend()
    save_path = Path(_file_).parent / "murcia.png"
    plt.savefig(save_path)
    plt.close()
    print(f"Gráfica guardada en: {save_path.resolve()}")
