#
# Conditional build:
# _without_gnome        - without GNOME support
#
Summary:	A language for data analysis and graphics
Summary(pl):	Jêzyk do analizy danych oraz grafiki
Name:		R
Version:	1.6.1
Release:	2
License:	Mixed (distributable), mostly GPL
Group:		Development/Languages
Source0:	ftp://stat.ethz.ch/R-CRAN/src/base/%{name}-%{version}.tgz
# Source0-md5:	7c9b8e8582812448aedd0322bcc135eb
Source1:	ftp://stat.ethz.ch/R-CRAN/src/contrib/KernSmooth_2.22-8.tar.gz
# Source1-md5:	6b1c0627c534e9229110dbde30dbeeec
Source2:	ftp://stat.ethz.ch/R-CRAN/src/contrib/VR_7.0-9.tar.gz
# Source2-md5:	95755187724901757f94d20875a1ea6c
Source3:	ftp://stat.ethz.ch/R-CRAN/src/contrib/acepack_1.3-2.tar.gz
# Source3-md5:	334452ea1a1ba351154aea9c4eb9912d
Source4:	ftp://stat.ethz.ch/R-CRAN/src/contrib/boot_1.2-8.tar.gz
# Source4-md5:	48f5bfbdd3b81dece8b206a660cd8e08
Source5:	ftp://stat.ethz.ch/R-CRAN/src/contrib/bootstrap_1.0-11.tar.gz
# Source5-md5:	7deba906ab0e88349c47a2fb3e8c5a9e
Source6:	ftp://stat.ethz.ch/R-CRAN/src/contrib/cluster_1.6-2.tar.gz
# Source6-md5:	4922165554622775c21889596041fe6c
Source7:	ftp://stat.ethz.ch/R-CRAN/src/contrib/date_1.2-12.tar.gz
# Source7-md5:	fbc71aba3c8401d7aede6f33d8c5c1aa
Source8:	ftp://stat.ethz.ch/R-CRAN/src/contrib/e1071_1.3-5.tar.gz
# Source8-md5:	c835647201dbe4d908841f733a735c33
Source9:	ftp://stat.ethz.ch/R-CRAN/src/contrib/foreign_0.5-6.tar.gz
# Source9-md5:	4a79983be6920326242f468a9184fccb
Source10:	ftp://stat.ethz.ch/R-CRAN/src/contrib/fracdiff_1.0-8.tar.gz
# Source10-md5:	58e196dcd8512e021bdb687b071c6dfb
Source11:	ftp://stat.ethz.ch/R-CRAN/src/contrib/gee_4.13-10.tar.gz
# Source11-md5:	7f32a7f7b022dd366d27482a3561d2a6
Source12:	ftp://stat.ethz.ch/R-CRAN/src/contrib/grid_0.7-1.tar.gz
# Source12-md5:	01cfb0d1c1fa134bb05b2844572edf8e
Source13:	ftp://stat.ethz.ch/R-CRAN/src/contrib/lattice_0.6-6.tar.gz
# Source13-md5:	588deaa2f8189dfdcc9ce0f3eafce6e2
Source14:	ftp://stat.ethz.ch/R-CRAN/src/contrib/leaps_2.5.tar.gz
# Source14-md5:	47567135b492a9ee3308b710e46264e5
Source15:	ftp://stat.ethz.ch/R-CRAN/src/contrib/mgcv_0.8-6.tar.gz
# Source15-md5:	eeb171868243db04f0f5300df7dedbe6
Source16:	ftp://stat.ethz.ch/R-CRAN/src/contrib/mlbench_0.5-7.tar.gz
# Source16-md5:	00ea4e9ab190ff5c86fc692947d85667
Source17:	ftp://stat.ethz.ch/R-CRAN/src/contrib/nlme_3.1-33.tar.gz
# Source17-md5:	25870da409c0d6e0ef1b220e420dba0f
Source18:	ftp://stat.ethz.ch/R-CRAN/src/contrib/oz_1.0-6.tar.gz
# Source18-md5:	0582275bed974be04ad8c194d3c61b54
Source19:	ftp://stat.ethz.ch/R-CRAN/src/contrib/polynom_1.1-10.tar.gz
# Source19-md5:	427e486a667e051dab899e3580072c0f
Source20:	ftp://stat.ethz.ch/R-CRAN/src/contrib/princurve_1.1-5.tar.gz
# Source20-md5:	d0092745f92687c54b055e2770fd6e5b
Source21:	ftp://stat.ethz.ch/R-CRAN/src/contrib/quadprog_1.4-5.tar.gz
# Source21-md5:	00c6b832f35632c80eadbaa700d54c73
Source22:	ftp://stat.ethz.ch/R-CRAN/src/contrib/rpart_3.1-8.tar.gz
# Source22-md5:	4b827ca24b940c86601df81ca19b55c8
Source23:	ftp://stat.ethz.ch/R-CRAN/src/contrib/survival_2.9-6.tar.gz
# Source23-md5:	f50fdeb0574953b4deff399450cd0edd
Source24:	ftp://stat.ethz.ch/R-CRAN/src/contrib/xgobi_1.2-7.tar.gz
# Source24-md5:	6d1c3fb1c8f3bdcc00263ef21875c0eb
Source25:	ftp://stat.ethz.ch/R-CRAN/src/contrib/Archive/integrate_2.2-3.tar.gz
# Source25-md5:	40cc14374a0992871dd651d41289b3e6
Source26:	%{name}.desktop
URL:		http://stat.auckland.ac.nz/r/r.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	gcc-c++
BuildRequires:	gcc-g77
BuildRequires:	perl >= 5.004
BuildRequires:	libtool
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-pdftex
BuildRequires:	zip
BuildRequires:	XFree86-devel
BuildRequires:	blas-devel
BuildRequires:	libpng-devel >= 1.0.5
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libxml-devel
BuildRequires:	zlib >= 1.1.3
BuildRequires:	readline-devel
#BuildRequires:	lpr
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
%{!?_without_gnome:BuildRequires:	ORBit-devel}
%{!?_without_gnome:BuildRequires:	libglade-gnome-devel}
Provides:	R-base
Provides:	R-contrib
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
Requires(post):	perl
Provides:	R-ctest R-eda R-lqs R-methods R-modreg R-mva R-nls R-splines
Provides:	R-stepfun R-tcltk R-tools R-ts

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
Provides:	R-KernSmooth R-VR R-boot R-cluster R-foreign R-grid
Provides:	R-lattice R-mgcv R-nlme	R-rpart R-survival
License:	GPL, free or free for non-commercial use
URL:		http://www.ci.tuwien.ac.at/R/
Requires(post,postun):	R-base
Requires(post,postun):	textutils
Requires(post,postun):	perl
Requires:	R-base >= %{version}
Obsoletes:	R-survival4 R-MASS R-clus R-class R-nnet R-spatial

