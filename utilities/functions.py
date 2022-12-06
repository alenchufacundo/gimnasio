from PIL import ImageTk, Image

def readImage (path,size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

#function for center a window
def centerWindow(window,width,height):    
    widthScreen = window.winfo_screenwidth()
    heightScreen = window.winfo_screenheight()
    x = int((widthScreen/2) - (width/2))
    y = int((heightScreen/2) - (height/2))
    return window.geometry(f"{width}x{height}+{x}+{y}")