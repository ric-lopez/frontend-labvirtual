import socket

experimentos = {
    "campo_gravitatorio" : "01",
    "polarizacion" : "02",
    "young" : '03',
    "velocidad_instantanea" : "04",
    "fotoelectrico" : '05',
    "tension_superficial" :'06'
}


def send_msg(exp_id, msg):
    print(exp_id, msg)
    print(msg)
    UDP_IP =""
    if(exp_id == '01'):
        UDP_IP = "10.51.82.100"
    elif(exp_id == '03'):
        UDP_IP = "10.51.82.101"
    elif(exp_id == '06'):
        UDP_IP = "10.51.82.102"
    UDP_PORT = 3333

    MESSAGE = bytes(exp_id+msg, "utf-8")
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print("\n\n 1. Client Sent : ", MESSAGE, "\n\n")

    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    print("Hostname: %s" % hostname)
    print("IP Address: %s" % ip_address)
    UDP_IP2 = ip_address
    try:
        sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock2.settimeout(5)
        sock2.bind((UDP_IP2, UDP_PORT))

        data, address = sock2.recvfrom(512)
        print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
        # close the socket
        sock.close()
        sock2.close()
    except:
        return False   
    return True




# def get_idExp():
#      id_experimento = instruction[0:3]
#      print(id_experimento)
#      if(id_experimento == "01"):
