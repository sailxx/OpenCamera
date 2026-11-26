[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [Čeština](README.cs.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Ελληνικά](README.el.md) · [Bahasa Indonesia](README.id.md) · [Gaeilge](README.ga.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Polski](README.pl.md) · [Română](README.ro.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Українська](README.uk.md) · [اردو](README.ur.md) · [ئۇيغۇرچە](README.ug.md) · **Tiếng Việt**

<div align="center">

<img src="design/open-camera.png" width="104" alt="Open Camera">

# Open Camera


**Bàn làm việc Linux gốc dành cho máy ảnh Video4Linux.**

Chọn một webcam, xem bản xem trước trực tiếp của nó, chọn chế độ chụp và điều chỉnh các điều khiển do trình điều khiển máy ảnh hiển thị.

<img src="https://img.shields.io/badge/status-early%20development-2E9BFF" alt="Tình trạng: phát triển sớm">
<img src="https://img.shields.io/badge/platform-Linux-2E9BFF" alt="Linux">
<img src="https://img.shields.io/badge/UI-GTK%204%20%7C%20libadwaita-2E9BFF" alt="GTK 4 và libadwaita">
<img src="https://img.shields.io/badge/video-GStreamer%20%7C%20V4L2-2E9BFF" alt="GStreamer và V4L2">

<br>

<img src="assets/readme/hero.svg" width="100%" alt="Open Camera, bàn làm việc dành cho máy ảnh Linux nguyên gốc. Hình ảnh cho thấy nguyên mẫu thiết kế tương tác.">

<a href="#run-on-linux"><img src="assets/readme/btn-linux.svg" height="48" alt="Chạy trên Linux"></a>&nbsp; &nbsp;<a href="#design"><img src="assets/readme/btn-design.svg" height="48" alt="Xem thiết kế"></a>&nbsp; &nbsp;<a href="#roadmap"><img src="assets/readme/btn-roadmap.svg" height="48" alt="Xem lộ trình"></a>

</div>

<br>

<img src="assets/readme/features.svg" width="100%" alt="Khám phá máy ảnh, xem trước trực tiếp, chế độ chụp, điều khiển phần cứng, chẩn đoán và giao diện">

<details>
<summary><b>Tìm hiểu thêm về các tính năng</b></summary>

- **Máy ảnh.** Chọn thiết bị V4L2 và quét lại sau khi kết nối hoặc ngắt kết nối camera.
- **Xem trước trực tiếp.** Bắt đầu và dừng luồng cục bộ và xem tốc độ ghi được đo tại nguồn. Khi có sẵn, ứng dụng sẽ vẽ khung bằng bồn rửa GStreamer GTK 4. Nó cũng hỗ trợ dự phòng kết cấu GTK có giới hạn.
- **Các chế độ chụp.** Sử dụng thương lượng tự động hoặc chọn kết hợp được quảng cáo giữa độ phân giải, định dạng pixel và tốc độ khung hình. Thay đổi chế độ giữa các phiên xem trước.
- **Điều khiển phần cứng.** Chỉnh sửa các điều khiển số, chuyển đổi và menu do trình điều khiển báo cáo. Các thay đổi sẽ được gửi tới trình điều khiển khi bạn thực hiện chúng.
- **Chẩn đoán và sự xuất hiện.** Kiểm tra quyền truy cập thiết bị, thiếu phần phụ thuộc và lỗi xem trước. Cài đặt cung cấp hệ thống, giao diện sáng và tối.

</details>

<br>

<img src="assets/readme/workflow.svg" width="100%" alt="Chọn thiết bị và chế độ, bắt đầu xem trước, sau đó điều chỉnh các điều khiển máy ảnh được hỗ trợ">

<br>

<img src="assets/readme/states.svg" width="100%" alt="Trạng thái xem trước: đã dừng, đang bắt đầu, đang chụp và bị gián đoạn">

<br>

<img src="assets/readme/numbers.svg" width="100%" alt="Mẫu thử nghiệm tổng hợp ở 30, 60 hoặc 120 FPS, cùng với ba chế độ xuất hiện gốc">

## Bắt đầu nhanh

1. Kết nối webcam và chọn nó trong **Thiết bị**. Sử dụng nút làm mới nếu nó được cắm sau khi mở ứng dụng.
2. Open Camera chọn 60 FPS khi máy ảnh báo cáo hoặc 59.94 FPS khi đó là chế độ duy nhất gần 60. Chọn **Tự động** để người lái xe thương lượng hoặc chọn một trong các kết hợp được báo cáo.
3. nhấp chuột **Bắt đầu xem trước**. Đầu đọc FPS đo các khung hình đến từ nguồn. Nó có thể khác với tốc độ được yêu cầu và không đo lường tốc độ làm mới màn hình.
4. Điều chỉnh các điều khiển mà trình điều khiển của bạn hiển thị trong khi xem bản xem trước. Việc thay đổi độ phân giải, định dạng hoặc tốc độ khung hình sẽ tự động khởi động lại bản xem trước.

Open Camera cung cấp bàn làm việc cục bộ để định cấu hình và kiểm tra webcam. Phiên bản 0.2.4 không có tính năng ghi hình, xử lý hiệu ứng hay xuất camera ảo.

<h2 id="roadmap">Lộ trình</h2>

<img src="assets/readme/roadmap.svg" width="100%" alt="Nền tảng máy ảnh, xác thực Linux, công cụ chụp ảnh và gói AppImage, Debian và RPM">

| Sân khấu | Công việc |
| --- | --- |
| **Có sẵn · v0.2.4** | Lựa chọn máy ảnh, xem trước trực tiếp, nguồn FPS, điều khiển trình điều khiển, chẩn đoán và ba gói Linux. |
| **Tiếp theo · Phần cứng và độ tin cậy** | Xác thực USB và camera tích hợp, kiểm tra hơn 60 chế độ FPS được quảng cáo trên phần cứng và kiểm tra khả năng khôi phục khi thiết bị bận hoặc đã rút phích cắm. |
| **Đã lên kế hoạch · Ghi lại quy trình làm việc** | Thêm tính năng chụp ảnh và quay video, lớp phủ và hiệu ứng, sau đó khám phá cấu hình và đầu ra của máy ảnh ảo. |

Lộ trình đặt ra các ưu tiên mà không có ngày mục tiêu.

<h2 id="run-on-linux">📦 Chạy trên Linux</h2>

Tải xuống Open Camera **v0.2.4** từ [GitHub phát hành](https://github.com/sailxx/OpenCamera/releases/tag/v0.2.4).

| Tải xuống | Cài đặt hoặc khởi chạy |
| --- | --- |
| [DEB](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera_0.2.4_all.deb) | `sudo apt install ./open-camera_0.2.4_all.deb` trên Ubuntu 24.04 |
| [RPM](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/open-camera-0.2.4-1.fc44.noarch.rpm) | `sudo dnf install ./open-camera-0.2.4-1.fc44.noarch.rpm` trên Fedora 44 |
| [AppImage](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/OpenCamera-0.2.4-x86_64.AppImage) | `chmod +x OpenCamera-0.2.4-x86_64.AppImage` sau đó `./OpenCamera-0.2.4-x86_64.AppImage` trên x86_64 Linux với glibc 2.39 hoặc mới hơn |

Bắt đầu cài đặt DEB hoặc RPM từ trình khởi chạy trên máy tính để bàn hoặc bằng `open-camera`. Nếu FUSE không khả dụng, hãy khởi chạy AppImage với `./OpenCamera-0.2.4-x86_64.AppImage --appimage-extract-and-run`.

Để kiểm tra tải xuống, hãy lưu [SHA256SUMS](https://github.com/sailxx/OpenCamera/releases/download/v0.2.4/SHA256SUMS) bên cạnh gói và chạy `sha256sum -c --ignore-missing SHA256SUMS` từ thư mục đó.

Quy trình phát hành đã cài đặt hoặc khởi chạy cả ba gói và kiểm tra bản xem trước trực tiếp bằng nguồn tổng hợp. Khả năng tương thích webcam vật lý vẫn cần được xác nhận.

### Chạy từ nguồn

Sử dụng máy tính để bàn Linux với Python 3.10+, GTK 4.8+, libadwaita 1.4+ và GStreamer 1.20+. Chạy từ thư mục kho lưu trữ bằng hệ thống Python để nó có thể tìm thấy các ràng buộc PyGObject của bản phân phối.

<details open>
<summary><b>Ubuntu 24.04 và mới hơn</b></summary>

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
<summary><b>Kiểm tra mà không cần máy ảnh vật lý</b></summary>

```sh
python3 -m open_camera --test-source
```

Để sử dụng cài đặt DEB hoặc RPM `open-camera --test-source`. Lựa chọn **Mẫu thử nghiệm GStreamer**, chọn 30, 60 hoặc 120 FPS ở 1280 × 720 và nhấp vào **Bắt đầu xem trước**. Các tỷ lệ này mô tả nguồn thử nghiệm. Các chế độ của thiết bị vật lý phụ thuộc vào máy ảnh và trình điều khiển.

</details>

### Khắc phục sự cố

| Triệu chứng | Những gì cần kiểm tra |
| --- | --- |
| Máy ảnh bị thiếu | Kết nối lại, làm mới danh sách thiết bị và kiểm tra **Chẩn đoán** để biết các thành phần hoặc quyền của thiết bị bị thiếu. |
| Xem trước không khởi động được | Đóng ứng dụng bằng camera, thử **Tự động**, sau đó kiểm tra **Chẩn đoán** đối với lỗi đường ống. Các chế độ được mã hóa có thể yêu cầu cài đặt bộ giải mã. |
| Nguồn FPS thấp hơn tỷ lệ đã chọn | Kiểm tra tỷ lệ có sẵn ở độ phân giải và định dạng đó. Hãy thử độ phân giải thấp hơn hoặc cổng USB khác và so sánh số đo. |

Khi báo cáo sự cố, hãy bao gồm thông tin phân phối, kiểu máy ảnh, chế độ chụp đã chọn và văn bản có liên quan từ **Chẩn đoán**.

<h2 id="design">Thiết kế</h2>

Biểu ngữ cho thấy **nguyên mẫu trình duyệt tương tác**. Nó bao gồm các khung hình, hiệu ứng và đầu ra ảo mô phỏng để giao diện có thể được khám phá độc lập với phần cứng máy ảnh. Tải xuống [nguyên mẫu HTML khép kín](design/open-camera-interface-options.html) và mở nó trong trình duyệt. các [biểu định kiểu chủ đề](design/open-camera-themes.css) có sẵn riêng biệt.

<details>
<summary><b>Phát triển và xác minh</b></summary>

| Con đường | Mục đích |
| --- | --- |
| [open_máy ảnh/](open_camera/) | Giao diện GTK, xem trước GStreamer và điều khiển V4L2 |
| [kiểm tra/](tests/) | Các thử nghiệm xác thực phân tích cú pháp và kiểm soát V4L2 |
| [thiết kế/](design/) | Nguyên mẫu tương tác, chủ đề, biểu tượng và ảnh chụp màn hình |
| [tài sản/readme/](assets/readme/) | Thẻ README và nút điều hướng |

```sh
python3 -m unittest discover -s tests -v
```

Trên máy tính để bàn Linux, hãy xác minh bắt đầu và dừng bằng mẫu thử nghiệm ở 30 và 60 FPS . Với camera vật lý, hãy kiểm tra các chế độ được quảng cáo, tốc độ đo được, các thay đổi đối với điều khiển của trình điều khiển và hành vi ngắt kết nối.

Để tạo lại bảng README, hãy cài đặt Gối trong môi trường phát triển của bạn và chạy:

```sh
python3 tools/build_readme_assets.py
```

</details>

## Về tác giả

<a href="https://github.com/sailxx"><img src="assets/readme/author.svg" width="100%" alt="sailxx trên GitHub"></a>

**sailxx** là người tạo ra Open Camera và [Tobi](https://github.com/sailxx/Tobi), dự án đã truyền cảm hứng cho phong cách hình ảnh của chiếc README này. Các dự án khác có sẵn trên [Hồ sơ GitHub](https://github.com/sailxx).
