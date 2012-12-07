Summary:	Recording tool for Skype Calls
Name:		skype-call-recorder
Version:	0.8
Release:	1
License:	GPL v2+
Group:		Applications/Networking
URL:		http://atdot.ch/scr/
Source0:	http://atdot.ch/scr/files/0.8/%{name}-%{version}.tar.gz
# Source0-md5:	937544a5245fdcfa50878d083dab706a
Patch0:		libs.patch
Patch1:		%{name}-0.8-cmake.patch
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	cmake >= 2.4.8
BuildRequires:	id3lib-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libogg-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel >= 1.2.0
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skype Call recorder allows you to record Skype calls to MP3, Ogg
Vorbis or WAV files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/skype-call-recorder
%{_desktopdir}/skype-call-recorder.desktop
%{_iconsdir}/hicolor/*/apps/skype-call-recorder.png
