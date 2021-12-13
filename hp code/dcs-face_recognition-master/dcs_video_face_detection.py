import sys
import os
import face_recognition
import cv2

# Location where known images are kept
KNOWN_FACES_DIR = "./images/known-faces"

video_location = sys.argv[1]

MODEL = "hog"
TOLERANCE = 0.45

# Object for known people name and their sample images
known_faces_encodings_by_person = {}

# Processing Known Images
print("Processing Known Images...")
for name in os.listdir(KNOWN_FACES_DIR):
    for sample in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        sample_image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{sample}")
        # All known images should be single face image
        sample_encoding = face_recognition.face_encodings(sample_image)[0]
        if(name not in known_faces_encodings_by_person):
            known_faces_encodings_by_person[name] = []
        known_faces_encodings_by_person[name].append(sample_encoding)

#load the surveillance video
video = cv2.VideoCapture(video_location)

known_person_found = []
while len(known_faces_encodings_by_person) > 0:
    ret, frame = video.read()
    if (ret):
        frame_faces_locations = face_recognition.face_locations(frame, model=MODEL)
        frame_faces = face_recognition.face_encodings(frame, frame_faces_locations)

        # finding who all among known person present in a frame of the video
        for frame_face in frame_faces:
            for name, known_face_encodings in known_faces_encodings_by_person.items():
                matches = face_recognition.compare_faces(known_face_encodings, frame_face, TOLERANCE)
                if True in matches:
                    known_person_found.append(name)
                    # as the current iterated frame face matched with one of the known person, we skip matching
                    # the frame face with remaining known person
                    # also we are eliminating the person to be searched for in upcoming iteration
                    del known_faces_encodings_by_person[name]
                    break
    else:
        break

print(known_person_found)

video.release()

if __name__ == "main":
    if len(sys.argv) != 2:
        exit("It takes only one argument: the video file location")
