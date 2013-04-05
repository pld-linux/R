#
# Conditional build
%bcond_without	tcl		# disable tcl support
%bcond_without	tests	# do not run "make check"
%bcond_without	docs	# do not build documentation
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
Version:	3.0.0
Release:	1
License:	Mixed (distributable), mostly GPL v2+
Group:		Development/Languages
# CRAN master site: ftp://cran.r-project.org/pub/R/src/
Source0:	ftp://stat.ethz.ch/R-CRAN/src/base/R-3/%{name}-%{version}.tar.gz
# Source0-md5:	5fb80535b0e144a978f67aa2158015de
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://www.r-project.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	blas-devel >= 3.2.2-2
BuildRequires:	bzip2-devel >= 1.0.6
BuildRequires:	cairo-devel >= 1.6
BuildRequires:	gcc-fortran
BuildRequires:	gettext-devel >= 0.14.5
BuildRequires:	lapack-devel >= 3.2.2-2
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.7
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libxml2-devel >= 2.6.26
BuildRequires:	pango-devel
BuildRequires:	pcre-devel >= 7.6
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov
%if %{with tcl}
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
%endif
%if %{with docs}
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	tetex-pdftex
BuildRequires:	texinfo-texi2dvi >= 4.7
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz-devel >= 4.999
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.3
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

%build
%{__aclocal} -I m4
%{__autoconf}
install -d build
cd build
../%configure \
	F77=gfortran \
	FC=gfortran \
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

%if %{with docs}
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

mv $RPM_BUILD_ROOT%{_libdir}/%{name}/include $RPM_BUILD_ROOT%{_includedir}/R
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
done > R.files

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f R.files
%defattr(644,root,root,755)
%doc NEWS README doc/{AUTHORS,COPYRIGHTS,FAQ,RESOURCES,THANKS}
%attr(755,root,root) %{_bindir}/R
%attr(755,root,root) %{_bindir}/Rscript
%dir %{_libdir}/R
%dir %{_libdir}/R/lib
%attr(755,root,root) %{_libdir}/R/lib/libR.so
%attr(755,root,root) %{_libdir}/libR.so
%{_libdir}/R/COPYING
%{_libdir}/R/NEWS
%{_libdir}/R/SVN-REVISION
%attr(755,root,root) %{_libdir}/R/bin
%exclude %{_libdir}/R/bin/javareconf
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
# library files list is autogenerated (see R.files above)
%attr(755,root,root) %{_libdir}/R/modules
%dir %{_libdir}/R/share
%{_libdir}/R/share/R
%{_libdir}/R/share/encodings
%{_libdir}/R/share/licenses
%{_libdir}/R/share/make
%{_libdir}/R/share/sh
%{_libdir}/R/share/texmf
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
