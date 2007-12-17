%define module  LWP-Authen-Wsse
%define name    perl-%{module}
%define version 0.05
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic and GPL
Group:		Development/Perl
Summary:    Library for enabling X-WSSE authentication in LWP
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/LWP/%{module}-%{version}.tar.bz2
BuildRequires:	perl(Digest::SHA1)
BuildArch:      noarch

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

