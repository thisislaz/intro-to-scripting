# url = input('Enter URL:\n')
#
# tokens = url.split('/')  # Uses '/' separator
# print(tokens)

# file = 'C:/Users/Charles Xavier//Documents//report.doc'
#
# separator = '/'
# results = file.split(separator)
# print('Separator ({}):'.format(separator), results)

title = 'Python-Lab-Warmup'
tokens = title.split('-')
print(tokens)
title=":".join(tokens)
print(title)

phone_number = input()
number_segments = phone_number.split("-")
area_code = number_segments[0]
print('Area code:', area_code)