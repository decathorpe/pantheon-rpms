Name:           pantheon-wayland
Version:        1.0.0
Release:        %autorelease
Summary:        Wayland integration library to the Pantheon Desktop
# vala sources: LGPL-3.0-or-later, wayland protocol: LGPL-2.1-or-later
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later

URL:            https://github.com/elementary/pantheon-wayland
Source:         %{url}/archive/%{version}/pantheon-wayland-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  wayland-devel

BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk4) >= 4.4
BuildRequires:  pkgconfig(gtk4-wayland) >= 4.4

%description
Pantheon Wayland is an utility library made exclusively for the Pantheon
Desktop utilities.


%package        devel
Summary:        Wayland integration library to the Pantheon Desktop (development files)
Requires:       pantheon-wayland%{?_isa} = %{version}-%{release}

%description    devel
Pantheon Wayland is an utility library made exclusively for the Pantheon
Desktop utilities.

This package contains files useful for developing against the
pantheon-desktop library.


%prep
%autosetup -n pantheon-wayland-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install


%files
%license COPYING
%doc README.md

%{_libdir}/libpantheon-wayland.so.1
%{_libdir}/libpantheon-wayland.so.1.0.0
%{_libdir}/girepository-1.0/PantheonWayland-1.typelib
%{_libdir}/pkgconfig/pantheon-wayland-1.pc

%files devel
%dir %{_includedir}/pantheon-wayland-1/
%{_includedir}/pantheon-wayland-1/pantheon-wayland.h

%{_libdir}/libpantheon-wayland.so

%{_datadir}/gir-1.0/PantheonWayland-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/pantheon-wayland-1.{deps,vapi}


%changelog
%autochangelog
