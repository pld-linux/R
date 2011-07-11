#
# Conditional build
%bcond_without	tcl		# disable tcl support
%bcond_without	tests		# do not run "make check"
#
# NOTE:
# - /etc/localtime must be present for tests to work
#
# TODO:
# - script for rpm to autoprovides/autorequires R internals
#
%include	/usr/lib/rpm/macros.perl
Summary:	A language for data analysis and graphics
Summary(pl.UTF-8):	Język do analizy danych oraz grafiki
Name:		R
Version:	2.13.1
Release:	1
License:	Mixed (distributable), mostly GPL
Group:		Development/Languages
# CRAN master site: ftp://cran.r-project.org/pub/R/src/
Source0:	ftp://stat.ethz.ch/R-CRAN/src/base/R-2/%{name}-%{version}.tar.gz
# Source0-md5:	28dd0d68ac3a0eab93fe7035565a1c30
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-install.patch
URL:		http://www.r-project.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	blas-devel >= 3.2.2-2
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel
BuildRequires:	gcc-fortran
BuildRequires:	gettext-devel
BuildRequires:	lapack-devel >= 3.2.2-2
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.26
BuildRequires:	pango-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov
%{?with_tcl:BuildRequires:	tcl-devel}
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	tetex-pdftex
BuildRequires:	texinfo-texi2dvi
%{?with_tcl:BuildRequires:	tk-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz-devel
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.1.3
#Requires:	lpr
Requires(post):	perl-base
Requires(post):	textutils
Requires:	blas >= 3.2.2-2
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

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%configure \
	--enable-R-shlib \
	--enable-largefile \
	--with-ICU \
	--with-blas \
	--with-cairo \
	--with-jpeglib \
	--with-lapack \
	--with-libpng \
	--with-readline \
	--with-recommended-packages \
	--with-system-bzlib \
	--with-system-pcre \
	--with-system-xz \
	--with-system-zlib \
	--with%{!?with_tcl:out}-tcltk \
	--with-x

%{__make}
%if %{with tests}
%{__make} check
%endif
%{__make} docs pdf info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/R,%{_includedir},%{_desktopdir},%{_pixmapsdir}}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

mv $RPM_BUILD_ROOT%{_libdir}/R/lib/libR*.so $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/include $RPM_BUILD_ROOT%{_includedir}/R
ln -sf %{_includedir}/R $RPM_BUILD_ROOT%{_libdir}/R/include

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README doc/{AUTHORS,COPYRIGHTS,FAQ,RESOURCES,THANKS}
%attr(755,root,root) %{_bindir}/R
%attr(755,root,root) %{_bindir}/Rscript
%attr(755,root,root) %{_libdir}/libR*.so
%dir %{_libdir}/R
%{_libdir}/R/COPYING
%{_libdir}/R/NEWS
%{_libdir}/R/SVN-REVISION
%attr(755,root,root) %{_libdir}/R/bin
# %{_libdir}/R/doc %except %{_libdir}/R/doc/html/{packages.html,search/index.txt}
%dir %{_libdir}/R/doc
%{_libdir}/R/doc/[KRm]*
%dir %{_libdir}/R/doc/html
%{_libdir}/R/doc/html/*.css
%{_libdir}/R/doc/html/[Ra-lr-u]*.html
%{_libdir}/R/doc/html/packages-head*.html
%{_libdir}/R/doc/html/*.jpg
%ghost %{_libdir}/R/doc/html/packages.html
%{_libdir}/R/etc
%{_libdir}/R/include
%dir %{_libdir}/R/library
%{_libdir}/R/library/KernSmooth
%{_libdir}/R/library/MASS
%{_libdir}/R/library/Matrix
%{_libdir}/R/library/base
%{_libdir}/R/library/boot
%{_libdir}/R/library/class
%{_libdir}/R/library/cluster
%{_libdir}/R/library/codetools
%{_libdir}/R/library/compiler
%{_libdir}/R/library/datasets
%{_libdir}/R/library/foreign
%{_libdir}/R/library/grDevices
%{_libdir}/R/library/graphics
%{_libdir}/R/library/grid
%{_libdir}/R/library/lattice
%{_libdir}/R/library/methods
%{_libdir}/R/library/mgcv
%{_libdir}/R/library/nlme
%{_libdir}/R/library/nnet
%{_libdir}/R/library/rpart
%{_libdir}/R/library/spatial
%{_libdir}/R/library/splines
%{_libdir}/R/library/stats
%{_libdir}/R/library/stats4
%{_libdir}/R/library/survival
%{_libdir}/R/library/tcltk
%{_libdir}/R/library/tools
%{_libdir}/R/library/utils
%attr(755,root,root) %{_libdir}/R/modules
%{_libdir}/R/share
%{_desktopdir}/R.desktop
%{_pixmapsdir}/R.xpm
%{_includedir}/R
%{_pkgconfigdir}/libR.pc
%{_mandir}/man1/R.1*
%{_mandir}/man1/Rscript*
