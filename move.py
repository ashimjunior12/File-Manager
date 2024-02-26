import os, shutil

fileExtension = input("Enter file Extension: ");
currentDircetory = os.getcwd()

videoDirectory = os.path.join(currentDircetory, "videos")
imageDirectory = os.path.join(currentDircetory, "images")
musicDirectory = os.path.join(currentDircetory, "songs")
pdfDirectory = os.path.join(currentDircetory, "pdf")


def createDirectory(fileExtension):
    if not os.path.exists(videoDirectory):
        os.mkdir(videoDirectory)

    elif not os.path.exists(imageDirectory):
        os.mkdir(imageDirectory)
    
    elif not os.path.exists(musicDirectory):
        os.mkdir(musicDirectory)
    elif not os.path.exists(pdfDirectory):
        os.mkdir(pdfDirectory)


def checkFiles(fileType):
    listOfFiles = os.listdir()
    videoFile = []
    imageFile = []
    songFile = []
    pdfFile = []

    for file in listOfFiles:
        if ".mp4" in file:
            videoFile.append(file)

        elif ".mp3" in file:
            songFile.append(file)

        elif ".pdf" in file:
            pdfFile.append(file)

        elif ".jpg" in file or ".jpeg" in file or ".png" in file:
            imageFile.append(file)
 
    for video in videoFile:
        sourceFile = os.path.join(currentDircetory, video)
        destinationFile = os.path.join(videoDirectory, video)
        
        shutil.move(sourceFile, destinationFile)


    for image in imageFile:
        sourceFile = os.path.join(currentDircetory, image)
        destinationFile = os.path.join(imageDirectory, image)
        
        shutil.move(sourceFile, destinationFile)


    for song in songFile:
        sourceFile = os.path.join(currentDircetory, song)
        destinationFile = os.path.join(musicDirectory, song)
        
        shutil.move(sourceFile, destinationFile)

    for pdf in pdfFile:
        sourceFile = os.path.join(currentDircetory, pdf)
        destinationFile = os.path.join(pdfDirectory, pdf)
        
        shutil.move(sourceFile, destinationFile)



createDirectory(fileExtension)
checkFiles(fileExtension)