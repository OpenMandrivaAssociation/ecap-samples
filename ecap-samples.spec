Summary:	Simple ecap samples
Name:		ecap-samples
Version:	0.0.3
Release:	%mkrel 1
License:	BSD
Group:		Networking/Other
URL:		https://www.ecap.org
Source0:	http://www.measurement-factory.com/tmp/ecap/ecap_adapter_sample-%{version}.tar.gz
BuildRequires:	ecap-devel
BuildRequires:	ecap
Buildroot:	%{_tmppath}/%{rname}-%{version}-%{release}-buildroot

%description
The sample contains three basic adapters. Please see the README file in the tarball for 
information about each adapter. The change log for the sample is also available.

%prep

%setup -n ecap_adapter_sample-%{version}

%configure2_5x 
%make

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/ecap_adapter_*

