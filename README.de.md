<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera

[English](README.md) · [Русский](README.ru.md) · **Deutsch**

**Ein natives Linux-Werkzeug zur Einrichtung von Webcams.**

Wähle eine Video4Linux2-Kamera, starte die Live-Vorschau und ändere die Einstellungen, die der Kameratreiber anbietet.

[Download](#run-on-linux) · [Schnellstart](#quick-start) · [Roadmap](#roadmap) · [Über den Autor](#author)

</div>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera. Die Abbildung zeigt den interaktiven Designprototyp.">

## Funktionen in v0.2.4

- **Kameraauswahl.** Die Liste der V4L2-Geräte lässt sich über die Schaltfläche neben der Kameraauswahl aktualisieren.
- **Live-Vorschau.** GStreamer zeigt einen lokalen Videostream und misst dessen Eingangsbildrate. Die Darstellung läuft über GTK 4.
- **Aufnahmemodus.** Der Modus lässt sich automatisch aushandeln oder aus den vom Treiber gemeldeten Kombinationen aus Auflösung, Pixelformat und Bildrate auswählen.
- **Geräteeinstellungen.** Verfügbare Zahlenwerte, Schalter und Listen lassen sich ändern. Änderungen werden direkt an den Treiber gesendet.
- **Diagnose.** **Diagnostics** zeigt fehlende Komponenten, Zugriffsprobleme und Fehler beim Start der Vorschau.
- **Darstellung.** Die native Oberfläche mit GTK 4 und libadwaita kann der Systemeinstellung folgen oder ein helles bzw. dunkles Design verwenden.

<h2 id="quick-start">Schnellstart</h2>

1. Schließe die Webcam an und wähle sie unter **Device**. Wurde die Kamera nach dem Programmstart angeschlossen, aktualisiere die Geräteliste.
2. Open Camera wählt 60 FPS, wenn die Kamera diesen Modus meldet, oder 59,94 FPS, wenn nur dieser Modus nahe 60 FPS verfügbar ist. Du kannst **Automatic** oder eine unterstützte Kombination wählen.
3. Klicke auf **Start preview**. Die FPS-Anzeige misst die eingehenden Bilder pro Sekunde. Der Wert kann von der eingestellten Rate abweichen und ist unabhängig von der Bildwiederholrate des Monitors.
4. Passe die Bildparameter während der Vorschau an. Beim Wechsel der Auflösung, des Formats oder der Bildrate startet die Vorschau automatisch neu.

<h2 id="run-on-linux">📦 Installation unter Linux</h2>

[Open Camera v0.2.4](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4) ist in drei Paketformaten verfügbar.

| Download | Installation oder Start |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | Ubuntu 24.04 · `sudo apt install ./open-camera_0.2.4_all.deb` |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | Fedora 44 · `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | Linux x86_64 mit glibc 2.39+ · `chmod +x OpenCamera-0.2.4-x86_64.AppImage`, dann `./OpenCamera-0.2.4-x86_64.AppImage` |

Nach der DEB- oder RPM-Installation lässt sich die App über das Anwendungsmenü oder mit `open-camera` öffnen. Wenn FUSE fehlt, starte das AppImage mit `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

Lade [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) in denselben Ordner wie das Paket und führe dort `sha256sum -c --ignore-missing SHA256SUMS` aus, um die Prüfsumme abzugleichen.

Der Start und die Live-Vorschau wurden für alle drei Pakete mit einer synthetischen Videoquelle geprüft. Tests mit echten Webcams stehen noch aus.

<details>
<summary><b>Aus dem Quellcode starten</b></summary>

Voraussetzungen sind Python 3.10+, GTK 4.8+, libadwaita 1.4+ und GStreamer 1.20+. Führe den Befehl im Repository mit dem System-Python aus, damit PyGObject verfügbar ist.

**Ubuntu 24.04**

```sh
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 \
  gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good v4l-utils
python3 -m open_camera
```

**Fedora**

```sh
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1 \
  gstreamer1-plugins-base gstreamer1-plugins-good v4l-utils
python3 -m open_camera
```

</details>

### Ohne Webcam testen

Starte `python3 -m open_camera --test-source` oder nach einer DEB- oder RPM-Installation `open-camera --test-source`. Wähle **GStreamer test pattern**, stelle bei 1280 × 720 eine Rate von 30, 60 oder 120 FPS ein und klicke auf **Start preview**. Diese Modi gelten für die Testquelle. Die verfügbaren Bildraten echter Webcams hängen von Gerät und Treiber ab.

### Fehlerbehebung

| Symptom | Prüfung |
| --- | --- |
| Die Kamera fehlt in der Liste | Schließe sie erneut an, aktualisiere die Liste und prüfe unter **Diagnostics** Zugriffsrechte und fehlende Komponenten. |
| Die Vorschau startet nicht | Schließe andere Programme, die die Kamera verwenden, wähle **Automatic** und prüfe den Streamfehler unter **Diagnostics**. Komprimierte Formate können einen Decoder benötigen. |
| Die gemessene Rate liegt unter dem gewählten Wert | Prüfe die verfügbaren Raten für Auflösung und Format. Teste eine geringere Auflösung oder einen anderen USB-Anschluss und vergleiche die Messwerte. |

Gib bei einer Fehlermeldung Linux-Distribution, Kameramodell, Aufnahmemodus und den relevanten Text aus **Diagnostics** an.

<h2 id="roadmap">Roadmap</h2>

| Abschnitt | Aufgaben |
| --- | --- |
| **Verfügbar · v0.2.4** | Kameraauswahl, Vorschau, FPS-Messung, Treibereinstellungen, Diagnose und drei Paketformate. |
| **Als Nächstes · Hardware und Stabilität** | USB- und integrierte Webcams testen, Modi ab 60 FPS auf realer Hardware prüfen und den Umgang mit belegten oder getrennten Geräten testen. |
| **Geplant · Arbeit mit Video** | Fotos und Videoaufnahme, Overlays und Effekte. Danach Profile und virtuelle Kameraausgabe untersuchen. |

Die Roadmap beschreibt Prioritäten ohne feste Termine.

## Design und Entwicklung

Die Grafik oben zeigt den [interaktiven HTML-Prototyp](design/open-camera-interface-options.html). Lade die Datei herunter und öffne sie im Browser, um simuliertes Video, Effekte und virtuelle Ausgabe zu sehen. Die [Theme-Stile](design/open-camera-themes.css) liegen separat vor. Aufnahme, Effekte und virtuelle Kameraausgabe sind in der nativen Version 0.2.4 noch nicht enthalten.

Der Quellcode liegt in [open_camera/](open_camera/), die Tests in [tests/](tests/) und die README-Grafiken in [assets/readme/](assets/readme/). Tests starten mit `python3 -m unittest discover -s tests -v`. Zur Neuerstellung der Grafiken installiere Pillow in der Entwicklungsumgebung und starte `python3 tools/build_readme_assets.py`.

<h2 id="author">Über den Autor</h2>

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx auf GitHub"></a>

**sailxx** hat Open Camera und [Tobi](https://github.com/sailxx/Tobi) erstellt. Das Design der Tobi-README diente als Vorlage. Weitere Projekte findest du im [GitHub-Profil](https://github.com/sailxx).
