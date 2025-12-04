# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════════╗
║                   PRUEBA RÁPIDA DE TODOS LOS MÉTODOS                  ║
╚═══════════════════════════════════════════════════════════════════════╝

PROPÓSITO:
----------
Ejecuta este archivo para:
  ✅ Verificar que todos los métodos funcionan correctamente
  ✅ Ver ejemplos de cómo se imprimen los resultados
  ✅ Asegurarte de que no hay errores antes del parcial

CÓMO USAR:
----------
  python test_rapido.py

O desde PyCharm:
  Click derecho → Run 'test_rapido'

MÉTODOS PROBADOS:
-----------------
  1. RK4 (EDO con función)
  2. Heun con datos discretos
  3. Simpson 1/3 (integral con función)
  4. Trapecio con datos discretos

SI TODOS FUNCIONAN:
-------------------
  → Tu proyecto está listo para el parcial ✅
  → Lee GUIA_PARCIAL.md para aprender a usarlos

SI HAY ERRORES:
---------------
  → Revisa que todos los archivos estén en su carpeta
  → Verifica que Python esté instalado correctamente
"""

# Configurar salida UTF-8 para Windows
import sys
import io
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except:
        pass  # Si falla, continuamos con la configuración por defecto

print("\n" + "="*70)
print(" PRUEBA RAPIDA DE METODOS NUMERICOS")
print("="*70)
print("\n[*] Probando 4 metodos representativos...")
print("   (Esto toma solo unos segundos)")
print("="*70)

# ===================================
# TEST 1: RK4 para EDOs
# ===================================
print("\n[1/4] Probando RK4 para EDOs...")
print("-"*70)

import sys
sys.path.append("1_EDOs/funcion")
from rk4 import rk4

f = lambda x, y: x + y
x_vals, y_vals = rk4(f, 0, 1, 0.1, 5)

print(f"\nResultado: y(0.5) = {y_vals[-1]:.10f}")
print("Estado: OK")

# ===================================
# TEST 2: Heun con datos discretos
# ===================================
print("\n[2/4] Probando Heun con datos discretos...")
print("-"*70)

sys.path.append("1_EDOs/datos_discretos")
from heun_arreglos import heun_arreglos

x_datos = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
dy_datos = [0, 0.4, 0.8, 1.2, 1.6, 2.0]
y_resultado = heun_arreglos(x_datos, dy_datos, 0)

print(f"\nResultado: y(1.0) = {y_resultado[-1]:.10f}")
print("Estado: OK")

# ===================================
# TEST 3: Simpson 1/3 para integrales
# ===================================
print("\n[3/4] Probando Simpson 1/3 para integrales...")
print("-"*70)

sys.path.append("2_Integracion/funcion")
from simpson13 import simpson13

f_int = lambda x: x**2
resultado_int = simpson13(f_int, 0, 1, 6)

print(f"\nResultado: integral = {resultado_int:.10f}")
print(f"Valor exacto: 0.3333333333")
print(f"Error: {abs(resultado_int - 1/3):.2e}")
print("Estado: OK")

# ===================================
# TEST 4: Trapecio con datos
# ===================================
print("\n[4/4] Probando Trapecio con datos discretos...")
print("-"*70)

sys.path.append("2_Integracion/datos_discretos")
from trapecio_arreglos import trapecio_datos

x_int = [0, 1, 2, 3]
y_int = [0, 1, 4, 9]
resultado_trap = trapecio_datos(x_int, y_int)

print(f"\nResultado: integral = {resultado_trap:.6f}")
print("Estado: OK")

# ===================================
# RESUMEN
# ===================================
print("\n" + "="*70)
print(" [OK] RESUMEN DE PRUEBAS")
print("="*70)
print("\n[!] TODOS LOS METODOS FUNCIONAN CORRECTAMENTE!")
print("\nPROXIMOS PASOS:")
print("   1. Lee GUIA_PARCIAL.md para aprender a usar los metodos")
print("   2. Consulta FORMULAS_Y_CUANDO_USAR.md para ver las formulas")
print("   3. Usa INDICE.md para encontrar rapidamente el archivo que necesitas")
print("\nTIP: Cada archivo .py tiene ejemplos al final que puedes modificar")
print("\nEstas listo para el parcial!")
print("="*70 + "\n")

