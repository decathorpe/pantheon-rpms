%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-bluetooth
%global appname io.elementary.wingpanel.bluetooth

Name:           wingpanel-indicator-bluetooth
Summary:        Bluetooth Indicator for wingpanel
Version:        7.0.1
Release:        1%{?dist}
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       bluez
Requires:       wingpanel%{?_isa}

Supplements:    (wingpanel%{?_isa} and bluez)


%description
A bluetooth indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang bluetooth-indicator

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/io.elementary.bluetooth.desktop

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/io.elementary.bluetooth-daemon.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f bluetooth-indicator.lang
%license COPYING
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/io.elementary.bluetooth-daemon.desktop
%{_bindir}/io.elementary.bluetooth
%{_libdir}/wingpanel/libbluetooth.so

%{_datadir}/applications/io.elementary.bluetooth.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.bluetooth.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
* Tue Nov 14 2023 Fabio Valentini <decathorpe@gmail.com> - 7.0.1-1
- Initial packaging

