Name: assistant
Version: 2024.10.4
Release: 3%{?dist}
Summary: Assistant container with Fedora IoT

License: EUPL-1.2
URL: https://github.com/jskov/kb

Source0: %{name}-%{version}.tar.gz

Requires(pre):    /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_systemd
BuildRequires: systemd-rpm-macros

%description
 
Necessary configuration for running Assistant in a Systemd container on Fedora IoT.

%global debug_package %{nil}

%prep
%setup -q

%build

%install

rm -f %{buildroot}/etc/containers/systemd/users/3000/assistant.container
rm -f %{buildroot}/usr/lib/systemd/system/assistant-prep.service

install -Dp -m644 assistant-prep.service %{buildroot}/usr/lib/systemd/system/assistant-prep.service
install -Dp -m644 assistant.container %{buildroot}/etc/containers/systemd/users/3000/assistant.container

%pre

%post
%systemd_post assistant-prep

%preun
%systemd_preun assistant-prep

%postun
%systemd_postun_with_restart assistant-prep

%files

/usr/lib/systemd/system/assistant-prep.service
/etc/containers/systemd/users/3000/assistant.container


%changelog
* Sat Jan 04 2025 Jesper Skov <jskov@mada.dk> 2024.10.4-2
- one source file (jskov@mada.dk)
- lint/tag gelp (jskov@mada.dk)

* Sat Jan 04 2025 Jesper Skov <jskov@mada.dk>
- lint/tag gelp (jskov@mada.dk)

* Sat Jan 04 2025 Jesper Skov <jskov@mada.dk>
- lint/tag gelp (jskov@mada.dk)

* Sat Jan 04 2025 Jesper Skov <jskov@mada.dk> 2024.10.5-1
- rpmlint cleanup (jskov@mada.dk)

* Sat Jan 04 2025 Jesper Skov <jskov@mada.dk>
- rpmlint cleanup (jskov@mada.dk)

* Sat Jan 04 2025 Jesper Skov <jskov@mada.dk>
- rpmlint cleanup (jskov@mada.dk)

* Sat Jan 04 2025 Jesper Skov <jskov@mada.dk> 2024.10.4-0
- new package built with tito

* Tue Sep 10 2024 Jesper Skov <jskov@mada.dk>
- First release