%description recommended
Packages which extend the capabilities of the R base distribution and
are distributed on the Comprehensive R Archive Network (CRAN).

%description recommended -l pl
Pakiety rozszerzaj±ce mo¿liwo¶ci podstawowej dystrybucji jêzyka R,
dystrubuowane w archiwum CRAN (Comprehensive R Archive Network).

%package contrib
Summary:	Contributed packages for the R language
Summary(pl):	Dodatkowe pakiety do jêzyka R
License:	Mixed
Group:		Development/Languages
URL:		http://www.ci.tuwien.ac.at/R/
Requires(post,postun):	R-base
Requires(post,postun):	textutils
Requires(post,postun):	perl
Requires:	R-base >= %{version}
Requires:	R-VR
Provides:	R-acepack R-bootstrap R-date R-e1071 R-fracdiff R-gee
Provides:	R-integrate R-leaps R-oz R-polynom R-princurve R-quadprog
Provides:	R-xgobi
Obsoletes:	R-principal.curve

%description contrib
Packages which extend the capabilities of the R base distribution and
are distributed on the Comprehensive R Archive Network (CRAN).

%description contrib -l pl
Pakiety rozszerzaj±ce mo¿liwo¶ci podstawowej dystrybucji jêzyka R,
dystrubuowane w archiwum CRAN (Comprehensive R Archive Network).

