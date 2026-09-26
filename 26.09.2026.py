class Oquvchi:
    def __init__(self, ism, yonalish, daraja):
        self.ism = ism
        self.yonalish = yonalish
        self.daraja = daraja

    def malumot(self):
        print(f"Ism: {self.ism}")
        print(f"Yo'nalish: {self.yonalish}")
        print(f"Daraja: {self.daraja}")


# Jonibek haqida ma'lumot
jonibek = Oquvchi(
    "Jonibek",
    "Backend Python",
    "Boshlang'ich"
)

jonibek.malumot()