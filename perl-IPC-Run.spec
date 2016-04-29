#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IPC-Run
Version  : 0.94
Release  : 6
URL      : http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/IPC-Run-0.94.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/IPC-Run-0.94.tar.gz
Summary  : 'system() and background procs w/ piping, redirs, ptys (Unix, Win32)'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-IPC-Run-doc

%description
NAME
IPC::Run - system() and background procs w/ piping, redirs, ptys (Unix,
Win32)

%package doc
Summary: doc components for the perl-IPC-Run package.
Group: Documentation

%description doc
doc components for the perl-IPC-Run package.


%prep
%setup -q -n IPC-Run-0.94

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/IPC/Run.pm
/usr/lib/perl5/site_perl/5.22.0/IPC/Run/Debug.pm
/usr/lib/perl5/site_perl/5.22.0/IPC/Run/IO.pm
/usr/lib/perl5/site_perl/5.22.0/IPC/Run/Timer.pm
/usr/lib/perl5/site_perl/5.22.0/IPC/Run/Win32Helper.pm
/usr/lib/perl5/site_perl/5.22.0/IPC/Run/Win32IO.pm
/usr/lib/perl5/site_perl/5.22.0/IPC/Run/Win32Pump.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
