# TODO:
# - move perl R libraries to standard perl location
#
# Conditional build:
# _without_gnome        - without GNOME support
#
Summary:	A language for data analysis and graphics
Summary(pl):	J�zyk do analizy danych oraz grafiki
Name:		R
Version:	2.0.0
Release:	0.1
License:	Mixed (distributable), mostly GPL
Group:		Development/Languages
# CRAN master site: ftp://cran.r-project.org/pub/R/src/
Source0:	ftp://stat.ethz.ch/R-CRAN/src/base/R-2/%{name}-%{version}.tar.gz
# Source0-md5:	3900bca37cabb4b76b8d736d51cc9251
# Source0-size:	10676072
Source1:	%{name}.desktop
URL:		http://www.r-project.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	blas-devel
BuildRequires:	gcc-c++
BuildRequires:	gcc-g77
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	readline-devel
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-pdftex
BuildRequires:	zip
BuildRequires:	zlib >= 1.1.3
#BuildRequires:	lpr
#Requires:	lpr
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
%{!?_without_gnome:BuildRequires:	ORBit-devel}
%{!?_without_gnome:BuildRequires:	libglade-gnome-devel}
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

%description -l pl
System do oblicze� statystycznych i grafiki. R sk�ada si� z j�zyka
oraz �rodowiska uruchomieniowego z grafik�, debuggerem, dost�pem do
niekt�rych funkcji systemowych oraz mo�liwo�ci� uruchamiania program�w
zapisanych w skryptach.

J�zyk R by� zainspirowany dwoma istniej�cymi j�zykami: S (Beckera,
Chambersa i Wilksa) oraz Scheme (Sussmana). R jest podobny do S, ale
implementacja i semantyka wywodzi si� ze Scheme.

%package base
Summary:	The R base distribution
Summary(pl):	Podstawowa dystrybucja R
License:	GPL v2 / LGPL
Group:		Development/Languages
Requires(post):	textutils
Requires(post):	perl
Provides:	R-base
Provides:       R-datasets
Provides:       R-grid
Provides:       R-graphics
Provides:       R-grDevices
Provides:       R-methods
Provides:       R-utils
Provides:       R-tcltk
Provides:       R-splines
Provides:       R-stats
Provides:       R-stats4
Provides:       R-tools

%description base
R is a language and run-time environment for carrying out interactive
statistical data analysis. It is not entirely dissimilar to the S
language developed at AT&T Bell Laboratories (and now Lucent
Technologies). Indeed, S users will find the environment quite
familiar and a good deal of S software will run without change under
R.

%description base -l pl
R jest j�zykiem i �rodowiskiem uruchomieniowym do interaktywnej
analizy danych statystycznych. R nie jest ca�kowicie zgodny z j�zykiem
S opracowanym w AT&T Bell Laboratiories (a teraz Lucent Technologies),
mimo to u�ytkownicy S zauwa�� zbli�one �rodowisko, a du�a cz��
oprogramowania w S b�dzie dzia�a�a bez zmian w R.

%package recommended
Summary:	Recommended contributed packages for the R language
Summary(pl):	Zalecane dodatkowe pakiety do j�zyka R
Group:		Development/Languages
Provides:	R-KernSmooth R-VR R-boot R-cluster R-foreign
Provides:	R-lattice R-mgcv R-nlme	R-rpart R-survival
License:	GPL, free or free for non-commercial use
URL:		http://www.ci.tuwien.ac.at/R/
Requires(post,postun):	R-base
Requires(post,postun):	textutils
Requires(post,postun):	perl
Requires:	R-base = %{version}-%{release}
Obsoletes:	R-survival4 R-MASS R-clus R-class R-nnet R-spatial

%description recommended
Packages which extend the capabilities of the R base distribution and
are distributed on the Comprehensive R Archive Network (CRAN).

%description recommended -l pl
Pakiety rozszerzaj�ce mo�liwo�ci podstawowej dystrybucji j�zyka R,
dystrubuowane w archiwum CRAN (Comprehensive R Archive Network).

%package contrib
Summary:	Contributed packages for the R language
Summary(pl):	Dodatkowe pakiety do j�zyka R
License:	Mixed
Group:		Development/Languages
URL:		http://www.ci.tuwien.ac.at/R/
Requires(post,postun):	R-base
Requires(post,postun):	textutils
Requires(post,postun):	perl
Requires:	R-base = %{version}-%{release}
Requires:	R-VR
Provides:	R-acepack R-bootstrap R-date R-e1071 R-fracdiff R-gee
Provides:	R-leaps R-oz R-polynom R-princurve R-quadprog
Provides:	R-xgobi
Obsoletes:	R-principal.curve

