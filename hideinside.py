import cv2
import numpy as np
from bitarray import bitarray


def get_img():
    img = cv2.imread('test.jpg')
    img = np.array(img, dtype=np.uint8)
    return img


def turn_bits(inf='I made it'):
    ret = bitarray(''.join([bin(int('1' + hex(c)[2:], 16))[3:] for c in inf.encode('utf-8')]))
    return ret


def encodeimg(img, bits):
    shape = img.shape
    img = np.reshape(img, (-1))
    for index, ele in enumerate(img):
        if index >= len(bits):
            break
        if ele == 255 or ele == 0:
            continue
        if bits[index]:
            img[index] += 1
        else:
            img[index] -= 1
    img = np.reshape(img, shape)
    return img


def decodeimg(orimg, img):
    if orimg.shape == img.shape:
        shape = orimg.shape
        orimg = np.reshape(orimg, (-1))
        img = np.reshape(img, (-1))
        bits = bitarray()
        for index, ele in enumerate(orimg):
            if ele == 255 or ele == 0:
                continue
            flag = int(ele) - int(img[index])
            if flag == -1:
                bits.append(True)
            elif flag == 1:
                bits.append(False)
            else:
                break
        orimg = np.reshape(orimg, shape)
        img = np.reshape(img, shape)
        print('extract '+str(len(bits))+' bits information')
        inf = bits.tobytes()
        return inf


if __name__ == '__main__':
    origin_img = get_img()
    bit_stream = turn_bits()
    encode_img = encodeimg(origin_img, bit_stream)
    cv2.imwrite('encode_img.jpg', encode_img)
    origin_img = get_img()
    information = decodeimg(origin_img, encode_img)
    print(information)
