#%%
def cordenadas(x1,y1,x2,y2):
    print("tempLevel.lines.push(new Line("+str(x1)+","+str(y1)+","+str(x2)+","+str(y1)+"));")
    print("tempLevel.lines.push(new Line("+str(x1)+","+str(y1)+","+str(x1)+","+str(y2)+"));")
    print("tempLevel.lines.push(new Line("+str(x2)+","+str(y1)+","+str(x2)+","+str(y2)+"));")
    print("tempLevel.lines.push(new Line("+str(x1)+","+str(y2)+","+str(x2)+","+str(y2)+"));")



#NIVEL 1
cordenadas(160,253,240,200)
print("  ")
cordenadas(375,85,825,30)
print("  ")
cordenadas(1050,660,1150,615)
print("  ")
cordenadas(880,500,985,455)
print("  ")
cordenadas(1050,327,1150,283)
print("  ")
cordenadas(375,80,835,30)
#%%
#NIVEL 2
cordenadas(0,900,120,800)
print(" ")
cordenadas(50,350,170,280)
print(" ")
cordenadas(450,670,615,570)
print(" ")
cordenadas(510,190,780,85)
print(" ")
cordenadas(1030,900,1200,410)

#%%
#NIVEL 3
cordenadas(15,880,200,840)
print(" ")
cordenadas(265,645,380,270)
print(" ")
cordenadas(205,550,270,490)
print(" ")
cordenadas(265,275,310,0)
print(" ")
cordenadas(0,195,85,135)
print("")
cordenadas(520,555,605,380)
print("")
cordenadas(780,555,870,380)
print("")
cordenadas(1030,555,1125,380)
print("")
cordenadas(780,900,1200,840)

# %%
import cv2
path = "/home/juanchx/Imágenes/fondo2.webp"
#%%
#show the image
img = cv2.imread(path)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
#become red to the image
img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# set green and blue channels to 0
img[:, :, 0] = 0
img[:, :, 1] = 0
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
#save the new image
cv2.imwrite("/home/juanchx/Imágenes/red.jpg",img)
# %%
0