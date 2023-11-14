%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-nightlight
%global appname io.elementary.wingpanel.nightlight

Name:           wingpanel-indicator-nightlight
Summary:        Night Light Indicator for wingpanel
Version:        2.1.2
Release:        1%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/wingpanel-indicator-nightlight
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A wingpanel indicator for Night Light.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang nightlight-indicator

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f nightlight-indicator.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel/libnightlight.so

%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
* Tue Nov 14 2023 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-1
- Initial packaging

