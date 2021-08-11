import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Ax01G_AWunj4p2iBwsVd9oAPr_p4ERZ5hpYVy7I882F4NJg9ssZXmc1lY4eETcH-TaSuTDuIM2d6AJi72kE3Og4KlQ6bYRIgtuNTOKrPu_Tdo0-gQk5YkTlR3byb0lLGOGtP063phos'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test1.txt'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()

