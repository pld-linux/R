# TODO:
# - move perl R libraries to standard perl location
# - script for rpm to autoprovides/autorequires R internals
#
# Conditional build:
%bcond_without	gnome	# without GNOME support
#
Summary:	A language for data analysis and graphics
Summary(pl):	Jêzyk do analizy danych oraz grafiki
Name:		R
Version:	2.0.1
Release:	2
License:	Mixed (distributable), mostly GPL
Group:		Development/Languages
# CRAN master site: ftp://cran.r-project.org/pub/R/src/
Source0:	ftp://stat.ethz.ch/R-CRAN/src/base/R-2/%{name}-%{version}.tar.gz
# Source0-md5:	fb47b1fdef4323031e24d541a2f36b2b
# Source0-size:	10676072
Source1:	%{name}.desktop
URL:		http://www.r-project.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	blas-devel
BuildRequires:	gcc-c++
BuildRequires:	gcc-g77
BuildRequires:	gettext-devel
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
%{?with_gnome:BuildRequires:	gnome-libs-devel}
%{?with_gnome:BuildRequires:	ORBit-devel}
%{?with_gnome:BuildRequires:	libglade-gnome-devel}
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
System do obliczeñ statystycznych i grafiki. R sk³ada siê z jêzyka
oraz ¶rodowiska uruchomieniowego z grafik±, debuggerem, dostêpem do
niektórych funkcji systemowych oraz mo¿liwo¶ci± uruchamiania programów
zapisanych w skryptach.

Jêzyk R by³ zainspirowany dwoma istniej±cymi jêzykami: S (Beckera,
Chambersa i Wilksa) oraz Scheme (Sussmana). R jest podobny do S, ale
implementacja i semantyka wywodzi siê ze Scheme.

%package base
Summary:	The R base distribution
Summary(pl):	Podstawowa dystrybucja R
License:	GPL v2 / LGPL
Group:		Development/Languages
Requires(post):	textutils
Requires(post):	perl-base
Provides:	R-cran-base
Provides:	R-cran-datasets
Provides:	R-cran-grid
Provides:	R-cran-graphics
Provides:	R-cran-grDevices
Provides:	R-cran-methods
Provides:	R-cran-utils
Provides:	R-cran-tcltk
Provides:	R-cran-splines
Provides:	R-cran-stats
Provides:	R-cran-stats4
Provides:	R-cran-tools

%description base
R is a language and run-time environment for carrying out interactive
statistical data analysis. It is not entirely dissimilar to the S
language developed at AT&T Bell Laboratories (and now Lucent
Technologies). Indeed, S users will find the environment quite
familiar and a good deal of S software will run without change under
R.

%description base -l pl
R jest jêzykiem i ¶rodowiskiem uruchomieniowym do interaktywnej
analizy danych statystycznych. R nie jest ca³kowicie zgodny z jêzykiem
S opracowanym w AT&T Bell Laboratiories (a teraz Lucent Technologies),
mimo to u¿ytkownicy S zauwa¿± zbli¿one ¶rodowisko, a du¿a czê¶æ
oprogramowania w S bêdzie dzia³a³a bez zmian w R.

%package recommended
Summary:	Recommended contributed packages for the R language
Summary(pl):	Zalecane dodatkowe pakiety do jêzyka R
Group:		Development/Languages
Requires:	R-cran-KernSmooth
Requires:	R-cran-VR
Requires:	R-cran-boot
Requires:	R-cran-cluster
Requires:	R-cran-foreign
Requires:	R-cran-lattice
Requires:	R-cran-mgcv
Requires:	R-cran-nlme
Requires:	R-cran-rpart
Requires:	R-cran-survival
License:	GPL, free or free for non-commercial use
URL:		http://www.ci.tuwien.ac.at/R/
Requires(post,postun):	R-base
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Obsoletes:	R-contrib
Requires:	R-base = %{version}-%{release}

%description recommended
Packages which extend the capabilities of the R base distribution and
are distributed on the Comprehensive R Archive Network (CRAN).

%description recommended -l pl
Pakiety rozszerzaj±ce mo¿liwo¶ci podstawowej dystrybucji jêzyka R,
dystrubuowane w archiwum CRAN (Comprehensive R Archive Network).

%prep
%setup -q

# These files have the path for Perl hard-coded as /usr/local/bin/perl
# We need to remove them to avoid dependency problems
rm -f ./doc/keyword-test.orig ./etc/undoc/R-funs.orig ./etc/undoc/extrExamp.orig

%build
%{__aclocal} -I m4
%{__autoconf}
cp -f /usr/share/automake/config.* .
%configure \
	--with%{!?with_gnome:out}-gnome \
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

%files recommended
