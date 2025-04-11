# SysTemp (System Temperature) Version 1.0.20250411a

## 🇪🇸 Español

## Descripción

🖥️ **SysTemp** Es un pequeño script en Python para mostrar las temperaturas del sistema de forma clara, amigable y legible desde la terminal. Ideal para técnicos e informáticos que quieren una vista rápida y organizada de los sensores de temperatura en su equipo Linux.

## 🚀 Características
- Muestra temperaturas de CPU, NVMe, WiFi, chipset y otros sensores.

- Agrupa por tipo de sensor.

- Usa emojis para mayor claridad visual:

-- 🛠️ Nombre del sensor
-- 🌡️ Temperatura
-- ⚠️ Límite de alerta (high)
-- 🚨 Límite crítico (critical)



📦 Requisitos
Python 3.6 o superior

psutil

Instalación rápida de psutil:

bash
Copiar
Editar
pip install psutil
💻 Uso
Ejecutá el script directamente:

bash
Copiar
Editar
python3 systemp.py
Salida esperada:

yaml
Copiar
Editar
===================== Temperaturas del sistema =====================

🛠️  Sensor: nvme
   🌡️ Composite: 29.9°C (⚠️  Alerta: 117.8°C) (🚨 Critico: 149.8°C)

🛠️  Sensor: coretemp
   🌡️ Core 0: 33.0°C (⚠️  Alerta: 100.0°C) (🚨 Critico: 100.0°C)

...
====================================================================
📜 Licencia
Este proyecto está licenciado bajo la GPLv3.
