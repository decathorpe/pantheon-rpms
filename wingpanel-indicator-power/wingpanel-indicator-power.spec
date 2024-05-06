%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-power
%global appname io.elementary.wingpanel.power

Name:           wingpanel-indicator-power
Summary:        Power indicator for wingpanel
Version:        6.2.1
Release:        1%{?dist}
License:        GPL-2.0-or-later

URL:            https://github.com/elementary/wingpanel-indicator-power
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.57.0
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A power indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang power-indicator

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f power-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libpower.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.power.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon May 06 2024 Fabio Valentini <decathorpe@gmail.com> - 6.2.1-1
- Initial packaging

