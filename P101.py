import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def uploadFiles(self, fileFrom, fileTo):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(fileFrom):
          print (files)
         relativePath=os.path.relpath(localPath, fileFrom)
         dropboxPath=os.path.join(fileTo, relativePath)
        with open(localPath, "rb") as f:
          dbx.files_upload(f.read(), dropboxPath, mode=WriteMode('overwrite'))

def main():
    access_token="sl.Apb324hyISvU7TKMt8Zywoaxk56tBv4FgNcrjVrQdI4S6FWgp03Qu4v7JJOUh7o81zy9rrGi7MJyS6xVwwdtFy4dsnXO2dYAgWEY6BWrxJ4QnMULio59kDwwgnX4aRNJq33Q6jR9"
    td=TransferData(access_token)
    fileFrom=input("Enter the file path to transfer")
    fileTo=input("Enter the full path to upload the dropbox")
    td.uploadFiles(fileFrom, fileTo)
    print("File has been moved")

if __name__=="__main__":
    main()
