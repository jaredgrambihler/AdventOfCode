from __future__ import annotations
from dataclasses import dataclass

with open("2021/input/day16input.txt") as f:
    input_text = f.read().strip()

hex_to_bits = {
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

# input_text = "9C0141080250320F1802104A08"

@dataclass
class Packet:
    version: int
    type_id: int
    value: int
    sub_packets: list[Packet]

def input_to_binary(input_str):
    binary = []
    for c in input_str:
        bit_str = hex_to_bits[c]
        for bit in bit_str:
            binary.append(bit)
    return binary


def get_number(bits):
    val = 0
    bit_val = 1
    for bit in reversed(bits):
        if bit == '1':
            val += bit_val
        bit_val  *= 2
    return val


def get_value(type_id, sub_packets):
    if type_id == 0:
        return sum(x.value for x in sub_packets)
    elif type_id == 1:
        val = 1
        for packet in sub_packets:
            val *= packet.value
        return val
    elif type_id == 2:
        return min(x.value for x in sub_packets)
    elif type_id == 3:
        return max(x.value for x in sub_packets)
    elif type_id == 5:
        if sub_packets[0].value > sub_packets[1].value:
            return 1
        else:
            return 0
    elif type_id == 6:
        if sub_packets[0].value < sub_packets[1].value:
            return 1
        else:
            return 0
    elif type_id == 7:
        if sub_packets[0].value == sub_packets[1].value:
            return 1
        else:
            return 0
    print(f"Unknown type id {type_id}")
    return 0


def get_packets(binary):
    packets = []
    # when we have a subpacket that is collecting subpackets, track number to collect with this counter
    num_subpackets_remaining = []
    num_subpackets = []
    while len(binary) > 6:
        version = get_number(binary[:3])
        type_id = get_number(binary[3:6])
        if type_id == 4:
            # number
            index = 6
            ended = False
            value_bits = []
            while not ended:
                cur_bits = binary[index: index + 5]
                index += 5
                if cur_bits[0] == '0':
                    ended = True
                for bit in cur_bits[1:]:
                    value_bits.append(bit)
            binary = binary[index:]
            packets.append(Packet(version=version, type_id=type_id, value = get_number(value_bits), sub_packets=[]))
        else:
            # not a number, get the length_type_id
            length_type_id = binary[6]
            if length_type_id == '0':
                packet_length_bits = get_number(binary[7:7 + 15])
                sub_packets = get_packets(binary[7+15: 7 + 15 + packet_length_bits])
                value = get_value(type_id, sub_packets)
                packets.append(Packet(version = version, type_id = type_id, value = value, sub_packets = sub_packets))
                binary = binary[ 7 + 15 + packet_length_bits:]
            else:
                num_subpackets.append(get_number(binary[7:7+11]))
                binary = binary[7+11:]
                num_subpackets_remaining.append(num_subpackets[-1] + 1) # increment by one so first packet is counted
                # add placeholder packet
                packets.append(Packet(version = version, type_id = type_id, value = 0, sub_packets = []))
        if len(num_subpackets_remaining) > 0:
            num_subpackets_remaining[-1] -= 1
            if num_subpackets_remaining[-1] == 0:
                # reached end of subpackets, append it
                sub_packets = packets[-num_subpackets[-1]:]
                packets = packets[:-num_subpackets[-1]]
                num_subpackets_remaining.pop()
                num_subpackets.pop()
                value = get_value(packets[-1].type_id, sub_packets)
                packets[-1].value = value
                packets[-1].sub_packets = sub_packets
    return packets


def get_versions_from_packets(packets):
    versions = []
    for packet in packets:
        versions.append(packet.version)
        versions.extend(get_versions_from_packets(packet.sub_packets))
    return versions


def get_versions(input_str):
    binary = input_to_binary(input_str)
    return get_versions_from_packets(get_packets(binary))

def evaluate(input_str):
    binary = input_to_binary(input_str)
    packets = get_packets(binary)
    return packets[0].value

print("Part 1")
print(f"Sum of versions: {sum(get_versions(input_text))}")
print("Part 2")
print(f"Value: {evaluate(input_text)}")
