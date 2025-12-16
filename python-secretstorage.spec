%global pkg_name secretstorage

Name:           python-%{pkg_name}
Version:        3.5.0
Release:        1
Summary:        Python bindings to FreeDesktop.org Secret Service API
Group:          Development/Python
License:        BSD 3-Clause License
URL:            https://pypi.org/project/SecretStorage
Source0:        https://files.pythonhosted.org/packages/source/s/secretstorage/secretstorage-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	dbus-x11
BuildRequires:	x11-server-xvfb
BuildSystem:	python
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(cryptography)
BuildRequires:	python%{pyver}dist(dbus-python)
BuildRequires:	python%{pyver}dist(pygobject)
BuildRequires:  python%{pyver}dist(jeepney)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(sphinx)

Requires:       python%{pyver}dist(cryptography)
Requires:       python%{pyver}dist(jeepney)

%description
This module provides a way for securely storing passwords and other secrets.
It uses D-Bus Secret Service API that is supported by GNOME Keyring.

%build -a
# generate html docs
PYTHONPATH=${PWD} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%files
%doc html
%{python_sitelib}/secretstorage
%{python_sitelib}/secretstorage-%{version}.dist-info
