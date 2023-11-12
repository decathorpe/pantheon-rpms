%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-applications

%global plug_type personal
%global plug_name applications
%global plug_rdnn io.elementary.switchboard.%{plug_name}

Name:           switchboard-plug-applications
Summary:        Switchboard Applications plug
Version:        7.0.1
Release:        1%{?dist}
License:        GPLv3+

URL:            http://github.com/elementary/switchboard-plug-applications
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(flatpak) >= 1.1.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.34
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       hicolor-icon-theme

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
The applications plug is a section in the Switchboard (System Settings)
that allows the user to manage application settings.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/icons/hicolor/*/apps/io.elementary.settings.applications.svg
%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Sun Nov 12 2023 Fabio Valentini <decathorpe@gmail.com> - 7.0.1-1
- Initial packaging

