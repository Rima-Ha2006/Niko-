[app]
title = NIKO
package.name = niko
package.domain = org.niko
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy
orientation = portrait

# هادي هي اللي كتحل المشكل!
android.accept_sdk_license_agreements = True
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
p4a.branch = master

[buildozer]
log_level = 2
