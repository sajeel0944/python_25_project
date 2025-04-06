import qrcode

def qrcode_convert(url:str):
    qr = qrcode.QRCode(
        version=1,   
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,  
        border=4, 
    )    

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qrcode.png")
    img.show()


def main():
    print("\n\t\tURL Convert Into Qr code")

    user_url= input("\nEnter Your Url : ")

    if user_url == "":
        print("Please Enter Your URL")
    else:
        qrcode_convert(user_url)


if __name__ in "__main__":
    main()
