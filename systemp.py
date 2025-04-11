#!/usr/bin/env python3
# 
# SysTemp (System Temperature) Version 1.0.20250411a
# 
# Autor: Axel O'BRIEN (LiGNUxMan) axelobrien@gmail.com y ChatGPT
# 
import psutil
BOLD = "\033[1m" #
RESET = "\033[0m"

def mostrar_temperaturas():
    """Muestra de forma clara las temperaturas reportadas por sensores del sistema."""
    temps = psutil.sensors_temperatures()
    if not temps:
        print("No se detectaron sensores de temperatura.")
        return

    print(f"{'='*21} Temperaturas del sistema {'='*21}")
    for sensor, lecturas in temps.items():
        print(f"")
        print(f"🛠️  Sensor: {BOLD}{sensor}{RESET}")
        for t in lecturas:
            label = t.label if t.label else "(sin etiqueta)"
            current = f"{BOLD}{t.current:.1f}°C{RESET}"
            high = f" (⚠️  Alerta: {t.high:.1f}°C)" if t.high else ""
            critical = f" (🚨 Critico: {t.critical:.1f}°C)" if t.critical else ""
            print(f"   🌡️ {label}: {current}{high}{critical}")

    print(f"")
    print(f"{'='*68}")

mostrar_temperaturas()

