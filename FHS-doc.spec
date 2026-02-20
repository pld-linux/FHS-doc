Summary:	FHS (File Hierarchy Standard) %{version} documentation
Summary(pl.UTF-8):	Dokumentacja standardu FHS (File Hierarchy Standard) %{version}
Name:		FHS-doc
Version:	3.0
Release:	3
License:	distributable
Group:		Documentation
Source0:	http://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html
# Source0-md5:	04536bf6340257d1615303e70d54199b
Source1:	http://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf
# Source1-md5:	0718d1e5043ce12dffb54654e795e526
URL:		http://refspecs.linuxfoundation.org/fhs.shtml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
FHS (File Hierarchy Standard) %{version} documentation.

%description -l pl.UTF-8
Dokumentacja standardu hierarchii plików FHS (File Hierarchy Standard)
w wersji %{version}.

%package html
Summary:	FHS %{version} documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja standardu FHS %{version} w formacie HTML
Group:		Documentation

%description html
FHS (File Hierarchy Standard) %{version} documentation in HTML format.

%description html -l pl.UTF-8
Dokumentacja standardu hierarchii plików FHS (File Hierarchy Standard)
w wersji %{version} w formacie HTML.

%package pdf
Summary:	FHS %{version} documentation in PDF format
Summary(pl.UTF-8):	Dokumentacja standardu FHS %{version} w formacie PDF
Group:		Documentation

%description pdf
FHS (File Hierarchy Standard) %{version} documentation in PDF format.

%description pdf -l pl.UTF-8
Dokumentacja standardu hierarchii plików FHS (File Hierarchy Standard)
w wersji %{version} w formacie PDF.

%prep
%setup -qcT
cp -p %{SOURCE0} %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files html
%defattr(644,root,root,755)
%doc fhs-3.0.html

%files pdf
%defattr(644,root,root,755)
%doc fhs-3.0.pdf
