path = "Images/" 

if ['.gif', '.png', '.jpg', '.jfif']:
  file_name = path+"/"+file

size = (width,height)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*DIVX),0.8, size)





