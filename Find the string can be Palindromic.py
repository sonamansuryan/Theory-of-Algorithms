text = input("Մուտքագրեք բառը: ").strip()

if text == text[::-1]:
    print("Պալինդրոմ է։")
else:
    print("Պալինդրոմ չէ։")

