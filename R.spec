Summary:	A language for data analysis and graphics
Name:		R
Version:	1.1.1
Release:	1
Source0:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/base/%{name}-%{version}.tgz
Source1:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/mlbench_0.4-1.tar.gz
Source2:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/acepack_1.2-1.tar.gz
Source3:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/bootstrap_1.0-5.tar.gz
#Source4:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/class_VR5-4.tar.gz
#Source5:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/clus_1.0-2.tar.gz
#Source6:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/ctest_0.9-1.tar.gz
Source7:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/date_1.2-4.tar.gz
Source8:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/e1071_0.9-2.tar.gz
Source9:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/fracdiff_1.0-6.tar.gz
Source10:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/gee_4.13-3.tar.gz
Source11:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/integrate_2.2-2.tar.gz
#Source12:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/jpn_1.0-1.tar.gz
Source13:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/leaps_2.0.tar.gz
#Source14:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/nnet_VR5-3.tar.gz
Source15:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/oz_1.0-3.tar.gz
Source16:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/polynom_1.1-3.tar.gz
#Source17:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/ratetables_1.0-2.tar.gz
#Source18:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/rational_1.0-1.tar.gz
#Source19:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/spatial_VR5-2.tar.gz
#Source20:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/splines_2.0-1.tar.gz
Source21:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/survival5_1.1-5.tar.gz
Source22:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/xgobi_1.2-2.tar.gz
#Source23:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/principal.curve_1.0-2.tar.gz
Source24:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/quadprog_1.4-1.tar.gz
Source31:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/mlbench.pdf
Source32:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/acepack.pdf
Source33:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/bootstrap.pdf
Source37:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/date.pdf
Source38:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/e1071.pdf
Source39:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/fracdiff.pdf
Source40:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/gee.pdf
Source41:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/intergate.pdf
Source43:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/leaps.pdf
Source45:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/oz.pdf
Source46:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/polymon.pdf
Source51:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/survival5.pdf
Source52:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/xgobi.pdf
Source54:	ftp://ftp.stat.math.ethz.ch/R-CRAN/src/contrib/quadprog.pdf
Patch0:		R-0.61.rpm.patch3
Copyright:	GPL
Group:		Development/Languages
URL:		http://stat.auckland.ac.nz/r/r.html
Provides:	R-base R-contrib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A system for statistical computation and graphics. R consists of a
language plus a run-time environment with graphics, a debugger, access
to certain system functions, and the ability to run programs stored in
script files.

The design of R has been heavily influenced by two existing languages:
Becker, Chambers & Wilks' S and Sussman's Scheme. Whereas the resulting
language is very similar in appearance to S, the underlying implementation
and semantics are derived from Scheme.

%package base
Summary:	The R base distribution
Group:		Development/Languages
Provides:	R-acepack R-bootstrap R-class R-clus R-ctest R-date R-e1071 
Provides:	R-fracdiff R-gee R-integrate R-jpn R-leaps R-mlbench R-nnet R-oz 
Provides:	R-polynom R-principal.curve R-quadprog R-ratetables R-rational 
Provides:	R-spatial R-splines R-survival4 R-xgobi

%description base
R is a language and run-time environment for carrying out interactive
statistical data analysis. It is not entirely dissimilar to the S language
developed at AT&T Bell Laboratories (and now Lucent Technologies). Indeed,
S users will find the environment quite familiar and a good deal of S
software will run without change under R.

%package contrib
Summary:	contributed packages for the R language
Group:		Development/Languages
Copyright:	Mixed
URL:		http://www.ci.tuwien.ac.at/R/
Requires:	R-base >= %{version}

%description contrib
Packages which extend the capabilities of the R base distribution
and are distributed on the Comprehensive R Archive Network (CRAN).

%package mlbench
Summary:	Machine learning benchmarks
Group:		Development/Languages
Copyright:	GPL
URL:		http://www.ics.uci.edu/~mlearn/MLRepository.html
Requires:	R-base >= %{version}

%description mlbench
R package which contains a collection of real-world datasets and
functions for creating artificial datasets that work as benchmarks
for machine learning methods.

%prep
%setup -q -c -n R-cran -T -b 2
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
%setup -q 
%setup -q -T -D -a 1
%patch0 -p1
# These files have the path for PERL hard-coded as /usr/local/bin/perl
# We need to remove them to avoid dependency problems
rm ./doc/keyword-test.orig ./etc/undoc/R-funs.orig ./etc/undoc/extrExamp.orig 

%build
%{__make} 
%{__make} help
%{__make} html
%{__make} clean
%{__make} acclean

# Install contrib packages
#
RHOME=`pwd`;export RHOME
cd ../R-cran
for pkg in `ls`
do
	${RHOME}/etc/INSTALL -latex ${pkg}
