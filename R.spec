#
# Conditional build:
# _without_gnome        - without gnome support
#
Summary:	A language for data analysis and graphics
Summary(pl):	Jêzyk do analizy danych oraz grafiki
Name:		R
Version:	1.4.0
Release:	1
Source0:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/base/%{name}-%{version}.tgz
Source1:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/mlbench_0.5-4.tar.gz
Source2:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/VR_6.3-1.tar.gz
Source3:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/acepack_1.3.tar.gz
Source4:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/bootstrap_1.0-9.tar.gz
Source5:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/cluster_1.3-6.tar.gz
Source6:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/date_1.2-11.tar.gz
Source7:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/e1071_1.2-1.tar.gz
Source8:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/fracdiff_1.0-7.tar.gz
Source9:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/gee_4.13-6.tar.gz
#Source10:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/integrate_2.2-3.tar.gz
# Source11:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/jpn_1.0-1.tar.gz
Source12:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/leaps_2.1-1.tar.gz
Source13:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/oz_1.0-6.tar.gz
Source14:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/polynom_1.1-8.tar.gz
Source15:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/princurve_1.1-3.tar.gz
Source16:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/quadprog_1.4-3.tar.gz
# Source17:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/ratetables_1.0-2.tar.gz
# Source18:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/rational_1.0-1.tar.gz
Source19:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/survival_2.6.tar.gz
Source20:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/xgobi_1.2-5.tar.gz
Patch0:		R-destdir.patch
# Patch0:		%{name}-0.61.rpm.patch3
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
URL:		http://stat.auckland.ac.nz/r/r.html
Provides:	R-base R-contrib
BuildRequires:	libstdc++-devel
BuildRequires:	gcc-c++
BuildRequires:	gcc-g77
BuildRequires:	perl >= 5
BuildRequires:	libtool
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-pdftex
BuildRequires:	zip
BuildRequires:	XFree86-devel
BuildRequires:	libpng-devel >= 1.0.5
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libxml-devel
BuildRequires:	zlib >= 1.1.3
BuildRequires:	readline-devel
#BuildRequires:	lpr
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
%{!?_without_gnome:BuildRequires:	ORBit-devel}
%{!?_without_gnome:BuildRequires:	libglade-devel}
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
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Provides:	R-acepack R-bootstrap R-VR R-cluster R-ctest R-date R-e1071
Provides:	R-fracdiff R-gee R-integrate R-jpn R-leaps R-mlbench R-oz
Provides:	R-polynom R-princurve R-quadprog R-ratetables R-rational
Provides:	R-splines R-survival R-xgobi
Obsoletes:	R-principal.curve R-survival4 R-clus R-class R-nnet R-spatial

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

%package contrib
Summary:	Contributed packages for the R language
Summary(pl):	Dodatkowe pakiety do jêzyka R
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
License:	Mixed
URL:		http://www.ci.tuwien.ac.at/R/
Requires:	R-base >= %{version}

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
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
License:	GPL
URL:		http://www.ics.uci.edu/~mlearn/MLRepository.html
Requires:	R-base >= %{version}

%description mlbench
R package which contains a collection of real-world datasets and
functions for creating artificial datasets that work as benchmarks for
machine learning methods.

%description mlbench -l pl
Ten podpakiet R zawiera zestaw rzeczywistych danych i funkcji do
zrobienia sztucznych danych dzia³aj±cych jako test wydajno¶ci metod
uczenia maszyny.

%prep
%setup -q -c -n R-cran -T -b 2
%setup -q -c -n R-cran -T -D -b 3
%setup -q -c -n R-cran -T -D -b 4
%setup -q -c -n R-cran -T -D -b 5
%setup -q -c -n R-cran -T -D -b 6
%setup -q -c -n R-cran -T -D -b 7
%setup -q -c -n R-cran -T -D -b 8
%setup -q -c -n R-cran -T -D -b 9
#%setup -q -c -n R-cran -T -D -b 10
# %setup -q -c -n R-cran -T -D -b 11
%setup -q -c -n R-cran -T -D -b 12
%setup -q -c -n R-cran -T -D -b 13
%setup -q -c -n R-cran -T -D -b 14
%setup -q -c -n R-cran -T -D -b 15
%setup -q -c -n R-cran -T -D -b 16
# %setup -q -c -n R-cran -T -D -b 17
# %setup -q -c -n R-cran -T -D -b 18
%setup -q -c -n R-cran -T -D -b 19
%setup -q -c -n R-cran -T -D -b 20
%setup -q 
%setup -q -T -D -a 1
%patch0 -p0
# %patch0 -p1
# These files have the path for PERL hard-coded as /usr/local/bin/perl
# We need to remove them to avoid dependency problems
rm -f ./doc/keyword-test.orig ./etc/undoc/R-funs.orig ./etc/undoc/extrExamp.orig 

%build
%configure2_13 \
	%{!?_without_gnome:--with-gnome} \
	%{?_without_gnome:--without-gnome} \
	--without-tcltk

%{__make} 
%{__make} help
%{__make} html
%{__make} clean
# %{__make} acclean

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

