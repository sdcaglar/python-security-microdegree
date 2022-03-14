from exif import Image


with open("1.jpg", "rb") as bil:
    photo = Image(bil)
    if photo.has_exif:
        print(photo.get("datetime"))
        print(photo.get("gps_altitude"))
        print(photo.get("gps_longtitude"))
        print(photo.get("gps_latitude"))
        print(photo.get("make"))
        print(photo.get("model"))
        print(photo.get("software"))

