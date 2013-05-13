%define         libname         %mklibname %{name}
%define         develname       %mklibname -d %{name}
%define         pythonname      python-%{name}
%define         ocamlname       ocaml-%{name}
%define         javaname        java-%{name}
%define         octavename      octave-%{name}

#OFF because not in mdv
#needs itcl
%define         enable_itcl     OFF
#needs itk
%define         enable_itk      OFF
#needs PDL::Graphics::PLplot
%define         enable_pdl      OFF
#needs D compiler
%define         enable_d        OFF
#needs lasi
%define         enable_psttf    OFF

#to find fonts for freetype
%define         gnu_font_path   "/usr/share/fonts/ttf"

#to compile against TCL 8.6
%define         c_flags         "-DTcl_Import_TCL_DECLARED -DUSE_INTERP_RESULT -lm"

#libs not found during compilation if ON
%define         skip_rpath      OFF

#to cd there such that makeinstall finds the Makefile
%define         build_dir       build

#make install default
%define         lua_version     5.1
%define         libada_dir      %{_libdir}/ada/adalib
%define         includeada_dir  %{_datadir}/ada/adainclude

#fortran includes reside in the gcc directory
%define         gccinstall_dir  %(%__cc --print-search-dirs | %__grep install | %__awk '{print $2}')
%define         includef_dir    %{gccinstall_dir}/finclude

Name:           plplot
Version:        5.9.9
Release:        5
Summary:        A cross-platform software package for creating scientific plots
License:        LGPLv2+
Group:          Development/Other

URL:            http://plplot.sourceforge.net/
Source0:        http://downloads.sourceforge.net/plplot/%{name}-%{version}.tar.gz
Patch0:         plplot-5.9.9-gcc46.patch
Patch1:		plplot-5.9.9.fpic.patch

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  gcc-gfortran
BuildRequires:  gcc-c++
BuildRequires:  gcc-gnat
BuildRequires:  libgnat
BuildRequires:  perl-PDL
BuildRequires:  perl-XML-DOM
BuildRequires:  chrpath

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  qhull-devel
BuildRequires:  ncurses-devel
BuildRequires:  libtool-devel
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  qt4-devel
BuildRequires:  wxgtku-devel

BuildRequires:  freetype-devel
BuildRequires:  tk-devel
BuildRequires:  tcl-devel
BuildRequires:  agg-devel
BuildRequires:  lua-devel
%if %mdkversion >= 201200
BuildRequires:  quadmath-devel
%endif
BuildRequires:  cairo-devel
BuildRequires:  python-devel
BuildRequires:  python-numpy-devel
BuildRequires:  java-devel
BuildRequires:  pkgconfig(libgcj-4.7)
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-doc
#This should be re-enabled as soon as ocaml is rebuilt correctly on mdv
#BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-lablgtk2-devel
BuildRequires:  octave-devel
Requires:       %{libname} = %{version}-%{release}

%description
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C
library, language bindings for that library, and device drivers which
control how the plots are presented in non-interactive and interactive
plotting contexts. The PLplot core library can be used to create
standard x-y plots, semi-log plots, log-log plots, contour plots, 3D
surface plots, mesh plots, bar charts and pie charts. Multiple graphs
(of the same or different sizes) may be placed on a single page, and
multiple pages are allowed for those device formats that support them.

%package -n %{libname}
Summary:        Shared libraries for PLplot
Group:          System/Libraries
Provides:       lib%{name} = %{version}-%{release}

%description -n %{libname}
%{summary}.

%package -n %{develname}
Summary:        Development headers and libraries for PLplot
Group:          Development/Other
Requires:       %{libname} = %{version}-%{release}
Requires:       pkgconfig
Requires:       qhull-devel
Requires:       freetype-devel
Requires:       libtool-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{summary}.

%package -n %{pythonname}
Summary:        PLplot support for Python
Group:          Development/Python
Requires:       %{name} = %{version}-%{release}
Requires:       python
Provides:       %{name}-python = %{version}-%{release}

