from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class NIKOApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        self.layout.add_widget(Label(text="NIKO - مساعد كريمة\nفابور - 5 لغات - كيتصل", font_size='16sp', size_hint_y=0.15))
        self.chat = TextInput(text="NIKO: سلام كريمة! أنا واجد ❤️\nكتبي: اتصل بفاطمة / عقل على...\n", readonly=True, size_hint_y=0.6)
        self.layout.add_widget(self.chat)
        self.input = TextInput(hint_text="مثلا: اتصل بفاطمة", size_hint_y=0.1, multiline=False)
        self.input.bind(on_text_validate=self.send)
        self.layout.add_widget(self.input)
        btns = BoxLayout(size_hint_y=0.15, spacing=8)
        btns.add_widget(Button(text="صيفط", on_press=self.send))
        btns.add_widget(Button(text="📞 اتصل بفاطمة", on_press=self.call_fatima))
        self.layout.add_widget(btns)
        return self.layout

    def send(self, *args):
        t = self.input.text.strip()
        if not t: return
        self.chat.text += f"\nكريمة: {t}\n"
        self.input.text = ""
        if "اتصل" in t: r = f"واخا كنتصل بـ {t.replace('اتصل ب','')}"
        elif "عقل" in t: r = f"عقلت على: {t}"
        elif "تركية" in t: r = "Merhaba Karima, ben NIKO"
        elif "فرنسية" in t: r = "Bonjour Karima, c'est NIKO"
        elif "انجليزية" in t: r = "Hello Karima, it's NIKO"
        else: r = f"سمعتك كريمة: {t} - أنا معاك"
        self.chat.text += f"NIKO: {r}\n"
        self.speak(r)

    def speak(self, text):
        try:
            from jnius import autoclass
            print(f"NIKO يقول: {text}")
        except: print(text)

    def call_fatima(self, *args):
        try:
            from jnius import autoclass
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            act = autoclass('org.kivy.android.PythonActivity').mActivity
            i = Intent()
            i.setAction(Intent.ACTION_CALL)
            i.setData(Uri.parse("tel:0612345678"))
            act.startActivity(i)
            self.chat.text += "\n[كنتصل بفاطمة...]\n"
        except:
            self.chat.text += "\n[فالتيليفون الحقيقي غادي يتصل بفاطمة]\n"

NIKOApp().run()
