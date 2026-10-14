Summary:	A powerful download manager powered by aria2
Name:		persepolis
Version:	5.2.0.0
Release:	2
License:	GPLv3+
Group:		Networking/File transfer
URL:		https://persepolisdm.github.io/
Source0:	https://github.com/persepolisdm/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: meson
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
# for tests
BuildRequires:	aria2
BuildRequires:	libnotify
BuildRequires:	pulseaudio-utils
BuildRequires:	python-qt5 >= 5.15.11-3
BuildRequires:	python%{pyver}dist(psutil)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(setproctitle)
BuildRequires:	sound-theme-freedesktop
BuildRequires:	yt-dlp
BuildRequires:	ffmpeg

Requires:	aria2
Requires:	libnotify
Requires:	pulseaudio-utils
Requires:	python-qt5 >= 5.15.11-3
Requires:	python%{pyver}dist(psutil)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(setproctitle)
Requires:	sound-theme-freedesktop
Requires:	yt-dlp
Suggests:	ffmpeg

BuildArch:	noarch

%description
Persepolis is a download manager and a GUI for aria written in Python.

  * Graphical UI for aria2
  * Multi segment downloading
  * Scheduling downloads
  * Download queuing

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/metainfo/com.github.persepolisdm.persepolis.appdata.xml
%{py_puresitedir}/%{name}
#{py_puresitedir}/%{name}-%{version}-py%{py_ver}.*-info
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/scalable/apps/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n persepolis-5.2.0
rm 'persepolis/Persepolis Download Manager.py'


%build
%meson
%meson_build

%install
%meson_install
# fix perm
chmod a+x %{buildroot}/%{python3_sitelib}/persepolis/__main__.py
