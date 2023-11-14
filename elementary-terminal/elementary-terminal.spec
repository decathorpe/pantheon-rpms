%global srcname terminal
%global appname io.elementary.terminal

Name:           elementary-terminal
Summary:        The terminal of the 21st century
Version:        6.1.2
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.40.0
BuildRequires:  xorg-x11-server-Xvfb

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gobject-2.0) >= 2.40
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(granite) >= 6.1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(vte-2.91) >= 0.59

Requires:       hicolor-icon-theme

%description
A super lightweight, beautiful, and simple terminal. It's designed to be
setup with sane defaults and little to no configuration. It's just a
terminal, nothing more, nothing less.


%package        fish
Summary:        The terminal of the 21st century (fish support)

BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       fish

Supplements:    (%{name} and fish)

%description    fish
A super lightweight, beautiful, and simple terminal. It's designed to be
setup with sane defaults and little to no configuration. It's just a
terminal, nothing more, nothing less.

This package contains the files needed to support "process completed"
notifications when using the fish shell.


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

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/open-pantheon-terminal-here.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/open-pantheon-terminal-here.desktop
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml

%files fish
%{_datadir}/fish/vendor_conf.d/pantheon_terminal_process_completion_notifications.fish


%changelog
* Tue Nov 14 2023 Fabio Valentini <decathorpe@gmail.com> - 6.1.2-1
- Initial packaging

