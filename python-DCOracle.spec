%define	pp_subname	DCOracle
Summary:	Oracle interface for Python language
Summary(pl.UTF-8):	Interfejs do bazy danych Oracle'a dla języka Python
Name:		python-%{pp_subname}
Version:	1.3.0
Release:	1
License:	Open Source
Group:		Development/Languages/Python
Source0:	DCOracle-%{version}-nonbin.tgz
#Source0:	http://www.zope.org/Products/DCOracle/DCOracle-%{version}.tgz
Patch0:		python-DCOracle-libs.patch
URL:		http://www.zope.org/Products/DCOracle/
#BuildRequires:	python-devel >= 1.5, sed
Requires:	python >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains module that allows connect to Oracle database in
Python programs.

%description -l pl.UTF-8
Pakiet ten zawiera moduł dla języka Python umożliwiający połączenie
się z bazą danych Oracle'a.

%prep
%setup -q -n DCOracle
%patch0 -p1

%build
cd DCOracle
python - <<END
import py_compile

py_compile.compile("__init__.py")
py_compile.compile("dbi.py")
py_compile.compile("ociBind.py")
py_compile.compile("ociCurs.py")
py_compile.compile("ociProc.py")
py_compile.compile("ociUtil.py")
py_compile.compile("ocidb.py")
py_compile.compile("ocitypes.py")

END

cd ../src
cp -f Setup-8.0.4 Setup
cp -f Makefile.pre.in-1.5 Makefile.pre.in
%{__make} -f Makefile.pre.in boot
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}

install src/{Buffer,oci_}.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
install %{pp_subname}/* $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
echo %{pp_subname} > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}.pth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {DCOracle,LICENSE,README,CHANGES}.txt
%{_libdir}/python1.5/site-packages/%{pp_subname}.pth
%{_libdir}/python1.5/site-packages/%{pp_subname}
