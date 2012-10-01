Summary:	WebKit-EFL - Web content engine for EFL applications
Summary(pl.UTF-8):	WebKit-EFL - silnik WWW dla aplikacji EFL
Name:		ewebkit
Version:	0
%define	subver	r127150
Release:	0.%{subver}.1
License:	BSD
Group:		Libraries
Source0:	http://packages.profusion.mobi/webkit-efl/webkit-efl-svn-%{subver}.tar.bz2
# Source0-md5:	54332bd571a23d44e32837f4fa3a1c76
URL:		http://trac.enlightenment.org/e/wiki/EWebKit
BuildRequires:	bison
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	cmake >= 2.8.3
BuildRequires:	dbus-devel
BuildRequires:	e_dbus-devel >= 1.1.0
BuildRequires:	ecore-devel >= 1.2.0
BuildRequires:	ecore-evas-devel >= 1.2.0
BuildRequires:	ecore-file-devel >= 1.2.0
BuildRequires:	ecore-x-devel >= 1.2.0
BuildRequires:	edje >= 1.0.0
BuildRequires:	edje-devel >= 1.0.0
BuildRequires:	eeze-devel >= 1.3.0
BuildRequires:	efreet-devel >= 1.0.0
BuildRequires:	eina-devel >= 1.2.0
BuildRequires:	evas-devel >= 1.0.0
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 2.8.0
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	glib2-devel >= 1:2.31.8
BuildRequires:	gperf
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	harfbuzz-devel >= 0.9.0
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsoup-devel >= 2.39.4.1
BuildRequires:	libxml2-devel >= 1:2.6
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	pango-devel
BuildRequires:	perl-base
BuildRequires:	python
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
Requires:	cairo >= 1.10
Requires:	e_dbus >= 1.1.0
Requires:	ecore >= 1.2.0
Requires:	ecore-evas >= 1.2.0
Requires:	ecore-file >= 1.2.0
Requires:	ecore-x >= 1.2.0
Requires:	edje-libs >= 1.0.0
Requires:	efreet >= 1.0.0
Requires:	eeze >= 1.3.0
Requires:	eina >= 1.2.0
Requires:	evas >= 1.0.0
Requires:	fontconfig-libs >= 2.8.0
Requires:	freetype >= 2.1.0
Requires:	glib2 >= 1:2.31.8
Requires:	gtk+2 >= 2:2.10
Requires:	harfbuzz >= 0.9.0
Requires:	libxml2 >= 1:2.6
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
Requires:	cairo-devel >= 1.10
Requires:	ecore-devel >= 1.2.0
Requires:	ecore-input-devel >= 1.2.0
Requires:	evas-devel >= 1.0.0
Requires:	libsoup-devel >= 2.39.4.1

%description devel
Header files for WebKit-EFL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WebKit-EFL.

%prep
%setup -q -n webkit-efl-svn-%{subver}

%build
# replace -g2 with -g1 to not run into 4 GB ar format limit
# https://bugs.webkit.org/show_bug.cgi?id=91154
# http://sourceware.org/bugzilla/show_bug.cgi?id=14625
CFLAGS="%(echo %{rpmcflags} | sed 's/ -g2/ -g1/g')"
CXXFLAGS="%(echo %{rpmcxxflags} | sed 's/ -g2/ -g1/g')"
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
%attr(755,root,root) %{_libdir}/libewebkit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libewebkit.so.0
%{_datadir}/ewebkit-0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libewebkit.so
%{_includedir}/ewebkit-0
%{_pkgconfigdir}/ewebkit.pc