%package mlbench
Summary:	Machine learning benchmarks
Summary(pl):	Testy wydajno¶ci uczenia maszyny
Group:		Development/Languages
License:	GPL
URL:		http://www.ics.uci.edu/~mlearn/MLRepository.html
Requires(post,postun):	R-base
Requires(post,postun):	textutils
Requires(post,postun):	perl
Requires:	R-base >= %{version}

%description mlbench
R package which contains a collection of real-world datasets and
functions for creating artificial datasets that work as benchmarks for
machine learning methods.

%description mlbench -l pl
Ten podpakiet R zawiera zestaw rzeczywistych danych i funkcji do
tworzenia sztucznych danych s³u¿±cych jako test wydajno¶ci metod
uczenia maszyny.

%prep
%setup -q -c -n R-cran -T -b 1
%setup -q -c -n R-cran -T -D -b 2
%setup -q -c -n R-cran -T -D -b 3
%setup -q -c -n R-cran -T -D -b 4
%setup -q -c -n R-cran -T -D -b 5
%setup -q -c -n R-cran -T -D -b 6
%setup -q -c -n R-cran -T -D -b 7
%setup -q -c -n R-cran -T -D -b 8
%setup -q -c -n R-cran -T -D -b 9
%setup -q -c -n R-cran -T -D -b 10
%setup -q -c -n R-cran -T -D -b 11
%setup -q -c -n R-cran -T -D -b 12
%setup -q -c -n R-cran -T -D -b 13
%setup -q -c -n R-cran -T -D -b 14
%setup -q -c -n R-cran -T -D -b 15
%setup -q -c -n R-cran -T -D -b 16
%setup -q -c -n R-cran -T -D -b 17
%setup -q -c -n R-cran -T -D -b 18
%setup -q -c -n R-cran -T -D -b 19
%setup -q -c -n R-cran -T -D -b 20
%setup -q -c -n R-cran -T -D -b 21
%setup -q -c -n R-cran -T -D -b 22
%setup -q -c -n R-cran -T -D -b 23
%setup -q -c -n R-cran -T -D -b 24
%setup -q -c -n R-cran -T -D -b 25
%setup -q
#%setup -q -T -D -a 14

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
	--without-tcltk

%{__make}
%{__make} help
%{__make} html
%{__make} clean

# Install contrib packages
#
R_HOME=`pwd`;export R_HOME
PERL5LIB=`pwd`/share/perl;export PERL5LIB
cd ../R-cran
for pkg in `ls`
do
${R_HOME}/bin/INSTALL ${pkg}
done
cd ${R_HOME}

#Remove old template files.
#
for oldinfile in `find . -name '*.in' -print`
do
	mv ${oldinfile} ${oldinfile}.old
#	rm ${oldinfile}
done

# Gather documentation from contrib packages in one directory
# Assume that anything not in one of the standard directories is
# documentation, and copy it.
#
mkdir ${R_HOME}/contrib
cd ${RPM_BUILD_DIR}/R-cran
for pkg in `ls`; do
        if [ -d ${pkg} ]; then
		mkdir ${R_HOME}/${pkg}
                for docfile in `ls ${pkg}`; do
                        case $docfile in
                                INDEX) ;;
                                TITLE) ;;
                                R) ;;
                                man) ;;
                                src) ;;
                                src-c) ;;
                                data) ;;
                                *) cp -R -P ${pkg}/${docfile} ${R_HOME};;
                        esac
                done
        fi
done
cd ${R_HOME}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/R,%{_applnkdir}/Scientific/Numerics}

install %{SOURCE26} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Numerics/%{name}.desktop

