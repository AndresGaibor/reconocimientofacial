# detector.py

from collections import Counter
from pathlib import Path
import pickle

from PIL import Image, ImageDraw
import face_recognition

import base64
from io import BytesIO
import numpy as np


BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"

DEFAULT_ENCODINGS_PATH = Path("output/encodings.pkl")

Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)

def encode_known_faces(
    model: str = "hog", encodings_location: Path = DEFAULT_ENCODINGS_PATH
) -> None:
    names = []
    encodings = []
    for filepath in Path("training").glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)
    name_encodings = {"names": names, "encodings": encodings}
    with encodings_location.open(mode="wb") as f:
        pickle.dump(name_encodings, f)

encode_known_faces()
        
def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding
    )
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    if votes:
        return votes.most_common(1)[0][0]
    
def recognize_faces(
    image_location: str,
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> None:
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)

    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )

    for _, unknown_encoding in zip(
        input_face_locations, input_face_encodings
    ):
        name = _recognize_face(unknown_encoding, loaded_encodings)

        if not name:
            name = "Unknown"
        return name
    return "Unknown"

def recognize_faces_base64(image_base64, model='hog', encodings_location=DEFAULT_ENCODINGS_PATH):
    # Decodifica la imagen base64 y la convierte en una imagen PIL
    image_data = base64.b64decode(image_base64)
    image = Image.open(BytesIO(image_data))
    
    # Convierte la imagen PIL a un array numpy para face_recognition
    np_image = np.array(image)

    # Carga las codificaciones conocidas
    with encodings_location.open(mode='rb') as f:
        loaded_encodings = pickle.load(f)

    # Encuentra las ubicaciones de las caras y sus codificaciones en la imagen
    face_locations = face_recognition.face_locations(np_image, model=model)
    face_encodings = face_recognition.face_encodings(np_image, face_locations)

    # Reconoce las caras
    namefound = "No reconocido"
    for unknown_encoding in face_encodings:
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if name:
            namefound = name;
            

    # Si no se encuentra ninguna cara, retorna 'Unknown'
    print("Consulta de ", namefound);
    
    return namefound


def validate(model: str = "hog"):
    for filepath in Path("validation").rglob("*"):
        if filepath.is_file():
            recognize_faces(
                image_location=str(filepath.absolute()), model=model
            )

# validate()
resultado = recognize_faces("unknown3.jpeg")
print(resultado);
# resultado = recognize_faces_base64("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")
# print(resultado)

# from typing import Union

# from fastapi import FastAPI