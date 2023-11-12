%global srcname pantheon-agent-geoclue2
%global appname io.elementary.desktop.agent-geoclue2

Name:           pantheon-agent-geoclue2
Summary:        Pantheon Geoclue2 Agent
Version:        1.0.6
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/pantheon-agent-geoclue2
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgeoclue-2.0)

%description
Provides a dialog asking for the user's permission when an application
requests access to location services.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

%{_libexecdir}/geoclue2-1-pantheon/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Nov 12 2023 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Initial packaging

