Summary:	Sqmgrlog generate reports per user/ip/name from SQUID log file.
Summary(pl):	Sqmgrlog generuje raporty z podzia³em na u¿ytkowników/ip/nazwy na podstawie logów SQUIDa
Name:		sqmgrlog
Version:	2.11
Release:	1
Group:          Networking/Utilities
Group(de):      Netzwerkwesen/Werkzeuge
Group(pl):      Sieciowe/Narzêdzia
License:	GPL
Source0:	%{name}-%{version}.tar.gz
#Source1:	-
#Source2:	-
#Patch0:		-
#Patch1:		-
#Patch2:		-
#URL:		-
#BuildPrereq:	-
#Requires:	-
#Prereq:		-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l de

%description -l fr

%description -l pl

%description -l tr

%prep
%setup  -q

%build
%configure --enable-prefix=/usr/sbin --enable-config=/etc/squid/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/{cron.d,squid},/usr/sbin}
install sqmgrlog $RPM_BUILD_ROOT/usr/sbin
install sqmgrlog.conf $RPM_BUILD_ROOT/etc/squid

gzip -9nf CONTRIBUTORS COPYING ChangeLog README

%pre

%preun

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/squid/sqmgrlog.conf
%attr(755,root,root) %{_sbindir}/*
%doc *.gz
