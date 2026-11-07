[app]
title = NIKO
package.name = niko
package.domain = org.niko

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1
requirements = python3,kivy

orientation = portrait

[buildozer]
log_level = 2

# مهم بزاف باش يقبل الليسانس!
[app:android]
android.accept_sdk_license_agreements = True

# هادو هما الصحاح
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
p4a.branch = master
