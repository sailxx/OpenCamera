[English](README.md) · [العربية](README.ar.md) · **简体中文** · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**适用于 Video4Linux 摄像机的本机 Linux 工作台。**

选择网络摄像头，查看其实时预览，选择捕获模式并调整摄像头驱动程序公开的控件。

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="状态：早期开发">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 和 libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer 和 V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera ，原生 Linux 相机工作台。该图显示了交互设计原型。">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="在Linux上运行"></a>&nbsp;;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="查看设计"></a>&nbsp;;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="查看路线图"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="相机发现、实时预览、捕捉模式、硬件控制、诊断和外观">

<details>
<summary><b>有关功能的更多信息</b></summary>

- **相机。** 选择 V4L2 设备并在连接或断开相机后重新扫描。
- **实时预览。** 启动和停止本地流并查看在源处测量的捕获率。如果可用，该应用程序可以使用 GStreamer GTK 4 接收器绘制框架。它还支持有界 GTK 纹理回退。
- **捕捉模式。** 使用自动协商或选择分辨率、像素格式和帧速率的广告组合。在预览会话之间更改模式。
- **硬件控制。** 编辑驱动程序报告的数字、开关和菜单控件。当您进行更改时，更改会发送给驱动程序。
- **诊断和外观。** 检查设备访问、缺少依赖项和预览错误。设置提供系统、浅色和深色外观。

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="选择设备和模式，开始预览，然后调整支持的相机控制">

<br>

<img src="assets/readme/states.svg" width="100%" alt="预览状态：停止、开始、捕获和中断">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="30、60 或 120 FPS 的合成测试图案，加上三种本机外观模式">

## 快速启动

1. 连接网络摄像头并在中选择它 **设备**。如果在打开应用程序后插入，请使用刷新按钮。
2. Open Camera 选择 60 FPS 当相机报告时，或者 59.94 FPS 这是唯一接近 60 的模式。选择 **自动的** 让驾驶员协商或选择报告的组合之一。
3. 点击 **开始预览**。 FPS 读数测量来自源的帧。它可能与请求的速率不同，并且不测量监视器刷新。
4. 调整驾驶员在观看预览时显示的控件。更改分辨率、格式或帧速率会自动重新启动预览。

Open Camera 提供用于配置和测试网络摄像头的本地工作台。 0.2.4版本没有录音、效果处理或虚拟摄像机输出。

<h2 id="roadmap">路线图</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="相机基础、Linux 验证、捕获工具以及 AppImage、Debian 和 RPM 打包">

| 阶段 | 工作 |
| --- | --- |
| **有货·v0.2.4** | 相机选择、实时预览、源 FPS、驱动程序控制、诊断和三个 Linux 包。 |
| **下一篇 · 硬件与可靠性** | 验证 USB 和内置摄像头，检查硬件上宣传的 60 多种 FPS 模式，并在设备繁忙或拔掉插头时测试恢复。 |
| **计划·捕获工作流程** | 添加照片和视频捕获、叠加和效果，然后探索配置文件和虚拟相机输出。 |

该路线图设定了优先事项，但没有目标日期。

<h2 id="run-on-linux">📦 在Linux上运行</h2>

下载Open Camera **v0.2.4** 从 [GitHub 发布](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| 下载 | 安装或启动 |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` 在 Ubuntu 24.04 上 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` 在 Fedora 44 上 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` 然后 `./OpenCamera-0.2.4-x86_64.AppImage` 在带有 glibc 2.39 或更新版本的 x86_64 Linux 上 |

从桌面启动器或使用以下命令启动 DEB 或 RPM 安装 `open-camera`。如果 FUSE 不可用，请启动 AppImage `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

要检查下载情况，请保存 [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) 在包旁边并运行 `sha256sum -c --ignore-missing SHA256SUMS` 从该目录。

发布工作流程安装或启动了所有三个软件包，并使用合成源检查了实时预览。物理网络摄像头兼容性仍需要验证。

### 从源代码运行

使用带有 Python 3.10 +、GTK 4.8 +、libadwaita 1.4 + 和 GStreamer 1.20 + 的 Linux 桌面。使用系统 Python 从存储库文件夹运行，以便它可以找到发行版的 PyGObject 绑定。

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
<summary><b>软呢帽</b></summary>

```sh
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1 \
  gstreamer1-plugins-base gstreamer1-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>没有物理相机的测试</b></summary>

```sh
python3 -m open_camera --test-source
```

对于 DEB 或 RPM 安装使用 `open-camera --test-source`。选择 **GStreamer 测试模式**, 在 1280 × 720 下选择 30、60 或 120 FPS，然后单击 **开始预览**。这些速率描述了测试源。物理设备模式取决于相机和驱动程序。

</details>

### 故障排除

| 症状 | 要检查什么 |
| --- | --- |
| 相机不见了 | 重新连接，刷新设备列表查看 **诊断** 缺少组件或设备权限。 |
| 预览无法启动 | 关闭使用相机的应用程序，尝试 **自动的**, 然后检查 **诊断** 对于管道错误。编码模式可能需要安装解码器。 |
| 源 FPS 低于所选速率 | 检查该分辨率和格式下的可用速率。尝试较低的分辨率或不同的 USB 端口并比较测量结果。 |

报告问题时，请包括分布、相机型号、选择的拍摄模式以及相关文本 **诊断**.

<h2 id="design">设计</h2>

横幅显示 **交互式浏览器原型**。它包括模拟帧、效果和虚拟输出，因此可以独立于相机硬件来探索界面。下载 [独立的 HTML 原型](design/open-camera-interface-options.html) 并在浏览器中打开它。这 [主题样式表](design/open-camera-themes.css) 是单独提供的。

<details>
<summary><b>开发验证</b></summary>

| 小路 | 目的 |
| --- | --- |
| [打开相机/](open_camera/) | GTK 界面、GStreamer 预览和 V4L2 控件 |
| [测试/](tests/) | V4L2 解析和控制验证测试 |
| [设计/](design/) | 交互式原型、主题、图标和屏幕截图 |
| [资产/自述文件/](assets/readme/) | README 卡和导航按钮 |

```sh
python3 -m unittest discover -s tests -v
```

在 Linux 桌面上，使用 30 和 60 FPS 处的测试模式验证启动和停止。使用物理摄像头检查广告模式、测量的速率、驾驶员控制的变化以及断开连接行为。

要重新生成 README 面板，请在开发环境中安装 Pillow 并运行:

```sh
python3 tools/build_readme_assets.py
```

</details>

## 关于作者

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx 上 GitHub"></a>

**sailxx** 是 Open Camera 的创造者， [Tobi](https://github.com/sailxx/Tobi), 该项目激发了 README 的视觉风格。其他项目可在 [GitHub简介](https://github.com/sailxx).
