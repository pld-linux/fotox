#
Summary:	Image processor
Name:		fotox
Version:	42
Release:	1
License:	GPLv2
Group:		Applications
Source0:	http://kornelix.squarespace.com/storage/fotox/%{name}.%{version}.tar.gz
# Source0-md5:	e527b692b236605fd60fe7a318cb26be
URL:		http://kornelix.squarespace.com/fotox/
BuildRequires:	bash
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fotox is a free open-source Linux program for improving image files made
with a digital camera.

%prep
%setup -q -n %{name}

%build
PREFIX=%{_prefix} bash ./build build

%install
rm -rf $RPM_BUILD_ROOT
PREFIX=$RPM_BUILD_ROOT%{_prefix} bash ./build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog fotox-guide.pdf schnellstart.pdf
%{_bindir}/fotox
%{_datadir}/fotox
