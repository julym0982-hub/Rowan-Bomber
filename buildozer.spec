[app]
title = Lulucat Bomber
package.name = lulucatbomber
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.0,requests,openssl
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, SEND_SMS, WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
