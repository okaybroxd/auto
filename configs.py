from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "7257728"))
    API_HASH = getenv("API_HASH", "8a1e2e70fedb8169828c46c2478374d1")
    BOT_TOKEN = getenv("BOT_TOKEN", "5667630550:AAG0xMjClq_3C_VImxMGLTalMwB7d_ghZnI")
    FSUB = getenv("FSUB", "Tcnproject")
    CHID = int(getenv("CHID", "-1001634707201"))
    SUDO = list(map(int, getenv("SUDO", "656059661")))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://doncana72:music1@musicbot1.nm4rmr0.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
