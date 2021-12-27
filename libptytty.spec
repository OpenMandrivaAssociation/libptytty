Name: libptytty
Version: 2.0
Release: 1
Summary: OS independent and secure pty/tty and utmp/wtmp/lastlog handling
License: GPLv2+
Group: Terminals
URL: http://software.schmorp.de/
Source0: http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gnupg2
BuildRequires: git
BuildRequires: ninja

%description
libptytty is a small library that offers pseudo-tty management in an OS-independent way.
It also offers session database support (utmp and optional wtmp/lastlog updates for login shells) 
and supports fork'ing after startup and dropping privileges in the calling process.  
Libptytty is written in C++, but it also offers a C-only API.

%package devel
Summary: Development headers for libptytty
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development packages for libptytty.

%prep
%autosetup -p1

%build
%cmake -G Ninja
%ninja -C build

%install
%ninja_install -C build

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
