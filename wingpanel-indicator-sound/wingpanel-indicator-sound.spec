%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-sound
%global appname io.elementary.wingpanel.sound

Name:           wingpanel-indicator-sound
Summary:        Sound Indicator for wingpanel
Version:        7.0.0
Release:        1%{?dist}
License:        GPL-3.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
A sound indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang sound-indicator

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f sound-indicator.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel/libsound.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.sound.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
* Tue Nov 14 2023 Fabio Valentini <decathorpe@gmail.com> - 7.0.0-1
- Initial packaging

