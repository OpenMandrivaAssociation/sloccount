%define name sloccount
%define version 2.26
%define debug_package          %{nil}


Name: %name
Summary: Measures source lines of code (SLOC) in programs
Version: %version
Release: 10
License: GPL
Group: Development/Other
Source: http://www.dwheeler.com/sloccount/%name-%version.tar.bz2
URL: https://www.dwheeler.com/sloccount
BuildRoot: %{_tmppath}/%name-buildroot
BuildRequires:	flex

%description
SLOCCount (pronounced "sloc-count") is a suite of programs for counting
physical source lines of code (SLOC) in potentially large software systems
(thus, SLOCCount is a "software metrics tool" or "software measurement tool").
SLOCCount can count physical SLOC for a wide number of languages;
listed alphabetically, they are: Ada, Assembly, awk, Bourne shell, C, C++,
C shell, COBOL, Expect, Fortran, Java, lex/flex, LISP (including Scheme),
Modula-3, Objective-C, Pascal, Perl, PHP, Python, sed, TCL, and Yacc.
SLOCCount can automatically determine if a file
is a source code file or not, and if so, which language it's written in.
As a result, you can analyze large systems completely automatically;
it's been used to examine entire GNU/Linux distributions, for example.
SLOCCount also includes some report-generating tools
to collect the data generated and present it in several different formats.
Normally you can just run "sloccount DIRECTORY" and all the source code
in the directory and its descendants will be counted.

%prep
%setup -q

%build
%make

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
make install_programs PREFIX=${RPM_BUILD_ROOT}%{_prefix}
make install_man PREFIX=${RPM_BUILD_ROOT}%{_prefix}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root)
%doc sloccount.html README ChangeLog COPYING TODO
%{_bindir}/*
%{_mandir}/*/*




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.26-8mdv2010.0
+ Revision: 433937
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.26-7mdv2009.0
+ Revision: 260809
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.26-6mdv2009.0
+ Revision: 252612
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.26-4mdv2008.1
+ Revision: 136503
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Oct 31 2006 Michael Scherer <misc@mandriva.org> 2.26-4mdv2007.0
+ Revision: 74682
- Bump release
- Import sloccount

