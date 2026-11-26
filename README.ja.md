[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · **日本語** · [한국어](README.ko.md) · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · [Tiếng Việt](README.vi.md)

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Video4Linux カメラ用のネイティブ Linux ワークベンチ。**

Web カメラを選択し、ライブ プレビューを確認し、キャプチャ モードを選択して、カメラ ドライバーによって公開されるコントロールを調整します。

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="ステータス: 開発初期">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 とリバドワイタ">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamerとV4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera 、ネイティブ Linux カメラ ワークベンチ。画像はインタラクティブなデザインのプロトタイプを示しています。">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Linuxで実行"></a>&nbsp;&nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="デザインを見る"></a>&nbsp;&nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="ロードマップを見る"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="カメラの検出、ライブ プレビュー、キャプチャ モード、ハードウェア コントロール、診断、および外観">

<details>
<summary><b>機能の詳細</b></summary>

- **カメラ。** V4L2デバイスを選択し、カメラの接続または切断後に再スキャンしてください。
- **ライブプレビュー。** ローカル ストリームを開始および停止し、ソースで測定されたキャプチャ レートを確認します。利用可能な場合、アプリは GStreamer GTK 4 シンクを使用してフレームをペイントします。制限付きの GTK テクスチャ フォールバックもサポートします。
- **キャプチャモード。** 自動ネゴシエーションを使用するか、公開されている解像度、ピクセル形式、およびフレーム レートの組み合わせを選択します。プレビュー セッション間でモードを変更します。
- **ハードウェア制御。** ドライバーによって報告された数値、スイッチ、およびメニュー コントロールを編集します。変更を行うと、変更がドライバーに送信されます。
- **診断と外観。** デバイスのアクセス、欠落している依存関係、およびプレビュー エラーを検査します。設定では、システム、明暗の外観を提供します。

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="デバイスとモードを選択し、プレビューを開始して、サポートされているカメラ コントロールを調整します">

<br>

<img src="assets/readme/states.svg" width="100%" alt="プレビューの状態: 停止、開始、キャプチャ、中断">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="30、60、または 120 FPS の合成テスト パターン、および 3 つのネイティブ外観モード">

## クイックスタート

1. Webカメラを接続して選択します **デバイス**。アプリを開いた後に更新ボタンが接続されている場合は、更新ボタンを使用します。
2. Open Camera は、カメラがそれを報告する場合は 60 FPS を選択し、それが唯一の 60 に近いモードである場合は 59.94 FPS を選択します。選ぶ **自動** ドライバーが交渉するか、報告された組み合わせの 1 つを選択できるようにします。
3. クリック **プレビューを開始**。 FPS の読み出しは、ソースから到着するフレームを測定します。要求されたレートと異なる場合があり、モニターのリフレッシュは測定されません。
4. プレビューを見ながら、ドライバーが公開するコントロールを調整します。解像度、形式、またはフレーム レートを変更すると、プレビューが自動的に再開されます。

Open Camera は、Web カメラの構成とテストのためのローカル ワークベンチを提供します。バージョン 0.2.4 には、録画、エフェクト処理、または仮想カメラ出力がありません。

<h2 id="roadmap">ロードマップ</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="カメラ基盤、Linux 検証、キャプチャ ツール、および AppImage、Debian および RPM パッケージ">

| ステージ | 仕事 |
| --- | --- |
| **在庫あり・v0.2.4** | カメラの選択、ライブ プレビュー、ソース FPS 、ドライバー コントロール、診断、および 3 つの Linux パッケージ。 |
| **次へ · ハードウェアと信頼性** | USB と内蔵カメラを検証し、ハードウェアで宣伝されている 60 以上の FPS モードを確認し、デバイスがビジー状態または接続されていないときの回復をテストします。 |
| **計画されたキャプチャ ワークフロー** | 写真とビデオのキャプチャ、オーバーレイ、エフェクトを追加し、プロファイルと仮想カメラ出力を探索します。 |

ロードマップでは、目標日付を設定せずに優先順位を設定します。

<h2 id="run-on-linux">📦 Linuxで実行</h2>

ダウンロード Open Camera **v0.2.4** から [GitHub リリース](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| ダウンロード | インストールまたは起動 |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` Ubuntu 24.04上 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` Fedora 44 で |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` それから `./OpenCamera-0.2.4-x86_64.AppImage` x86_64 Linux (glibc 2.39 以降) |

デスクトップランチャーから、または次のコマンドを使用して、DEB または RPM のインストールを開始します。 `open-camera`。 FUSE が利用できない場合は、次のコマンドで AppImage を起動します。 `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

ダウンロードを確認するには、保存してください [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) パッケージの横に置いて実行します `sha256sum -c --ignore-missing SHA256SUMS` そのディレクトリから。

リリース ワークフローでは、3 つのパッケージすべてをインストールまたは起動し、合成ソースを使用してライブ プレビューをチェックしました。物理的な Web カメラの互換性はまだ検証が必要です。

### ソースから実行

Python 3.10 +、GTK 4.8 +、libadwaita 1.4 +、および GStreamer 1.20 + を備えた Linux デスクトップを使用します。システム Python を使用してリポジトリ フォルダーから実行して、ディストリビューションの PyGObject バインディングを見つけられるようにします。

<details open>
<summary><b>Ubuntu 24.04 以降</b></summary>

```sh
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 \
  gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>フェドーラ</b></summary>

```sh
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1 \
  gstreamer1-plugins-base gstreamer1-plugins-good v4l-utils
python3 -m open_camera
```

</details>

<details>
<summary><b>物理的なカメラを使用しないテスト</b></summary>

```sh
python3 -m open_camera --test-source
```

DEB または RPM のインストールの場合は、 `open-camera --test-source`。選択 **GStreamer テスト パターン**, 1280 × 720 で 30、60、または 120 FPS を選択し、クリックします **プレビューを開始**。これらのレートはテストソースを表します。物理デバイスのモードはカメラとドライバーによって異なります。

</details>

### トラブルシューティング

| 症状 | 何を確認するか |
| --- | --- |
| カメラがありません | 再接続し、デバイスリストを更新して確認してください **診断** 欠落しているコンポーネントまたはデバイスの権限について。 |
| プレビューが開始できない | カメラを使用しているアプリを閉じて試してください **自動**, それからチェックしてください **診断** パイプラインエラーの場合。エンコードされたモードでは、デコーダのインストールが必要な場合があります。 |
| ソース FPS は選択されたレートを下回っています | その解像度と形式で利用可能なレートを確認してください。より低い解像度または別の USB ポートを試して、測定を比較してください。 |

問題を報告するときは、ディストリビューション、カメラ モデル、選択したキャプチャ モード、および関連するテキストを含めてください。 **診断**.

<h2 id="design">デザイン</h2>

バナーに表示されるのは、 **インタラクティブブラウザのプロトタイプ**。シミュレートされたフレーム、エフェクト、仮想出力が含まれているため、カメラ ハードウェアに関係なくインターフェイスを探索できます。ダウンロード [内蔵型 HTML プロトタイプ](design/open-camera-interface-options.html) そしてブラウザで開きます。の [テーマのスタイルシート](design/open-camera-themes.css) 別途ご用意しております。

<details>
<summary><b>開発と検証</b></summary>

| パス | 目的 |
| --- | --- |
| [オープンカメラ/](open_camera/) | GTK インターフェイス、GStreamer プレビュー、および V4L2 コントロール |
| [テスト/](tests/) | V4L2 の解析と制御の検証のテスト |
| [デザイン/](design/) | インタラクティブなプロトタイプ、テーマ、アイコン、スクリーンショット |
| [アセット/readme/](assets/readme/) | README カードとナビゲーション ボタン |

```sh
python3 -m unittest discover -s tests -v
```

Linux デスクトップで、30 および 60 FPS のテスト パターンを使用して開始と停止を確認します。物理的なカメラを使用して、宣伝されたモード、測定されたレート、ドライバー制御の変更、および切断動作を確認します。

README パネルを再生成するには、開発環境に Pillow をインストールして実行します。:

```sh
python3 tools/build_readme_assets.py
```

</details>

## 著者について

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx 上の GitHub"></a>

**sailxx** Open Cameraの作者です [Tobi](https://github.com/sailxx/Tobi), このREADMEのビジュアルスタイルにインスピレーションを与えたプロジェクト。他のプロジェクトは、 [GitHub プロフィール](https://github.com/sailxx).
