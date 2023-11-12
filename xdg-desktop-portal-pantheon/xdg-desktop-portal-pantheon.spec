%global srcname portals
%global appname io.elementary.portals

Name:           xdg-desktop-portal-pantheon
Version:        7.1.1
Release:        1%{?dist}
Summary:        Portal implementations for Pantheon
License:        GPLv3+

URL:            https://github.com/elementary/portals
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-x11)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)

Requires:       xdg-desktop-portal

%description
%{summary}.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang xdg-desktop-portal-pantheon


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.metainfo.xml


%post
%systemd_user_post xdg-desktop-portal-pantheon.service


%preun
%systemd_user_preun xdg-desktop-portal-pantheon.service


%files -f xdg-desktop-portal-pantheon.lang
%license COPYING
%doc README.md

%{_libexecdir}/xdg-desktop-portal-pantheon

%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.pantheon.service
%{_datadir}/xdg-desktop-portal/portals/pantheon.portal

%{_metainfodir}/%{appname}.metainfo.xml
%{_userunitdir}/xdg-desktop-portal-pantheon.service


%changelog
* Sun Nov 12 2023 Fabio Valentini <decathorpe@gmail.com> - 7.1.1-1
- Initial packaging

