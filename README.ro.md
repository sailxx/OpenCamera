[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Polski](README.pl.md) · **Română** · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Un banc de lucru nativ Linux pentru camerele Video4Linux.**

Selectați o cameră web, vedeți previzualizarea live a acesteia, alegeți un mod de captură și reglați comenzile expuse de driverul camerei.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="Stare: dezvoltare timpurie">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 si libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer și V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera , un banc de lucru nativ pentru camere foto Linux. Imaginea prezintă prototipul de design interactiv.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Rulați pe Linux"></a>&nbsp; &nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="Vedeți designul"></a>&nbsp; &nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="Vezi foaia de parcurs"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="Descoperirea camerei, previzualizare live, moduri de captură, comenzi hardware, diagnosticare și aspect">

<details>
<summary><b>Mai multe despre caracteristici</b></summary>

- **Camere de luat vederi.** Selectați un dispozitiv V4L2 și scanați din nou după conectarea sau deconectarea unei camere.
- **Previzualizare live.** Porniți și opriți un flux local și vedeți rata de captare măsurată la sursă. Când este disponibilă, aplicația pictează rame cu chiuveta GStreamer GTK 4. De asemenea, acceptă o soluție de rezervă limitată a texturii GTK.
- **Moduri de captură.** Utilizați negocierea automată sau alegeți o combinație promovată de rezoluție, format de pixeli și rata de cadre. Schimbați modurile între sesiunile de previzualizare.
- **Comenzi hardware.** Editați comenzile numerice, comutatoare și meniu raportate de șofer. Modificările sunt trimise șoferului pe măsură ce le faceți.
- **Diagnosticare și aspect.** Inspectați accesul la dispozitiv, dependențele lipsă și erorile de previzualizare. Setările oferă sistem, aspect deschis și întunecat.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="Alegeți un dispozitiv și un mod, porniți previzualizarea, apoi ajustați comenzile camerei acceptate">

<br>

<img src="assets/readme/states.svg" width="100%" alt="Stări de previzualizare: oprit, pornit, capturare și întrerupt">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="Model de testare sintetic la 30, 60 sau 120 FPS, plus trei moduri de aspect nativ">

## Pornire rapidă

1. Conectați o cameră web și selectați-o **Dispozitiv**. Folosiți butonul de reîmprospătare dacă a fost conectat după deschiderea aplicației.
2. Open Camera selectează 60 FPS când camera o raportează sau 59.94 FPS când acesta este singurul mod de aproape 60. Alege **Automat** pentru a lăsa șoferul să negocieze sau să selecteze una dintre combinațiile raportate.
3. Clic **Începe previzualizarea**. Citirea FPS măsoară cadrele care sosesc de la sursă. Poate diferi de rata solicitată și nu măsoară reîmprospătarea monitorului.
4. Reglați comenzile pe care le expune șoferul în timp ce vizionați previzualizarea. Schimbarea rezoluției, formatului sau ratei cadrelor repornește automat previzualizarea.

Open Camera oferă un banc de lucru local pentru configurarea și testarea unei camere web. Versiunea 0.2.4 nu are înregistrare, procesare efecte sau ieșire de cameră virtuală.

<h2 id="roadmap">Foaia de parcurs</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="Fundația camerei, validarea Linux, instrumente de captură și ambalarea AppImage, Debian și RPM">

| Etapă | Lucru |
| --- | --- |
| **Disponibil · v0.2.4** | Selectarea camerei, previzualizare live, sursa FPS, comenzi pentru driver, diagnosticare și trei pachete Linux. |
| **Următorul · Hardware și fiabilitate** | Validați USB și camerele încorporate, verificați peste 60 de moduri FPS afișate pe hardware și testați recuperarea atunci când un dispozitiv este ocupat sau deconectat. |
| **Planificat · Captură flux de lucru** | Adăugați captură foto și video, suprapuneri și efecte, apoi explorați profilurile și ieșirea camerei virtuale. |

Foaia de parcurs stabilește priorități fără date țintă.

<h2 id="run-on-linux">📦 Rulați pe Linux</h2>

