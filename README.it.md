[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · **Italiano** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Un workbench nativo Linux per telecamere Video4Linux.**

Seleziona una webcam, guarda la sua anteprima dal vivo, scegli una modalità di acquisizione e regola i controlli esposti dal driver della fotocamera.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="Stato: sviluppo iniziale">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 e libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer e V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera, un banco di lavoro nativo per fotocamera Linux. L&#x27;immagine mostra il prototipo di design interattivo.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Funziona su Linux"></a>&nbsp; &nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="Visualizza il disegno"></a>&nbsp; &nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="Vedi la tabella di marcia"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="Rilevamento della fotocamera, anteprima dal vivo, modalità di acquisizione, controlli hardware, diagnostica e aspetto">

<details>
<summary><b>Maggiori informazioni sulle funzionalità</b></summary>

- **Fotocamere.** Selezionare un dispositivo V4L2 ed eseguire nuovamente la scansione dopo aver collegato o scollegato una fotocamera.
- **Anteprima dal vivo.** Avvia e interrompi un flusso locale e visualizza la velocità di acquisizione misurata alla fonte. Quando disponibile, l'app dipinge le cornici con il lavello GStreamer GTK 4. Supporta anche il fallback di texture GTK delimitato.
- **Modalità di cattura.** Utilizza la negoziazione automatica o scegli una combinazione pubblicizzata di risoluzione, formato pixel e frequenza fotogrammi. Cambia modalità tra le sessioni di anteprima.
- **Controlli hardware.** Modifica i controlli numerici, di commutazione e di menu segnalati dal driver. Le modifiche vengono inviate al driver man mano che le apporti.
- **Diagnostica e aspetto.** Controlla l'accesso al dispositivo, le dipendenze mancanti e gli errori di anteprima. Le impostazioni offrono sistema, aspetto chiaro e scuro.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="Scegli un dispositivo e una modalità, avvia l&#x27;anteprima, quindi regola i controlli della fotocamera supportati">

<br>

<img src="assets/readme/states.svg" width="100%" alt="Stati dell&#x27;anteprima: interrotto, in avvio, in acquisizione e interrotto">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="Modello di test sintetico a 30, 60 o 120 FPS, più tre modalità di aspetto native">

## Avvio rapido

1. Collega una webcam e selezionala **Dispositivo**. Utilizza il pulsante di aggiornamento se è stato collegato dopo aver aperto l'app.
2. Open Camera seleziona 60 FPS quando la fotocamera lo segnala, o 59.94 FPS quando questa è l'unica modalità quasi 60. Scegliere **Automatico** per consentire al conducente di negoziare o selezionare una delle combinazioni riportate.
3. Clic **Avvia l'anteprima**. La lettura FPS misura i frame che arrivano dalla sorgente. Può differire dalla velocità richiesta e non misura l'aggiornamento del monitor.
4. Regola i controlli che il tuo conducente espone mentre guarda l'anteprima. La modifica della risoluzione, del formato o della frequenza dei fotogrammi riavvia automaticamente l'anteprima.

Open Camera fornisce un workbench locale per la configurazione e il test di una webcam. La versione 0.2.4 non dispone di registrazione, elaborazione di effetti o uscita della fotocamera virtuale.

<h2 id="roadmap">Tabella di marcia</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="Fondamenti della fotocamera, convalida Linux, strumenti di acquisizione e packaging AppImage, Debian e RPM">

| Palcoscenico | Lavoro |
| --- | --- |
| **Disponibile · v0.2.4** | Selezione della telecamera, anteprima dal vivo, sorgente FPS, controlli del driver, diagnostica e tre pacchetti Linux. |
| **Avanti · Hardware e affidabilità** | Convalida USB e le fotocamere integrate, controlla oltre 60 modalità FPS pubblicizzate sull'hardware e verifica il ripristino quando un dispositivo è occupato o scollegato. |
| **Pianificato · Acquisizione del flusso di lavoro** | Aggiungi acquisizione di foto e video, sovrapposizioni ed effetti, quindi esplora i profili e l'output della fotocamera virtuale. |

La tabella di marcia fissa le priorità senza date obiettivo.

<h2 id="run-on-linux">📦 Funziona su Linux</h2>

Scarica Open Camera **v0.2.4** da [Rilasci GitHub](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| Scaricamento | Installa o avvia |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` su Ubuntu 24.04 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` su Fedora44 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` Poi `./OpenCamera-0.2.4-x86_64.AppImage` su x86_64 Linux con glibc 2.39 o successivo |

Avviare l'installazione di DEB o RPM dal launcher del desktop o con `open-camera`. Se FUSE non è disponibile, avvia AppImage con `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

Per verificare il download, salva [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) accanto al pacchetto ed esegui `sha256sum -c --ignore-missing SHA256SUMS` da quella directory.

Il flusso di lavoro di rilascio ha installato o avviato tutti e tre i pacchetti e ha controllato l'anteprima dal vivo utilizzando una fonte sintetica. La compatibilità fisica della webcam necessita ancora di convalida.

### Esegui dalla fonte

Utilizza un desktop Linux con Python 3.10 +, GTK 4.8 +, libadwaita 1.4 + e GStreamer 1.20 +. Esegui dalla cartella del repository con il sistema Python in modo che possa trovare i collegamenti PyGObject della distribuzione.

<details open>
<summary><b>Ubuntu 24.04 e versioni successive</b></summary>

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
<summary><b>Prova senza una fotocamera fisica</b></summary>

```sh
python3 -m open_camera --test-source
```

Per l'installazione DEB o RPM `open-camera --test-source`. Selezionare **Modello di prova GStreamer**, scegli 30, 60 o 120 FPS a 1280×720 e clicca **Avvia l'anteprima**. Queste tariffe descrivono la fonte del test. Le modalità del dispositivo fisico dipendono dalla fotocamera e dal driver.

</details>

### Risoluzione dei problemi

| Sintomo | Cosa controllare |
| --- | --- |
| Manca la fotocamera | Ricollegalo, aggiorna l'elenco dei dispositivi e controlla **Diagnostica** per componenti mancanti o autorizzazioni del dispositivo. |
| L'anteprima non si avvia | Chiudi le app utilizzando la fotocamera, prova **Automatico**, quindi controlla **Diagnostica** per l'errore della pipeline. Le modalità codificate potrebbero richiedere un decoder installato. |
| La sorgente FPS è inferiore alla tariffa scelta | Controlla le tariffe disponibili con quella risoluzione e formato. Prova una risoluzione inferiore o una porta USB diversa e confronta la misurazione. |

Quando segnali un problema, includi la distribuzione, il modello della fotocamera, la modalità di acquisizione selezionata e il testo pertinente **Diagnostica**.

<h2 id="design">Progetto</h2>

Il banner mostra il **prototipo di browser interattivo**. Include fotogrammi simulati, effetti e output virtuale in modo che l'interfaccia possa essere esplorata indipendentemente dall'hardware della fotocamera. Scarica il [prototipo HTML autonomo](design/open-camera-interface-options.html) e aprirlo in un browser. IL [foglio di stile del tema](design/open-camera-themes.css) è disponibile separatamente.

<details>
<summary><b>Sviluppo e verifica</b></summary>

| Sentiero | Scopo |
| --- | --- |
| [open_camera/](open_camera/) | Interfaccia GTK, anteprima GStreamer e controlli V4L2 |
| [prove/](tests/) | Test per l'analisi V4L2 e la convalida del controllo |
| [progetto/](design/) | Prototipo interattivo, temi, icone e screenshot |
| [risorse/leggimi/](assets/readme/) | Schede README e pulsanti di navigazione |

```sh
python3 -m unittest discover -s tests -v
```

Su un desktop Linux, verificare l'avvio e l'arresto con il modello di prova su 30 e 60 FPS. Con una fotocamera fisica, controlla le modalità pubblicizzate, la velocità misurata, le modifiche ai controlli del conducente e il comportamento di disconnessione.

Per rigenerare i pannelli README, installa Pillow nel tuo ambiente di sviluppo ed esegui:

```sh
python3 tools/build_readme_assets.py
```

</details>

## Informazioni sull'autore

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx su GitHub"></a>

**sailxx** è il creatore di Open Camera e [Tobi](https://github.com/sailxx/Tobi), il progetto che ha ispirato lo stile visivo di questo README. Altri progetti sono disponibili su [Profilo GitHub](https://github.com/sailxx).
