def download_complete():
    print("Download Finished!")

def download_file(callback):
    print("Downloading file...")
    callback()

download_file(download_complete)