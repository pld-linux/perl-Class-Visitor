%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Visitor
Summary:	Class::Visitor perl module
Summary(pl):	Modu³ perla Class::Visitor
Name:		perl-Class-Visitor
Version:	0.02
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b4ae495cdfac41c85351017631b37f5b
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Class/*.pm
