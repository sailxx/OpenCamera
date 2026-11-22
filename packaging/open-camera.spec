Name:           open-camera
Version:        %{app_version}
Release:        1%{?dist}
Summary:        Native Linux camera workbench
# Source license has not yet been declared by the repository owner.
License:        LicenseRef-Unspecified
URL:            https://github.com/sailxx/OpenCamera
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3 >= 3.10
Requires:       python3-gobject
Requires:       gtk4 >= 4.8
Requires:       libadwaita >= 1.4
Requires:       gstreamer1 >= 1.20
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       librsvg2
Requires:       v4l-utils

%description
Preview a Video4Linux camera, inspect capture modes and adjust controls
exposed by the camera driver.

%prep
%autosetup

%install
bash packaging/stage.sh "%{buildroot}"

%files
%{_bindir}/open-camera
%{_datadir}/open-camera
%{_datadir}/applications/io.github.sailxx.OpenCamera.desktop
%{_datadir}/icons/hicolor/scalable/apps/io.github.sailxx.OpenCamera.svg
