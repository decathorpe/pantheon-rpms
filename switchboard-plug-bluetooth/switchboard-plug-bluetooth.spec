%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-bluetooth

%global plug_type network
%global plug_name bluetooth
%global plug_rdnn io.elementary.switchboard.bluetooth

Name:           switchboard-plug-bluetooth
Summary:        Switchboard Bluetooth plug
Version:        2.3.6
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/switchboard-plug-bluetooth
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       bluez
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and bluez)

%description
The Bluetooth plug is a section in the Switchboard (System Settings)
that allows the user to manage bluetooth settings and connected
devices.


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

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Tue Nov 14 2023 Fabio Valentini <decathorpe@gmail.com> - 2.3.6-1
- Initial packaging

