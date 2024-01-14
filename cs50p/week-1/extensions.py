def main():
    file = input("What's the filename? ").strip().lower()
    filename, extension = file.rsplit(".", 1)
    match extension:
        case "gif":
            print("MIME type: image/gif")
        case "jpeg":
            print("MIME type: image/jpeg")
        case "jpg":
            print("MIME type: image/jpeg")
        case "png":
            print("MIME type: image/png")
        case "pdf":
            print("MIME type: application/pdf")
        case "txt":
            print("MIME type: text/plain")
        case "zip":
            print("MIME type: application.zip")
        case _:
            print("MIME type: application/octet-stream")

main()
