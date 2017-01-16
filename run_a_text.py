from tkinter import *
import os
from tkinter import filedialog

#http://www.cnblogs.com/kongzhagen/p/6148737.html 关于tkinter菜单
'''
#注意Tkinter出错，在python3种大部门模块已经是小写开头了
root = Tk()

#label = Label(root,bitmap='error')
label = Label(root,fg='red',bg='blue',text = 'Hello Tkinter')
#pack（）是用来管理和显示组件的，它的参数我们以后再说。
label.pack()
root.title('记事本')
root.mainloop()
'''

def die():
	root.destroy()
	 
class Create: 
	def __init__(self,root):
		self.root=(root) 
	  
		self.menubar=Menu(root)  
		
		self.filemenu = Menu(self.menubar, tearoff=0)  
	 
		self.textpad = Text(root)
		self.textpad.pack(expand=YES,fill=BOTH)
	
		self.filemenu=Menu(self.menubar,tearoff=0)  
		self.filemenu.add_command(label="新建",accelerator="Ctrl+N")  
		self.filemenu.add_command(label="打开",command=self.openfile)  
		self.filemenu.add_separator()  
		self.filemenu.add_command(label="保存",command=self.save)
		self.filemenu.add_command(label="另存为",command=self.donothing)  
		self.filemenu.add_separator()  
		self.filemenu.add_command(label="页面设置",accelerator="U",command=self.donothing)  
		self.filemenu.add_command(label="打印",accelerator="Ctrl+P",command=self.donothing)  
		self.filemenu.add_separator()  
		self.filemenu.add_command(label="退出",accelerator="X",command=die)  
		self.menubar.add_cascade(label="文件",menu=self.filemenu)  
		
		self.editmenu = Menu(self.menubar, tearoff=0)  
		self.editmenu.add_command(label="Undo", command=self.donothing)  
		self.editmenu.add_command(label="Cut", command=self.donothing)  
		self.editmenu.add_command(label="Copy", command=self.donothing)  
		self.menubar.add_cascade(label="edit",menu=self.editmenu)

		  
		self.helpmenu = Menu(self.menubar, tearoff=0)  
		self.helpmenu.add_command(label="Help Index", command=self.donothing)  
		self.helpmenu.add_command(label="About...", command=self.donothing)  
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)  
		
		self.root.config(menu=self.menubar)  
		  

	def donothing(self):  
		filewin=Toplevel(self.root)  
		button=Button(filewin,text="hi，添加你的代码")  
		button.pack() 
	def openfile(self):
		
		filename = filedialog.askopenfilename(title = "打开",filetypes = [("文件","*.txt")])
		if filename == '':
			filename = None
		else:
			root.title('FileName:'+os.path.basename(filename))
			self.textpad.delete(1.0,END)
			f = open(filename,'r+')
			self.textpad.insert(1.0,f.read())
			f.close()
	#保存
	def save(self):
		sname = filedialog.asksaveasfilename(title = "保存",filetypes = [("保存文件","*.txt")])

		f = open(sname,'w+')
		msg = self.textpad.get(1.0,END)
		f.write(msg)
		f.close()

	
	
if __name__ == "__main__":  
	root = Tk()
	root.title('记事本')
	root.geometry("800x500")
	window = Create(root)
	root.mainloop()