#
# Conditional build
%bcond_without	openmp	# OpenMP support
%bcond_without	tcl	# Tcl/Tk support
%bcond_without	tests	# test suite
%bcond_without	doc	# PDF documentation
%bcond_with	sse2	# SSE2 instructions on x86
#
# NOTE:
# - /etc/localtime must be present for tests to work
#
# TODO:
# - script for rpm to autoprovides/autorequires R internals
#
Summary:	A language for data analysis and graphics
Summary(pl.UTF-8):	Język do analizy danych oraz grafiki
Name:		R
Version:	4.4.3
Release:	1
License:	mixed (distributable), mostly GPL v2+
Group:		Development/Languages
Source0:	https://cran.r-project.org/src/base/R-4/%{name}-%{version}.tar.xz
# Source0-md5:	4d87af81f83f992456a7d68d07bbbbf4
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-timezone.patch
URL:		https://www.r-project.org/
# yes, it is, or tests will fail
BuildRequires:	/etc/localtime
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	blas-devel >= 3.2.2-2
BuildRequires:	bzip2-devel >= 1.0.6
BuildRequires:	cairo-devel >= 1.6
BuildRequires:	curl-devel >= 7.28.0
BuildRequires:	gcc-fortran
BuildRequires:	gettext-tools >= 0.16.1
BuildRequires:	lapack-devel >= 3.2.2-2
%{?with_openmp:BuildRequires:	libgomp-devel}
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 2:1.2.7
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtirpc-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pango-devel
BuildRequires:	pcre2-8-devel
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 2.043
%if %{with tcl}
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
%endif
# 0.8.0 is too old currently (checking for tre_regncompb in -ltre... no)
#BuildRequires:	tre-devel >= ?
%if %{with doc}
BuildRequires:	texinfo-texi2dvi >= 4.7
BuildRequires:	texlive-dvips
BuildRequires:	texlive-fonts-rsfs
BuildRequires:	texlive-latex
BuildRequires:	texlive-latex-ae
BuildRequires:	texlive-pdftex
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz-devel >= 5.0.3
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.3
%if %{with tests} && %{with sse2}
BuildRequires:	cpuinfo(sse2)
%endif
#Requires:	lpr
Requires(post):	perl-base
Requires(post):	textutils
Requires:	blas >= 3.2.2-2
Requires:	bzip2 >= 1.0.6
Requires:	curl-libs >= 7.28.0
Requires:	pcre >= 8.32
Requires:	xz-libs >= 5.0.3
Requires:	zlib >= 1.2.3
%if %{with sse2}
Requires:	cpuinfo(sse2)
%endif
Suggests:	rkward
Obsoletes:	R-base
Obsoletes:	R-contrib
Obsoletes:	R-recommended
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A system for statistical computation and graphics. R consists of a
language plus a run-time environment with graphics, a debugger, access
to certain system functions, and the ability to run programs stored in
script files.

The design of R has been heavily influenced by two existing languages:
Becker, Chambers & Wilks' S and Sussman's Scheme. Whereas the
resulting language is very similar in appearance to S, the underlying
implementation and semantics are derived from Scheme.

%description -l pl.UTF-8
System do obliczeń statystycznych i grafiki. R składa się z języka
oraz środowiska uruchomieniowego z grafiką, debuggerem, dostępem do
niektórych funkcji systemowych oraz możliwością uruchamiania programów
zapisanych w skryptach.

Język R był zainspirowany dwoma istniejącymi językami: S (Beckera,
Chambersa i Wilksa) oraz Scheme (Sussmana). R jest podobny do S, ale
implementacja i semantyka wywodzi się ze Scheme.

%package java-tools
Summary:	R Java tools
Summary(pl.UTF-8):	Narzędzia R w Javie
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description java-tools
R Java classes.

%description java-tools -l pl.UTF-8
Narzędzia R w Javie.

%prep
%setup -q
%patch -P0 -p1

%ifarch %{ix86}
%if %{without sse2}
# some tests fail with 387 math
%{__sed} -i -e 's/ reg-tests-1d\.R//;s/p-qbeta-strict-tst\.R //' tests/Makefile.common
%endif
%endif

%build
%if %{with sse2}
CFLAGS="%{rpmcflags} -msse2 -mfpmath=sse"
CXXFLAGS="%{rpmcxxflags} -msse2 -mfpmath=sse"
%endif
%{__aclocal} -I m4
%{__autoconf}
install -d build
cd build
%define	configuredir ..
%configure \
	F77=gfortran \
	FC=gfortran \
	--enable-R-shlib \
	--enable-largefile \
	%{!?with_openmp:--disable-openmp} \
	--with-internal-tzcode \
	--with-ICU \
	--with-blas \
	--with-cairo \
	--with-jpeglib \
	--with-lapack \
	--with-libpng \
	--with-readline \
	--with-recommended-packages \
	--with-system-tre \
