%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-network
%global appname io.elementary.wingpanel.network

Name:           wingpanel-indicator-network
Summary:        Network Indicator for wingpanel
Version:        7.1.0
Release:        1%{?dist}
License:        LGPL-2.1-or-later AND GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/wingpanel-indicator-network
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm) >= 1.24
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       network-manager-applet%{?_isa}
Requires:       wingpanel%{?_isa}

Supplements:    wingpanel%{?_isa}


%description
A network indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang network-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f network-indicator.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel/libnetwork.so

%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
* Mon May 06 2024 Fabio Valentini <decathorpe@gmail.com> - 7.1.0-1
- Initial packaging

