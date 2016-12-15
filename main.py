from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class RootWidget(Widget):
    pass


class AwesomeButton(Button):
    input_text = ObjectProperty(None)
    output_label = ObjectProperty(None)
    lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']


    def on_press(self):
        sentence = self.input_text.text
        sentence = sentence.split()
        for k in range(len(sentence)):
            i = sentence[k]
            if i[0] in ['a', 'e', 'i', 'o', 'u']:
                sentence[k] = i + 'ay'
            elif self.t(i) in self.lst:
                sentence[k] = i[2:] + i[:2] + 'ay'
            elif i.isalpha() == False:
                sentence[k] = i
            else:
                sentence[k] = i[1:] + i[0] + 'ay'
        self.output_label.text = ' '.join(sentence)

    def t(self, str):
        return str[0]+str[1]


class IntroApp(App):
    def build(self):
        root = RootWidget()
        return root

if __name__ == '__main__':
    IntroApp().run()