%if %{with tcl}
	--with-tcltk \
	--with-tcl-config=/usr/lib/tclConfig.sh \
	--with-tk-config=/usr/lib/tkConfig.sh \
%else
	--without-tcltk \
%endif
	--with-x

%{__make} -j1

%if %{with tests}
%{__make} check
%endif

%if %{with doc}
%{__make} docs pdf info
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/R,%{_includedir},%{_desktopdir},%{_pixmapsdir}}

%{__make} -C build -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf %{_libdir}/R/lib/libR.so $RPM_BUILD_ROOT%{_libdir}

%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/include $RPM_BUILD_ROOT%{_includedir}/R
ln -sf %{_includedir}/R $RPM_BUILD_ROOT%{_libdir}/R/include

gen_lang() {
	dir="$1"
	for d in $RPM_BUILD_ROOT${dir}/* ; do
		bd=$(basename $d)
		lang="${bd%@*}"
		echo "%lang($lang) ${dir}/${bd}"
	done
}

for moddir in $RPM_BUILD_ROOT%{_libdir}/R/library/* ; do
	module=$(basename $moddir)
	echo "%dir %{_libdir}/R/library/${module}"
	if [ "$module" = "translations" ]; then
		for f in $moddir/* ; do
			bf=$(basename $f)
			case "$bf" in
			  DESCRIPTION|en|en@quot)
				echo "%{_libdir}/R/library/${module}/${bf}"
				;;
			  *)
				echo "%lang(${bf}) %{_libdir}/R/library/${module}/${bf}"
				;;
			esac
		done
	else
		for f in $moddir/* ; do
			bf=$(basename $f)
			case "$bf" in
			  po)
				echo "%dir %{_libdir}/R/library/${module}/po"
				gen_lang %{_libdir}/R/library/${module}/po
				;;
			  libs)
				echo "%dir %{_libdir}/R/library/${module}/libs"
				echo "%attr(755,root,root) %{_libdir}/R/library/${module}/libs/*.so"
				;;
			  *)
				echo "%{_libdir}/R/library/${module}/${bf}"
				;;
			esac
		done
	fi
done > R.files

# just GPL
%{__rm} $RPM_BUILD_ROOT%{_libdir}/R/doc/COPYING
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/R/doc/{AUTHORS,COPYRIGHTS,FAQ,NEWS.rds,THANKS}
%if %{with doc}
# pdf version of NEWS
%{__rm} $RPM_BUILD_ROOT%{_libdir}/R/doc/NEWS.pdf
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f R.files
%defattr(644,root,root,755)
%doc README doc/{AUTHORS,COPYRIGHTS,FAQ,NEWS,NEWS.[012],RESOURCES,THANKS}
%attr(755,root,root) %{_bindir}/R
%attr(755,root,root) %{_bindir}/Rscript
%dir %{_libdir}/R
%dir %{_libdir}/R/lib
%attr(755,root,root) %{_libdir}/R/lib/libR.so
%attr(755,root,root) %{_libdir}/libR.so
%{_libdir}/R/COPYING
%{_libdir}/R/SVN-REVISION
%attr(755,root,root) %{_libdir}/R/bin
%exclude %{_libdir}/R/bin/javareconf
# %{_libdir}/R/doc %except %{_libdir}/R/doc/html/{packages.html,search/index.txt}
%dir %{_libdir}/R/doc
%{_libdir}/R/doc/[KRm]*
%{_libdir}/R/doc/BioC_mirrors.csv
%{_libdir}/R/doc/CRAN_mirrors.csv
%{_libdir}/R/doc/NEWS*
%dir %{_libdir}/R/doc/html
%{_libdir}/R/doc/html/[NRSa-lr-u]*.html
%{_libdir}/R/doc/html/packages-head*.html
%{_libdir}/R/doc/html/favicon.ico
%{_libdir}/R/doc/html/*.css
%{_libdir}/R/doc/html/*.jpg
%{_libdir}/R/doc/html/*.js
%{_libdir}/R/doc/html/*.svg
%{_libdir}/R/doc/html/katex
%ghost %{_libdir}/R/doc/html/packages.html
%{_libdir}/R/etc
%{_libdir}/R/include
%dir %{_libdir}/R/library
# library files list is autogenerated (see R.files above)
%attr(755,root,root) %{_libdir}/R/modules
%dir %{_libdir}/R/share
%{_libdir}/R/share/R
%{_libdir}/R/share/Rd
%{_libdir}/R/share/dictionaries
%{_libdir}/R/share/encodings
%{_libdir}/R/share/licenses
%{_libdir}/R/share/make
%{_libdir}/R/share/sh
%{_libdir}/R/share/texmf
%{_libdir}/R/share/zoneinfo
%{_desktopdir}/R.desktop
%{_pixmapsdir}/R.xpm
%{_includedir}/R
%{_pkgconfigdir}/libR.pc
%{_mandir}/man1/R.1*
%{_mandir}/man1/Rscript*

%files java-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/R/bin/javareconf
%{_libdir}/R/share/java
