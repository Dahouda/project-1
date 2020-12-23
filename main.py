
"""
-------------------Master ---------------------------
Face Detection for White and Black People
-------------------Programmer 2---------------------------


-------------------Programmer 3---------------------------


-------------------Programmer testing 1--------------------
I am a student.
"""
print("Import some Libraries")

import PIL.Image
import PIL.ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file('DeLaMardonne.jpg')
# image = face_recognition.load_image_file('people.jpg')
# image = face_recognition.load_image_file('brothers2.jpg')
# image = face_recognition.load_image_file('face2.jpg')
# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

number_of_faces = len(face_locations)
print("I found {} face(s) in this photograph.".format(number_of_faces))

# Load the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = PIL.Image.fromarray(image)

for face_location in face_locations:
    # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # Let's draw a box around the face
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="yellow")

# Display the image on screen
pil_image.show()
