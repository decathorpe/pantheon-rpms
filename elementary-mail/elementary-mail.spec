%global srcname mail
%global appname io.elementary.mail

%global __provides_exclude_from ^%{_libdir}/%{appname}/webkit2/.*\\.so$

Name:           elementary-mail
Summary:        Mail app designed for elementary
Version:        7.2.0
Release:        1%{?dist}
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-only

URL:            https://github.com/elementary/mail
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(camel-1.2) >= 3.28
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.28
BuildRequires:  pkgconfig(libedataserverui-1.2) >= 3.28
BuildRequires:  pkgconfig(libhandy-1) >= 1.1.90
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)

%if 0%{?fedora} >= 39
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.1)
%endif

%if 0%{?fedora} == 38
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.28
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.0) >= 2.28
%endif

Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
* Wed Nov 15 2023 Fabio Valentini <decathorpe@gmail.com> - 7.2.0-1
- Initial packaging

