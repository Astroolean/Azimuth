class AstrooleanSignature:
    def __init__(self, NAME="Astroolean"):
        self.NAME = NAME
    def Signature(self):
        Astro = "Astro - The online name ive always went by."
        Boolean = "Boolean - Embracing the simplicity of true/false."
        return f"\nSignature:\n{Astro}\n{Boolean}\nAll-in-all its just Astroolean."
Astroolean = AstrooleanSignature()
print(Astroolean.Signature())