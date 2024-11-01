Name: assistant
Version: 2024.10.4
Release: 0%{?dist}
Summary: Assistant container with Fedora IoT

License: EUPL-1.2
URL: https://github.com/jskov/kb

Source0: assistant-prep.service
Source1: assistant.dockerfile

Requires(pre):    /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_systemd
BuildRequires: systemd-rpm-macros

%description
 
Necessary configuration for running Assistant f in a Systemd container on Fedora IoT.

# No prep/setup, using files directly from the source folder
#%prep
#%setup -q
#%build

%install

rm -f %{buildroot}/etc/containers/systemd/users/3000/assistant.container
rm -f %{buildroot}/usr/lib/systemd/system/assistant-prep.service

install -Dp -m644 %{SOURCE0} %{buildroot}/usr/lib/systemd/system/assistant-prep.service
install -Dp -m644 %{SOURCE1} %{buildroot}/etc/containers/systemd/users/3000/assistant.container

%pre

%post
%systemd_post assistant-prep

%preun
%systemd_preun assistant-prep

%postun
%systemd_postun_with_restart assistant-prep

%clean

rm -rf $RPM_BUILD_ROOT
 
%files

/usr/lib/systemd/system/assistant-prep.service
/etc/containers/systemd/users/3000/assistant.container


%changelog
 
* Tue Sep 10 2024 Jesper Skov <jskov@mada.dk>
- First release
