%global __provides_exclude_from ^%{_libdir}/gala/.*\\.so$

Name:           gala
Version:        7.1.3
Release:        1%{?dist}
Summary:        Gala window manager
License:        GPL-3.0-or-later AND LGPL-3.0-or-later

URL:            https://github.com/elementary/gala
Source:         %{url}/archive/%{version}/gala-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala >= 0.46

%if 0%{?fedora} >= 39
BuildRequires:  pkgconfig(libmutter-13)
BuildRequires:  pkgconfig(mutter-clutter-13)
BuildRequires:  pkgconfig(mutter-cogl-13)
BuildRequires:  pkgconfig(mutter-cogl-pango-13)
%endif
%if 0%{?fedora} == 38
BuildRequires:  pkgconfig(libmutter-12)
BuildRequires:  pkgconfig(mutter-clutter-12)
BuildRequires:  pkgconfig(mutter-cogl-12)
BuildRequires:  pkgconfig(mutter-cogl-pango-12)
%endif

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.44.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon) >= 3.15.2
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libsystemd)

# gala's multitasking view is activated via dbus
Requires:       dbus

# GTK-based notifications use this new notifications server
Requires:       elementary-notifications

# https://bugzilla.redhat.com/show_bug.cgi?id=605675
Provides:       firstboot(windowmanager) = gala

%description
Gala is Pantheon's Window Manager, part of the elementary project.


%package        x11
Summary:        Gala window manager X11 support
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       gnome-session
Requires:       xorg-x11-server-Xorg

%description    x11
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the support files for running gala on X11.


%package        wayland
Summary:        Gala window manager Wayland support
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       gnome-session
Requires:       xorg-x11-server-Xwayland

%description    wayland
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the support files for running gala on Wayland.


%package        devel
Summary:        Gala window manager development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the development headers.


%prep
%autosetup -n gala-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang gala

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/gala*.desktop

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/gala-daemon.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml


%post x11
%systemd_user_post io.elementary.gala@x11.service

%post wayland
%systemd_user_post io.elementary.gala@wayland.service

%preun x11
%systemd_user_preun io.elementary.gala@x11.service

%preun wayland
%systemd_user_preun io.elementary.gala@wayland.service

%postun x11
%systemd_user_postun io.elementary.gala@x11.service

%postun wayland
%systemd_user_postun io.elementary.gala@wayland.service


%files -f gala.lang
%license COPYING
%doc AUTHORS
%doc HACKING
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/gala-daemon.desktop

%{_bindir}/gala
%{_bindir}/gala-daemon

%{_libdir}/gala/
%{_libdir}/libgala.so.0
%{_libdir}/libgala.so.0.0.0

%{_datadir}/applications/gala*.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%{_datadir}/glib-2.0/schemas/20_elementary.pantheon.wm.gschema.override
%{_datadir}/metainfo/%{name}.metainfo.xml

%{_userunitdir}/io.elementary.gala.target

%files x11
%{_userunitdir}/io.elementary.gala@x11.service

%files wayland
%{_userunitdir}/io.elementary.gala@wayland.service

%files devel
%{_includedir}/gala/

%{_libdir}/libgala.so
%{_libdir}/pkgconfig/gala.pc

%{_datadir}/vala/vapi/gala.deps
%{_datadir}/vala/vapi/gala.vapi


%changelog
* Sun Nov 12 2023 Fabio Valentini <decathorpe@gmail.com> - 7.1.3-1
- Update to version 7.1.3.

* Tue May 23 2023 Fabio Valentini <decathorpe@gmail.com> - 7.0.3-1
- Initial packaging

