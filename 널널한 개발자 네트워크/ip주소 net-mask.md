ip주소 net-mask

ip = internet protocol (인터넷 통신 규칙)

ip address =ipv4: 32bit  구분자 = . 8bit씩 끊어서 표시 최대: 2^32 ==? 43억
            ipv6: 128bit 구분자 = :

192.168.60.14

128 = 1000 0000 =>
      B    0
192 = 1100 0000 =>
      C    0

netmask 255.255.255.0 일시, (1111 1111 1111 1111 1111 1111 0000 0000)
network ID host ID
192.168.60 14

cidr 표기 : 192.168.60.14/24
