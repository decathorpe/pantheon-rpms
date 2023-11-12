%global srcname notifications
%global appname io.elementary.notifications

Name:           elementary-notifications
Version:        7.0.1
Release:        1%{?dist}
Summary:        GTK Notifications Server
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/notifications
Source:         %{url}/archive/%{version}/notifications-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libhandy-1)

%description
elementary Notifications is a GTK notification server for Pantheon.

%package demo
Summary:        GTK Notifications Server (demo application)
Requires:       %{name} = %{version}-%{release}

%description demo
elementary Notifications is a GTK notification server for Pantheon.

This package contains a demo application.


%prep
%autosetup -n notifications-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

# remove the specified stock icon from appdata (invalid for desktop components)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/%{appname}

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml

%files demo
%{_bindir}/%{appname}.demo

%{_datadir}/applications/%{appname}.demo.desktop


%changelog
* Sun Nov 12 2023 Fabio Valentini <decathorpe@gmail.com> - 7.0.1-1
- Initial packaging

