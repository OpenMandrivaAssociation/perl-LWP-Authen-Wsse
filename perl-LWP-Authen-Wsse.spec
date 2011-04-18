%define upstream_name    LWP-Authen-Wsse
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Library for enabling X-WSSE authentication in LWP
License:	Artistic and GPL+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/LWP/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Digest::SHA1)
BuildArch:      noarch
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}

%description
LWP::Authen::Wsse allows LWP to authenticate against servers that are using 
the X-WSSE authentication scheme, as required by the Atom Authentication API.

%prep
%setup -q -n LWP-Authen-Wsse-%{upstream_version}

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
