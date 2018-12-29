#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : PyNaCl
Version  : 1.3.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/61/ab/2ac6dea8489fa713e2b4c6c5b549cc962dd4a842b5998d9e80cf8440b7cd/PyNaCl-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/61/ab/2ac6dea8489fa713e2b4c6c5b549cc962dd4a842b5998d9e80cf8440b7cd/PyNaCl-1.3.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/61/ab/2ac6dea8489fa713e2b4c6c5b549cc962dd4a842b5998d9e80cf8440b7cd/PyNaCl-1.3.0.tar.gz.asc
Summary  : Python binding to the Networking and Cryptography (NaCl) library
Group    : Development/Tools
License  : Apache-2.0 ISC
Requires: PyNaCl-license = %{version}-%{release}
Requires: PyNaCl-python = %{version}-%{release}
Requires: PyNaCl-python3 = %{version}-%{release}
Requires: cffi
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================================
PyNaCl: Python binding to the libsodium library
===============================================

%package license
Summary: license components for the PyNaCl package.
Group: Default

%description license
license components for the PyNaCl package.


%package python
Summary: python components for the PyNaCl package.
Group: Default
Requires: PyNaCl-python3 = %{version}-%{release}
Provides: pynacl-python

%description python
python components for the PyNaCl package.


%package python3
Summary: python3 components for the PyNaCl package.
Group: Default
Requires: python3-core

%description python3
python3 components for the PyNaCl package.


%prep
%setup -q -n PyNaCl-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545416886
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PyNaCl
cp LICENSE %{buildroot}/usr/share/package-licenses/PyNaCl/LICENSE
cp src/libsodium/LICENSE %{buildroot}/usr/share/package-licenses/PyNaCl/src_libsodium_LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyNaCl/LICENSE
/usr/share/package-licenses/PyNaCl/src_libsodium_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
