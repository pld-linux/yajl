#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	Yet Another JSON Library
Summary(pl.UTF-8):	Yet Another JSON Library - jeszcze jedna biblioteka JSON
Name:		yajl
Version:	2.1.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/lloyd/yajl/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6887e0ed7479d2549761a4d284d3ecb0
Patch0:		%{name}-pc.patch
URL:		http://lloyd.github.io/yajl/
BuildRequires:	cmake >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAJL (Yet Another JSON Library) is a JSON parsing library written in
C.

%description -l pl.UTF-8
YAJL (Yet Another JSON Library, czyli jeszcze jedna biblioteka JSON)
to biblioteka analizatora JSON napisana w C.

%package devel
Summary:	Header files for YAJL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki YAJL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for YAJL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki YAJL.

%package static
Summary:	Static YAJL library
Summary(pl.UTF-8):	Statyczna biblioteka YAJL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static YAJL library.

%description static -l pl.UTF-8
Statyczna biblioteka YAJL.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build

%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_VERBOSE_MAKEFILE=ON

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/json_reformat
%attr(755,root,root) %{_bindir}/json_verify
%attr(755,root,root) %{_libdir}/libyajl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyajl.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyajl.so
%{_includedir}/yajl
%{_pkgconfigdir}/yajl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libyajl_s.a
