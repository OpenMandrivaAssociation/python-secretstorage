# Created by pyp2rpm-3.3.2
%global pypi_name SecretStorage
%global pkg_name secretstorage

Name:           python-%{pkg_name}
Version:        3.3.1
Release:        %mkrel 1
Summary:        Python bindings to FreeDesktop.org Secret Service API
Group:          Development/Python
License:        BSD 3-Clause License
URL:            https://pypi.org/project/SecretStorage
Source0:        %{pypi_source}
Source1:		http://download.gnome.org/sources/libsecret/0.18/libsecret-0.18.6.tar.xz
BuildArch:      noarch
BuildRequires:	dbus-x11
BuildRequires:	x11-server-xvfb
BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)
BuildRequires:	python3dist(dbus-python)
BuildRequires:	python3dist(pygobject)
BuildRequires:  python3dist(jeepney)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
This module provides a way for securely storing passwords and other secrets.
It uses D-Bus Secret Service API that is supported by GNOME Keyring.

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cryptography)
Requires:       python3dist(jeepney)

%description -n python3-%{pkg_name}
This module provides a way for securely storing passwords and other secrets.
It uses D-Bus Secret Service API that is supported by GNOME Keyring.

%prep
%autosetup -n SecretStorage-%{version}
tar xf %{SOURCE1}

# Remove bundled egg-info
rm -rf *.egg-info

%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
for MOCK in libsecret-0.18.6/libsecret/mock-service-{normal,only-plain,lock}.py; do
  xvfb-run -a dbus-launch --exit-with-session %{__python3} tests/run_tests.py ${MOCK}
done
	
%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst html
%{python3_sitelib}/secretstorage
%{python3_sitelib}/SecretStorage-%{version}-py?.?.egg-info
