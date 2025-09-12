masala_spices = ("cumin", "coriander", "turmeric", "chili powder", "ginger")

print(masala_spices)

(first_spice, second_spice, *other_spices) = masala_spices
print(first_spice)

#membership
print("cumin" in masala_spices)
print("black pepper" in masala_spices)
