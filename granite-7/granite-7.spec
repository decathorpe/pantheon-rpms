%global _description %{expand:
Granite is a companion library for GTK and GLib. Among other things, it
provides complex widgets and convenience functions designed for use in
apps built for elementary OS.}

Name:           granite-7
Version:        7.2.0
Release:        1%{?dist}
Summary:        Extend GTK with common widgets and utilities
License:        LGPL-3.0-or-later

URL:            https://github.com/elementary/granite
Source:         %{url}/archive/%{version}/granite-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.49
BuildRequires:  sassc
BuildRequires:  vala >= 0.48.2

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.4.0

%description %{_description}


%package        devel
Summary:        Granite Toolkit (development headers)

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description    devel %{_description}

This package contains the development headers.


%prep
%autosetup -n granite-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang granite-7

# remove the specified stock icon from appdata (invalid for desktop components)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/granite-7.appdata.xml


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/io.elementary.granite-7.demo.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/granite-7.appdata.xml


%files -f granite-7.lang
%doc README.md
%license COPYING
%{_libdir}/libgranite-7.so.7
%{_libdir}/libgranite-7.so.7.*
%{_libdir}/girepository-1.0/Granite-7.0.typelib
%{_metainfodir}/%{name}.appdata.xml

%files devel
%{_bindir}/granite-7-demo
%{_libdir}/libgranite-7.so
%{_libdir}/pkgconfig/granite-7.pc
%{_includedir}/granite-7/
%{_datadir}/applications/io.elementary.granite-7.demo.desktop
%{_datadir}/icons/hicolor/*/apps/io.elementary.granite-7.svg
%{_datadir}/gir-1.0/Granite-7.0.gir
%{_datadir}/vala/vapi/granite-7.deps
%{_datadir}/vala/vapi/granite-7.vapi


%changelog
* Tue May 23 2023 Fabio Valentini <decathorpe@gmail.com> - 7.2.0-1
- Initial packaging

