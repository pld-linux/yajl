Summary:	Yet Another JSON Library
Summary(pl.UTF-8):	Yet Another JSON Library - jeszcze jedna biblioteka JSON
Name:		yajl
Version:	1.0.11
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://github.com/lloyd/yajl/tarball/1.0.11/%{name}-%{version}.tar.gz
# Source0-md5:	5b60f4d59b3b1fb42d7808d08460fb12
URL:		http://lloyd.github.com/yajl/
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
%setup -q -n lloyd-yajl-f4baae0

%build
install -d build
cd build

%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_VERBOSE_MAKEFILE=ON

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
%attr(755,root,root) %ghost %{_libdir}/libyajl.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyajl.so
%{_includedir}/yajl

%files static
%defattr(644,root,root,755)
%{_libdir}/libyajl_s.a
