Name:		blue-flame-os-repos
Version:	30
Release:	1%{?dist}
Summary:	Repository files for Blue Flame OS

License:	GPL
URL:		https://github.com/blueflameos/blue-flame-os-repos
Source0:        https://github.com/blueflameos/blue-flame-os-repos/archive/master.zip
BuildArch:	noarch

# For rpmfusions-nonfree repo keys
Requires:	distribution-gpg-keys

# For /etc/yum.repos.d
Requires:	fedora-repos

%description
Repository files for Blue Flame OS.

%prep
%setup -q -n blue-flame-os-repos-master

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
cp "_copr:copr.fedorainfracloud.org:youssefmsourani:BlueFlameOS.repo" $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp "_copr:copr.fedorainfracloud.org:youssefmsourani:sgvrecord.repo" $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp "_copr:copr.fedorainfracloud.org:youssefmsourani:st-trans.repo" $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp "_copr_youssefmsourani-arcontrolcenter.repo" $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp "_copr_youssefmsourani-luniversalinstaller.repo" $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/_copr:copr.fedorainfracloud.org:youssefmsourani:BlueFlameOS.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/_copr:copr.fedorainfracloud.org:youssefmsourani:sgvrecord.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/_copr:copr.fedorainfracloud.org:youssefmsourani:st-trans.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/_copr_youssefmsourani-arcontrolcenter.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/_copr_youssefmsourani-luniversalinstaller.repo

%changelog
* Sun Feb 03 2019 yucuf Sourani <youssef.m.sourani@gmail.com> - 30-1
- Version 30

* Fri Nov 16 2018 yucuf Sourani <youssef.m.sourani@gmail.com> - 29-1
- Initial For BlueFlameOS 29

* Thu Oct 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 29-1
- Make repo files %%config(noreplace) so they aren't clobbered on upgrade if
  they have been modified (such as being enabled).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Kalev Lember <klember@redhat.com> - 28-1
- Add rpmfusion-nonfree-nvidia-driver.repo and rpmfusion-nonfree-steam.repo

* Thu Apr 05 2018 Kalev Lember <klember@redhat.com> - 25-5
- Add URL that points to a Workstation third party software wiki page

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 27 2016 Matthias Clasen <mclasen@redhat.com> - 25-1
- Add the Google Chrome repository

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun  8 2015 Matthias Clasen <mclasen@redhat.com>
- Initial packaging

