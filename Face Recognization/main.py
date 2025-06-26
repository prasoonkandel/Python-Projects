import cv2
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img_name = "man.png"
img_path = f"./Images/{img_name}"
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imwrite(f"./detected/{img_name}", img)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
