Summary:	A utility for managing .Xauthority files
Name:		mkxauth
Version:	1.7
Release:	34
License:	GPLv2
Group:		File tools
Url:		https://www.tummy.com/krud/packages/mkxauth.html
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	xauth 
Requires:	coreutils
Requires:	procps
Requires:	gzip

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
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -m 0755 mkxauth %{buildroot}%{_bindir}/mkxauth
install -m 0444 mkxauth.1x.bz2 %{buildroot}%{_mandir}/man1/mkxauth.1x.bz2

%files
%{_bindir}/mkxauth
%{_mandir}/man1/*

