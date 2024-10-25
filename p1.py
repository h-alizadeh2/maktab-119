# from os.path import split


class add():
    def __init__(self, string):
       self.string = string

    def __add__(self, others):
        a = self.string
        b = others.string
        c=""
        for i in range(max(len(a),len(b))):
            if i < len(a):
                c += a[i]
            if i < len(b):
                c += b[i]

        return add(c)

    # ترکیب با map و zip


    def __str__(self):
        return self.string

# a='abcd'
# b='xyz'
# z=''
obj1=add('salam')
obj2=add('chetori')
result = obj1 + obj2
print(result)