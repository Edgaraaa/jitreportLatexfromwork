from PIL import Image
import os
def file_name_listdir(file_dir):
    for files in os.listdir(file_dir+"\\img"):
        print("files", files)
        file_name=file_dir+"\\img\\"+files
        a=Image.open(file_name)
        width=(a.size[0])/100
        height=(a.size[1])/100
        print(width)
        print(height)
        file=open(file_dir+"\pic.txt","ab+")
        pics="\\center{{\\includegraphics[width="+str(width)+"cm,height="+str(height)+"cm]  {img/"+files+"}}\\\\ \\songti\\wuhao{图 } }\\\\ \n"
        file.write("\\end{flushleft}\n".encode('utf-8'))
        file.write(pics.encode('utf-8'))
        file.write("\\begin{flushleft}\n".encode('utf-8'))

#file_name_walk('C:\\Users\\lenovo\\Desktop\\实验报告和作业集合\\网络编程\\jitreportLatexfromwork')
file_name_listdir("C:\\Users\\lenovo\\Desktop\\实验报告和作业集合\\网络编程\\jitreportLatexfromwork")