import pywhatkit as kit

# you need to open whatsapp web to send message from your main browser

try:
    country_code = int(input("Enter your country code (e.g: +90 [Turkey])\n>"))
    phone_number = int(input("Enter the phone number (e.g: 5393958530)\n>"))
    message = str(input("Enter message you want to send\n>"))
    hour = int(input("Enter the hour you want to send the message (e.g: 12)\n>"))
    minute = int(input("Enter the minute you want to send the message (e.g: 54)\n>"))
    print("Inputs taken successfully\n")
except:
    print("Error occurred while taking inputs...")

try:
    kit.sendwhatmsg(f"+{country_code}{phone_number}", f"{message}", hour, minute, wait_time=0)
except:
    print("Error occurred while sending the message...")