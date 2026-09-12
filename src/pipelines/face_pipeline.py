# import numpy as np
# import dlib
# import face_recognition_models
# from sklearn.svm import SVC
# import streamlit as st

# from src.database.db import get_all_students


# # load your models
# detector = dlib.get_frontal_face_detector()
# sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# #facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
# facerec= dlib.face_recognition_model_v1(
#         face_recognition_models.face_recognition_model_location()
#     )

# @st.cache_resource
# def get_trained_model():
#     X = []
#     y = []
#     student_db = get_all_students()

#     if not student_db:
#         print("DB EMPTY - no students")
#         return None

#     for student in student_db:
#         emb = student.get('face_embedding')
#         if emb and len(emb) > 0:
#             X.append(np.array(emb, dtype=np.float64))
#             y.append(student.get('student_id'))

#     print(f"Loaded {len(X)} embeddings from DB")

#     if len(X) == 0:
#         return None # FIX was return 0

#     if len(X) == 1:
#         # Only 1 student, can't train SVC, return for distance comparison
#         return {'clf': None, 'X': np.array(X), 'y': y}

#     clf = SVC(kernel='linear', probability=True, class_weight='balanced')
#     try:
#         clf.fit(np.array(X), y)
#         return {'clf': clf, 'X': np.array(X), 'y': y} # FIX was missing return
#     except Exception as e:
#         print(f"SVC fit failed: {e}")
#         return {'clf': None, 'X': np.array(X), 'y': y}

# def get_face_embedding(image_np):
#     dets = detector(image_np, 1)
#     if len(dets) == 0:
#         return []
#     # take first face
#     shape = sp(image_np, dets[0])
#     face_descriptor = facerec.compute_face_descriptor(image_np, shape)
#     return [np.array(face_descriptor)]

# def train_classifier():
#     st.cache_resource.clear()
#     model_data= get_trained_model()
#     return bool(model_data)

# def predict_attendance(image_np, threshold=0.6):
#     model_data = get_trained_model()

#     if not model_data:
#         print("No model_data")
#         return {}, [], 0

#     X = model_data['X']
#     y = model_data['y']
#     clf = model_data['clf']

#     encodings = get_face_embedding(image_np)
#     num_faces = len(encodings)

#     print(f"Faces found in query: {num_faces}")

#     detected = {}
#     all_ids = y

#     if num_faces == 0:
#         return {}, all_ids, 0

#     for emb in encodings:
#         # calculate distances to all known faces
#         distances = [np.linalg.norm(emb - x) for x in X]
#         min_dist = min(distances)
#         min_idx = int(np.argmin(distances))
#         pred_id = y[min_idx]

#         print(f"Min distance: {min_dist} for ID {pred_id}, threshold {threshold}")

#         if min_dist < threshold:
#             detected[pred_id] = detected.get(pred_id, 0) + 1
#         # else not recognized

#     return detected, all_ids, num_faces



# import dlib
# import numpy as np
# import face_recognition_models
# from sklearn.svm import SVC
# import streamlit as st

# from src.database.db import get_all_students

# @st.cache_resource         # sirf ek baar load hoga hmare system mein. jisse 
# def load_dlib_models():

#     # Load all the models we need: a detector to find the faces, a shape predictor
#     detector= dlib.get_frontal_face_detector()


#     # to find face landmarks so we can precisely localize the face, and finally the
#     sp= dlib.shape_predictor(
#         face_recognition_models.pose_predictor_model_location()
#     )

#     # face recognition model.
#     facerec= dlib.face_recognition_model_v1(
#         face_recognition_models.face_recognition_model_location()
#     )

#     return detector, sp, facerec

# def get_face_embedding(image_np):
#     detector, sp, facerec= load_dlib_models()
#     faces= detector(image_np, 1)

#     encodings=[]

#     for face in faces:
#         shape= sp(image_np, face)
#         face_descriptor= facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

#         encodings.append(np.array(face_descriptor))
#     return encodings

# @st.cache_resource   
# def get_trained_model():
#     X= []
#     y= []

#     student_db= get_all_students()

#     if not student_db:
#         return None

#     for student in student_db:
#         embedding= student.get('face_embedding')
#         if embedding:
#             X.append(np.array(embedding))
#             y.append(student.get('student_id'))

#     if len(X)==0:
#         return 0

#     clf= SVC(kernel='linear', probability=True, class_weight= 'balanced')

#     try:
#         clf.fit(X,y)
#     except ValueError:
#         pass

# def train_classifier():
#     st.cache_resource.clear()
#     model_data= get_trained_model()
#     return bool(model_data)

# def predict_attendance(class_image_np):
#     encodings= get_face_embedding(class_image_np)

#     detected_student={}

#     model_data= get_trained_model()

#     if not model_data:
#         return detected_student, [], len(encodings)

#     clf= model_data['clf']
#     X_train= model_data['X']
#     y_train= model_data['y']

#     all_students= sorted(list(set(y_train)))

#     for encoding in encodings:
#         if len(all_students)>=2:
#             predicted_id= int(clf.predict([encoding])[0])

#         else:
#             predicted_id= int(all_students[0])

#         student_embedding= X_train[y_train.index(predicted_id)]

#         best_match_score= np.linalg.norm(student_embedding-encoding)

#         resemblance_threshold= 0.6

#         if resemblance_threshold >=best_match_score:
#             detected_student[predicted_id]= True

#     return detected_student, all_students, len(encoding)



import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector() 


    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec

def get_face_embedding(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)

    encodings= []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    X = []
    y = []


    student_db = get_all_students()

    if not student_db:
        return None
    
    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))

    if len(X) ==0:
        return 0
    
    clf = SVC(kernel='linear', probability=True, class_weight='balanced')

    try:
        clf.fit(X, y)
    except ValueError:
        pass

    return {'clf': clf, 'X':X, "y":y}


def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embedding(class_image_np)

    detected_student = {}


    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)
    
    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if len(all_students)>= 2:
            predicted_id= int(clf.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)]

        best_match_score = np.linalg.norm(student_embedding - encoding)

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True
    return detected_student, all_students, len(encodings)