mv doc/R.1 $RPM_BUILD_ROOT%{_mandir}/man1/
sed "s,`pwd`,%{_libdir}/R,g" < bin/R > bin/R. ; mv bin/R. bin/R
mv bin/R $RPM_BUILD_ROOT%{_bindir}/R

find . -name 'Makefile*' -exec rm -f {} \;
rm -rf etc/*.old

cp -R AUTHORS afm bin doc etc include library modules share \
	$RPM_BUILD_ROOT%{_libdir}/R

%clean
rm -rf $RPM_BUILD_ROOT

%post base
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

#%preun base
## These files are not owned by any package, so we have to remove them
## but only if this is the last version of R-base on the system.
##
#if [ "$1" = 0 ];
#then
#	rm -f %{_libdir}/R/doc/html/search/index.txt
#	rm -f %{_libdir}/R/doc/html/packages.html
#fi

%post contrib
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun contrib
if [ -f ../bin/Rcmd ];then
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%post recommended
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun recommended
if [ -f ../bin/Rcmd ];then
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%post mlbench
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun mlbench
if [ -f ../bin/Rcmd ];then
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files base
%defattr(644,root,root,755)
%{_mandir}/man1/R.1*
%attr(755,root,root) %{_bindir}/R
%dir %{_libdir}/R
%{_libdir}/R/afm
%attr(755,root,root) %{_libdir}/R/bin
%{_libdir}/R/etc
%{_libdir}/R/include
%{_libdir}/R/share
%{_libdir}/R/AUTHORS
%dir %{_libdir}/R/library
%{_libdir}/R/library/*.css
%{_libdir}/R/library/base
%{_libdir}/R/library/ctest
%{_libdir}/R/library/eda
%{_libdir}/R/library/lqs
%{_libdir}/R/library/methods
%{_libdir}/R/library/modreg
%{_libdir}/R/library/mva
%{_libdir}/R/library/nls
%{_libdir}/R/library/splines
%{_libdir}/R/library/stepfun
%{_libdir}/R/library/tcltk
%{_libdir}/R/library/tools
%{_libdir}/R/library/ts
%{_libdir}/R/modules
%doc BUGS COPYRIGHTS FAQ NEWS README RESOURCES THANKS Y2K
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
%{_applnkdir}/Scientific/Numerics/*

%files recommended
%defattr(644,root,root,755)
%{_libdir}/R/library/MASS
%{_libdir}/R/library/class
%{_libdir}/R/library/nnet
%{_libdir}/R/library/spatial
%doc VR
%{_libdir}/R/library/KernSmooth
%doc KernSmooth
%{_libdir}/R/library/boot
%doc boot
%{_libdir}/R/library/cluster
%doc cluster
%{_libdir}/R/library/foreign
%doc foreign
%{_libdir}/R/library/grid
%doc grid
%{_libdir}/R/library/lattice
%doc lattice
%{_libdir}/R/library/mgcv
%doc mgcv
%{_libdir}/R/library/nlme
%doc nlme
%{_libdir}/R/library/rpart
%doc rpart
%{_libdir}/R/library/survival
%doc survival

%files contrib
%defattr(644,root,root,755)
%{_libdir}/R/library/acepack
%doc acepack
%{_libdir}/R/library/bootstrap
%doc bootstrap
%{_libdir}/R/library/date
%doc date
%{_libdir}/R/library/e1071
%doc e1071
%{_libdir}/R/library/fracdiff
%doc fracdiff
%{_libdir}/R/library/gee
%doc gee
%{_libdir}/R/library/integrate
%doc integrate
%{_libdir}/R/library/leaps
%doc leaps
%{_libdir}/R/library/oz
%doc oz
%{_libdir}/R/library/polynom
%doc polynom
%{_libdir}/R/library/princurve
%doc princurve
%{_libdir}/R/library/quadprog
%doc quadprog
%{_libdir}/R/library/xgobi
%doc xgobi

%files mlbench
%defattr(644,root,root,755)
%{_libdir}/R/library/mlbench
%doc mlbench