# Install mlbench
#
${R_HOME}/bin/INSTALL mlbench

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
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
install doc/R.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
install -d ${RPM_BUILD_ROOT}%{_libdir}/R
# cp -R afm bin cmd demos doc etc html include library ${RPM_BUILD_ROOT}%{_libdir}/R
cp -R afm bin doc etc include library modules ${RPM_BUILD_ROOT}%{_libdir}/R
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 bin/R ${RPM_BUILD_ROOT}%{_bindir}/R

%clean
# rm -rf $RPM_BUILD_ROOT

%post base
(cd %{_libdir}/R/library; cat */TITLE > LibIndex; ../etc/build-htmlpkglist)

%preun base
# These files are not owned by any package, so we have to remove them
# but only if this is the last version of R-base on the system.
#
if [ "$1" = 0 ];
then
	rm -f %{_libdir}/R/library/LibIndex
	rm -f %{_libdir}/R/library/index.html
fi

%post contrib
(cd %{_libdir}/R/library; cat */TITLE > LibIndex; ../etc/build-htmlpkglist)

%postun contrib
(cd %{_libdir}/R/library; cat */TITLE > LibIndex; ../etc/build-htmlpkglist)

%post mlbench
(cd %{_libdir}/R/library; cat */TITLE > LibIndex; ../etc/build-htmlpkglist)

%postun mlbench
(cd %{_libdir}/R/library; cat */TITLE > LibIndex; ../etc/build-htmlpkglist)

%files base
%defattr(644,root,root,755)
%attr(-,root,root) %{_mandir}/man1/R.1*
%attr(-,root,root) %{_bindir}/R
%attr(-,root,root) %dir %{_libdir}/R
%attr(-,root,root) %{_libdir}/R/afm
%attr(-,root,root) %{_libdir}/R/bin
# %attr(-,root,root) %{_libdir}/R/cmd
# %attr(-,root,root) %{_libdir}/R/demos
%attr(-,root,root) %{_libdir}/R/etc
%attr(-,root,root) %{_libdir}/R/include
%attr(-,root,root) %dir %{_libdir}/R/library
%attr(-,root,root) %{_libdir}/R/library/base/
%attr(-,root,root) %{_libdir}/R/library/ctest
%attr(-,root,root) %{_libdir}/R/library/eda/
%attr(-,root,root) %{_libdir}/R/library/mva/
%attr(-,root,root) %{_libdir}/R/library/splines
%attr(-,root,root) %{_libdir}/R/library/stepfun/
%attr(-,root,root) %{_libdir}/R/modules
%attr(-,root,root) %doc CHANGES COPYING COPYRIGHTS MIRROR-SITES PROJECTS README RESOURCES TASKS
%attr(-,root,root) %doc html

%files contrib
%defattr(644,root,root,755)
%attr(-,root,root) %{_libdir}/R/library/MASS
%attr(-,root,root) %{_libdir}/R/library/class
%attr(-,root,root) %{_libdir}/R/library/spatial
%attr(-,root,root) %{_libdir}/R/library/nnet
%attr(-,root,root) %doc VR
%attr(-,root,root) %{_libdir}/R/library/acepack
%attr(-,root,root) %doc acepack
%attr(-,root,root) %{_libdir}/R/library/bootstrap
%attr(-,root,root) %doc bootstrap
%attr(-,root,root) %{_libdir}/R/library/cluster
%attr(-,root,root) %doc cluster
%attr(-,root,root) %{_libdir}/R/library/date
%attr(-,root,root) %doc date
%attr(-,root,root) %{_libdir}/R/library/e1071
%attr(-,root,root) %doc e1071
%attr(-,root,root) %{_libdir}/R/library/fracdiff
%attr(-,root,root) %doc fracdiff
%attr(-,root,root) %{_libdir}/R/library/gee
%attr(-,root,root) %doc gee
%attr(-,root,root) %{_libdir}/R/library/integrate
%attr(-,root,root) %doc integrate
# %attr(-,root,root) %{_libdir}/R/library/jpn
# %attr(-,root,root) %doc jpn
%attr(-,root,root) %{_libdir}/R/library/leaps
%attr(-,root,root) %doc leaps
%attr(-,root,root) %{_libdir}/R/library/oz
%attr(-,root,root) %doc oz
%attr(-,root,root) %{_libdir}/R/library/polynom
%attr(-,root,root) %doc polynom
%attr(-,root,root) %{_libdir}/R/library/princurve
%attr(-,root,root) %doc princurve
%attr(-,root,root) %{_libdir}/R/library/quadprog
%attr(-,root,root) %doc quadprog
# %attr(-,root,root) %{_libdir}/R/library/ratetables
# %attr(-,root,root) %doc ratetables
# %attr(-,root,root) %{_libdir}/R/library/rational
# %attr(-,root,root) %doc rational
%attr(-,root,root) %{_libdir}/R/library/survival
%attr(-,root,root) %doc survival
%attr(-,root,root) %{_libdir}/R/library/xgobi
%attr(-,root,root) %doc xgobi

%files mlbench
%defattr(644,root,root,755)
%attr(-,root,root) %{_libdir}/R/library/mlbench
%attr(-,root,root) %doc mlbench/COPYRIGHT
%attr(-,root,root) %doc mlbench/ChangeLog
%attr(-,root,root) %doc mlbench/README
