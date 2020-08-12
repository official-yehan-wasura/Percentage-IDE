# -*- coding: utf-8 -*-
 

# Symbols handler per language
SYMBOLS_HANDLER = {}


def set_symbols_handler(language, symbols_handler):
    """
    Set a symbol handler for the given language
    """
    global SYMBOLS_HANDLER
    SYMBOLS_HANDLER[language] = symbols_handler


def get_symbols_handler(language):
    """
    Returns the symbol handler for the given language
    """
    global SYMBOLS_HANDLER
    return SYMBOLS_HANDLER.get(language, None)


def init_basic_handlers():
    # Import introspection here, it not needed in the namespace of
    # the rest of the file.
    from percentage_ide.tools import introspection
    # Set Default Symbol Handler
    set_symbols_handler('python', introspection)
