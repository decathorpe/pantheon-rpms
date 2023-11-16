%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-printers

%global plug_type hardware
%global plug_name printers
%global plug_rdnn io.elementary.switchboard.printers

Name:           switchboard-plug-printers
Summary:        Switchboard Printers Plug
Version:        2.2.1
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/switchboard-plug-printers
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  cups-devel

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       cups%{?_isa}
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and cups%{?_isa})

%description
A printers plug for Switchboard.


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
* Thu Nov 16 2023 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-1
- Initial packaging

