import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


x = sp.symbols('x')


fonksiyon_str = input(
    "İntegralini almak istediğiniz fonksiyonu girin (örnek: x**2 + 3*x): ")
fonksiyon = sp.sympify(fonksiyon_str)


a = float(input("Alt sınırı girin: "))
b = float(input("Üst sınırı girin: "))


alan = sp.integrate(fonksiyon, (x, a, b))
print(f"\nFonksiyonun {a} ile {b} arasındaki belirli integrali (alan): {alan}")


fonksiyon_numeric = sp.lambdify(x, fonksiyon, "numpy")


x_vals = np.linspace(a - 1, b + 1, 400)
y_vals = fonksiyon_numeric(x_vals)


plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=f'f(x) = {fonksiyon_str}', color='blue')
plt.fill_between(x_vals, y_vals, where=(x_vals >= a) & (
    x_vals <= b), color='skyblue', alpha=0.5, label='Alan (integral)')
plt.title(f"f(x) fonksiyonu ve [{a}, {b}] aralığında kalan alan")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
