# SysTemp (System Temperature) Version 1.0.20250411a

## 🇪🇸 Español

## 🖥️ Descripción

 **SysTemp** Es un pequeño script en Python para mostrar las temperaturas del sistema de forma clara, amigable y legible desde la terminal. Ideal para técnicos e informáticos que quieren una vista rápida y organizada de los sensores de temperatura en su equipo Linux.


## 🚀 Características
- Muestra temperaturas de CPU, NVMe, WiFi, chipset y otros sensores.

- Agrupa por tipo de sensor.

- Usa emojis para mayor claridad visual:

   - 🛠️ Nombre del sensor
   - 🌡️ Temperatura
   - ⚠️ Límite de alerta (high)
   - 🚨 Límite crítico (critical)


## 📦 Requisitos
-Python 3.6 o superior
-psutil


Instalación rápida de psutil:

```pip install psutil


## 💻 Uso
Ejecutá el script directamente:
```bash
```python3 systemp.py
```


## Salida esperada:
```
===================== Temperaturas del sistema =====================

🛠️  Sensor: acpitz
   🌡️ (sin etiqueta): 32.0°C
   🌡️ (sin etiqueta): 29.0°C

🛠️  Sensor: nvme
   🌡️ Composite: 29.9°C (⚠️  Alerta: 117.8°C) (🚨 Critico: 149.8°C)

🛠️  Sensor: coretemp
   🌡️ Package id 0: 47.0°C (⚠️  Alerta: 100.0°C) (🚨 Critico: 100.0°C)
   🌡️ Core 0: 47.0°C (⚠️  Alerta: 100.0°C) (🚨 Critico: 100.0°C)
   🌡️ Core 1: 35.0°C (⚠️  Alerta: 100.0°C) (🚨 Critico: 100.0°C)

🛠️  Sensor: pch_skylake
   🌡️ (sin etiqueta): 28.0°C

🛠️  Sensor: iwlwifi_1
   🌡️ (sin etiqueta): 36.0°C

====================================================================
```

📜 Licencia
Este proyecto está licenciado bajo la GPLv3.
