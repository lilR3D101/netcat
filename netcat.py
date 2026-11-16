#!/usr/bin/env python3
import socket
import sys
import datetime

def log_connection(addr):
	current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	log_message = f"[+]connection  from {addr[0]} at {current_time}\n"

	with open("connection_log.txt", "a") as log_file:

		log_file.write(log_message)

def start_listener(port):
#القاعده  الاولي  فتح المنفذ (نضع المقبس tcp)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#القاعده الثانيه  الاستماع والانتظار (الجلوس والانتظار شخص ما )وظيفته نحدد رقم    الغرفهاورقمالشقهوليكن مثلا 5555
#ونقول للباب افتح للجميع  وليكن مثلا (0.0.0.0)
#القانون الثاني  تحديد مكان البوابه والانتظار 
#نربط الخادم  بكل الاجهزه علي المنفذ 5555
	server.bind(("0.0.0.0", 5555))

#
#اجلس وانتظر اتصالا واحدا فقط
	server.listen(1)
	print("[*]5555 انا استمع الان علي المنفذ ....")

#القاعده الثالثه التفاعل والتنفيذ  استقبال الطلب وتنفيذ المطاوب وارصسال الرد 
#عندما يتصل الشخص خد بياناته في متغيرين (كابل الاتصال والعنوان )
	client_socket, addr = server.accept()
	print(F"[+]اتصل بجهاز من العنوان ياله من روعه {addr}")

#استدعاء داله التوثيق فور الاتصلال 
	log_connection(addr)

#فور اتصاله تقول له ارسالللعميل رساله ترحيب 
#"welcome to my custom Netcat!\n"
#تلوين  رساله الترحيب 
	client_socket.send(b"\033[95m[+] welcome to my custom Netcat!\033[0m\n")


if __name__ == "__main__":
	start_listener(5555)
