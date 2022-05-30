def get_class_name(x):    
    return (type(x)).__name__

print(get_class_name(235235235))
print(get_class_name(1.4))
print(get_class_name(True))
print(get_class_name('aasasfa'))
print(get_class_name(None))
print(get_class_name(['a', 'v']))
