[app]

title = ABG Analyzer Pro

package.name = abganalyzer
package.domain = drelyasibabak.ir

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,json
source.exclude_dirs = .git,.github,.buildozer,bin,venv,.venv,buildenv,__pycache__

version = 1.0

requirements = python3,kivy==2.3.1,kivymd==1.2.0

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 24
android.ndk = 27c
android.archs = arm64-v8a

android.accept_sdk_license = True

log_level = 2

warn_on_root = 0

[buildozer]
log_level = 2
