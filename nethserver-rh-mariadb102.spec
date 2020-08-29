Summary: NethServer mariadb102 configuration and templates.
Name: nethserver-rh-mariadb102
Version: 0.0.6
Release: 1%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: rh-mariadb102
Requires: nethserver-base
Requires: nethserver-lib >= 1.0.1
Requires: procps-ng
BuildRequires: nethserver-devtools
AutoReq: no


%description
This package adds necessary startup and configuration items for
mysql.

%prep
%setup

%build
%{__mkdir} -p root/etc/e-smith/sql/init102
%{__mkdir} -p root/var/lib/rh-mariadb102
%{__mkdir} -p root/var/log/rh-mariadb102

perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} \
    --dir   /var/log/rh-mariadb102 'attr(0755,mysql,mysql)' \
    --dir   /var/lib/rh-mariadb102 'attr(0755,mysql,mysql)' \
    --file  /usr/bin/mysql102 'attr(0755,root,root)' \
    --file  /usr/bin/mysqladmin102 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlbinlog102 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlcheck102 'attr(0755,root,root)' \
    --file  /usr/bin/mysql_config_editor102 'attr(0755,root,root)' \
    --file  /usr/bin/mysqld_multi102 'attr(0755,root,root)' \
    --file  /usr/bin/mysqldump102 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlimport102 'attr(0755,root,root)' \
    --file  /usr/bin/mysql_plugin102 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlshow102 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlslap102 'attr(0755,root,root)' \
$RPM_BUILD_ROOT \
    > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT


%preun

%post
/usr/bin/systemctl enable rh-mariadb102-mariadb

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%changelog
* Sat Aug 29 2020 stephane de labrusse <stephdl@de-labrusse.fr> 0.0.6
- Expand phpmyadmin-save if installed

* Sun Jul 8 2018 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.5
- Release for rh-mariadb102
- Avoid conflicting file between mariadb101 and mariadb102

* Sun Oct 1  2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4
- Stop mysqld_safe with 'mysqladmin102 shutdown'
- Restore the root password with post-restore-config

* Sat Sep 30 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3
- Added phpMyAdmin configuration template

* Sun May 22 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2
- backup and restore function added

* Tue May 10 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- First release