%description contrib
Packages which extend the capabilities of the R base distribution and
are distributed on the Comprehensive R Archive Network (CRAN).

%description contrib -l pl
Pakiety rozszerzaj�ce mo�liwo�ci podstawowej dystrybucji j�zyka R,
dystrubuowane w archiwum CRAN (Comprehensive R Archive Network).

%package mlbench
Summary:	Machine learning benchmarks
Summary(pl):	Testy wydajno�ci uczenia maszyny
Group:		Development/Languages
License:	GPL
URL:		http://www.ics.uci.edu/~mlearn/MLRepository.html
Requires(post,postun):	R-base
Requires(post,postun):	textutils
Requires(post,postun):	perl
Requires:	R-base = %{version}-%{release}

%description mlbench
R package which contains a collection of real-world datasets and
functions for creating artificial datasets that work as benchmarks for
machine learning methods.

%description mlbench -l pl
Ten podpakiet R zawiera zestaw rzeczywistych danych i funkcji do
tworzenia sztucznych danych s�u��cych jako test wydajno�ci metod
uczenia maszyny.
%prep
%setup -q

# These files have the path for PERL hard-coded as /usr/local/bin/perl
# We need to remove them to avoid dependency problems
rm -f ./doc/keyword-test.orig ./etc/undoc/R-funs.orig ./etc/undoc/extrExamp.orig

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.* .
%configure \
	%{!?_without_gnome:--with-gnome} \
	%{?_without_gnome:--without-gnome} \
	--enable-R-shlib \
	--enable-linux-lfs \
	--with-zlib \
	--with-bzlib \
	--with-pcre \
	--without-recommended-packages

%{__make}
%{__make} check
%{__make} docs
%{__make} help
%{__make} html
%{__make} info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/R,%{_includedir},%{_desktopdir}}

%{__make} install \
	rhome=$RPM_BUILD_ROOT%{_libdir}/R \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

find $RPM_BUILD_ROOT%{_libdir}/R -name 'Makefile*' -exec rm -f {} \;
mv $RPM_BUILD_ROOT%{_libdir}/R/lib/libR*.so $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/include $RPM_BUILD_ROOT%{_includedir}/R
ln -sf %{_includedir}/R $RPM_BUILD_ROOT%{_libdir}/R/include
rm $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -i -e "s#$RPM_BUILD_ROOT##g" $RPM_BUILD_ROOT%{_libdir}/%{name}/bin/%{name}
ln -sf %{_libdir}/%{name}/bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
/sbin/ldconfig

%postun	-p /sbin/ldconfig

%files base
%defattr(644,root,root,755)
%doc COPYRIGHTS FAQ NEWS README RESOURCES THANKS Y2K

%{_mandir}/man1/R.1*
%attr(755,root,root) %{_bindir}/R
%dir %{_libdir}/R
%{_libdir}/R/afm
%attr(755,root,root) %{_libdir}/R/bin
%attr(755,root,root) %{_libdir}/libR*.so
%{_libdir}/R/etc
%{_libdir}/R/include
%{_includedir}/R
%{_libdir}/R/share
%{_libdir}/R/AUTHORS
%dir %{_libdir}/R/library
# %{_libdir}/R/doc %except %{_libdir}/R/doc/html/{packages.html,search/index.txt}
%dir %{_libdir}/R/doc
%{_libdir}/R/doc/[KRm]*
%dir %{_libdir}/R/doc/html
%{_libdir}/R/doc/html/*.css
%{_libdir}/R/doc/html/[Ra-lr-u]*.html
%{_libdir}/R/doc/html/packages-head.html
%{_libdir}/R/doc/html/*.jpg
%dir %{_libdir}/R/doc/html/search
%{_libdir}/R/doc/html/search/[A-Z]*
%ghost %{_libdir}/R/doc/html/search/index.txt
%ghost %{_libdir}/R/doc/html/packages.html
%{_desktopdir}/*

%attr(755,root,root) %{_libdir}/%{name}/modules

%{_libdir}/%{name}/library/base
%{_libdir}/%{name}/library/datasets
%{_libdir}/%{name}/library/grid
%{_libdir}/%{name}/library/graphics
%{_libdir}/%{name}/library/grDevices
%{_libdir}/%{name}/library/methods
%{_libdir}/%{name}/library/utils
%{_libdir}/%{name}/library/tcltk
%{_libdir}/%{name}/library/splines
%{_libdir}/%{name}/library/stats
%{_libdir}/%{name}/library/stats4
%{_libdir}/%{name}/library/tools
