#
# Conditional build
%bcond_without	tcl		# disable tcl support
%bcond_without	tests		# do not run "make check"
#
# TODO:
# - script for rpm to autoprovides/autorequires R internals
#
%define	KernSmooth_version	2.22r19
%define	VR_version		7.2r30
%define	boot_version		1.2r27
%define	cluster_version		1.11.4
%define	foreign_version		0.8r18
%define	lattice_version		0.14r16
%define	mgcv_version		1.3r22
%define	nlme_version		3.1r78
%define	rpart_version		3.1r33
%define	survival_version	2.30

%include	/usr/lib/rpm/macros.perl
Summary:	A language for data analysis and graphics
Summary(pl.UTF-8):	Język do analizy danych oraz grafiki
Name:		R
Version:	2.6.1
Release:	2
License:	Mixed (distributable), mostly GPL
Group:		Development/Languages
# CRAN master site: ftp://cran.r-project.org/pub/R/src/
Source0:	ftp://stat.ethz.ch/R-CRAN/src/base/R-2/%{name}-%{version}.tar.gz
# Source0-md5:	19c35a69e1afa73f5f70f91ff9939233
Source1:	%{name}.desktop
URL:		http://www.r-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	blas-devel
BuildRequires:	bzip2-devel
BuildRequires:	gcc-c++
BuildRequires:	gcc-fortran
BuildRequires:	gettext-devel
BuildRequires:	lapack-devel >= 3.1.1-4
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.26
BuildRequires:	pcre-devel
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov
%{?with_tcl:BuildRequires:	tcl-devel}
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	tetex-pdftex
%{?with_tcl:BuildRequires:	tk-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.1.3
#Requires:	lpr
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

%package base
Summary:	The R base distribution
Summary(pl.UTF-8):	Podstawowa dystrybucja R
License:	GPL v2 / LGPL
Group:		Development/Languages
Requires(post):	perl-base
Requires(post):	textutils
Provides:	R-cran-base
Provides:	R-cran-datasets
Provides:	R-cran-grDevices
Provides:	R-cran-graphics
Provides:	R-cran-grid
Provides:	R-cran-methods
Provides:	R-cran-splines
Provides:	R-cran-stats
Provides:	R-cran-stats4
Provides:	R-cran-tcltk
Provides:	R-cran-tools
Provides:	R-cran-utils

%description base
R is a language and run-time environment for carrying out interactive
statistical data analysis. It is not entirely dissimilar to the S
language developed at AT&T Bell Laboratories (and now Lucent
Technologies). Indeed, S users will find the environment quite
familiar and a good deal of S software will run without change under
R.

%description base -l pl.UTF-8
R jest językiem i środowiskiem uruchomieniowym do interaktywnej
analizy danych statystycznych. R nie jest całkowicie zgodny z językiem
S opracowanym w AT&T Bell Laboratiories (a teraz Lucent Technologies),
mimo to użytkownicy S zauważą zbliżone środowisko, a duża część
oprogramowania w S będzie działała bez zmian w R.

%package recommended
Summary:	Recommended contributed packages for the R language
Summary(pl.UTF-8):	Zalecane dodatkowe pakiety do języka R
License:	GPL, free or free for non-commercial use
Group:		Development/Languages
URL:		http://www.ci.tuwien.ac.at/R/
Requires(post,postun):	R-base
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R-base = %{version}-%{release}
Provides:	R-cran-KernSmooth = %{KernSmooth_version}
Provides:	R-cran-MASS = %{VR_version}
Provides:	R-cran-VR = %{VR_version}
Provides:	R-cran-boot = %{boot_version}
Provides:	R-cran-class = %{VR_version}
Provides:	R-cran-cluster = %{cluster_version}
Provides:	R-cran-foreign = %{foreign_version}
Provides:	R-cran-lattice = %{lattice_version}
Provides:	R-cran-mgcv = %{mgcv_version}
Provides:	R-cran-nlme = %{nlme_version}
Provides:	R-cran-nnet = %{VR_version}
Provides:	R-cran-rpart = %{rpart_version}
Provides:	R-cran-spatial = %{VR_version}
Provides:	R-cran-survival = %{survival_version}
Obsoletes:	R-contrib
Obsoletes:	R-cran-KernSmooth
Obsoletes:	R-cran-MASS
Obsoletes:	R-cran-VR
Obsoletes:	R-cran-boot
Obsoletes:	R-cran-class
Obsoletes:	R-cran-cluster
Obsoletes:	R-cran-foreign
Obsoletes:	R-cran-lattice
Obsoletes:	R-cran-mgcv
Obsoletes:	R-cran-nlme
Obsoletes:	R-cran-nnet
Obsoletes:	R-cran-rpart
Obsoletes:	R-cran-spatial
Obsoletes:	R-cran-survival

%description recommended
Packages which extend the capabilities of the R base distribution and
are distributed on the Comprehensive R Archive Network (CRAN).

%description recommended -l pl.UTF-8
Pakiety rozszerzające możliwości podstawowej dystrybucji języka R,
dystrubuowane w archiwum CRAN (Comprehensive R Archive Network).

%prep
%setup -q

%build
%configure \
	--enable-R-shlib \
	--enable-linux-lfs \
	--with-system-zlib \
	--with-system-bzlib \
	--with-system-pcre \
	--with-libpng \
	--with-jpeglib \
	--with-blas \
	--with-lapack \
	--with-readline \
	--with%{!?with_tcl:out}-tcltk \
	--with-recommended-packages

%{__make}
%if %{with tests}
%{__make} check
%endif
%{__make} docs help html info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/R,%{_includedir},%{_desktopdir}}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/{R,Text}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

