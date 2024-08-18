import struct

ball_file = open('ball.bmp', 'rb')
ball_data = ball_file.read()
ball_file.close()

# this is for testing with the pixels of the image
amount = 5000

#bmp image gile format stores location
#of pixel rgb values n bytes 10-14
pixel_data_loc = ball_data[10:14]
print("pixel_data_loc: {}".format(pixel_data_loc))

# converts byte sequence into integer object
pixel_data_loc = struct.unpack('<L',pixel_data_loc)[0]
print("pixel_data_loc after the struct: {}".format(pixel_data_loc))

#create sequence of 3000 red, green, and yellow pixels each
new_pixels = b'\x01'*amount + b'\x02'*amount + b'\x03'*amount

# create sequence of 3000 blue, black, and orange pixels each
# new_pixels = b'\xFF\x00\x00'*amount + b'\x00\x00\x00'*amount + b'\x00\xA5\xFF'*amount

#overwrite pixels in image with new pixels
new_ball_data = ball_data[:pixel_data_loc] + \
                new_pixels + \
                ball_data[pixel_data_loc + len(new_pixels):]


#write new image
new_ball_file = open('new_ball.bmp', 'wb')
new_ball_file.write(new_ball_data)
new_ball_file.close()

print('Result of packing 5:', end=' ')
print(struct.pack('>h', 5))

print('Result of packing 256:', end=' ')
print(struct.pack('>h', 256))

print('Result of packing 5 and 256:', end=' ')
print(struct.pack('>hh', 5, 256))

print('Result of unpacking {}:'.format(repr('\x00\x05')), end=' ')
print(struct.unpack('>h', b'\x00\x05'))


print('Result of unpacking {}:'.format(repr('\x01\x00')), end=' ')
print(struct.unpack('>h', b'\x01\x00'))

print('Result of unpacking {}:'.format(repr('\x00\x05\x01\x00')), end=' ')
print(struct.unpack('>hh', b'\x00\x05\x01\x00'))