Descărcați Open Camera **v0.2.4** din [Lansări GitHub](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| Descărcați | Instalați sau lansați |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` pe Ubuntu 24.04 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` pe Fedora 44 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` apoi `./OpenCamera-0.2.4-x86_64.AppImage` pe x86_64 Linux cu glibc 2.39 sau mai nou |

Porniți instalarea DEB sau RPM din lansatorul desktop sau cu `open-camera`. Dacă FUSE nu este disponibil, lansați AppImage cu `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

Pentru a verifica descărcarea, salvați [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) lângă pachet și fugi `sha256sum -c --ignore-missing SHA256SUMS` din acel director.

Fluxul de lucru de lansare a instalat sau a lansat toate cele trei pachete și a verificat previzualizarea live folosind o sursă sintetică. Compatibilitatea fizică a camerei web necesită încă validare.

### Rulați de la sursă

Utilizați un desktop Linux cu Python 3.10 +, GTK 4.8 +, libadwaita 1.4 + și GStreamer 1.20 +. Rulați din folderul de depozit cu sistemul Python, astfel încât să poată găsi legăturile PyGObject ale distribuției.

<details open>
<summary><b>Ubuntu 24.04 și mai noi</b></summary>

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
<summary><b>Testați fără cameră fizică</b></summary>

```sh
python3 -m open_camera --test-source
```

Pentru o instalare DEB sau RPM utilizați `open-camera --test-source`. Selecta **Model de testare GStreamer**, alegeți 30, 60 sau 120 FPS la 1280 × 720 și faceți clic **Începe previzualizarea**. Aceste rate descriu sursa de testare. Modurile dispozitivului fizic depind de cameră și driver.

</details>

### Depanare

| Simptom | Ce trebuie verificat |
| --- | --- |
| Camera lipsește | Reconectați-l, reîmprospătați lista de dispozitive și verificați **Diagnosticare** pentru componente lipsă sau permisiuni pentru dispozitiv. |
| Previzualizarea nu reușește să pornească | Închideți aplicațiile folosind camera, încercați **Automat**, apoi verifica **Diagnosticare** pentru eroarea conductei. Modurile codificate pot necesita un decodor instalat. |
| Sursa FPS este sub rata aleasă | Verificați tarifele disponibile la acea rezoluție și format. Încercați o rezoluție mai mică sau un alt port USB și comparați măsurarea. |

Când raportați o problemă, includeți distribuția, modelul camerei, modul de captură selectat și textul relevant de la **Diagnosticare**.

<h2 id="design">Proiecta</h2>

Bannerul arată **Prototip de browser interactiv**. Include cadre simulate, efecte și ieșire virtuală, astfel încât interfața poate fi explorată independent de hardware-ul camerei. Descărcați [Prototip autonom HTML](design/open-camera-interface-options.html) și deschideți-l într-un browser. The [foaie de stil temă](design/open-camera-themes.css) este disponibil separat.

<details>
<summary><b>Dezvoltare și verificare</b></summary>

| Cale | Scop |
| --- | --- |
| [deschide_camera/](open_camera/) | Interfață GTK, previzualizare GStreamer și comenzi V4L2 |
| [teste/](tests/) | Teste pentru analizarea V4L2 și validarea controlului |
| [proiecta/](design/) | Prototip interactiv, teme, pictograme și capturi de ecran |
| [active/citește-mă/](assets/readme/) | Carduri README și butoane de navigare |

```sh
python3 -m unittest discover -s tests -v
```

Pe un desktop Linux, verificați pornirea și oprirea cu modelul de testare la 30 și 60 FPS . Cu o cameră fizică, verificați modurile afișate, rata măsurată, modificările comenzilor șoferului și comportamentul de deconectare.

Pentru a regenera panourile README, instalați Pillow în mediul dvs. de dezvoltare și rulați:

```sh
python3 tools/build_readme_assets.py
```

</details>

## Despre autor

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx pe GitHub"></a>

**sailxx** este creatorul lui Open Camera și [Tobi](https://github.com/sailxx/Tobi), proiectul care a inspirat stilul vizual al acestui README. Alte proiecte sunt disponibile pe [Profil GitHub](https://github.com/sailxx).
