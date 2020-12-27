# Copy paste the Following code in Google Colab
!pip install face_recognition
import face_recognition
import PIL.Image
import PIL.ImageDraw
from google.colab import files
uploaded = files.upload()
import json 
import math

# Added Functions
def dist(val1,val2):
  a1,a2 = val1
  b1,b2 = val2
  len = math.sqrt((a1-b1)**2 + (a2-b2)**2)
  return len

def Golden(x,y):
  Max = max(x,y)
  return (x+y)/Max

def Mean(A,B):
  x1,y1 = A
  x2,y2 = B
  val =((x1+x2)/2,(y1+y2)/2)
  return val

arr_upload = list(uploaded.items())
input_image = face_recognition.load_image_file(arr_upload[0][0])
face_landmarks = face_recognition.face_landmarks(input_image)
print(face_landmarks[0])
output_image = PIL.Image.fromarray(input_image)
draw = PIL.ImageDraw.Draw(output_image)

chin = face_landmarks[0].get('chin')
left_eyebrow = face_landmarks[0].get('left_eyebrow')
right_eyebrow = face_landmarks[0].get('right_eyebrow')
left_eye = face_landmarks[0].get('left_eye')
right_eye = face_landmarks[0].get('right_eye')
nose_bridge = face_landmarks[0].get('nose_bridge')
nose_tip = face_landmarks[0].get('nose_tip')
top_lip = face_landmarks[0].get('top_lip')
bottom_lip = face_landmarks[0].get('bottom_lip') 

face_mask = chin + left_eyebrow + right_eyebrow  + nose_bridge + nose_tip + left_eye + right_eye + top_lip + bottom_lip

#print(landmark)
for loc in face_mask:
  x,y = loc
  draw.rectangle((x,y,x+2,y+2),outline='red')

print('\n\n')

arc_eyebrow = Mean(face_mask[19],face_mask[24])
upper_lip = face_mask[51]
bottom_lip = face_mask[63]
center_of_lip = Mean(face_mask[57],face_mask[69])
nostril_top = Mean(face_mask[31],face_mask[35])

m1 = Mean(face_mask[37],face_mask[38])
m2 = Mean(face_mask[43],face_mask[44])
eye_top = Mean(m1,m2)

m1 = Mean(face_mask[41],face_mask[40])
m2 = Mean(face_mask[47],face_mask[46])
eye_bottom = Mean(m1,m2)

# #print(center_of_lip)
# x,y = eye_top
# draw.rectangle((x,y,x+2,y+2),outline='blue')

# x,y = eye_bottom
# draw.rectangle((x,y,x+2,y+2),outline='white')

## ============================================================================================
print('Face Beauty Identification w.r.t Golden Number(phi = 1.618) \n\n')
print('Vertical Golden Ratio Calculation \n\n')

# Golden Ratio -1 (Giving Inaccurate Results)
d1 = dist(face_mask[27],face_mask[30])
d2 = dist(face_mask[30],face_mask[33])
gr1 = Golden(d1,d2)
print(f'Eyes to Nose_Flair to Nose_base = {gr1}')
index = (gr1/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')

# Golden Ratio -2
d1 = dist(face_mask[27],nostril_top)
d2 = dist(nostril_top,center_of_lip)
gr2 = Golden(d1,d2)
print(f'Eyes to Nostril_top to center_of_lip = {gr2}')
index = (gr2/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')

# Golden Ratio -3 (Giving inaccurate results)
d1 = dist(face_mask[27],face_mask[33])
d2 = dist(face_mask[33],face_mask[57])
gr3 = Golden(d1,d2)
print(f'Eyes to Nose_Base to Bottom of Lips = {gr3}')
index = (gr3/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')


# Golden Ratio -4
d1 = dist(face_mask[27],center_of_lip)
d2 = dist(center_of_lip,face_mask[8])
gr4 = Golden(d1,d2)
print(f'Eyes to Center of Lips to Bottom of chin = {gr4}')
index = (gr4/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')

# Golden Ratio -5
d1 = dist(face_mask[30],bottom_lip)
d2 = dist(bottom_lip,face_mask[8])
gr5 = Golden(d1,d2)
print(f'Nose Flair to bottom of Lips to Bottom of chin = {gr5}')
index = (gr5/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')

# Golden Ratio -6
d1 = dist(face_mask[30],upper_lip)
d2 = dist(upper_lip,face_mask[8])
gr6 = Golden(d1,d2)
print(f'Nose Flair to Top of Lips to Bottom of chin = {gr6}')
index = (gr6/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')

# Golden Ratio -7
d1 = dist(arc_eyebrow,eye_top)
d2 = dist(eye_top,eye_bottom)
gr7 = Golden(d1,d2)
print(f'Arc of Eyebrow to Top of Eye to Bottom of Eye = {gr7}')
index = (gr7/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')

# Golden Ratio -8
d1 = dist(upper_lip,bottom_lip)
d2 = dist(bottom_lip,face_mask[8])
gr8 = Golden(d1,d2)
print(f'Top of Lips to Bottom of Lips to Bottom of Chin = {gr8}')
index = (gr8/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')

# Golden Ratio -9
d1 = dist(upper_lip,center_of_lip)
d2 = dist(center_of_lip,bottom_lip)
gr9 = Golden(d1,d2)
print(f'Top of Lips to Center of Lips to Bottom of Lips= {gr9}')
index = (gr9/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')

# Golden Ratio -10
d1 = dist(arc_eyebrow,upper_lip)
d2 = dist(upper_lip,face_mask[8])
gr10 = Golden(d1,d2)
print(f'Arc of Eyebrows to Top of Lips to Bottom of Chin = {gr10}')
index = (gr10/1.618)*100
print(f'Beauty Index(%) = {index}\n\n')

#Your final Beauty Score

score = (gr1-1.618)**2 + (gr2-1.618)**2 + (gr3-1.618)**2 + (gr4-1.618)**2 + (gr5-1.618)**2 + (gr6-1.618)**2 + (gr7-1.618)**2 + (gr8-1.618)**2 + (gr9-1.618)**2 + (gr10-1.618)**2 
standard_deviation = math.sqrt(score/8)
# print(standard_deviation)
final_score = ((1.618-standard_deviation)*100)/1.618
print(f'\n\n FINAL BEAUTY SCORE(%) = {final_score}\n\n')

# Your Image 
display(output_image)


