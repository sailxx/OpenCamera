[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · **Čeština** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Nativní pracovní stůl Linux pro kamery Video4Linux.**

Vyberte webovou kameru, prohlédněte si její živý náhled, vyberte režim snímání a upravte ovládací prvky vystavené ovladačem fotoaparátu.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="Stav: raný vývoj">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 a libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer a V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera, nativní pracovní stůl pro fotoaparáty Linux. Na obrázku je prototyp interaktivního designu.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Spusťte na Linux"></a>&nbsp; &nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="Prohlédněte si design"></a>&nbsp; &nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="Podívejte se na cestovní mapu"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="Zjištění fotoaparátu, živý náhled, režimy snímání, ovládání hardwaru, diagnostika a vzhled">

<details>
<summary><b>Více o funkcích</b></summary>

- **Kamery.** Vyberte zařízení V4L2 a po připojení nebo odpojení fotoaparátu znovu naskenujte.
- **Živý náhled.** Spusťte a zastavte místní proud a podívejte se na rychlost zachycení naměřenou u zdroje. Pokud je aplikace k dispozici, maluje rámy pomocí dřezu GStreamer GTK 4. Podporuje také omezenou texturu GTK.
- **Režimy snímání.** Použijte automatické vyjednávání nebo zvolte inzerovanou kombinaci rozlišení, formátu pixelů a snímkové frekvence. Změňte režimy mezi relacemi náhledu.
- **Hardwarové ovládání.** Upravte numerické ovládací prvky, přepínače a ovládací prvky nabídky hlášené řidičem. Změny se odesílají řidiči, jakmile je provedete.
- **Diagnostika a vzhled.** Zkontrolujte přístup k zařízení, chybějící závislosti a náhled chyb. Nastavení nabízí systémový, světlý a tmavý vzhled.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="Vyberte zařízení a režim, spusťte náhled a upravte podporované ovládací prvky fotoaparátu">

<br>

<img src="assets/readme/states.svg" width="100%" alt="Stavy náhledu: zastaveno, spouštěno, zachycováno a přerušeno">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="Syntetický testovací obrazec při 30, 60 nebo 120 FPS plus tři režimy přirozeného vzhledu">

## Rychlý start

1. Připojte webovou kameru a vyberte ji **Zařízení**. Použijte tlačítko pro obnovení, pokud bylo připojeno po otevření aplikace.
2. Open Camera vybere 60 FPS, když to kamera hlásí, nebo 59.94 FPS, když je to jediný režim blízko 60. Vybrat **Automatický** nechat řidiče vyjednat nebo vybrat jednu z nahlášených kombinací.
3. Klikněte **Spustit náhled**. Údaj FPS měří snímky přicházející ze zdroje. Může se lišit od požadované frekvence a neměří obnovení monitoru.
4. Upravte ovládací prvky, které váš řidič odkryje při sledování náhledu. Změna rozlišení, formátu nebo snímkové frekvence automaticky restartuje náhled.

Open Camera poskytuje místní pracovní plochu pro konfiguraci a testování webové kamery. Verze 0.2.4 nemá žádný záznam, zpracování efektů ani výstup virtuální kamery.

<h2 id="roadmap">Cestovní mapa</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="Základ fotoaparátu, ověření Linux, nástroje pro snímání a balení AppImage , Debian a RPM">

| Fáze | Práce |
| --- | --- |
| **K dispozici · v0.2.4** | Výběr kamery, živý náhled, zdroj FPS, ovládací prvky ovladače, diagnostika a tři balíčky Linux. |
| **Další · Hardware a spolehlivost** | Ověřte USB a vestavěné kamery, zkontrolujte inzerovaných 60+ režimů FPS na hardwaru a otestujte obnovu, když je zařízení zaneprázdněné nebo odpojené. |
| **Plánované · Zachycení pracovního postupu** | Přidejte zachycení fotografií a videa, překryvy a efekty a poté prozkoumejte profily a výstup virtuální kamery. |

Plán stanoví priority bez cílových dat.

<h2 id="run-on-linux">📦 Spusťte na Linux</h2>

Stáhněte si Open Camera **v0.2.4** z [Vydání GitHub](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| Stáhnout | Nainstalujte nebo spusťte |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` na Ubuntu 24.04 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` na Fedoře 44 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` pak `./OpenCamera-0.2.4-x86_64.AppImage` na x86_64 Linux s glibc 2.39 nebo novější |

Spusťte instalaci DEB nebo RPM ze spouštěče plochy nebo pomocí `open-camera`. Pokud FUSE není k dispozici, spusťte AppImage pomocí `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

Chcete-li zkontrolovat stahování, uložte [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) vedle balíčku a spustit `sha256sum -c --ignore-missing SHA256SUMS` z toho adresáře.

Pracovní postup vydání nainstaloval nebo spustil všechny tři balíčky a zkontroloval živý náhled pomocí syntetického zdroje. Fyzická kompatibilita s webovou kamerou stále vyžaduje ověření.

### Spustit ze zdroje

Použijte desktop Linux s Python 3.10 +, GTK 4.8 +, libadwaita 1.4 + a GStreamer 1.20 +. Spusťte ze složky úložiště se systémovým Pythonem, aby mohl najít vazby PyGObject distribuce.

<details open>
<summary><b>Ubuntu 24.04 a novější</b></summary>

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
<summary><b>Test bez fyzické kamery</b></summary>

```sh
python3 -m open_camera --test-source
```

Pro instalaci DEB nebo RPM `open-camera --test-source`. Vybrat **Testovací vzor GStreamer**, vyberte 30, 60 nebo 120 FPS při 1280 × 720 a klikněte **Spustit náhled**. Tyto sazby popisují testovací zdroj. Režimy fyzického zařízení závisí na fotoaparátu a ovladači.

</details>

### Odstraňování problémů

| Příznak | Co zkontrolovat |
| --- | --- |
| Fotoaparát chybí | Znovu jej připojte, obnovte seznam zařízení a zkontrolujte **Diagnostika** pro chybějící součásti nebo oprávnění zařízení. |
| Náhled se nespustí | Zavřete aplikace pomocí fotoaparátu, zkuste to **Automatický**, pak zkontrolujte **Diagnostika** za chybu potrubí. Kódované režimy mohou vyžadovat nainstalovaný dekodér. |
| Zdroj FPS je pod zvolenou rychlostí | Zkontrolujte dostupné sazby v daném rozlišení a formátu. Zkuste nižší rozlišení nebo jiný port USB a porovnejte měření. |

Při hlášení problému uveďte distribuci, model fotoaparátu, vybraný režim snímání a příslušný text **Diagnostika**.

<h2 id="design">Design</h2>

Banner zobrazuje **prototyp interaktivního prohlížeče**. Obsahuje simulované snímky, efekty a virtuální výstup, takže rozhraní lze prozkoumat nezávisle na hardwaru fotoaparátu. Stáhněte si [samostatný prototyp HTML](design/open-camera-interface-options.html) a otevřete jej v prohlížeči. The [šablona stylů motivu](design/open-camera-themes.css) je k dispozici samostatně.

<details>
<summary><b>Vývoj a ověřování</b></summary>

| Cesta | Účel |
| --- | --- |
| [otevřená_kamera/](open_camera/) | Rozhraní GTK, náhled GStreamer a ovládací prvky V4L2 |
| [testy/](tests/) | Testy pro analýzu V4L2 a ověření kontroly |
| [design/](design/) | Interaktivní prototyp, témata, ikona a snímky obrazovky |
| [aktiva/readme/](assets/readme/) | Karty README a navigační tlačítka |

```sh
python3 -m unittest discover -s tests -v
```

Na ploše Linux ověřte spuštění a zastavení pomocí testovacího vzoru na 30 a 60 FPS . Pomocí fyzické kamery zkontrolujte inzerované režimy, naměřenou rychlost, změny ovládacích prvků řidiče a chování při odpojení.

Pro regeneraci panelů README nainstalujte Pillow do svého vývojového prostředí a spusťte:

```sh
python3 tools/build_readme_assets.py
```

</details>

## O autorovi

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx na GitHub"></a>

**sailxx** je tvůrcem Open Camera a [Tobi](https://github.com/sailxx/Tobi), projekt, který inspiroval vizuální styl tohoto README. Další projekty jsou k dispozici na [Profil GitHub](https://github.com/sailxx).
