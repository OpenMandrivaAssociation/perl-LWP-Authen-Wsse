%define upstream_name    LWP-Authen-Wsse
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Library for enabling X-WSSE authentication in LWP
License:	Artistic and GPL+
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/LWP/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::SHA1)
BuildArch:	noarch

%description
LWP::Authen::Wsse allows LWP to authenticate against servers that are using 
the X-WSSE authentication scheme, as required by the Atom Authentication API.

%prep
%setup -q -n LWP-Authen-Wsse-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 655036
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 406069
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.05-4mdv2009.0
+ Revision: 241650
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-2mdv2008.0
+ Revision: 88412
- rebuild


* Wed Aug 09 2006 Michael Scherer <misc@mandriva.org> 0.05-1mdv2007.0
- First Mandriva package

