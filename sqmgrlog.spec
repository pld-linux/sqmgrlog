Summary:	Sqmgrlog generate reports per user/ip/name from SQUID log file
Summary(pl):	Sqmgrlog generuje raporty na podstawie logów SQUIDa
Name:		sqmgrlog
Version:	2.12
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://web.onda.com.br/orso/%{name}-%{version}.tar.gz
URL:		http://web.onda.com.br/orso/
BuildRequires:	perl
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	squid
Requires:	httpd
Requires:	/bin/mail
Requires:	crondaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sqmgrlog generate reports per user/ip/name from SQUID log file. The
reports will be generated in HTML or email.

%description -l pl
Sqmgrlog generuje raporty wed³ug u¿ytkownika/numeru IP/nazwy hosta
korzystaj±c z logów SQUIDa. Raporty mog± generowane w HTML lub
wysy³ane poczt± elektroniczn±.

%prep
%setup  -q
perl -pi -e "s;/usr/local/squid/logs/access.log;/var/log/squid/access.log;" *.c
perl -pi -e "s;/usr/local/etc/httpd/htdocs/squid-reports;/home/httpd/html/squid-reports;" *.c

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-prefix=%{_prefix} \
	--enable-config=%{_sysconfdir}/squid/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{cron.d,squid},%{_sbindir},/home/httpd/html/squid-reports}
install sqmgrlog $RPM_BUILD_ROOT%{_sbindir}
install sqmgrlog.conf $RPM_BUILD_ROOT%{_sysconfdir}/squid


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/squid/sqmgrlog.conf
%attr(755,root,root) %{_sbindir}/*
%doc CONTRIBUTORS COPYING ChangeLog README
%dir /home/httpd/html/squid-reports
