from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(App):
        label = Label(text='Hello from kivy, I can be used for web app development',
                        size_hint= (10,10),
                        pos_hint={'center_x': .5, 'center_y': .5})
        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()