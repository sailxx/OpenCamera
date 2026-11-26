[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · **한국어** · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Video4Linux 카메라용 기본 Linux 워크벤치.**

웹캠을 선택하고, 실시간 미리보기를 보고, 캡처 모드를 선택하고, 카메라 드라이버에 표시되는 컨트롤을 조정하세요.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="상태: 초기 개발">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 및 libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer 및 V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera , 기본 Linux 카메라 작업대. 이미지는 대화형 디자인 프로토타입을 보여줍니다.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Linux에서 실행"></a>&nbsp; &nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="디자인 보기"></a>&nbsp; &nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="로드맵 보기"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="카메라 검색, 실시간 미리보기, 캡처 모드, 하드웨어 제어, 진단 및 모양">

<details>
<summary><b>기능에 대해 자세히 알아보기</b></summary>

- **카메라.** V4L2 장치를 선택하고 카메라를 연결하거나 연결을 끊은 후 다시 검색하세요.
- **실시간 미리보기.** 로컬 스트림을 시작 및 중지하고 소스에서 측정된 캡처 속도를 확인하세요. 가능한 경우 앱은 GStreamer GTK 4 싱크로 프레임을 그립니다. 또한 제한된 GTK 텍스처 폴백을 지원합니다.
- **캡처 모드.** 자동 협상을 사용하거나 광고된 해상도, 픽셀 형식 및 프레임 속도 조합을 선택하세요. 미리보기 세션 간에 모드를 변경합니다.
- **하드웨어 제어.** 운전자가 보고한 숫자, 스위치 및 메뉴 컨트롤을 편집합니다. 변경 사항은 사용자가 작성하는 대로 드라이버로 전송됩니다.
- **진단 및 외관.** 장치 액세스, 누락된 종속성 및 미리보기 오류를 검사합니다. 설정은 시스템, 밝고 어두운 모습을 제공합니다.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="장치와 모드를 선택하고 미리보기를 시작한 다음 지원되는 카메라 컨트롤을 조정하세요.">

<br>

<img src="assets/readme/states.svg" width="100%" alt="미리보기 상태: 중지됨, 시작 중, 캡처 중, 중단됨">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="30, 60 또는 120 FPS의 합성 테스트 패턴과 세 가지 기본 모양 모드">

## 빠른 시작

1. 웹캠을 연결하고 선택하세요. **장치**. 앱을 연 후 연결한 경우 새로고침 버튼을 사용하세요.
2. Open Camera는 카메라가 이를 보고할 때 60 FPS를 선택하고, 이것이 유일한 60에 가까운 모드인 경우 59.94 FPS를 선택합니다. 선택하다 **오토매틱** 운전자가 보고된 조합 중 하나를 협상하거나 선택할 수 있도록 합니다.
3. 딸깍 하는 소리 **미리보기 시작**. FPS 판독값은 소스에서 도착하는 프레임을 측정합니다. 요청된 속도와 다를 수 있으며 모니터 새로 고침을 측정하지 않습니다.
4. 미리보기를 보면서 운전자가 노출하는 컨트롤을 조정하세요. 해상도, 형식 또는 프레임 속도를 변경하면 미리보기가 자동으로 다시 시작됩니다.

Open Camera는 웹캠 구성 및 테스트를 위한 로컬 워크벤치를 제공합니다. 버전 0.2.4에는 녹화, 효과 처리 또는 가상 카메라 출력이 없습니다.

<h2 id="roadmap">로드맵</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="카메라 기초, Linux 검증, 캡처 도구, AppImage, Debian 및 RPM 패키징">

| 단계 | 일하다 |
| --- | --- |
| **사용 가능 · v0.2.4** | 카메라 선택, 실시간 미리보기, 소스 FPS, 드라이버 제어, 진단 및 3개의 Linux 패키지. |
| **다음 · 하드웨어 및 안정성** | USB 및 내장 카메라를 검증하고, 하드웨어에서 광고된 60개 이상의 FPS 모드를 확인하고, 장치가 사용 중이거나 연결이 끊어졌을 때 복구를 테스트하세요. |
| **계획 · 캡처 워크플로우** | 사진 및 비디오 캡처, 오버레이 및 효과를 추가한 다음 프로필 및 가상 카메라 출력을 살펴보세요. |

로드맵은 목표 날짜 없이 우선순위를 설정합니다.

<h2 id="run-on-linux">📦 Linux에서 실행</h2>

Open Camera 다운로드 **v0.2.4** ~에서 [GitHub 출시](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| 다운로드 | 설치 또는 실행 |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` 우분투 24.04에서 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` 페도라 44에서 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` 그 다음에 `./OpenCamera-0.2.4-x86_64.AppImage` glibc 2.39 이상을 사용하는 x86_64 Linux |

데스크톱 실행기나 다음을 사용하여 DEB 또는 RPM 설치를 시작하세요. `open-camera`. FUSE를 사용할 수 없는 경우 다음을 사용하여 AppImage를 실행하세요. `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

다운로드를 확인하려면 저장하세요. [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) 패키지 옆에 실행 `sha256sum -c --ignore-missing SHA256SUMS` 해당 디렉토리에서.

릴리스 워크플로는 세 가지 패키지를 모두 설치하거나 실행하고 합성 소스를 사용하여 실시간 미리 보기를 확인했습니다. 물리적 웹캠 호환성은 아직 검증이 필요합니다.

### 소스에서 실행

Python 3.10 +, GTK 4.8 +, libadwaita 1.4 + 및 GStreamer 1.20 +와 함께 Linux 데스크탑을 사용하십시오. 배포판의 PyGObject 바인딩을 찾을 수 있도록 시스템 Python을 사용하여 저장소 폴더에서 실행합니다.

<details open>
<summary><b>우분투 24.04 이상</b></summary>

```sh
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 \
  gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>페도라</b></summary>

```sh
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1 \
  gstreamer1-plugins-base gstreamer1-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>실제 카메라 없이 테스트</b></summary>

```sh
python3 -m open_camera --test-source
```

DEB 또는 RPM 설치용 `open-camera --test-source`. 선택하다 **GStreamer 테스트 패턴**, 1280 × 720에서 30, 60 또는 120 FPS를 선택하고 **미리보기 시작**. 이 비율은 테스트 소스를 설명합니다. 물리적 장치 모드는 카메라와 드라이버에 따라 다릅니다.

</details>

### 문제 해결

| 징후 | 확인해야 할 사항 |
| --- | --- |
| 카메라가 없습니다 | 다시 연결하고 장치 목록을 새로 고친 후 확인하십시오. **진단** 누락된 구성 요소 또는 장치 권한. |
| 미리보기가 시작되지 않습니다. | 카메라를 사용하여 앱을 닫고 시도해 보세요. **오토매틱**, 그럼 확인해봐 **진단** 파이프라인 오류 때문입니다. 인코딩된 모드에는 설치된 디코더가 필요할 수 있습니다. |
| 소스 FPS가 선택한 속도보다 낮습니다. | 해당 해상도와 형식에서 사용 가능한 속도를 확인하세요. 더 낮은 해상도나 다른 USB 포트를 사용해 보고 측정값을 비교하십시오. |

문제를 보고할 때 분포, 카메라 모델, 선택한 캡처 모드 및 관련 텍스트를 포함하십시오. **진단**.

<h2 id="design">설계</h2>

배너는 다음을 보여줍니다. **대화형 브라우저 프로토타입**. 여기에는 시뮬레이션된 프레임, 효과 및 가상 출력이 포함되어 있어 인터페이스를 카메라 하드웨어와 독립적으로 탐색할 수 있습니다. 다운로드 [독립형 HTML 프로토타입](design/open-camera-interface-options.html) 브라우저에서 엽니다. 그만큼 [테마 스타일시트](design/open-camera-themes.css) 별도로 이용 가능합니다.

<details>
<summary><b>개발 및 검증</b></summary>

| 길 | 목적 |
| --- | --- |
| [open_camera/](open_camera/) | GTK 인터페이스, GStreamer 미리보기 및 V4L2 컨트롤 |
| [테스트/](tests/) | V4L2 구문 분석 및 제어 검증 테스트 |
| [설계/](design/) | 대화형 프로토타입, 테마, 아이콘 및 스크린샷 |
| [자산/읽어보기/](assets/readme/) | README 카드 및 탐색 버튼 |

```sh
python3 -m unittest discover -s tests -v
```

Linux 데스크탑에서 30 및 60 FPS 의 테스트 패턴으로 시작 및 중지를 확인합니다. 실제 카메라를 사용하여 광고 모드, 측정된 속도, 운전자 제어 변경 사항 및 연결 끊김 동작을 확인합니다.

README 패널을 재생성하려면 개발 환경에 Pillow를 설치하고 실행하세요.:

```sh
python3 tools/build_readme_assets.py
```

</details>

## 저자 소개

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="GitHub의 sailxx"></a>

**sailxx** Open Camera의 제작자이며 [Tobi](https://github.com/sailxx/Tobi), 이 README의 시각적 스타일에 영감을 준 프로젝트입니다. 다른 프로젝트는 다음에서 확인 가능합니다. [GitHub 프로필](https://github.com/sailxx).
