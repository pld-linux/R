#
# Conditional build
%bcond_without	tcl		# disable tcl support
%bcond_without	tests		# do not run "make check"
#
# NOTE:
# - /etc/localtime must be present for tests to work
#
# TODO:
# - faulty build on i486 (test stats-Ex.R):
#	error in optim(init[mask], getLike, method = "L-BFGS-B", lower = rep(0,  :
#          non-finite value supplied by optim
# - script for rpm to autoprovides/autorequires R internals
#
%include	/usr/lib/rpm/macros.perl
Summary:	A language for data analysis and graphics
Summary(pl.UTF-8):	Język do analizy danych oraz grafiki
Name:		R
Version:	2.11.1
Release:	1
License:	Mixed (distributable), mostly GPL
Group:		Development/Languages
# CRAN master site: ftp://cran.r-project.org/pub/R/src/
Source0:	ftp://stat.ethz.ch/R-CRAN/src/base/R-2/%{name}-%{version}.tar.gz
# Source0-md5:	7421108ade3e9223263394b9bbe277ce
Source1:	%{name}.desktop
URL:		http://www.r-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	blas-devel
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel
BuildRequires:	gcc-fortran
BuildRequires:	gettext-devel
BuildRequires:	lapack-devel >= 3.1.1-4
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.5
BuildRequires:	libstdc++-devel
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

%build
%{__aclocal} -I m4
%{__autoconf}
%configure \
	--enable-R-shlib \
	--enable-linux-lfs \
	--with-system-zlib \
	--with-system-bzlib \
	--with-system-pcre \
	--with-system-xz \
	--with-libpng \
	--with-jpeglib \
	--with-blas \
	--with-lapack \
	--with-readline \
	--with%{!?with_tcl:out}-tcltk \
	--with-cairo \
	--with-libpng \
	--with-jpeglib \
	--with-system-zlib \
	--with-system-bzlib \
	--with-system-pcre \
	--with-iconv \
	--with-ICU \
	--with-x \
	--with-recommended-packages

%{__make}
%if %{with tests}
%{__make} check
%endif
%{__make} docs pdf info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/R,%{_includedir},%{_desktopdir}}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/{R,Text}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_libdir}/R/lib/libR*.so $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/include $RPM_BUILD_ROOT%{_includedir}/R
ln -sf %{_includedir}/R $RPM_BUILD_ROOT%{_libdir}/R/include

(cd $RPM_BUILD_ROOT%{_libdir}/%{name}/share/perl/R/
for f in * ; do
  ln -s %{_libdir}/%{name}/share/perl/R/$f $RPM_BUILD_ROOT%{perl_vendorlib}/R/
done)

rm -r $RPM_BUILD_ROOT%{perl_vendorlib}/R
rm -r $RPM_BUILD_ROOT%{_libdir}/R/share/perl/File
mv    $RPM_BUILD_ROOT%{_libdir}/R/share/perl/R $RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README doc/{AUTHORS,COPYRIGHTS,FAQ,RESOURCES,THANKS}

%{_mandir}/man1/R.1*
%{_mandir}/man1/Rscript*
%attr(755,root,root) %{_bindir}/R
%attr(755,root,root) %{_bindir}/Rscript
%dir %{_libdir}/R
%attr(755,root,root) %{_libdir}/R/bin
%attr(755,root,root) %{_libdir}/libR*.so
%{_libdir}/R/etc
%{_libdir}/R/include
%{_includedir}/R
%{_libdir}/R/share
%{_libdir}/R/COPYING
%{_libdir}/R/NEWS
%{_libdir}/R/SVN-REVISION
%dir %{_libdir}/R/library
%{_libdir}/%{name}/library/R.css
# %{_libdir}/R/doc %except %{_libdir}/R/doc/html/{packages.html,search/index.txt}
%dir %{_libdir}/R/doc
%{_libdir}/R/doc/[KRm]*
%dir %{_libdir}/R/doc/html
%{_libdir}/R/doc/html/*.css
%{_libdir}/R/doc/html/[Ra-lr-u]*.html
%{_libdir}/R/doc/html/packages-head*.html
%{_libdir}/R/doc/html/*.jpg
%ghost %{_libdir}/R/doc/html/packages.html
%{_desktopdir}/*.desktop

%{perl_vendorlib}/R

%attr(755,root,root) %{_libdir}/%{name}/modules

%{_libdir}/%{name}/library/KernSmooth
%{_libdir}/%{name}/library/MASS
%{_libdir}/%{name}/library/Matrix
%{_libdir}/%{name}/library/base
%{_libdir}/%{name}/library/boot
%{_libdir}/%{name}/library/class
%{_libdir}/%{name}/library/cluster
%{_libdir}/%{name}/library/codetools
%{_libdir}/%{name}/library/datasets
%{_libdir}/%{name}/library/foreign
%{_libdir}/%{name}/library/grDevices
%{_libdir}/%{name}/library/graphics
%{_libdir}/%{name}/library/grid
%{_libdir}/%{name}/library/lattice
%{_libdir}/%{name}/library/methods
%{_libdir}/%{name}/library/mgcv
%{_libdir}/%{name}/library/nlme
%{_libdir}/%{name}/library/nnet
%{_libdir}/%{name}/library/rpart
%{_libdir}/%{name}/library/spatial
%{_libdir}/%{name}/library/splines
%{_libdir}/%{name}/library/stats
%{_libdir}/%{name}/library/stats4
%{_libdir}/%{name}/library/survival
%{_libdir}/%{name}/library/tcltk
%{_libdir}/%{name}/library/tools
%{_libdir}/%{name}/library/utils

%{_pkgconfigdir}/*.pc
