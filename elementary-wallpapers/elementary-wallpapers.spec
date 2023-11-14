%global srcname wallpapers
%global default_wallpaper "Ryan Schroeder.jpg"

Name:           elementary-wallpapers
Summary:        Collection of wallpapers from the elementary project
Version:        5.4
Release:        7%{?dist}

# License breakdown is available in debian/copyright
License:        Public Domain

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# background settings file for gnome-control-center
Source1:        %{name}.xml

BuildRequires:  coreutils

BuildArch:      noarch

Provides:       pandora-wallpapers = %{version}-%{release}
Obsoletes:      pandora-wallpapers < 0.1.8-2


%description
This is the official collection of wallpapers from the elementary
project.


%package        gnome
Summary:        Collection of wallpapers from elementary (GNOME settings)

Requires:       %{name} = %{version}-%{release}
Requires:       gnome-control-center

Supplements:    (%{name} and gnome-control-center)

%description    gnome
This is the official collection of wallpapers from the elementary
project. This package contains the settings file that will make the
wallpapers show up in gnome-control-center.


%prep
%autosetup -n %{srcname}-%{version}


%build
# Nothing to do


%install
# copy wallpapers to install location
mkdir -p %{buildroot}/%{_datadir}/backgrounds/elementary
cp -pav *.jpg %{buildroot}/%{_datadir}/backgrounds/elementary/

# create default wallpaper symlink
ln -s ./%{default_wallpaper} %{buildroot}/%{_datadir}/backgrounds/elementary/default

# copy backgrounds list for gnome-control-center to install location
mkdir -p %{buildroot}/%{_datadir}/gnome-background-properties
cp -pav %{SOURCE1} %{buildroot}/%{_datadir}/gnome-background-properties/


%files
%license debian/copyright
%doc README.md

%{_datadir}/backgrounds/elementary/


%files gnome
%{_datadir}/gnome-background-properties/elementary-wallpapers.xml


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4-1
- Update to version 5.4.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3-2
- Add symlink for default wallpaper.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3-1
- Update to version 5.3.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2-1
- Update to version 5.2.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1-1
- Update to version 5.1.

* Sun Jan 21 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0-1
- Initial package obsoleting pandora-wallpapers.


