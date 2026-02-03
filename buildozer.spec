[app]

# (str) Title of your application
title = Lulucat Bomber

# (str) Package name
package.name = lulucatbomber

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 0.1

# (list) Application requirements
# requests နဲ့ openssl ကို ထည့်ပေးထားလို့ အင်တာနက်ကနေ SMS ပို့တာ အဆင်ပြေပါလိမ့်မယ်
requirements = python3,kivy==2.3.0,requests,openssl,urllib3,charset-normalizer,idna

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Fullscreen or not
fullscreen = 0

# (list) Permissions 
# SMS ပို့ဖို့နဲ့ အင်တာနက်သုံးဖို့ Permission တွေ ထည့်ထားပါတယ်
android.permissions = INTERNET, SEND_SMS, WRITE_EXTERNAL_STORAGE, READ_PHONE_STATE

# (int) Target Android API
android.api = 31

# (int) Minimum API support
android.minapi = 21

# (bool) If True, then automatically accept SDK license
# ဒါက GitHub မှာ အလုပ်လုပ်ဖို့ အရေးကြီးဆုံး အချက်ပါ
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
