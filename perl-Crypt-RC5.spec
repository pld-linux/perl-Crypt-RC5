%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	RC5
Summary:	Crypt::RC5 Perl module - RC5 encryption algorithm implementation
Summary(pl):	Modu³ Perla Crypt::RC5 - implementacja algorytmu szyfrowania RC5
Name:		perl-Crypt-RC5
Version:	2.00
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	79649f6eba759a4415513a8512eaeb21
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl implementation of the RC5 algorithm. RC5 is a fast block cipher
designed by Ronald Rivest for RSA Data Security (now RSA Security) in
1994. It is a parameterized algorithm with a variable block size, a
variable key size, and a variable number of rounds. This particular
implementation is 32 bit. As such, it is suggested that a minimum of
12 rounds be performed.

%description -l pl
Implementacja algorytmu RC5 w Perlu. RC5 jest szybkim szyfrem blokowym
opracowanym przez Ronalda Rivesta dla RSA Data Security (teraz RSA
Security) w 1994 roku. Jest to sparametryzowany algorytm ze zmiennym
rozmiarem bloku, zmiennym rozmiarem klucza i zmienn± liczb± kroków.
Ta konkretna implementacja jest 32-bitowa. Sugeruje siê wykonywanie
minimum 12 kroków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/RC5.pm
%{_mandir}/man3/*
