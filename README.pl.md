[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Polski** · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Natywny stół warsztatowy Linux dla kamer Video4Linux.**

Wybierz kamerę internetową, zobacz jej podgląd na żywo, wybierz tryb przechwytywania i dostosuj elementy sterujące udostępniane przez sterownik kamery.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="Stan: wczesny rozwój">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 i libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer i V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera, natywny stół warsztatowy z kamerą Linux. Na zdjęciu prototyp interaktywnego projektu.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Uruchom na Linux"></a>&nbsp; &nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="Zobacz projekt"></a>&nbsp; &nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="Zobacz plan działania"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="Wykrywanie kamer, podgląd na żywo, tryby przechwytywania, sterowanie sprzętem, diagnostyka i wygląd">

<details>
<summary><b>Więcej o funkcjach</b></summary>

- **Kamery.** Wybierz urządzenie V4L2 i przeskanuj ponownie po podłączeniu lub odłączeniu kamery.
- **Podgląd na żywo.** Rozpocznij i zatrzymaj strumień lokalny i sprawdź szybkość przechwytywania mierzoną u źródła. Jeśli jest to możliwe, aplikacja maluje ramki za pomocą zlewu GStreamer GTK 4. Obsługuje również ograniczone zastępcze tekstury GTK.
- **Tryby przechwytywania.** Użyj automatycznej negocjacji lub wybierz reklamowaną kombinację rozdzielczości, formatu pikseli i liczby klatek na sekundę. Zmieniaj tryby pomiędzy sesjami podglądu.
- **Sterowanie sprzętowe.** Edytuj elementy sterujące numeryczne, przełączniki i menu zgłaszane przez kierowcę. Zmiany są wysyłane do sterownika po ich wprowadzeniu.
- **Diagnostyka i wygląd.** Sprawdź dostęp do urządzenia, brakujące zależności i podgląd błędów. Ustawienia oferują systemowy, jasny i ciemny wygląd.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="Wybierz urządzenie i tryb, rozpocznij podgląd, a następnie dostosuj obsługiwane elementy sterujące aparatu">

<br>

<img src="assets/readme/states.svg" width="100%" alt="Stany podglądu: zatrzymany, uruchomiony, przechwytywanie i przerwany">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="Syntetyczny wzór testowy przy 30, 60 lub 120 FPS plus trzy tryby wyglądu natywnego">

## Szybki start

1. Podłącz kamerę internetową i wybierz ją **Urządzenie**. Użyj przycisku odświeżania, jeśli był podłączony po otwarciu aplikacji.
2. Open Camera wybiera 60 FPS, gdy kamera to zgłasza, lub 59.94 FPS, gdy jest to jedyny tryb bliski 60. Wybierać **Automatyczny** aby kierowca mógł negocjować lub wybrać jedną ze zgłoszonych kombinacji.
3. Trzask **Rozpocznij podgląd**. Odczyt FPS mierzy ramki przychodzące ze źródła. Może różnić się od żądanej szybkości i nie mierzy częstotliwości odświeżania monitora.
4. Dostosuj elementy sterujące udostępniane przez sterownik podczas oglądania podglądu. Zmiana rozdzielczości, formatu lub liczby klatek na sekundę powoduje automatyczne ponowne uruchomienie podglądu.

Open Camera zapewnia lokalny stół warsztatowy do konfigurowania i testowania kamery internetowej. Wersja 0.2.4 nie posiada funkcji nagrywania, przetwarzania efektów ani wyjścia z kamery wirtualnej.

<h2 id="roadmap">Plan działania</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="Podstawa kamery, walidacja Linux, narzędzia do przechwytywania i pakiety AppImage, Debian i RPM">

| Scena | Praca |
| --- | --- |
| **Dostępne · v0.2.4** | Wybór kamery, podgląd na żywo, źródło FPS, sterowanie sterownikami, diagnostyka i trzy pakiety Linux. |
| **Dalej · Sprzęt i niezawodność** | Sprawdź USB i wbudowane kamery, sprawdź ponad 60 reklamowanych trybów FPS na sprzęcie i przetestuj przywracanie, gdy urządzenie jest zajęte lub odłączone. |
| **Planowane · Przechwytywanie przepływu pracy** | Dodaj przechwytywanie zdjęć i wideo, nakładki i efekty, a następnie przeglądaj profile i nagrania z kamery wirtualnej. |

W planie działania określono priorytety bez dat docelowych.

<h2 id="run-on-linux">📦 Uruchom na Linux</h2>

Pobierz Open Camera **v0.2.4** z [Wydania GitHub](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| Pobierać | Zainstaluj lub uruchom |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` na Ubuntu 24.04 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` na Fedorze 44 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` Następnie `./OpenCamera-0.2.4-x86_64.AppImage` na x86_64 Linux z glibc 2.39 lub nowszym |

Rozpocznij instalację DEB lub RPM z poziomu programu uruchamiającego na komputerze lub za pomocą `open-camera`. Jeśli FUSE jest niedostępny, uruchom AppImage za pomocą `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

Aby sprawdzić pobranie, zapisz [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) obok paczki i uruchom `sha256sum -c --ignore-missing SHA256SUMS` z tego katalogu.

Proces wydania instalował lub uruchamiał wszystkie trzy pakiety i sprawdzał podgląd na żywo przy użyciu źródła syntetycznego. Zgodność fizycznej kamery internetowej nadal wymaga sprawdzenia.

### Uruchom ze źródła

Użyj pulpitu Linux z Pythonem 3.10 +, GTK 4.8 +, libadwaita 1.4 + i GStreamer 1.20 +. Uruchom z folderu repozytorium z systemem Python, aby mógł znaleźć powiązania PyGObject dystrybucji.

<details open>
<summary><b>Ubuntu 24.04 i nowsze</b></summary>

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
<summary><b>Przetestuj bez fizycznej kamery</b></summary>

```sh
python3 -m open_camera --test-source
```

Do zastosowania instalacyjnego DEB lub RPM `open-camera --test-source`. Wybierać **Wzór testowy GStreamera**, wybierz 30, 60 lub 120 FPS w rozdzielczości 1280 × 720 i kliknij **Rozpocznij podgląd**. Wskaźniki te opisują źródło testowe. Tryby urządzenia fizycznego zależą od aparatu i sterownika.

</details>

### Rozwiązywanie problemów

| Objaw | Co sprawdzić |
| --- | --- |
| Brakuje aparatu | Podłącz go ponownie, odśwież listę urządzeń i sprawdź **Diagnostyka** w przypadku brakujących komponentów lub uprawnień urządzenia. |
| Nie można uruchomić podglądu | Zamknij aplikacje za pomocą aparatu, spróbuj **Automatyczny**, następnie sprawdź **Diagnostyka** za błąd rurociągu. Tryby kodowane mogą wymagać zainstalowanego dekodera. |
| Źródło FPS jest poniżej wybranej szybkości | Sprawdź dostępne szybkości w tej rozdzielczości i formacie. Wypróbuj niższą rozdzielczość lub inny port USB i porównaj pomiar. |

Zgłaszając problem, podaj jego dystrybucję, model kamery, wybrany tryb przechwytywania i odpowiedni tekst **Diagnostyka**.

<h2 id="design">Projekt</h2>

Baner przedstawia **interaktywny prototyp przeglądarki**. Zawiera symulowane klatki, efekty i wirtualne dane wyjściowe, dzięki czemu interfejs można eksplorować niezależnie od sprzętu aparatu. Pobierz [samodzielny prototyp HTML](design/open-camera-interface-options.html) i otwórz go w przeglądarce. The [arkusz stylów motywu](design/open-camera-themes.css) jest dostępny osobno.

<details>
<summary><b>Opracowanie i weryfikacja</b></summary>

| Ścieżka | Zamiar |
| --- | --- |
| [otwarta_kamera/](open_camera/) | Interfejs GTK, podgląd GStreamera i sterowanie V4L2 |
| [testy/](tests/) | Testy analizowania i walidacji sterowania V4L2 |
| [projekt/](design/) | Interaktywny prototyp, motywy, ikona i zrzuty ekranu |
| [zasoby/przeczytaj/](assets/readme/) | Karty README i przyciski nawigacyjne |

```sh
python3 -m unittest discover -s tests -v
```

Na komputerze stacjonarnym Linux sprawdź start i stop za pomocą wzorca testowego przy 30 i 60 FPS . Za pomocą fizycznej kamery sprawdź reklamowane tryby, zmierzoną prędkość, zmiany w elementach sterujących sterownika i zachowanie podczas rozłączania.

Aby zregenerować panele README, zainstaluj Pillow w swoim środowisku programistycznym i uruchom:

```sh
python3 tools/build_readme_assets.py
```

</details>

## O autorze

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx na GitHub"></a>

**sailxx** jest twórcą Open Camera i [Tobi](https://github.com/sailxx/Tobi), projekt, który zainspirował styl wizualny README. Inne projekty dostępne są na stronie [Profil GitHub](https://github.com/sailxx).
