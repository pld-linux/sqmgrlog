Summary:	Sqmgrlog generate reports per user/ip/name from SQUID log file.
Summary(pl):	Sqmgrlog generuje raporty z podzia³em na u¿ytkowników/ip/nazwy na podstawie logów SQUIDa
Name:		sqmgrlog
Version:	2.12
Release:	2
Group:          Networking/Utilities
Group(de):      Netzwerkwesen/Werkzeuge
Group(pl):      Sieciowe/Narzêdzia
License:	GPL
URL:            http://web.onda.com.br/orso/
Source0:        http://web.onda.com.br/orso/%{name}-%{version}.tar.gz
Requires:	squid
Requires:	httpd
Requires:	/bin/mail
Requires:	crondaemon
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sqmgrlog generate reports per user/ip/name from SQUID log file. The
reports will be generated in HTML or email.

%description -l de

%description -l fr

%description -l pl
Sqmgrlog generuje raporty wed³ug u¿ytkownika/numeru IP/nazwy hosta
korzystaj±c z logów SQUID'a. Raporty mog± generowane w HTML lub
wysy³ane poczta e-mail.

%prep
%setup  -q
perl -pi -e "s;/usr/local/squid/logs/access.log;/var/log/squid/access.log;" *.c
perl -pi -e "s;/usr/local/etc/httpd/htdocs/squid-reports;/home/httpd/html/squid-reports;" *.c

%build
%configure --enable-prefix=%{_prefix} --enable-config=%{_sysconfdir}/squid/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/{cron.d,squid},/usr/sbin,/home/httpd/html/squid-reports}
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
%dir /home/httpd/html/squid-reports