%description -n %{pythonname}
%{summary}.

#This should be re-enabled as soon as ocaml is rebuilt correctly on mdv
#%package -n %{ocamlname}
#Summary:        PLplot support for OCaml
#Group:          Development/Other
#Requires:       ocaml
#Requires:       %{name} = %{version}-%{release}
#Provides:       %{name}-ocaml = %{version}-%{release}

#%description -n %{ocamlname}
#%{summary}.

%package -n %{javaname}
Summary:        PLplot support for Java
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       java
Provides:       %{name}-java = %{version}-%{release}

%description -n %{javaname}
%{summary}.

%package -n %{octavename}
Summary:        PLplot support for Octave
Group:          Sciences/Mathematics
Requires:       %{name} = %{version}-%{release}
Requires:       octave
Provides:       %{name}-octave = %{version}-%{release}

%description -n %{octavename}
%{summary}.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .fpic

%build
%cmake  -DENABLE_itcl=%{enable_itcl} \
        -DENABLE_itk=%{enable_itk} \
        -DENABLE_pdl=%{enable_pdl} \
        -DENABLE_d=%{enable_d} \
        -DPLD_psttf=%{enable_psttf} \
        -DPL_FREETYPE_FONT_PATH:PATH=%{gnu_font_path} \
        -DCMAKE_C_FLAGS:STRING=%{c_flags} \
        -DCMAKE_SKIP_RPATH=%{skip_rpath} \
        -DF95_MOD_DIR:PATH=%{includef_dir}/%{name} \
        -DF77_INCLUDE_DIR:PATH=%{includef_dir}/%{name} \
        -DOCAML_INSTALL_DIR:PATH=%{_libdir}/ocaml \
        -DJAVAWRAPPER_DIR:PATH=%{_libdir}/%{name}
%make

%install
cd %{build_dir}
%makeinstall_std

