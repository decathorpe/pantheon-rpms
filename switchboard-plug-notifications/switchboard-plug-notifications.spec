%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-notifications

%global plug_type personal
%global plug_name notifications
%global plug_rdnn io.elementary.switchboard.notifications

Name:           switchboard-plug-notifications
Summary:        Switchboard Notifications plug
Version:        2.2.0
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/switchboard-plug-notifications
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       gala%{?_isa}
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and gala%{?_isa})

%description
Configure which apps should be allowed to show notifications.

This is a GModule plugin for Switchboard that configures gsettings keys
related to the Notifications plugin for Gala.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%license COPYING
%doc README.md

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Thu Nov 16 2023 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Initial packaging

