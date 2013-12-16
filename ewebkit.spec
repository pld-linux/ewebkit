Summary:	WebKit-EFL - Web content engine for EFL applications
Summary(pl.UTF-8):	WebKit-EFL - silnik WWW dla aplikacji EFL
Name:		ewebkit
Version:	0.1.0
%define	subver	r160591
Release:	0.%{subver}.1
License:	BSD
Group:		Libraries
# older snapshots:
#Source0:	http://packages.profusion.mobi/webkit-efl/webkit-efl-svn-%{subver}.tar.bz2
# svn checkout https://svn.webkit.org/repository/webkit/trunk WebKit
# tar cJf webkit-r160591.tar.xz --exclude=.svn --exclude=LayoutTests --exclude=ManualTests --exclude=PerformanceTests --exclude=WebKitLibraries --exclude=Websites WebKit
Source0:	webkit-%{subver}.tar.xz
# Source0-md5:	b450c3c4030062571c3c05eea3cf4f30
Patch0:		%{name}-lib.patch
Patch1:		%{name}-bounds.patch
Patch2:		%{name}-include.patch
Patch3:		%{name}-build.patch
URL:		http://trac.enlightenment.org/e/wiki/EWebKit
BuildRequires:	OpenGL-devel
BuildRequires:	atk-devel >= 1:2.10.0
BuildRequires:	bison >= 2.4.1
BuildRequires:	cairo-devel >= 1.10.2
BuildRequires:	cmake >= 2.8.3
BuildRequires:	dbus-devel
BuildRequires:	e_dbus-devel >= 1.7
BuildRequires:	ecore-devel >= 1.8
BuildRequires:	ecore-evas-devel >= 1.8
BuildRequires:	ecore-file-devel >= 1.8
BuildRequires:	ecore-imf-devel >= 1.8
BuildRequires:	ecore-imf-evas-devel >= 1.8
BuildRequires:	ecore-input-devel >= 1.8
BuildRequires:	ecore-x-devel >= 1.8
BuildRequires:	edje >= 1.8
BuildRequires:	edje-devel >= 1.8
BuildRequires:	eet-devel >= 1.8
BuildRequires:	eeze-devel >= 1.8
BuildRequires:	efreet-devel >= 1.8
BuildRequires:	eina-devel >= 1.8
BuildRequires:	eo-devel >= 1.8
BuildRequires:	evas-devel >= 1.8
BuildRequires:	flex >= 2.5.34
BuildRequires:	fontconfig-devel >= 2.8.0
BuildRequires:	freetype-devel >= 1:2.4.2
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gperf >= 3.0.1
BuildRequires:	gstreamer-devel >= 1.0.5
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.5
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	harfbuzz-devel >= 0.9.18
BuildRequires:	harfbuzz-icu-devel >= 0.9.18
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 1:2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	pango-devel
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	python >= 1:2.6.0
BuildRequires:	ruby >= 1.8.7
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	atk >= 1:2.10.0
Requires:	cairo >= 1.10.2
Requires:	e_dbus >= 1.7
Requires:	ecore >= 1.8
Requires:	ecore-evas >= 1.8
Requires:	ecore-file >= 1.8
Requires:	ecore-imf >= 1.8
Requires:	ecore-imf-evas >= 1.8
Requires:	ecore-input >= 1.8
Requires:	ecore-x >= 1.8
Requires:	edje-libs >= 1.8
Requires:	efreet >= 1.8
Requires:	eeze >= 1.8
Requires:	eina >= 1.8
Requires:	evas >= 1.8
Requires:	fontconfig-libs >= 2.8.0
Requires:	freetype >= 2.1.0
Requires:	glib2 >= 1:2.36.0
Requires:	gstreamer >= 1.0.5
Requires:	gstreamer-plugins-base >= 1.0.5
Requires:	harfbuzz >= 0.9.18
Requires:	harfbuzz-icu >= 0.9.18
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebKit-EFL - Web content engine for EFL applications.

%description -l pl.UTF-8
WebKit-EFL - silnik WWW dla aplikacji EFL.

%package devel
Summary:	Header files for WebKit-EFL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki WebKit-EFL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.10.2
Requires:	ecore-devel >= 1.2.0
Requires:	ecore-input-devel >= 1.2.0
Requires:	evas-devel >= 1.0.0
Requires:	harfbuzz-devel
Requires:	libsoup-devel >= 2.42.0
Requires:	libstdc++-devel

%description devel
Header files for WebKit-EFL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WebKit-EFL.

%prep
%setup -q -n WebKit
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# replace -g2 with -g1 to not run into 4 GB ar format limit
# https://bugs.webkit.org/show_bug.cgi?id=91154
# http://sourceware.org/bugzilla/show_bug.cgi?id=14625
CFLAGS="%(echo %{rpmcflags} | sed 's/ -g2/ -g1/g')"
CXXFLAGS="%(echo %{rpmcxxflags} | sed 's/ -g2/ -g1/g') -Wno-deprecated-declarations"
%cmake . \
	-DPORT=Efl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog Source/WebKit/LICENSE
%attr(755,root,root) %{_bindir}/PluginProcess
%attr(755,root,root) %{_bindir}/WebProcess
%attr(755,root,root) %{_libdir}/libewebkit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libewebkit.so.0
%attr(755,root,root) %{_libdir}/libewebkit2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libewebkit2.so.0
%{_datadir}/ewebkit-0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libewebkit.so
%attr(755,root,root) %{_libdir}/libewebkit2.so
%{_includedir}/ewebkit-0
%{_includedir}/ewebkit2-0
%{_pkgconfigdir}/ewebkit.pc
%{_pkgconfigdir}/ewebkit2.pc
%{_libdir}/cmake/EWebKit
%{_libdir}/cmake/EWebKit2
