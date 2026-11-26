[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · **Français** · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Un établi Linux natif pour les caméras Video4Linux.**

Sélectionnez une webcam, consultez son aperçu en direct, choisissez un mode de capture et ajustez les commandes exposées par le pilote de la caméra.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="Statut : développement précoce">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 et Libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer et V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera, un établi de caméra Linux natif. L&#x27;image montre le prototype de conception interactive.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Exécuter sur Linux"></a>&nbsp;;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="Voir la conception"></a>&nbsp;;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="Voir la feuille de route"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="Découverte de la caméra, aperçu en direct, modes de capture, commandes matérielles, diagnostics et apparence">

<details>
<summary><b>En savoir plus sur les fonctionnalités</b></summary>

- **Caméras.** Sélectionnez un appareil V4L2 et effectuez une nouvelle analyse après avoir connecté ou déconnecté une caméra.
- **Aperçu en direct.** Démarrez et arrêtez un flux local et consultez le taux de capture mesuré à la source. Lorsqu'elle est disponible, l'application peint les cadres avec l'évier GStreamer GTK 4. Il prend également en charge une texture de repli limitée GTK.
- **Modes de capture.** Utilisez la négociation automatique ou choisissez une combinaison annoncée de résolution, de format de pixel et de fréquence d'images. Changez de mode entre les sessions de prévisualisation.
- **Contrôles matériels.** Modifiez les commandes numériques, de commutation et de menu signalées par le conducteur. Les modifications sont envoyées au chauffeur au fur et à mesure que vous les effectuez.
- **Diagnostic et apparence.** Inspectez l’accès aux appareils, les dépendances manquantes et les erreurs d’aperçu. Les paramètres offrent une apparence système, claire et sombre.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="Choisissez un appareil et un mode, démarrez l&#x27;aperçu, puis ajustez les commandes de caméra prises en charge">

<br>

<img src="assets/readme/states.svg" width="100%" alt="États d&#x27;aperçu : arrêté, démarrage, capture et interrompu">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="Mire de test synthétique à 30, 60 ou 120 FPS, plus trois modes d&#x27;apparence natifs">

## Démarrage rapide

1. Connectez une webcam et sélectionnez-la dans **Appareil**. Utilisez le bouton d'actualisation s'il a été branché après l'ouverture de l'application.
2. Open Camera sélectionne 60 FPS lorsque la caméra le signale, ou 59.94 FPS lorsqu'il s'agit du seul mode proche de 60. Choisir **Automatique** pour laisser le conducteur négocier ou sélectionner l'une des combinaisons signalées.
3. Cliquez **Démarrer l'aperçu**. La lecture FPS mesure les images provenant de la source. Il peut différer du taux demandé et ne mesure pas le rafraîchissement du moniteur.
4. Ajustez les commandes exposées par votre pilote tout en regardant l'aperçu. La modification de la résolution, du format ou de la fréquence d'images redémarre automatiquement l'aperçu.

Open Camera fournit un atelier local pour configurer et tester une webcam. La version 0.2.4 n'a pas d'enregistrement, de traitement d'effets ou de sortie de caméra virtuelle.

<h2 id="roadmap">Feuille de route</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="Base de la caméra, validation Linux, outils de capture et packaging AppImage, Debian et RPM">

| Scène | Travail |
| --- | --- |
| **Disponible · v0.2.4** | Sélection de caméra, aperçu en direct, source FPS, commandes du pilote, diagnostics et trois packages Linux. |
| **Suivant · Matériel et fiabilité** | Validez le USB et les caméras intégrées, vérifiez plus de 60 modes FPS annoncés sur le matériel et testez la récupération lorsqu'un appareil est occupé ou débranché. |
| **Planifié · Flux de travail de capture** | Ajoutez des captures photo et vidéo, des superpositions et des effets, puis explorez les profils et la sortie de la caméra virtuelle. |

La feuille de route fixe des priorités sans dates cibles.

<h2 id="run-on-linux">📦 Exécuter sur Linux</h2>

Télécharger Open Camera **v0.2.4** depuis [Sorties GitHub](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| Télécharger | Installer ou lancer |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` sur Ubuntu 24.04 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` sur Fedora 44 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` alors `./OpenCamera-0.2.4-x86_64.AppImage` sur x86_64 Linux avec glibc 2.39 ou plus récent |

Démarrez l'installation du DEB ou du RPM à partir du lanceur de bureau ou avec `open-camera`. Si le FUSE n'est pas disponible, lancez le AppImage avec `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

Pour vérifier le téléchargement, enregistrez [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) à côté du paquet et exécutez `sha256sum -c --ignore-missing SHA256SUMS` à partir de ce répertoire.

Le workflow de publication a installé ou lancé les trois packages et vérifié l'aperçu en direct à l'aide d'une source synthétique. La compatibilité physique des webcams doit encore être validée.

### Exécuter à partir des sources

Utilisez un bureau Linux avec Python 3.10+, GTK 4.8+, libadwaita 1.4+ et GStreamer 1.20+. Exécutez à partir du dossier du référentiel avec le système Python afin qu'il puisse trouver les liaisons PyGObject de la distribution.

<details open>
<summary><b>Ubuntu 24.04 et plus récent</b></summary>

```sh
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 \
  gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>Feutre</b></summary>

```sh
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1 \
  gstreamer1-plugins-base gstreamer1-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>Test sans caméra physique</b></summary>

```sh
python3 -m open_camera --test-source
```

Pour une installation DEB ou RPM, utilisez `open-camera --test-source`. Sélectionner **Modèle de test GStreamer**, choisissez 30, 60 ou 120 FPS à 1280 × 720 et cliquez **Démarrer l'aperçu**. Ces tarifs décrivent la source du test. Les modes du périphérique physique dépendent de la caméra et du pilote.

</details>

### Dépannage

| Symptôme | Que vérifier |
| --- | --- |
| Il manque la caméra | Reconnectez-le, actualisez la liste des appareils et vérifiez **Diagnostic** pour les composants manquants ou les autorisations de périphérique. |
| L'aperçu ne démarre pas | Fermez les applications à l'aide de l'appareil photo, essayez **Automatique**, puis vérifie **Diagnostic** pour l'erreur de pipeline. Les modes codés peuvent nécessiter un décodeur installé. |
| La source FPS est en dessous du débit choisi | Vérifiez les tarifs disponibles à cette résolution et ce format. Essayez une résolution inférieure ou un autre port USB et comparez la mesure. |

Lorsque vous signalez un problème, incluez la distribution, le modèle de caméra, le mode de capture sélectionné et le texte pertinent de **Diagnostic**.

<h2 id="design">Conception</h2>

La bannière montre le **prototype de navigateur interactif**. Il comprend des images simulées, des effets et une sortie virtuelle afin que l'interface puisse être explorée indépendamment du matériel de la caméra. Téléchargez le [prototype autonome HTML](design/open-camera-interface-options.html) et ouvrez-le dans un navigateur. Le [feuille de style du thème](design/open-camera-themes.css) est disponible séparément.

<details>
<summary><b>Développement et vérification</b></summary>

| Chemin | But |
| --- | --- |
| [caméra_ouverte/](open_camera/) | Interface GTK, aperçu GStreamer et commandes V4L2 |
| [essais/](tests/) | Tests d'analyse et de validation du contrôle V4L2 |
| [conception/](design/) | Prototype interactif, thèmes, icône et captures d'écran |
| [actifs/lisez-moi/](assets/readme/) | Cartes README et boutons de navigation |

```sh
python3 -m unittest discover -s tests -v
```

Sur un bureau Linux, vérifiez le démarrage et l'arrêt avec la mire de test à 30 et 60 FPS . Avec une caméra physique, vérifiez les modes annoncés, le débit mesuré, les modifications apportées aux commandes du conducteur et le comportement de déconnexion.

Pour régénérer les panneaux README, installez Pillow dans votre environnement de développement et exécutez:

```sh
python3 tools/build_readme_assets.py
```

</details>

## À propos de l'auteur

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx sur GitHub"></a>

**sailxx** est le créateur de Open Camera et [Tobi](https://github.com/sailxx/Tobi), le projet qui a inspiré le style visuel de cette README. D'autres projets sont disponibles sur le [Profil GitHub](https://github.com/sailxx).
