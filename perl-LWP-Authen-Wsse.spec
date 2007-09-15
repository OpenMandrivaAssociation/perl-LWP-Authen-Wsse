%define realname   LWP-Authen-Wsse

Name:		perl-%{realname}
Version:    0.05
Release:    %mkrel 2
License:	Artistic and GPL
Group:		Development/Perl
Summary:    Library for enabling X-WSSE authentication in LWP
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/LWP/LWP-Authen-Wsse-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel

BuildArch: noarch

%description
LWP::Authen::Wsse allows LWP to authenticate against servers that are using 
the X-WSSE authentication scheme, as required by the Atom Authentication API.

%prep
%setup -q -n LWP-Authen-Wsse-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

