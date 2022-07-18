# Automatizaciones hechas en Python

Scripts en Python para automatizar tareas.

## Generar código QR ([script](./qrcode.py))

Script para generar código QR (png) de una url pasada por parámetro.

```shell
python3 qrcode.py nombreDeImagen url
```

> Necesario instalar `pyqrcode` y `pypng`.

## Comprimir imágenes ([script](./compress.py))

Script para comprimir las imágenes que hay en el directorio de **descargas**.

```shell
python3 compress.py
```

> Necesario instalar `pillow`.

## Detalles del teléfono ([script](./phoneDetail.py))

Script para obtener los datos del teléfono pasado por parámetro.

```shell
python3 phoneDetails.py numeroDeTelefonoConExtension
```

> Necesario instalar `phonenumbers`.
