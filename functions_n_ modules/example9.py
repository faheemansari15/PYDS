# keywords arguments

def saveInfo(file = "info.txt", **kwargs):
    with open(file, "a") as f:
        for k,v in kwargs.items():
            f.write(f"{k}->{v}\n")

saveInfo(mobile="redmi", price="Theek thaak", expiry="2030", features="Camera kamaal ka he")            