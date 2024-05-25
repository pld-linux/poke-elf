Summary:	GNU poke support for editing ELF files
Summary(pl.UTF-8):	Obsługa edycji plików ELF dla GNU poke
Name:		poke-elf
Version:	1.0
Release:	1
License:	GPL v3+
Group:		Applications/Editors
Source0:	https://ftp.gnu.org/gnu/poke/%{name}-%{version}.tar.gz
# Source0-md5:	74dead66563d781c035a491b3d2e40f2
Patch0:		%{name}-info.patch
URL:		http://www.jemarch.net/poke
BuildRequires:	automake
BuildRequires:	poke >= 4.0
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
Requires:	poke >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
poke-elf is a full-fledged GNU poke pickle for editing ELF object
files, executables, shared libraries and core dumps.  It supports many
architectures and extensions.

%description -l pl.UTF-8
poke-elf to w pełni przygotowany zbiór reguł GNU poke do edycji plików
ELF, w tym obiektów, plików wykonywalnych, bibliotek współdzielonych i
zrzutów pamięci. Obsługuje wiele architektur i rozszerzeń.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env sh,/bin/sh,' examples/prelinkr

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/prelinkr
%{_datadir}/poke/pickles/elf*.pk
%{_infodir}/poke-elf.info*
