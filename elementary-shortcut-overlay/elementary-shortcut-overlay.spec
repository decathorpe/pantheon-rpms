%global srcname shortcut-overlay
%global appname io.elementary.shortcut-overlay

Name:           elementary-shortcut-overlay
Summary:        Native, OS-wide shortcut overlay
Version:        8.1.0
Release:        %autorelease
License:        #GPLv3

URL:            https://github.com/elementary/shortcut-overlay
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite-7) >= 7.3.0
BuildRequires:  pkgconfig(gtk4)

%description
This GTK+ applet reads window manager and OS keyboard shortcuts from
dconf and exposes them to the user when launched. Inspired by the
similar feature of Ubuntu Unity introduced in Ubuntu 12.04.

The shortcut window opens centered on the primary display. The gear in
the titlebar opens the system keyboard settings.


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
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license LICENSE
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
%autochangelog
