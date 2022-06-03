# # aprakstam klasi - aprakstam kā strādā cilindri
# class Cylinder:

#     def __init__(self, radius, height):
#         self.height = height
#         self.radius = radius


# # veidojam objektu – konkrētu cilindu
# cilindrs = Cylinder(height=5, radius=10)
# print(cilindrs.height)
# print(cilindrs.radius)
# aprakstam klasi - aprakstam kā strādā cilindri
class Cylinder:

    def __init__(self, radius, height):
        # atribūti – īpašības kas piemīt objektiem
        self.height = height
        self.radius = radius

    # metodes – darbības ko var darīt ar objektu
    def get_area(self):
        base_area = 3.14 * (self.radius ** 2)
        side_area = 2 * 3.14 * self.radius * self.height
        full_area = side_area + 2 * base_area

        return full_area
    
    def get_volume(self):
        volume = 3.14 * (self.radius ** 2) * self.height
        return volume

# veidojam objektu – konkrētu cilindu
cilindrs = Cylinder(height=5, radius=10)
volume = cilindrs.get_volume()
print(volume)
