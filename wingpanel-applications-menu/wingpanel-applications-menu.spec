%global appname io.elementary.wingpanel.applications-menu

%global __provides_exclude_from ^%{_libdir}/(wingpanel|%{appname})/.*\\.so$

Name:           wingpanel-applications-menu
Summary:        Lightweight and stylish app launcher
Version:        2.11.1
Release:        1%{?dist}
# - GPL-3.0-or-later: applies to most applications-menu sources
# - GPL-2.0-or-later: applies to all files derived from the synapse launcher
License:        GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/applications-menu
Source:         %{url}/archive/%{version}/applications-menu-%{version}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.32.1

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.1.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(wingpanel) >= 2.1.0

Requires:       redhat-menus

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
The lightweight and stylish app launcher from elementary.


%prep
%autosetup -n applications-menu-%{version} -p1


%build
%meson -Dwith-zeitgeist=false
%meson_build


%install
%meson_install

%find_lang slingshot


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f slingshot.lang
%license COPYING
%doc README.md

%{_libdir}/%{appname}/
%{_libdir}/wingpanel/libslingshot.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.applications-menu.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Tue May 23 2023 Fabio Valentini <decathorpe@gmail.com> - 2.11.1-1
- Initial packaging

