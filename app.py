
#!/home/radik1981/Desktop/youtube_down/venv/bin/python3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.layout import Layout



		
class MyApp(App):


	def build(self):
		layout = BoxLayout()
		bt = Button(text='button')
		layout.add_widget(bt)
		bt1 = Button(text='button')
		layout.add_widget(bt1)
		return layout



MyApp().run()
 
