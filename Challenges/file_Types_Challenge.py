#ask the user for the file name 
while True:
    file_name = input("what is your file name? ")

    #convert the file into all uppercase
    file_name = file_name.upper()
    #find the different file types
    if file_name.endswith(".JPEG"):
        print("image/jpeg")
    elif file_name.endswith(".GIF"):
        print("image/gif")
    elif file_name.endswith(".JPG"):
        print("image/jpg")
    elif file_name.endswith(".PNG"):
        print("image/png")
    elif file_name.endswith(".PDF"):
        print("document/pdf")
    elif file_name.endswith(".TXT"):
        print("document/txt")
    elif file_name.endswith(".ZIP"):
        print("file/zip")    
    else:
        print("application/octet-stream")

    #tell what the file type is
