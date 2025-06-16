%global srcname greeter
%global appname io.elementary.greeter

%global commit      4bcb6ee549d95592f93f26cc1d2faa4a4b269f51
%global shortcommit %(c=%{commit}; echo ${c:0:7}) 
%global gitdate     20250611

Name:           elementary-greeter
Summary:        LightDM Login Screen for the elementary desktop
Version:        8.0.1^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/greeter
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.58.0
BuildRequires:  vala

%if 0%{?fedora} >= 42
BuildRequires:  pkgconfig(libmutter-16)
BuildRequires:  pkgconfig(mutter-clutter-16)
BuildRequires:  pkgconfig(mutter-cogl-16)
BuildRequires:  pkgconfig(mutter-mtk-16)
%endif
%if 0%{?fedora} == 41
BuildRequires:  pkgconfig(libmutter-15)
BuildRequires:  pkgconfig(mutter-clutter-15)
BuildRequires:  pkgconfig(mutter-cogl-15)
BuildRequires:  pkgconfig(mutter-cogl-pango-15)
BuildRequires:  pkgconfig(mutter-mtk-15)
%endif

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite) >= 5.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)

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
%{_bindir}/%{appname}-session-manager
%{_sbindir}/%{appname}

%{_datadir}/glib-2.0/schemas/%{appname}-compositor.gschema.xml
%{_datadir}/lightdm/lightdm.conf.d/40-io.elementary.greeter.conf
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/xgreeters/%{appname}.desktop


%changelog
%autochangelog
