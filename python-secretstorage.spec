%global pkg_name secretstorage

Name:           python-%{pkg_name}
Version:        3.5.0
Release:        3
Summary:        Python bindings to FreeDesktop.org Secret Service API
Group:          Development/Python
License:        BSD 3-Clause License
URL:            https://pypi.org/project/SecretStorage
Source0:        https://files.pythonhosted.org/packages/source/s/secretstorage/secretstorage-%{version}.tar.gz
BuildArch:      noarch

%bcond docs 0

%if %{with docs}
BuildRequires:	dbus-x11
BuildRequires:	x11-server-xvfb
BuildRequires:	python%{pyver}dist(dbus-python)
BuildRequires:	python%{pyver}dist(pygobject)
BuildRequires:	python%{pyver}dist(sphinx)
%endif
BuildSystem:	python
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(cryptography)
BuildRequires:  python%{pyver}dist(jeepney)
BuildRequires:  python%{pyver}dist(setuptools)

Requires:       python%{pyver}dist(cryptography)
Requires:       python%{pyver}dist(jeepney)

%description
This module provides a way for securely storing passwords and other secrets.
It uses D-Bus Secret Service API that is supported by GNOME Keyring.

%if %{with docs}
%build -a
# generate html docs
PYTHONPATH=${PWD} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%files
%if %{with docs}
%doc html
%endif
%{python_sitelib}/secretstorage
%{python_sitelib}/secretstorage-%{version}.dist-info
