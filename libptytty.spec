%define major 0
%define libpackage %mklibname ptytty %{major}
%define devpackage %mklibname -d ptytty

Name: libptytty
Version: 2.0
Release: 2
Summary: OS independent and secure pty/tty and utmp/wtmp/lastlog handling
License: GPLv2+
Group: Terminals
URL: http://software.schmorp.de/
Source0: http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gnupg2
BuildRequires: git

%description
libptytty is a small library that offers pseudo-tty management in an OS-independent way.
It also offers session database support (utmp and optional wtmp/lastlog updates for login shells) 
and supports fork'ing after startup and dropping privileges in the calling process.  
Libptytty is written in C++, but it also offers a C-only API.

%package -n %{libpackage}
Summary:	libptytty is a small library that offers pseudo-tty management in an OS-independent way.
Group:		System/Libraries

%description -n %{libpackage}
libptytty is a small library that offers pseudo-tty management in an OS-independent way.
It also offers session database support (utmp and optional wtmp/lastlog updates for login shells) 
and supports fork'ing after startup and dropping privileges in the calling process.  
Libptytty is written in C++, but it also offers a C-only API.

%package -n %{devpackage}
Summary:	Development files for libptytty
Group:		System/Libraries
Requires:	%{libpackage} = %{EVRD}

%description -n %{devpackage}
Development files for libptytty.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libpackage}
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/*.so.%{major}*

%files -n %{devpackage}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%doc Changes
%doc README
