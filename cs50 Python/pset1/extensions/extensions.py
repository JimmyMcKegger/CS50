# Determines the media type for a file

defaultType = "application/octet-stream"

types = {
  ".gif": "image/gif",
".jpg": "image/jpeg",
".jpeg": "image/jpeg",
".png": "image/png",
".pdf": "application/pdf",
".txt": "text/plain",
".zip": "application/zip"
}

defaultType = "application/octet-stream"

def main():
  f = input("File name: ").strip()
  try:
    dot = f.rindex('.')
    ext = f[dot:].lower()
    print(types.get(ext, defaultType))
  except:
    print(defaultType)

if __name__ == "__main__":
  main()
