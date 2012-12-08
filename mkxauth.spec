%define name	mkxauth
%define version	1.7
%define release	%mkrel 21

Summary:	A utility for managing .Xauthority files
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		File tools
Url:		http://www.tummy.com/krud/packages/mkxauth.html
Source0: 	%{name}-%{version}.tar.bz2
BuildArch: 	noarch
Requires: 	xauth 
Requires: 	coreutils
Requires:	procps
Requires:	gzip
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root

%description
The mkxauth utility helps create and maintain X authentication
databases (.Xauthority files).  Mkxauth is used to create an
.Xauthority file or to merge keys from another local or remote
.Xauthority file.  .Xauthority files are used by the xauth
user-oriented access control program, which grants or denies
access to X servers based on the contents of the .Xauthority
file.

The mkxauth package should be installed if you're going to use
user-oriented access control to provide security for your X Window
System (a good idea).

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -m 0755 mkxauth $RPM_BUILD_ROOT%{_bindir}/mkxauth
install -m 0444 mkxauth.1x.bz2 $RPM_BUILD_ROOT%{_mandir}/man1/mkxauth.1x.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/mkxauth
%{_mandir}/man1/*





%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7-20mdv2011.0
+ Revision: 666438
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-19mdv2011.0
+ Revision: 606650
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-18mdv2010.1
+ Revision: 523323
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.7-17mdv2010.0
+ Revision: 426153
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.7-16mdv2009.1
+ Revision: 351609
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.7-15mdv2009.0
+ Revision: 223294
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.7-13mdv2008.1
+ Revision: 153124
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.7-12mdv2008.0
+ Revision: 69904
- fileutils, sh-utils & textutils have been obsoleted by coreutils a long time ago


* Mon Aug 28 2006 Pixel <pixel@mandriva.com>
+ 2006-08-28 10:58:53 (58270)
- silent %%setup

* Mon Aug 28 2006 Pixel <pixel@mandriva.com>
+ 2006-08-28 10:57:04 (58269)
- move from /usr/X11R6/bin to /usr/bin

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 16 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-16 16:16:01 (27424)
- do not depend on a hardcode path. Better depend on a package

* Mon May 15 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-15 19:29:55 (27411)
- adding mkxauth to the repository

* Thu Oct 13 2005 Pixel <pixel@mandriva.com> 1.7-9mdk
- rebuild

