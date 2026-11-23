"""Registro de eventos y errores en archivo (único uso permitido de archivos)."""
import logging
import os

RUTA_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", "eventos.log")
os.makedirs(os.path.dirname(RUTA_LOG), exist_ok=True)

logger = logging.getLogger("software_fj")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _h = logging.FileHandler(RUTA_LOG, mode="w", encoding="utf-8")
    _h.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    logger.addHandler(_h)
