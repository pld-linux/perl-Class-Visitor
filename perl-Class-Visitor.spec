%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Visitor
Summary:	Class::Visitor perl module
Summary(pl):	Modu³ perla Class::Visitor
Name:		perl-Class-Visitor
Version:	0.02
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Visitor extends the Class::Template Perl module with
implementations of the Visitor and Iterator design patterns for
multi-level container hierarchies.

%description -l pl
Class::Visitor rozszerza modu³ Class::Template o implementacje wzorców
Visitor i Iterator do wielopoziomowych hierarchii kontenerów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{perl_sitelib}/Class
%{perl_sitelib}/Class/*.pm
