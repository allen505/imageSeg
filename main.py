from appJar import gui
from os import listdir,environ
from os.path import isfile, join

START_WINDOW_SIZE="450x150"
TWO_VIEW_WINDOW_SIZE=(800,800)
IMAGE_FRAME_SIZE=(200,200)

selectedImage=""
windowCounter=0

# ─── TO BE CALLED WITH PATH TO THE OUTPUT IMAGE ─────────────────────────────────

def outputImage(path):
    
    app.setImage("Input", path)


# ─── A SAMPLE/DUMMY FUNCTION WHICH IS CALLED WHEN THE PROCESS IMAGE BUTTON IS CALLED 

def dummy(event):
    # ─── selectedImage IS A GLOBAL VARIABLE THAT CAN BE USED TO ACCESS THE NAME OF THE SELECTEDIMAGE 
    print("Dummy called")
    print(selectedImage)


# ────────────────────────────────────────────────────────────────────────────────


def selectImage(event):
    global selectedImage
    selectedImage=(app.getListBox("ListOfImages"))[0]
    app.setImage("Input", selectedImage)

def TwoViewWindow(path):
    windowTitle="Folder View "+str(windowCounter)
    app.startSubWindow(windowTitle, modal=True)    
    app.setSize(TWO_VIEW_WINDOW_SIZE)
    app.setBg("#FFFFFF")
    app.setImageLocation(path)    
    imagesInPath = [f for f in listdir(path) if isfile(join(path, f))]
    
    app.startFrame("LEFT", row=0, column=0)
    app.setSize(IMAGE_FRAME_SIZE)
    app.addImage("Input", None ,compound="bottom")
    app.stopFrame()
    
    app.startFrame("CENTER", row=0, column=1)
    app.addListBox("ListOfImages", imagesInPath)
    app.addButton("Select", selectImage)
    app.addButton("Process Image", dummy)
    app.stopFrame()
    
    app.startFrame("RIGHT", row=0, column=2)
    app.setSize(IMAGE_FRAME_SIZE)
    app.addImage("Output", None,compound="bottom")
    app.stopFrame()    
    
    app.stopSubWindow()
    app.showSubWindow(windowTitle, hide=False)


def StartPress(button):
    if button == "Close":
        app.stop()
    else:
        # print("Opening")
        choosenFolder=app.directoryBox(title="Open Folder", dirName="images/Sample_Images/input")
        TwoViewWindow(choosenFolder)
        

if environ.get('DISPLAY','') == '':
    # print('no display found. Using :0.0')
    environ.__setitem__('DISPLAY', ':0.0')
    

app=gui("Image Segmentation",START_WINDOW_SIZE)
app.addButtons(["Open Folder", "Close"], StartPress)
app.go()