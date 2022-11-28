import sys
from math import prod


def read_input(file, hex_bin_dict):
    packet = ''
    for line in file:
        for hex in line.rstrip():
            packet += hex_bin_dict[hex]
    return packet


def bti(byte):
    return eval('0b' + byte)


def parse_packet(packet, pt, ver_total=0):
    version = bti(packet[pt: pt+3])
    ver_total += version
    pt += 3
    id = bti(packet[pt: pt+3])
    pt += 3
    if id == 4:
        more_bits = True
        num = ''
        while more_bits:
            bits = packet[pt: pt+5]
            pt += 5
            if bits[0] == '0':
                more_bits = False
            num += bits[1:]
        num = bti(num)
        return ver_total, pt, num
    else:
        ltype = packet[pt]
        pt += 1
        nums = []
        if ltype == '0':
            length = bti(packet[pt: pt+15])
            pt += 15
            end = pt + length
            while pt <= end-1:
                ver_total, pt, result = parse_packet(packet, pt, ver_total)
                nums.append(result)
        else:
            total = bti(packet[pt: pt+11])
            pt += 11
            count = 0
            while count <= total-1:
                ver_total, pt, result = parse_packet(packet, pt, ver_total)
                nums.append(result)
                count += 1
        if id == 0:
            result = sum(nums)
        elif id == 1:
            result = prod(nums)
        elif id == 2:
            result = min(nums)
        elif id == 3:
            result = max(nums)
        elif id == 5:
            result = 1 if nums[0] > nums[1] else 0
        elif id == 6:
            result = 1 if nums[0] < nums[1] else 0
        elif id == 7:
            result = 1 if nums[0] == nums[1] else 0
        return ver_total, pt, result
    return ver_total


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
    ver_total, _, result = parse_packet(packet, 0)
    print(ver_total, result)


if __name__ == '__main__':
    main()
