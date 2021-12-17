import sys


def read_input(file, hex_bin_dict):
    packet = ''
    for line in file:
        for hex in line.rstrip():
            packet += hex_bin_dict[hex]
    return packet


def byte_to_int(byte):
    return eval('0b' + byte)


def parse_packet(packet):
    version = byte_to_int(packet[:3])
    id = byte_to_int(packet[3:6])
    if id == 4:
        more_bits = True
        i = 6
        num = ''
        while more_bits:
            bits = packet[i:i+5]
            if bits[0] == '0':
                more_bits = False
            num += bits[1:]
            i += 5
        num = byte_to_int(num)
        print(num)
        return version
    else:
        ltype = packet[6]
        if ltype == '0':
            length = byte_to_int(packet[7:22])
            subver = None
            subid = None
            subnum = ''
            i = 22
            while i < 22 + length:
                if not subver:
                    subver = byte_to_int(packet[i:i+3])
                    i += 3
                elif not subid:
                    subid = byte_to_int(packet[i:i+3])
                    i += 3
                else:
                    if subid == 4:
                        subnum += packet[i:i+5]
                        i += 5
                        if packet[i] == 0:
                            subver, subid, subnum = None, None, ''
                    else:
                        subltype = packet[i]
                        if subltype == '0':
                            sublen = byte_to_int(packet[i:i+15])
                            i += 15
                            parse_packet(packet[i:i+sublen])
                            i += sublen
                        else:
                            subcount = byte_to_int(packet[i:i+11])
                            i += 11
                            subread = 0
                            while subread < subcount:
                                packstart = i
                                packver = byte_to_int(packet[i:i+3])
                                i += 3
                                packid = byte_to_int(packet[i:i+3])
                                i += 3
                                if pack
        else:
            pass


def main():
    hex_bin_dict = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'
        }
    packet = read_input(sys.stdin, hex_bin_dict)
    print(packet)
    print(parse_packet(packet))


if __name__ == '__main__':
    main()
