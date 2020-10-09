class Button:
    def __init__(self, fn):
        self.fn = fn

    def click(self):
        self.fn()


def test(string):
    print(string)


fn = lambda: test('Pesho')
button_1 = Button(fn)
button_1.click()
button_1.click()
button_2 = Button(lambda: test('Toto'))
button_2.click()
