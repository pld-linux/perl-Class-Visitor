%include	/usr/lib/rpm/macros.perl
Summary:	Class::Visitor perl module
Summary(pl):	Modu³ perla Class::Visitor
Name:		perl-Class-Visitor
Version:	0.02
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Class/Class-Visitor-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Visitor extends the Class::Template Perl module with
implementations of the Visitor and Iterator design patterns for
multi-level container hierarchies.

%prep
%setup -q -n Class-Visitor-%{version}

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
