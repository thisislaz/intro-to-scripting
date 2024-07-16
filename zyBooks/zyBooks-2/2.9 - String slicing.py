# my_str = "The cat jumped the brown cow"
# animal = my_str[4:7]
# print('The animal is a {}'.format(animal))
#
# my_str = 'The fox jumped the brown llama'
# print('The animal is still a', animal)  # animal variable remains unchanged.
#
# usr_text = input('Enter a string: ')
# print()
#
# first_half = usr_text[:len(usr_text)//2]
# last_half = usr_text[len(usr_text)//2:]
#
# print('The first half of the string is "{}"'.format(first_half))
# print('The second half of the string is "{}"'.format(last_half))

my_str = 'http://reddit.com/r/python'
print(my_str[17:])

my_str = 'http://reddit.com/r/python'
protocol = 'http://'
print(my_str[len(protocol):])

my_str = 'Agt2t3afc2kjMhagrds!'
print(my_str[0:5:1])

my_str = 'Agt2t3afc2kjMhagrds!'
print(my_str[::2])

start_index = int(input())
end_index = int(input())
rhyme_lyric = 'The cow jumped over the moon.'
sub_lyric = rhyme_lyric[start_index:end_index]
print(sub_lyric)