done
cd ${RHOME}

# Install mlbench
#
${RHOME}/etc/INSTALL mlbench

#Remove old template files.
#
for oldinfile in `find . -name '*.in' -print`
do
	rm ${oldinfile}
done

# Gather documentation from contrib packages in one directory
# Assume that anything not in one of the standard directories is
# documentation, and copy it.
#
mkdir ${RHOME}/contrib
cd ${RPM_BUILD_DIR}/R-cran
for pkg in `ls`; do
        if [ -d ${pkg} ]; then
		mkdir ${RHOME}/${pkg}
                for docfile in `ls ${pkg}`; do
                        case $docfile in
                                INDEX) ;;
                                TITLE) ;;
                                R) ;;
                                man) ;;
                                src) ;;
                                src-c) ;;
                                data) ;;
                                *) cp -R -P ${pkg}/${docfile} ${RHOME};;
                        esac
                done
        fi
done
cd ${RHOME}

%install
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
install R.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
install -d ${RPM_BUILD_ROOT}%{_libdir}/R
cp -R afm bin cmd demos doc etc html include library ${RPM_BUILD_ROOT}%{_libdir}/R
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 bin/R ${RPM_BUILD_ROOT}%{_bindir}/R

%files base
%defattr(644,root,root,755)
%attr(-,root,root) %{_mandir}/man1/R.1
%attr(-,root,root) %{_bindir}/R
%attr(-,root,root) %dir %{_libdir}/R
%attr(-,root,root) %{_libdir}/R/afm
%attr(-,root,root) %{_libdir}/R/bin
%attr(-,root,root) %{_libdir}/R/cmd
%attr(-,root,root) %{_libdir}/R/demos
%attr(-,root,root) %{_libdir}/R/etc
%attr(-,root,root) %{_libdir}/R/html
%attr(-,root,root) %{_libdir}/R/include
%attr(-,root,root) %dir %{_libdir}/R/library
%attr(-,root,root) %{_libdir}/R/library/base/
%attr(-,root,root) %{_libdir}/R/library/eda/
%attr(-,root,root) %{_libdir}/R/library/mva/
%attr(-,root,root) %{_libdir}/R/library/stepfun/
%attr(-,root,root) %doc CHANGES COPYING COPYRIGHTS MIRROR-SITES PROJECTS README RESOURCES TASKS

%files contrib
%defattr(644,root,root,755)
%attr(-,root,root) %{_libdir}/R/library/acepack
%attr(-,root,root) %doc acepack
%attr(-,root,root) %{_libdir}/R/library/bootstrap
%attr(-,root,root) %doc bootstrap
%attr(-,root,root) %{_libdir}/R/library/class
%attr(-,root,root) %doc class
%attr(-,root,root) %{_libdir}/R/library/clus
%attr(-,root,root) %doc clus
%attr(-,root,root) %{_libdir}/R/library/ctest
%attr(-,root,root) %doc ctest
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
%attr(-,root,root) %{_libdir}/R/library/jpn
%attr(-,root,root) %doc jpn
%attr(-,root,root) %{_libdir}/R/library/leaps
%attr(-,root,root) %doc leaps
%attr(-,root,root) %{_libdir}/R/library/nnet
%attr(-,root,root) %doc nnet
%attr(-,root,root) %{_libdir}/R/library/oz
%attr(-,root,root) %doc oz
%attr(-,root,root) %{_libdir}/R/library/polynom
%attr(-,root,root) %doc polynom
%attr(-,root,root) %{_libdir}/R/library/ratetables
%attr(-,root,root) %doc ratetables
%attr(-,root,root) %{_libdir}/R/library/rational
%attr(-,root,root) %doc rational
%attr(-,root,root) %{_libdir}/R/library/spatial
%attr(-,root,root) %doc spatial
%attr(-,root,root) %{_libdir}/R/library/splines
%attr(-,root,root) %doc splines
%attr(-,root,root) %{_libdir}/R/library/survival4
%attr(-,root,root) %doc survival4
%attr(-,root,root) %{_libdir}/R/library/xgobi
%attr(-,root,root) %doc xgobi
%attr(-,root,root) %{_libdir}/R/library/principal.curve
%attr(-,root,root) %doc principal.curve
%attr(-,root,root) %{_libdir}/R/library/quadprog
%attr(-,root,root) %doc quadprog

%files mlbench
%defattr(644,root,root,755)
%attr(-,root,root) %{_libdir}/R/library/mlbench
%attr(-,root,root) %doc mlbench/COPYRIGHT
%attr(-,root,root) %doc mlbench/ChangeLog
%attr(-,root,root) %doc mlbench/README

%clean
rm -rf ${RPM_BUILD_ROOT}

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
