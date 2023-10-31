def camel_case(s):
    words = s.split('_')
    return ''.join(word.capitalize() for word in words)