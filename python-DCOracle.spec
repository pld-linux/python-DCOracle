Summary(pl): Oracle interface for Python language
Name:        python-DCOracle
Version:     1.2.1
Release:     1
Copyright:   Open Source
Group:       Development/Languages/Python
Source:      DCOracle-%{version}-nonbin.tgz 
Patch:       python-DCOracle-libs.patch
BuildRoot:	 /tmp/%{name}-%{version}-root
Requires:    python>=1.5
#Buildprereq: python-devel>=1.5, sed

%description

%description -l pl

						
%prep
%setup -n DCOracle-%{version}-nonbin
%patch -p1

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
cp Setup-8.0.4 Setup
cp Makefile.pre.in-1.5 Makefile.pre.in
make -f Makefile.pre.in boot
make

%install
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/DCOracle
install src/{Buffer,oci_}.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/DCOracle
install -m 644 DCOracle/* $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/DCOracle
echo %{_libdir}/python1.5/site-packages/DCOracle \
  > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/DCOracle.pth
gzip -9nf {DCOracle,LICENSE,README,CHANGES}.txt 


%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc {DCOracle,LICENSE,README,CHANGES}.txt.gz
%{_libdir}/python1.5/site-packages/DCOracle.pth
%{_libdir}/python1.5/site-packages/DCOracle
