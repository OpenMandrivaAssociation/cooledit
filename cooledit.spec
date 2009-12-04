%define lib_major		1
%define lib_name %mklibname Cw %lib_major
%define lib_name_orig libCw

Summary: 	Full featured multiple window programmer's text editor
Name: 		cooledit
Version: 	3.17.17
Release: 	%mkrel 5
License: 	GPLv2+
Group: 		Editors
Requires: 	python %lib_name = %version
BuildRequires:	X11-devel xpm-devel

Source: 	ftp://ftp.ibiblio.org/pub/Linux/apps/editors/X/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}_48x48.xpm

Patch0:         cooledit-gcc4.patch
Patch1:		cooledit-3.17.17-mdv-fix-str-fmt.patch
Patch2:		cooledit-3.17.17-mdv-fix-underlinking.patch

BuildRoot: 	%_tmppath/%name-%version-%release-root
URL: 		ftp://ftp.ibiblio.org/pub/Linux/apps/editors/X/cooledit/

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

%package -n %lib_name
Group:          Editors
Summary:        Shared library files for cooledit

%description -n %lib_name
Shared library files for cooledit.

%package -n %lib_name-devel
Group:          Development/C
Summary:        Development files for cooledit
Requires(pre):  %name = %version-%release, %lib_name = %version-%release
Provides:       %lib_name_orig-devel

%description -n %lib_name-devel
Files for development from the cooledit package.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1 -b .strfmt
%patch2 -p1 -b .undlnk

%build
autoreconf -f -i
%configure --program-prefix=''
%make


%install
rm -fr %buildroot

%makeinstall
%find_lang %{name}

# Mandriva menu entries

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=CoolEdit
Comment=Programmer's text editor with Python and shell scripting hooks
Exec=%{_bindir}/%{name}
Icon=editors_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Editors;TextEditor;
EOF

# (sb) installed but unpackaged files
rm -f $RPM_BUILD_ROOT/usr/share/locale/locale.alias

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%if %mdkversion < 200900
%post -n %lib_name -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %lib_name -p /sbin/ldconfig
%endif

%clean
rm -fr %buildroot

%files -f %{name}.lang
%defattr (-,root,root)
%doc ABOUT-NLS AUTHORS BUGS COPYING FAQ INSTALL INTERNATIONAL HINTS
%doc NEWS README TODO VERSION ChangeLog
%doc cooledit.lsm cooledit.spec
%doc cooledit_16x16.xpm cooledit_32x32.xpm rxvt/README.rxvt
%dir %_datadir/cooledit/
%_datadir/cooledit/*
%_bindir/*
%_mandir/man1/*
%{_datadir}/applications/%{name}.desktop

%files -n %lib_name
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %lib_name-devel
%defattr(-,root,root)
%_libdir/*.a
%_libdir/*.so
%_libdir/*.la