find $RPM_BUILD_ROOT%{_libdir}/R -name 'Makefile*' -exec rm -f {} \;
mv $RPM_BUILD_ROOT%{_libdir}/R/lib/libR*.so $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/include $RPM_BUILD_ROOT%{_includedir}/R
ln -sf %{_includedir}/R $RPM_BUILD_ROOT%{_libdir}/R/include
rm $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -i -e "s#$RPM_BUILD_ROOT##g" $RPM_BUILD_ROOT%{_libdir}/%{name}/bin/%{name}
ln -sf %{_libdir}/%{name}/bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

(cd $RPM_BUILD_ROOT%{_libdir}/%{name}/share/perl/R/
for f in * ; do
  ln -s %{_libdir}/%{name}/share/perl/R/$f $RPM_BUILD_ROOT%{perl_vendorlib}/R/
done)
(cd $RPM_BUILD_ROOT%{_libdir}/%{name}/share/perl/Text
for f in * ; do
  ln -s %{_libdir}/%{name}/share/perl/Text/$f $RPM_BUILD_ROOT%{perl_vendorlib}/Text/
done)

rm -r $RPM_BUILD_ROOT%{perl_vendorlib}/{Text,R}
rm -r $RPM_BUILD_ROOT%{_libdir}/R/share/perl/{File,Text}
mv    $RPM_BUILD_ROOT%{_libdir}/R/share/perl/R $RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
/sbin/ldconfig

%postun	-p /sbin/ldconfig

%files base
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
%dir %{_libdir}/R/doc/html/search
%{_libdir}/R/doc/html/search/[A-Z]*
%ghost %{_libdir}/R/doc/html/search/index.txt
%ghost %{_libdir}/R/doc/html/packages.html
%{_desktopdir}/*.desktop

%{perl_vendorlib}/R

%attr(755,root,root) %{_libdir}/%{name}/modules

%{_libdir}/%{name}/library/KernSmooth
%{_libdir}/%{name}/library/MASS
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
%{_libdir}/%{name}/library/rcompgen
%{_libdir}/%{name}/library/rpart
%{_libdir}/%{name}/library/spatial
%{_libdir}/%{name}/library/survival
%{_libdir}/%{name}/library/splines
%{_libdir}/%{name}/library/stats
%{_libdir}/%{name}/library/stats4
%{_libdir}/%{name}/library/tcltk
%{_libdir}/%{name}/library/tools
%{_libdir}/%{name}/library/utils

%{_pkgconfigdir}/*.pc

%files recommended
%defattr(644,root,root,755)
