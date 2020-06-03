#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IPC-Run
Version  : 20200505.0
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/IPC-Run-20200505.0.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/IPC-Run-20200505.0.tar.gz
Summary  : 'system() and background procs w/ piping, redirs, ptys (Unix, Win32)'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-IPC-Run-license = %{version}-%{release}
Requires: perl-IPC-Run-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
![linux](https://github.com/toddr/IPC-Run/workflows/linux/badge.svg) ![windows](https://github.com/toddr/IPC-Run/workflows/windows/badge.svg) ![macos](https://github.com/toddr/IPC-Run/workflows/macos/badge.svg)

%package dev
Summary: dev components for the perl-IPC-Run package.
Group: Development
Provides: perl-IPC-Run-devel = %{version}-%{release}
Requires: perl-IPC-Run = %{version}-%{release}

%description dev
dev components for the perl-IPC-Run package.


%package license
Summary: license components for the perl-IPC-Run package.
Group: Default

%description license
license components for the perl-IPC-Run package.


%package perl
Summary: perl components for the perl-IPC-Run package.
Group: Default
Requires: perl-IPC-Run = %{version}-%{release}

%description perl
perl components for the perl-IPC-Run package.


%prep
%setup -q -n IPC-Run-20200505.0
cd %{_builddir}/IPC-Run-20200505.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IPC-Run
cp %{_builddir}/IPC-Run-20200505.0/LICENSE %{buildroot}/usr/share/package-licenses/perl-IPC-Run/10b18134d80c6f0904ad1c836170dedb386d3533
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IPC::Run.3
/usr/share/man/man3/IPC::Run::Debug.3
/usr/share/man/man3/IPC::Run::IO.3
/usr/share/man/man3/IPC::Run::Timer.3
/usr/share/man/man3/IPC::Run::Win32Helper.3
/usr/share/man/man3/IPC::Run::Win32IO.3
/usr/share/man/man3/IPC::Run::Win32Pump.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IPC-Run/10b18134d80c6f0904ad1c836170dedb386d3533

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/IPC/Run.pm
/usr/lib/perl5/vendor_perl/5.30.3/IPC/Run/Debug.pm
/usr/lib/perl5/vendor_perl/5.30.3/IPC/Run/IO.pm
/usr/lib/perl5/vendor_perl/5.30.3/IPC/Run/Timer.pm
/usr/lib/perl5/vendor_perl/5.30.3/IPC/Run/Win32Helper.pm
/usr/lib/perl5/vendor_perl/5.30.3/IPC/Run/Win32IO.pm
/usr/lib/perl5/vendor_perl/5.30.3/IPC/Run/Win32Pump.pm
