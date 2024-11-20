
import json
payload_bytes = b'\x00'
# id
payload_bytes += b'\x00'
payload_bytes += b'\x00'
payload_bytes += b'\x00'
payload_bytes += b'\x01'
prop_int16 = 11
payload_bytes += bytes([prop_int16 // 256])
# print(prop_int16 // 256)
# print(payload_bytes)
# payload_bytes += bytes([prop_int16 % 256])
# print(prop_int16 % 256)
# print(payload_bytes)
# byte转成int。
def bytes_to_int(bytes):
    data = ['%02X' % i for i in bytes]
    return int(''.join(data), 16)



# 8位整型转成byte数组。
def int_8_to_byte(value):
    t_value = '%02X' % value
    if len(t_value) % 2 != 0:
        t_value += '0'

    return hex_string_to_byte_array(t_value)


# 32位整型转成byte数组。
def int_32_to_byte(value):
    t_value = '%08X' % value
    if len(t_value) % 2 != 0:
        t_value += '0'

    return hex_string_to_byte_array(t_value)


# 16位整型转成byte数组。
def int_16_to_byte(value):
    t_value = '%04X' % value
    if len(t_value) % 2 != 0:
        t_value += '0'

    return hex_string_to_byte_array(t_value)


# float转成整型数组。
def float_to_byte(param):
    return hex_string_to_byte_array(struct.pack(">f", param).encode('hex'))


# 16进制字符串转成byte数组。
def hex_string_to_byte_array(str_value):
    if len(str_value) % 2 != 0:
        return None

    cycle = len(str_value) / 2

    pos = 0
    result = []
    for i in range(0, cycle, 1):
        temp_str_value = str_value[pos:pos + 2]
        temp_int_value = int(temp_str_value, base=16)

        result.append(temp_int_value)
        pos += 2
    return result

hx = '5b3232302c2031302c2032362c2033382c20302c20312c20302c20302c20302c20302c20302c20302c20302c20302c20302c20312c20323239382c20302c20302c20302c20323239372c20302c20302c20302c20323239362c20302c20302c20302c20323239362c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c203235362c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20302c20312c2036353439362c2036353439362c2032395d'
print(bytes.fromhex(hx).decode())
print(hex(22))
n = 91
hex_str = hex(n)[2:]  # 移除开头的'0x'
print(hex_str)

n = 255
hex_str = format(n, 'x')
print(hex_str)
print(bytes_to_int(1234))
