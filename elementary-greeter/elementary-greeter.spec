%global srcname greeter
%global appname io.elementary.greeter

%global commit      7111c2201d7bb5042ab76069aafb899bef360e1c
%global shortcommit %(c=%{commit}; echo ${c:0:7}) 
%global commitdate  20231109

Name:           elementary-greeter
Summary:        LightDM Login Screen for the elementary desktop
Version:        7.0.0
Release:        1.%{commitdate}.git%{shortcommit}%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/greeter
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.58.0
BuildRequires:  vala

BuildRequires:  mesa-libEGL-devel

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite) >= 5.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(x11)

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

Provides:       pantheon-greeter = %{version}-%{release}
Obsoletes:      pantheon-greeter < 3.2.0-7

Requires:       lightdm%{?_isa}
Requires:       wingpanel%{?_isa}

# runtime requirement for numlock capture
Requires:       numlockx

# requirements for default artwork
Requires:       elementary-icon-theme
Requires:       elementary-theme-gtk3
Requires:       elementary-wallpapers

# requirements for accountsservice extension
Requires:       pantheon-session-settings >= 30.90

# all LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

# alternate descriptive names
Provides:       lightdm-%{name} = %{version}-%{release}
Provides:       lightdm-%{name}%{?_isa} = %{version}-%{release}

%description
The elementary Greeter is a styled Login Screen for LightDM.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/lightdm/%{appname}.conf

%{_bindir}/%{appname}-compositor
%{_sbindir}/%{appname}

%{_datadir}/lightdm/lightdm.conf.d/40-io.elementary.greeter.conf
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/xgreeters/%{appname}.desktop


%changelog
* Wed Nov 15 2023 Fabio Valentini <decathorpe@gmail.com> - 7.0.0-1.20231109.git7111c22
- Initial packaging

