%global _empty_manifest_terminate_build 0
Name:		python-lightgbm
Version:	3.2.1
Release:	2
Summary:	LightGBM Python Package
License:	The MIT License
URL:		https://github.com/microsoft/LightGBM
Source0:	https://files.pythonhosted.org/packages/7a/6d/db0f5effd3f7982632111f37fcd2fa386b8407f1ff58ef30b71d65e1a444/lightgbm-3.2.1.tar.gz

BuildRequires:	python3-wheel
Requires:	python3-wheel
Requires:	python3-numpy
Requires:	python3-scipy
Requires:	python3-scikit-learn
Requires:	python3-dask[array]
Requires:	python3-dask[dataframe]
Requires:	python3-dask[distributed]
Requires:	python3-pandas

%description
LightGBM is a fast, distributed, high performance gradient boosting framework that uses tree based learning algorithms. 

%package -n python3-lightgbm
Summary:	LightGBM Python Package
Provides:	python-lightgbm
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-cffi
BuildRequires:	gcc
BuildRequires:	gdb
%description -n python3-lightgbm
LightGBM is a fast, distributed, high performance gradient boosting framework that uses tree based learning algorithms. 

%package help
Summary:	Development documents and examples for lightgbm
Provides:	python3-lightgbm-doc
%description help
LightGBM is a fast, distributed, high performance gradient boosting framework that uses tree based learning algorithms. 

%prep
%autosetup -n lightgbm-3.2.1

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-lightgbm -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed May 18 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 3.2.1-2
- add necessary BuildRequires

* Thu May 27 2021 Python_Bot <Python_Bot@openeuler.org> - 3.2.1-1
- Package Spec generated
