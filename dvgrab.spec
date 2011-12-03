Summary:        Utility to capture video from a DV camera
Name:           dvgrab
Version:        3.4
Release:        3.1%{?dist}
License:        GPLv2+
Group:          Applications/Multimedia
URL:            http://www.kinodv.org/
Source:         http://dl.sf.net/kino/dvgrab-%{version}.tar.gz
Patch0:         dvgrab-3.3-fix-gcc-4.4-build.patch
Patch1:         dvgrab-3.4-set-proper-retval-on-failure.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libraw1394-devel libavc1394-devel libdv-devel
BuildRequires:  libiec61883-devel libjpeg-devel
ExcludeArch:    s390 s390x

%description
The dvgrab utility will capture digital video from a DV source on the firewire
(IEEE-1394) bus.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README COPYING ChangeLog NEWS
%{_bindir}/dvgrab
%{_mandir}/man1/dvgrab.1*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.4-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 19 2009 Jarod Wilson <jarod@redhat.com> - 3.4-2
- Set retval to 1 if we get an error, to make life easier for folks
  who wrap dvgrab to tell if something went wrong (#486061).

* Tue Feb 24 2009 Jarod Wilson <jarod@redhat.com> - 3.4-1
- New upstream release, v3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Jarod Wilson <jarod@redhat.com> - 3.3-1
- New upstream release, v3.3
- Fix build w/gcc 4.4

* Tue Aug 05 2008 Jarod Wilson <jwilson@redhat.com> - 3.2-1
- New upstream release

* Wed Jul 23 2008 Jarod Wilson <jwilson@redhat.com> - 3.1-5
- Bump and rebuild for libraw1394 v2.0.0

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.1-4
- fix license tag

* Tue Jun 24 2008 Jarod Wilson <jwilson@redhat.com> - 3.1-3
- Fix segfault when we get bogus timecodes (#370931)

* Wed Feb 13 2008 Jarod Wilson <jwilson@redhat.com> - 3.1-2
- Fix build with gcc 4.3

* Wed Dec 12 2007 Jarod Wilson <jwilson@redhat.com> - 3.1-1
- New upstream release
- Drop libpng, libogg and libvorbis BRs, since dvgrab has
  long since dropped support for them (circa v2.1)

* Mon Oct 22 2007 Jarod Wilson <jwilson@redhat.com> - 3.0-2
- Fix segfault on cleanup (#331271)
- fix pipe output in conjunction with file capture
- fix hang at end of reading from stdin
- fix potential data loss due to short writes

* Sun Oct 07 2007 Jarod Wilson <jwilson@redhat.com> - 3.0-1
- New upstream release

* Sun Feb 04 2007 Jarod Wilson <jwilson@redhat.com> - 2.1-3
- Minor clean-ups for core/extras merge review (#225713)

* Tue Jan 23 2007 Jarod Wilson <jwilson@redhat.com> - 2.1-2
- It helps to set DESTDIR if you nuke makeinstall...

* Tue Jan 23 2007 Jarod Wilson <jwilson@redhat.com> - 2.1-1
- New upstream release

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.0-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.0-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 Matthias Saou <http://freshrpms.net/> 2.0-1
- Update to 2.0.

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 28 2005 Warren Togami <wtogami@redhat.com> 1.7-2
- gcc4 rebuild

* Sun Feb 06 2005 Warren Togami <wtogami@redhat.com> 1.7-1
- 1.7

* Sun Sep 19 2004 Warren Togami <wtogami@redhat.com> 1.6-1
- upgrade to 1.6

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 05 2004 Warren Togami <wtogami@redhat.com> 1.5-2
- rebuild against new libdv

* Thu Feb 12 2004 Warren Togami <wtogami@redhat.com> 1.5-1
- upgrade to 1.5
- spec cleanups
- remove INSTALL, TODO; Add NEWS
- Now requires libdv, docs say it is much faster and better output than raw1394
- BuildRequires libraw1394-devel, libavc1394-devel, libdv-devel, libjpeg-devel,
  libpng-devel, libogg-devel, libvorbis-devel

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 1.01-9
- fix build on gcc 3.3 (include <assert.h>)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 1.01-7
- rebuild on all arches

* Wed Nov 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- exclude on mainframe

* Sat Aug 10 2002 Elliot Lee <sopwith@redhat.com>
- rebuilt with gcc-3.2 (we hope)

* Tue Jul 23 2002 Tim Powers <timp@redhat.com>
- build using gcc-3.2-0.1

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 09 2002 Michael Fulbright <msf@redhat.com>
- First RPM build

