Name: libptytty
Version: 2.0
Release: 1%{?dist}
Summary: OS independent and secure pty/tty and utmp/wtmp/lastlog handling
License: GPLv2+
URL: http://software.schmorp.de/
Source0: http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz
Source1: http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz.sig
Source2: http://dist.schmorp.de/signing-key.pub
Source3: http://dist.schmorp.de/signing-key.pub.gpg.sig
Source4: gpgkey-84874CAB6D1A397A.gpg
# To recreate Source4:
#     gpg --recv-key 84874CAB6D1A397A
#     gpg --export --export-options export-minimal 84874CAB6D1A397A \
#         > gpgkey-84874CAB6D1A397A.gpg

BuildRequires: cmake
BuildRequires: gcc-g++
BuildRequires: gnupg2
BuildRequires: git
BuildRequires: ninja-build
BuildRequires: signify

%global desc \
libptytty is a small library that offers pseudo-tty management in an \
OS-independent way.  It also offers session database support (utmp and \
optional wtmp/lastlog updates for login shells) and supports fork'ing after \
startup and dropping privileges in the calling process.  Libptytty is \
written in C++, but it also offers a C-only API. \
%{nil}
%description %{desc}

%package devel
Summary: Development headers for libptytty
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%desc

%prep
%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE2}'
signify -V -p '%{SOURCE2}' -m '%{SOURCE0}'
%autosetup -S git

%build
%cmake -G Ninja
%cmake_build

%install
%cmake_install

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%doc Changes
%doc README

%changelog
* Mon Nov 22 2021 Robbie Harwood <rharwood@redhat.com> - 2.0-1
- Initial import (2.0)