rm -rf %{buildroot}/%{_datadir}/%{name}%{version}/examples/tk/tk01
strip %{buildroot}/%{_libexecdir}/octave/site/oct/*/plplot_octave.oct
chrpath -d %{buildroot}/%{_libdir}/*.so.*
chrpath -d %{buildroot}/%{_libdir}/%{name}/plplotjavac_wrap.so
chrpath -d %{buildroot}/%{_libdir}/%{name}%{version}/driversd/*.so
chrpath -d %{buildroot}/%{_libdir}/lua/5.1/plplot/plplotluac.so
chrpath -d %{buildroot}/%{_libexecdir}/octave/site/oct/*/plplot_octave.oct
chrpath -d %{buildroot}/%{python_sitearch}/*.so
chrpath -d %{buildroot}/%{_bindir}/*

%files
%doc README README.* AUTHORS NEWS PROBLEMS FAQ ChangeLog.* ToDo
%doc Copyright COPYING.*
%{_mandir}/man1/*
%{_bindir}/pl*

%files -n %{libname}
%{_libdir}/libcsiro*.so.*
%{_libdir}/libqsastime.so.*
%{_libdir}/libplplot*.so.*
%{_libdir}/libtclmatrixd.so.*
%dir %{_datadir}/%{name}%{version}
%{_datadir}/%{name}%{version}/*.fnt
%{_datadir}/%{name}%{version}/*.map
%{_datadir}/%{name}%{version}/*.pal
%{_datadir}/%{name}%{version}/*.tcl
%{_datadir}/%{name}%{version}/tcl/
%if %mdkversion >= 201100
%dir %{libada_dir}
%{libada_dir}/plplotadad
%endif
%dir %{_libdir}/%{name}%{version}
%{_libdir}/%{name}%{version}/driversd

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{includef_dir}/%{name}
%{includef_dir}/%{name}/*.h
%{includef_dir}/%{name}/*.mod
%{_libdir}/libcsiro*.so
%{_libdir}/libqsastime.so
%{_libdir}/libplplot*.so
%{_libdir}/libtclmatrixd.so
%{_libdir}/lua/%{lua_version}/plplot/plplotluac.so
%{_libdir}/pkgconfig/plplotd*.pc
#%exclude %{_libdir}/pkgconfig/plplotd-ocaml.pc
%if %mdkversion >= 201100
%dir %{includeada_dir}
%{includeada_dir}/plplotadad
%endif
%dir %{_datadir}/%{name}%{version}/examples
%{_datadir}/%{name}%{version}/examples/CMakeLists.txt
%{_datadir}/%{name}%{version}/examples/Makefile
%if %mdkversion >= 201100
%{_datadir}/%{name}%{version}/examples/ada
%{_datadir}/%{name}%{version}/examples/test_ada.sh
%endif
%{_datadir}/%{name}%{version}/examples/c++
%{_datadir}/%{name}%{version}/examples/c
%{_datadir}/%{name}%{version}/examples/cmake
%{_datadir}/%{name}%{version}/examples/f77
%{_datadir}/%{name}%{version}/examples/f95
%{_datadir}/%{name}%{version}/examples/lena.pgm
%{_datadir}/%{name}%{version}/examples/lua
%{_datadir}/%{name}%{version}/examples/plplot-test*
%{_datadir}/%{name}%{version}/examples/tcl
%{_datadir}/%{name}%{version}/examples/test_c.sh
%{_datadir}/%{name}%{version}/examples/test_c_interactive.sh
%{_datadir}/%{name}%{version}/examples/test_cxx.sh
%{_datadir}/%{name}%{version}/examples/test_diff.sh
%{_datadir}/%{name}%{version}/examples/test_f77.sh
%{_datadir}/%{name}%{version}/examples/test_f95.sh
%{_datadir}/%{name}%{version}/examples/test_lua.sh
%{_datadir}/%{name}%{version}/examples/test_tcl.sh
#%exclude %{_datadir}/%{name}%{version}/examples/test_ocaml.sh
%exclude %{_datadir}/%{name}%{version}/examples/test_python.sh
%exclude %{_datadir}/%{name}%{version}/examples/test_java.sh
%{_datadir}/%{name}%{version}/examples/tk

%files -n %{pythonname}
%{python_sitearch}/_plplotcmodule.so
%{python_sitearch}/plplot*
%{python_sitearch}/Plframe.py
%{python_sitearch}/TclSup.py
%{_datadir}/%{name}%{version}/examples/python
%{_datadir}/%{name}%{version}/examples/test_python.sh

#This should be re-enabled as soon as ocaml is rebuilt correctly on mdv
#%files -n %{ocamlname}
#%{_libdir}/ocaml/%{name}
#%{_libdir}/ocaml/stublibs/*
#%{_libdir}/pkgconfig/plplotd-ocaml.pc
#%{_datadir}/%{name}%{version}/examples/ocaml/
#%{_datadir}/%{name}%{version}/examples/test_ocaml.sh


%files -n %{javaname}
%{_libdir}/%{name}/plplotjavac_wrap.so
%{_datadir}/java/plplot.jar
%{_datadir}/%{name}%{version}/examples/java/
%{_datadir}/%{name}%{version}/examples/test_java.sh

%files -n %{octavename}
%{_datadir}/plplot_octave/
%{_datadir}/octave/site/m/PLplot/
%{_libexecdir}/octave/site/oct/*/plplot_octave.oct
%{_datadir}/%{name}%{version}/examples/lena.img
%{_datadir}/%{name}%{version}/examples/octave/
%{_datadir}/%{name}%{version}/examples/test_octave.sh
%{_datadir}/%{name}%{version}/examples/test_octave_interactive.sh


%changelog
* Tue May 29 2012 Frank Kober <emuse@mandriva.org> 5.9.9-3mdv2012.0
+ Revision: 801140
- moved some data files to lib package such that gnudl works without plplot main package
- bump release
- fixed mdkversion macro usage
- ada support unavailable in 2010.1
- try building /wo quadmath when backported

* Fri May 25 2012 Frank Kober <emuse@mandriva.org> 5.9.9-1
+ Revision: 800576
- add missing BR
- imported package plplot

