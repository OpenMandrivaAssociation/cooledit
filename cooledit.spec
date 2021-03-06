%define major		1
%define libname %mklibname Cw %{major}
%define develname %mklibname -d Cw

Summary:	Full featured multiple window programmer's text editor
Name:		cooledit
Version:	4.0.0
Release:	1
License:	GPLv2+
Group:		Editors
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xt)
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(freetype2)

URL:		ftp://ftp.ibiblio.org/pub/Linux/apps/editors/X/cooledit/
Source0:	ftp://ftp.ibiblio.org/pub/Linux/apps/editors/X/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}_48x48.xpm
Patch1:		cooledit-3.17.17-mdv-fix-str-fmt.patch
Patch2:		cooledit-4.0.0-linking.patch
Patch3:		cooledit-4.0.0-python3.patch

%description 
Full-featured X Window text editor; multiple edit windows; 3D Motif-ish
look and feel; shift-arrow and mouse text highlighting; column text
highlighting and manipulation; color syntax highlighting for various
sources; buildin Python interpretor for macro program.; interactive
graphical debugger - interface to gdb; key for key undo; macro
recording; regular expression search and replace; pull-down menus; drag
and drop; interactive man page browser; run make and other shell
commands with seamless shell interface; redefine keys with an easy
interactive key learner; full support for proportional fonts;

%package -n %{libname}
Group:		Editors
Summary:	Shared library files for cooledit

%description -n %{libname}
Shared library files for cooledit.

%package -n %{develname}
Group:		Development/C
Summary:	Development files for cooledit
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Files for development from the cooledit package.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fi
%configure --program-prefix='' --disable-static
%make_build

%install
%make_install

# Mandriva menu entries

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=CoolEdit
Comment=Programmer's text editor with Python and shell scripting hooks
Exec=%{_bindir}/%{name}
Icon=editors_section
Terminal=false
Type=Application
StartupNotify=true
Categories=TextEditor;Utility;
EOF

%files
%doc AUTHORS NEWS README TODO VERSION
%doc cooledit_16x16.xpm cooledit_32x32.xpm rxvt/README.rxvt
%license COPYING
%_bindir/*
%_datadir/cooledit/
%_mandir/man1/*
%{_datadir}/applications/%{name}.desktop

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 3.17.17-7mdv2011.0
+ Revision: 635148
- new devel package policy

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3.17.17-6mdv2011.0
+ Revision: 610160
- rebuild

* Fri Dec 04 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 3.17.17-5mdv2010.1
+ Revision: 473630
- fix str fmt
- fix underlinking
- fix license tag

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.17.17-2mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - s/Mandrake/Mandriva/
    - kill hardcoded icon extension
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
    - kill icon tag


* Fri Jan 05 2007 Stew Benedict <sbenedict@mandriva.com> 3.17.17-2mdv2007.0
+ Revision: 104600
- Import cooledit

* Fri Jan 05 2007 Stew Benedict <sbenedict@mandriva.com> 3.17.17-2mdv2007.1
- rebuild for new python

* Fri Aug 25 2006 Stew Benedict <sbenedict@mandriva.com> 3.17.17-1mdv2007.0
- 3.17.17, xdg menu

* Tue Apr 11 2006 Michael Scherer <misc@mandriva.org> 3.17.14-4mdk
- remove pythonlib wrong requires

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.17.14-3mdk
- Rebuild

* Fri Aug 12 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.17.14-2mdk
- fix rpmlint errors (PreReq) 
- fix build with gcc4 ( P1 )

* Tue May 03 2005 Stew Benedict <sbenedict@mandriva.com> 3.17.14-1mdk
- 3.17.14, update URL, drop coolicon stuff

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 3.17.7-8mdk
- Rebuild for new  python

* Mon Sep 06 2004 Stew Benedict <sbenedict@mandrakesoft.com> 3.17.7-7mdk
- rebuild

