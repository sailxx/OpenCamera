[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · **ئۇيغۇرچە** · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Video4Linux كامېراسىنىڭ يەرلىك Linux خىزمەت پونكىتى.**

تور كامېراسىنى تاللاڭ ، ئۇنىڭ نەق مەيدان كۆرۈنۈشىنى كۆرۈڭ ، تۇتۇش ھالىتىنى تاللاڭ ۋە كامېرا قوزغاتقۇچ ئاشكارىلىغان كونترولنى تەڭشەڭ.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="ھالىتى: دەسلەپكى تەرەققىيات">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 ۋە libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer ۋە V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera ، يەرلىك Linux كامېرا خىزمەت پونكىتى. رەسىمدە ئۆز-ئارا لايىھىلەنگەن ئەسلى تىپ كۆرسىتىلدى.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Linux دا ئىجرا قىلىڭ"></a>&nbsp; & nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="لايىھەنى كۆرۈڭ"></a>&nbsp; & nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="يول خەرىتىسىنى كۆرۈڭ"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="كامېرا بايقاش ، نەق مەيداننى كۆرۈش ، تۇتۇش ھالىتى ، قاتتىق دېتال كونترول قىلىش ، دىئاگنوز قويۇش ۋە كۆرۈنۈش">

<details>
<summary><b>ئىقتىدارلىرى ھەققىدە تېخىمۇ كۆپ</b></summary>

- **كامېرا.** كامېرانى ئۇلىغان ياكى ئۈزۈۋەتكەندىن كېيىن V4L2 ئۈسكۈنىسىنى تاللاڭ ۋە ئەسلىگە كەلتۈرۈڭ.
- **نەق مەيدان ئالدىن كۆرۈش.** يەرلىك ئېقىننى باشلاڭ ۋە توختىتىڭ ، مەنبەدە ئۆلچەنگەن تۇتۇش نىسبىتىنى كۆرۈڭ. ئىشلەتكىلى بولىدىغان ۋاقىتتا ، بۇ دېتال GStreamer GTK 4 چۆككۈچ بىلەن رامكا سىزغان. ئۇ يەنە چەكلەنگەن GTK توقۇلما يوچۇقنى قوللايدۇ.
- **تۇتۇش ھالىتى.** ئاپتوماتىك سۆھبەتنى ئىشلىتىڭ ياكى ئېنىقلىق دەرىجىسى ، پېكسىل فورماتى ۋە رامكا نىسبىتىنىڭ ئېلان بىرىكمىسىنى تاللاڭ. ئالدىن كۆرۈش يىغىنلىرى ئارىسىدىكى ھالەتنى ئۆزگەرتىڭ.
- **قاتتىق دېتال كونتروللىرى.** قوزغاتقۇچ دوكلات قىلغان سان ، ئالماشتۇرۇش ۋە تىزىملىك ​​كونتروللىرىنى تەھرىرلەڭ. ئۆزگەرتىشلەرنى قوزغاتقاندا قوزغاتقۇچقا ئەۋەتىلىدۇ.
- **دىئاگنوز ۋە تاشقى كۆرۈنۈش.** ئۈسكۈنىنىڭ زىيارەت قىلىنىشى ، بېقىنىشچانلىقى ۋە ئالدىن كۆرۈش خاتالىقىنى تەكشۈرۈڭ. تەڭشەكلەر سىستېما ، يورۇق ۋە قاراڭغۇ كۆرۈنۈش بىلەن تەمىنلەيدۇ.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="ئۈسكۈنە ۋە ھالەتنى تاللاڭ ، ئالدىن كۆرۈشنى باشلاڭ ، ئاندىن قوللايدىغان كامېرا كونتروللىرىنى تەڭشەڭ">

<br>

<img src="assets/readme/states.svg" width="100%" alt="ئالدىن كۆرۈش: توختىتىش ، باشلاش ، تۇتۇش ۋە ئۈزۈش">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="30 ، 60 ياكى 120 FPS دىكى بىرىكمە سىناق ئەندىزىسى ، ئۈچ خىل تاشقى كۆرۈنۈش شەكلى قوشۇلغان">

## تېز باشلاش

1. كامېرانى ئۇلاپ تاللاڭ **ئۈسكۈنە**. ئەگەر ئەپ ئاچقاندىن كېيىن چېتىلغان بولسا يېڭىلاش كۇنۇپكىسىنى ئىشلىتىڭ.
2. كامېرا دوكلات قىلغاندا Open Camera 60 FPS ياكى 59.94 FPS نى تاللايدۇ. تاللاڭ **ئاپتوماتىك** شوپۇرغا سۆھبەتلىشىش ياكى مەلۇم قىلىنغان بىرىكمىلەرنى تاللاش.
3. چېكىڭ **ئالدىن كۆرۈشنى باشلاڭ**. FPS ئوقۇش مەنبەسى مەنبەدىن كەلگەن رامكىلارنى ئۆلچەيدۇ. ئۇ تەلەپ قىلىنغان سۈرئەت بىلەن پەرقلىنىپ ، ئېكراننىڭ يېڭىلىنىشىنى ئۆلچىمەيدۇ.
4. ئالدىن كۆرۈشنى كۆرگەندە شوپۇرنىڭ ئاشكارىلىغان كونتروللىرىنى تەڭشەڭ. ئېنىقلىق دەرىجىسى ، فورماتى ياكى رامكا نىسبىتىنى ئۆزگەرتىش ئالدىن كۆرۈشنى قايتا قوزغىتىدۇ.

Open Camera تور كامېراسىنى تەڭشەش ۋە سىناق قىلىش ئۈچۈن يەرلىك خىزمەت پونكىتى بىلەن تەمىنلەيدۇ. 0.2.4 نەشرىدە خاتىرىلەش ، ئۈنۈم بىر تەرەپ قىلىش ياكى مەۋھۇم كامېرا چىقىرىش يوق.

<h2 id="roadmap">يول خەرىتىسى</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="كامېرا ئاساسى ، Linux دەلىللەش ، تۇتۇش قوراللىرى ۋە AppImage ، Debian ۋە RPM ئورالمىسى">

| باسقۇچ | خىزمەت |
| --- | --- |
| **ئىشلەتكىلى بولىدۇ · v0.2.4** | كامېرا تاللاش ، نەق مەيدان ئالدىن كۆرۈش ، مەنبە FPS ، قوزغاتقۇچ كونترول قىلىش ، دىئاگنوز قويۇش ۋە ئۈچ Linux ئورالمىسى. |
| **كېيىنكى · قاتتىق دېتال ۋە ئىشەنچلىك** | USB ۋە ئىچىگە ئورۇنلاشتۇرۇلغان كامېرالارنى دەلىللەڭ ، قاتتىق دېتالدا ئېلان قىلىنغان 60+ FPS ھالىتىنى تەكشۈرۈپ بېقىڭ ، ئۈسكۈنىلەر ئالدىراش ياكى توكقا چېتىلغاندا ئەسلىگە كەلتۈرۈشنى سىناڭ. |
| **پىلانلانغان · خىزمەت ئېقىمىنى تۇتۇش** | رەسىم ۋە سىنغا ئېلىش ، قاپلاش ۋە ئۈنۈم قوشۇش ، ئاندىن ئارخىپ ۋە مەۋھۇم كامېرا چىقىرىش ئۈستىدە ئىزدىنىڭ. |

يول خەرىتىسى نىشان ۋاقتى بولمىغان مۇھىم نۇقتىلارنى بەلگىلەيدۇ.

<h2 id="run-on-linux">📦 Linux دا ئىجرا قىلىڭ</h2>

Open Camera نى چۈشۈرۈڭ **v0.2.4** from [GitHub ئېلان قىلىندى](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| چۈشۈرۈش | قاچىلاش ياكى قوزغىتىش |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` ئۇبۇنتۇ 24.04 دا |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` Fedora 44 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` ئاندىن `./OpenCamera-0.2.4-x86_64.AppImage` x86_64 Linux بىلەن glibc 2.39 ياكى تېخىمۇ يېڭى |

ئۈستەل يۈزى قوزغاتقۇچتىن ياكى DEB ياكى RPM قاچىلاشنى قوزغىتىڭ `open-camera`. ئەگەر FUSE ئىشلەتكىلى بولمىسا ، AppImage نى قوزغىتىڭ `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

چۈشۈرۈشنى تەكشۈرۈش ئۈچۈن ساقلاڭ [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) بولاقنىڭ يېنىدا ئىجرا قىلىڭ `sha256sum -c --ignore-missing SHA256SUMS` ئۇ مۇندەرىجىدىن.

قويۇپ بېرىش خىزمەت ئېقىمى ئۈچ بولاقنىڭ ھەممىسىنى ئورناتتى ياكى قوزغىتىپ ، بىرىكمە مەنبە ئارقىلىق نەق مەيدان كۆرۈپ بېقىشنى تەكشۈردى. فىزىكىلىق كامېرا ماسلىشىشچانلىقى يەنىلا دەلىللەشكە موھتاج.

### مەنبەدىن ئىجرا قىلىڭ

Python 3.10 + ، GTK 4.8 + ، libadwaita 1.4 + ۋە GStreamer 1.20 + بىلەن Linux ئۈستەل يۈزى ئىشلىتىڭ. Python سىستېمىسى بىلەن ئامبار ھۆججەت قىسقۇچىدىن ئىجرا قىلىڭ ، ئۇ تارقىتىشنىڭ PyGObject باغلىنىشىنى تاپالايدۇ.

<details open>
<summary><b>Ubuntu 24.04 ۋە تېخىمۇ يېڭى</b></summary>

```sh
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 \
  gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>Fedora</b></summary>

```sh
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1 \
  gstreamer1-plugins-base gstreamer1-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>فىزىكىلىق كامېراسىز سىناق</b></summary>

```sh
python3 -m open_camera --test-source
```

DEB ياكى RPM ئورنىتىش ئۈچۈن `open-camera --test-source`. تاللاڭ **GStreamer سىناق ئەندىزىسى**, 1280 × 720 دىكى 30 ، 60 ياكى 120 FPS نى تاللاڭ ۋە چېكىڭ **ئالدىن كۆرۈشنى باشلاڭ**. بۇ باھا سىناق مەنبەسىنى تەسۋىرلەيدۇ. فىزىكىلىق ئۈسكۈنىنىڭ ھالىتى كامېرا ۋە قوزغاتقۇچقا باغلىق.

</details>

### كاشىلا

| ئالامىتى | نېمىنى تەكشۈرۈش كېرەك |
| --- | --- |
| كامېرا يوقاپ كەتتى | ئۇنى قايتا ئۇلاڭ ، ئۈسكۈنە تىزىملىكىنى يېڭىلاپ تەكشۈرۈڭ **دىئاگنوز قويۇش** يوقاپ كەتكەن زاپچاسلار ياكى ئۈسكۈنىلەرنىڭ ئىجازەتنامىسى. |
| ئالدىن كۆرۈش مەغلۇپ بولدى | كامېرا ئارقىلىق ئەپلەرنى تاقاڭ ، سىناپ بېقىڭ **ئاپتوماتىك**, ئاندىن تەكشۈرۈڭ **دىئاگنوز قويۇش** تۇرۇبا خاتالىقى. كودلانغان ھالەتلەر قاچىلانغان كود يەشكۈچنى تەلەپ قىلىشى مۇمكىن. |
| مەنبە FPS تاللانغان ئۆلچەمدىن تۆۋەن | بۇ ئېنىقلىق ۋە فورماتتىكى ئىشلەتكىلى بولىدىغان باھالارنى تەكشۈرۈڭ. تۆۋەن ئېنىقلىق ياكى باشقا USB ئېغىزى ئىشلىتىپ سىناپ بېقىڭ. |

مەسىلە مەلۇم قىلغاندا ، تارقىتىش ، كامېرا مودېلى ، تاللانغان تۇتۇش ھالىتى ۋە مۇناسىۋەتلىك تېكىستلەرنى ئۆز ئىچىگە ئالىدۇ **دىئاگنوز قويۇش**.

<h2 id="design">لايىھىلەش</h2>

بايراقنى كۆرسىتىدۇ **ئۆز-ئارا تەسىر كۆرسىتىدىغان توركۆرگۈچ ئەسلى نۇسخىسى**. ئۇ تەقلىد قىلىنغان رامكا ، ئۈنۈم ۋە مەۋھۇم چىقىرىشنى ئۆز ئىچىگە ئالىدۇ ، شۇڭا كۆرۈنمە يۈزى كامېرا قاتتىق دېتالىدىن مۇستەقىل ئىزدىنىشكە بولىدۇ. نى چۈشۈرۈڭ [ئۆزى ئۆز ئىچىگە ئالغان HTML ئەسلى تىپ](design/open-camera-interface-options.html) ئۇنى توركۆرگۈدە ئېچىڭ. The [ئۇسلۇب ئۇسلۇبى](design/open-camera-themes.css) ئايرىم ئىشلەتكىلى بولىدۇ.

<details>
<summary><b>ئېچىش ۋە دەلىللەش</b></summary>

| Path | مەقسەت |
| --- | --- |
| [open_camera/](open_camera/) | GTK كۆرۈنمە يۈزى ، GStreamer ئالدىن كۆرۈش ۋە V4L2 كونتروللىرى |
| [سىناق/](tests/) | V4L2 تەھلىل قىلىش ۋە كونترول دەلىللەش سىنىقى |
| [لايىھىلەش/](design/) | ئۆز-ئارا تەسىر كۆرسىتىدىغان ئەسلى تىپ ، تېما ، سىنبەلگە ۋە ئېكران كۆرۈنۈشلىرى |
| [مۈلۈك / ئوقۇش/](assets/readme/) | README كارتا ۋە يول باشلاش كۇنۇپكىسى |

```sh
python3 -m unittest discover -s tests -v
```

Linux ئۈستەل يۈزىدە ، 30 ۋە 60 FPS دىكى سىناق ئەندىزىسىنى باشلاش ۋە توختىتىشنى تەكشۈرۈپ بېقىڭ. فىزىكىلىق كامېرا ئارقىلىق ئېلان شەكلى ، ئۆلچەملىك نىسبىتى ، قوزغاتقۇچ كونتروللۇقىدىكى ئۆزگىرىش ۋە ھەرىكەتنى ئۈزۈڭ.

README تاختىسىنى ئەسلىگە كەلتۈرۈش ئۈچۈن ، تەرەققىيات مۇھىتىڭىزغا ياستۇق ئورنىتىپ ئىجرا قىلىڭ:

```sh
python3 tools/build_readme_assets.py
```

</details>

## ئاپتور ھەققىدە

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="GitHub دىكى sailxx"></a>

**sailxx** Open Camera نىڭ قۇرغۇچىسى [Tobi](https://github.com/sailxx/Tobi), بۇ README نىڭ كۆرۈنۈش ئۇسلۇبىغا ئىلھام بەرگەن تۈر. باشقا تۈرلەر بار [GitHub ئارخىپى](https://github.com/sailxx).
