def sanitizar(text):
    """
    Función para limpiar el input del usuario, returnando un texto:
    - En mnúsculas.
    - Sin tíldes.
    - Sin caracteres especiales.
    - Sin espacios al inicio y al final.

    Args:
        texto (str): Texto a sanitizar.
    Returns:
        str: Texto sanitizado.

    Resultado esperado:
        sanitizar(" precio de la acción de Apple") -> "precio de la accion apple"
    """
    import unicodedata
    import re

    # Convertir a minúsculas
    text = text.lower()
    # Eliminar tildes
    text = ''.join(
        (c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    )
    # Eliminar caracteres especiales
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Eliminar espacios al inicio y al final
    text = text.strip()

    return text