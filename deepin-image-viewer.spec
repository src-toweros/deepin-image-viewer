Name:           deepin-image-viewer
Version:        5.6.3.49
Release:        1
Summary:        Deepin Image Viewer
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-image-viewer
Source0:        %{name}_%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires: qt5-devel

BuildRequires:  freeimage-devel
BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires:  dtkgui-devel
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  udisks2-qt5-devel
BuildRequires:  libgio-qt libgio-qt-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%setup -q

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
mkdir build && pushd build
%qmake_qt5 PREFIX=%{_prefix} VERSION=%{version} DEFINES+="VERSION=%{version}" ../
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_qt5_plugindir}/imageformats/*.so
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{name}/
%{_datadir}/dman/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.6.3.49-3
- Update 5.6.3.49

* Fri Sep 4 2020 chenbo pan <panchenbo@uniontech.com> - 1.3.17-3
- fix compile fail

* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 1.3.17-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.3.17-1
- Package init
