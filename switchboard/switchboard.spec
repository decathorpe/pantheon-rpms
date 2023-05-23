%global appname io.elementary.switchboard

Name:           switchboard
Version:        6.0.2
Release:        1%{?dist}
Summary:        Modular Desktop Settings Hub
# - LGPL-2.1-or-later: everything except src/Widgets/*.vala
# - GPL-2.0-or-later: src/Widgets/*.vala
License:        LGPL-2.1-or-later and GPL-2.0-or-later

URL:            https://github.com/elementary/switchboard
Source0:        %{url}/archive/%{version}/switchboard-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0

Requires:       hicolor-icon-theme

%description
Extensible System Settings application.


%package        devel
Summary:        Modular Desktop Settings Hub (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Extensible System Settings application.

This package contains the files required for developing plugs for
switchboard.


%prep
%autosetup -n switchboard-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# create plug directories
mkdir -p %{buildroot}/%{_libdir}/%{name}

mkdir -p %{buildroot}/%{_libdir}/%{name}/hardware
mkdir -p %{buildroot}/%{_libdir}/%{name}/network
mkdir -p %{buildroot}/%{_libdir}/%{name}/personal
mkdir -p %{buildroot}/%{_libdir}/%{name}/system


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%dir %{_libdir}/switchboard
%dir %{_libdir}/switchboard/*

%{_libdir}/libswitchboard-2.0.so.0
%{_libdir}/libswitchboard-2.0.so.2.0

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%files devel
%{_includedir}/switchboard-2.0/

%{_libdir}/libswitchboard-2.0.so
%{_libdir}/pkgconfig/switchboard-2.0.pc

%{_datadir}/vala/vapi/switchboard-2.0.deps
%{_datadir}/vala/vapi/switchboard-2.0.vapi


%changelog
* Tue May 23 2023 Fabio Valentini <decathorpe@gmail.com> - 6.0.2-1
- Initial packaging

