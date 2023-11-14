%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-a11y
%global appname io.elementary.wingpanel.a11y

Name:           wingpanel-indicator-a11y
Summary:        Wingpanel Universal Access Indicator
Version:        1.0.2
Release:        1%{?dist}
License:        GPLv2

URL:            https://github.com/elementary/wingpanel-indicator-a11y
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
%{summary}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang a11y-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.metainfo.xml


%files -f a11y-indicator.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel/liba11y.so
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.a11y.gschema.xml
%{_metainfodir}/%{appname}.metainfo.xml


%changelog
* Tue Nov 14 2023 Fabio Valentini <decathorpe@gmail.com> - 1.0.2-1
- Initial packaging

