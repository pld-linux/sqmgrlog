Summary:	Sqmgrlog generate reports per user/ip/name from SQUID log file
Summary(pl):	Sqmgrlog generuje raporty na podstawie logów SQUIDa
Name:		sqmgrlog
Version:	2.12
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://web.onda.com.br/orso/%{name}-%{version}.tar.gz
# Source0-md5:	5ea6cce40796fca8c1dd8bf03b9b3e13
URL:		http://web.onda.com.br/orso/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl
Requires:	/bin/mail
Requires:	crondaemon
Requires:	webserver
Requires:	squid
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
perl -pi -e "s;/usr/local/etc/httpd/htdocs/squid-reports;/home/services/httpd/html/squid-reports;" *.c

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-prefix=%{_prefix} \
	--enable-config=%{_sysconfdir}/squid/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{cron.d,squid},%{_sbindir},/home/services/httpd/html/squid-reports}
install sqmgrlog $RPM_BUILD_ROOT%{_sbindir}
install sqmgrlog.conf $RPM_BUILD_ROOT%{_sysconfdir}/squid


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS ChangeLog README
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/squid/sqmgrlog.conf
%attr(755,root,root) %{_sbindir}/*
%dir /home/services/httpd/html/squid-reports
