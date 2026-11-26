[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · **繁體中文** · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**適用於 Video4Linux 攝影機的本機 Linux 工作台。**

選擇網路攝影機，查看其實時預覽，選擇捕捉模式並調整攝影機驅動程式公開的控制。

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="狀態：早期開發">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 和 libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer 和 V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera ，原生 Linux 相機工作台。此圖顯示了互動設計原型。">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="在Linux上運行"></a>&nbsp;;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="查看設計"></a>&nbsp;;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="查看路線圖"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="相機發現、即時預覽、捕捉模式、硬體控制、診斷和外觀">

<details>
<summary><b>有關功能的更多信息</b></summary>

- **相機。** 選擇 V4L2 裝置並在連接或斷開相機後重新掃描。
- **即時預覽。** 啟動和停止本地流並查看在來源處測量的捕獲率。如果可用，該應用程式可以使用 GStreamer GTK 4 接收器繪製框架。它還支援有界 GTK 紋理回退。
- **捕捉模式。** 使用自動協商或選擇解析度、像素格式和幀速率的廣告組合。在預覽會話之間變更模式。
- **硬體控制。** 編輯驅動程式報告的數字、開關和選單控制項。當您進行變更時，變更會傳送給驅動程式。
- **診斷和外觀。** 檢查設備存取、缺少依賴項和預覽錯誤。設定提供系統、淺色和深色外觀。

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="選擇設備和模式，開始預覽，然後調整支援的相機控制">

<br>

<img src="assets/readme/states.svg" width="100%" alt="預覽狀態：停止、開始、捕捉和中斷">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="30、60 或 120 FPS 的合成測試圖案，加上三種本機外觀模式">

## 快速啟動

1. 連接網路攝影機並在中選擇它 **裝置**。如果在開啟應用程式後插入，請使用刷新按鈕。
2. Open Camera 選擇 60 FPS 當相機報告時，或者 59.94 FPS 這是唯一接近 60 的模式。選擇 **自動的** 讓駕駛員協商或選擇報告的組合之一。
3. 點選 **開始預覽**。 FPS 讀數測量來自來源的幀。它可能與請求的速率不同，並且不測量監視器刷新。
4. 調整駕駛員在觀看預覽時顯示的控制項。變更解析度、格式或幀速率會自動重新啟動預覽。

Open Camera 提供用於配置和測試網路攝影機的本機工作台。 0.2.4版本沒有錄音、效果處理或虛擬攝影機輸出。

<h2 id="roadmap">路線圖</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="相機基礎、Linux 驗證、擷取工具以及 AppImage、Debian 和 RPM 打包">

| 階段 | 工作 |
| --- | --- |
| **有貨·v0.2.4** | 相機選擇、即時預覽、來源 FPS、驅動程式控制、診斷和三個 Linux 套件。 |
| **下一篇 · 硬體與可靠性** | 驗證 USB 和內建鏡頭，檢查硬體上宣傳的 60 多種 FPS 模式，並在裝置繁忙或拔掉插頭時測試恢復。 |
| **計劃·捕獲工作流程** | 添加照片和影片擷取、疊加和效果，然後探索設定檔和虛擬相機輸出。 |

該路線圖設定了優先事項，但沒有目標日期。

<h2 id="run-on-linux">📦 在Linux上運行</h2>

下載Open Camera **v0.2.4** 從 [GitHub 發布](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| 下載 | 安裝或啟動 |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` 在 Ubuntu 24.04 上 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` 在 Fedora 44 上 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` 然後 `./OpenCamera-0.2.4-x86_64.AppImage` 在有 glibc 2.39 或更新版本的 x86_64 Linux 上 |

從桌上型啟動器或使用下列指令啟動 DEB 或 RPM 安裝 `open-camera`。如果 FUSE 不可用，請啟動 AppImage `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

若要檢查下載情況，請儲存 [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) 在包旁邊並運行 `sha256sum -c --ignore-missing SHA256SUMS` 從該目錄。

發布工作流程安裝或啟動了所有三個軟體包，並使用合成來源檢查了即時預覽。實體網路攝影機相容性仍需要驗證。

### 從原始碼運行

使用 Python 3.10 +、GTK 4.8 +、libadwaita 1.4 + 和 GStreamer 1.20 + 的 Linux 桌面。使用系統 Python 從儲存庫資料夾運行，以便它可以找到發行版的 PyGObject 綁定。

<details open>
<summary><b>Ubuntu 24.04 及更新版本</b></summary>

```sh
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 \
  gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>軟呢帽</b></summary>

```sh
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1 \
  gstreamer1-plugins-base gstreamer1-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>沒有實體相機的測試</b></summary>

```sh
python3 -m open_camera --test-source
```

對於 DEB 或 RPM 安裝使用 `open-camera --test-source`。選擇 **GStreamer 測試模式**, 在 1280 × 720 下選擇 30、60 或 120 FPS，然後按一下 **開始預覽**。這些速率描述了測試來源。實體設備模式取決於相機和驅動程式。

</details>

### 故障排除

| 症狀 | 要檢查什麼 |
| --- | --- |
| 相機不見了 | 重新連接，刷新設備清單查看 **診斷** 缺少組件或設備權限。 |
| 預覽無法啟動 | 關閉使用相機的應用程序，嘗試 **自動的**, 然後檢查 **診斷** 對於管道錯誤。編碼模式可能需要安裝解碼器。 |
| 源 FPS 低於所選速率 | 檢查該解析度和格式下的可用速率。嘗試較低的解析度或不同的 USB 連接埠並比較測量結果。 |

報告問題時，請包括分佈、相機型號、選擇的拍攝模式以及相關文本 **診斷**.

<h2 id="design">設計</h2>

橫幅顯示 **互動式瀏覽器原型**。它包括模擬幀、效果和虛擬輸出，因此可以獨立於相機硬體來探索介面。下載 [獨立的 HTML 原型](design/open-camera-interface-options.html) 並在瀏覽器中打開它。這 [主題樣式表](design/open-camera-themes.css) 是單獨提供的。

<details>
<summary><b>開發驗證</b></summary>

| 小路 | 目的 |
| --- | --- |
| [開啟相機/](open_camera/) | GTK 介面、GStreamer 預覽和 V4L2 控件 |
| [測試/](tests/) | V4L2 解析與控制驗證測試 |
| [設計/](design/) | 互動式原型、主題、圖示和螢幕截圖 |
| [資產/自述文件/](assets/readme/) | README 卡和導航按鈕 |

```sh
python3 -m unittest discover -s tests -v
```

在 Linux 桌面上，使用 30 和 60 FPS 處的測試模式驗證啟動和停止。使用實體攝影機檢查廣告模式、測量的速率、駕駛員控制的變化以及斷開連接行為。

若要重新產生 README 面板，請在開發環境中安裝 Pillow 並執行:

```sh
python3 tools/build_readme_assets.py
```

</details>

## 關於作者

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx 上 GitHub"></a>

**sailxx** 是 Open Camera 的創造者， [Tobi](https://github.com/sailxx/Tobi), 該項目激發了 README 的視覺風格。其他項目可在 [GitHub簡介](https://github.com/sailxx).
