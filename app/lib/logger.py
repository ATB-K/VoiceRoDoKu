import logging
import logging.handlers


# VoiceRoDoKuログ定義
def server_handler():
    server = logging.handlers.RotatingFileHandler("log/VoiceRoDoKu.log", "a+", maxBytes=50000, backupCount=5)
    server.setLevel(logging.DEBUG) 
    server.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(module)s.py]: %(message)s'))
    return server