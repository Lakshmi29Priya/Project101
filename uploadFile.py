import dropbox
class TransferData:
      def __init__(self,access_token):
          self.access_token=access_token

      def upload_file(self,file_from,file_to):
          dbx=dropbox.Dropbox(self.access_token)

          f=open(file_from,'rb')
          dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.AxfS2DQKWqU-mFA2iSxMHhFGYptJ3kLyeDBwTVEItuViDZ5qsNKChh6hoM--SzVPeEn39iumaRs0OoMepO8GGke97_ytINUriutDb3mRTcU8LM1v1V4BI5zB3qh5XhPGKoAlK1M'
    transferData=TransferData(access_token)

    file_from=input("Enter the name of the file")
    file_to=input("Enter the path of the file")

    transferData.upload_file(file_from,file_to)
    print("the file has been moved")

main()

     
