%define __noautoreq '\/usr\/share\/plplot5.10.0\/examples\/tk\/xtk01'
#define	svnversion	0.0.0
#define	svnsnapshot	svn
#define	baseversion	#{svnversion}
#define	srcversion	#{version}#{svnsnapshot}

%define baseversion %{version}
%define srcversion %{version}

%define majorcsiro 0
%define libcsiro %mklibname csiro %{majorcsiro}

%define majorqsastime 0
%define libqsastime %mklibname qsastime %{majorqsastime}

%define majorplplotadad 1
%define libadad %mklibname %{name}adad %{majorplplotadad}

%define majorplplotqtd  1
%define libqtd %mklibname %{name}qtd %{majorplplotqtd}

%define majorplplotf95d 11
%define libf95d %mklibname %{name}f95d %{majorplplotf95d}

%define majorplplotcxxd 11
%define libcxxd %mklibname %{name}cxxd %{majorplplotcxxd}

%define majortclmatrixd 9
%define libtclmatrixd %mklibname tclmatrixd %{majortclmatrixd}

%define majorplplottcltkd 11
%define libtcltkd %mklibname %{name}tcltkd %{majorplplottcltkd}

%define majorplplottcltk_Maind  0
%define libtcltk_maind %mklibname %{name}tcltk_maind %{majorplplottcltk_Maind}

%define majorplplotd 12
%define libname %mklibname plplotd %{majorplplotd}
%define devname %mklibname %{name} -d

%define pythonname python-%{name}
%define ocamlname ocaml-%{name}
%define javaname java-%{name}
%define octavename octave-%{name}
%define luaname lua-%{name}

#OFF because not yet on mga
#needs itcl
%define enable_itcl OFF

#itk also requires iwidgets, we currently have inconsistent versions
#(itk-3 and iwidgets-4 euuhhh?)
%define enable_itk OFF
%define itk_version 3.4
%define iwidget_dir %{_datadir}/tcl8.5/iwidgets4.1

#needs PDL::Graphics::PLplot
%define enable_pdl OFF

#needs D compiler
%define enable_d OFF

#needs lasi
%define enable_psttf OFF

#to find fonts for freetype
%define gnu_font_path "/usr/share/fonts/ttf"

#to compile against TCL 8.6
%define c_flags "-DUSE_INTERP_RESULT -lm"

#make install default
%define lua_version 5.1

#autodetection of tk version fails due to no X11 environment
%define tk_version 8.5.15

#shapelib includedir
%define includeshp_dir %{_includedir}/libshp

#fortran and ada files reside in the gcc directory
%define gccinstall_dir %(LC_ALL=C %__cc --print-search-dirs | %__grep install | %__awk '{print $2}')
%define includef_dir %{gccinstall_dir}/finclude
%define libada_dir %{gccinstall_dir}/adalib
%define includeada_dir %{gccinstall_dir}/adainclude

Summary:	A cross-platform software package for creating scientific plots
Name:		plplot
Version:	5.10.0
Release:	18
License:	LGPLv2+
Group:		Development/Other
Url:		http://plplot.sourceforge.net/
Source0:	http://downloads.sourceforge.net/plplot/%{name}-%{version}.tar.gz
Patch1:		plplot-5.10.0-lua5.2.patch
Patch2:		plplot-5.10.0-build-fpic.patch
Patch3:		plplot-5.10.0-incqhull.patch
Patch4:		plplot-5.10.0-cairo-dpi.patch
#From Fedora:
Patch5:		plplot-5.10.0-octave.patch
Patch6:		plplot-5.10.0-octave38.patch
#From Gentoo
Patch7:		plplot-5.10.0-have-config-h.patch

BuildRequires:	cmake
BuildRequires:	gcc-gfortran
BuildRequires:	quadmath-devel
BuildRequires:	gcc-c++
BuildRequires:	gcc-gnat >= 4.7
BuildRequires:	libgnat >= 4.7
#BuildRequires:	gnu-free-fonts-compat
#BuildRequires:	gnu-free-mono-fonts
#BuildRequires:	gnu-free-sans-fonts
#BuildRequires:	gnu-free-serif-fonts
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-doc
BuildRequires:	ocaml-camlidl-devel
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	ocaml-cairo-devel
BuildRequires:	perl-PDL
BuildRequires:	perl-XML-DOM
BuildRequires:	sed
BuildRequires:	swig
BuildRequires:	itk-devel
BuildRequires:	java-1.7.0-openjdk-devel #java-devel-openjdk
BuildRequires:	libltdl-devel
BuildRequires:	octave-devel
BuildRequires:	python-numpy-devel
BuildRequires:	qhull-devel
BuildRequires:	qt4-devel
BuildRequires:	shapelib-devel
#BuildRequires:	wxgtk-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libagg)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(sm)
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(tk)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xcomposite)

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

%files
%doc README README.* AUTHORS NEWS PROBLEMS FAQ ChangeLog.*
%{_bindir}/pl*
%{_mandir}/man1/*
%{_datadir}/%{name}%{baseversion}/*.fnt
%{_datadir}/%{name}%{baseversion}/*.shp
%{_datadir}/%{name}%{baseversion}/*.shx
%{_datadir}/%{name}%{baseversion}/*.pal
%{_datadir}/%{name}%{baseversion}/*.tcl
%{_datadir}/%{name}%{baseversion}/tcl/

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library and driver modules for PLplot
Group:		System/Libraries
Obsoletes:	%{_lib}plplot12 < 5.10.0-4

%description -n %{libname}
%{summary}.

%files -n %{libname}
%doc ABOUT Copyright COPYING.*
%dir %{_libdir}/%{name}%{baseversion}
%{_libdir}/libplplotd.so.%{majorplplotd}
%{_libdir}/libplplotd.so.%{majorplplotd}.*
%{_libdir}/%{name}%{baseversion}/driversd/cairo.*
%{_libdir}/%{name}%{baseversion}/driversd/mem.*
%{_libdir}/%{name}%{baseversion}/driversd/ntk.*
%{_libdir}/%{name}%{baseversion}/driversd/null.*
%{_libdir}/%{name}%{baseversion}/driversd/ps.*
%{_libdir}/%{name}%{baseversion}/driversd/svg.*
%{_libdir}/%{name}%{baseversion}/driversd/xfig.*
%{_libdir}/%{name}%{baseversion}/driversd/xwin.*

#----------------------------------------------------------------------------

%package -n %{libcsiro}
Summary:	Scientific plotting library (CSIRO libraries)
Group:		System/Libraries
Conflicts:	%{_lib}plplot12 < 5.10.0-4
Conflicts:	%{_lib}plplot11 < 5.10.0-4

%description -n %{libcsiro}
This package contains shared libraries for plplot used in geometry
applications.

%files -n %{libcsiro}
%{_libdir}/libcsirocsa.so.%{majorcsiro}
%{_libdir}/libcsirocsa.so.%{majorcsiro}.*
%{_libdir}/libcsironn.so.%{majorcsiro}
%{_libdir}/libcsironn.so.%{majorcsiro}.*

#----------------------------------------------------------------------------

%package -n %{libqsastime}
Summary:	Time format conversion library
Group:		System/Libraries
Conflicts:	%{_lib}plplot12 < 5.10.0-4
Conflicts:	%{_lib}plplot11 < 5.10.0-4

%description -n %{libqsastime}
The qsastime library is a simple library for handling time format
conversion. It overcomes the limitations of the POSIX time handling
routines by allow high precision time variables over a large range
of ranges of dates and by correctly handling leap seconds. It was
designed with the needs of scientific data plotting in mind.

%files -n %{libqsastime}
%{_libdir}/libqsastime.so.%{majorqsastime}
%{_libdir}/libqsastime.so.%{majorqsastime}.*

#----------------------------------------------------------------------------

%package -n %{libadad}
Summary:	Ada runtime support library for PLplot
Group:		System/Libraries
Conflicts:	%{_lib}plplot12 < 5.10.0-4
Conflicts:	%{_lib}plplot11 < 5.10.0-4

%description -n %{libadad}
This package contains Ada runtime support library for PLplot.

%files -n %{libadad}
%{_libdir}/libplplotadad.so.%{majorplplotadad}
%{_libdir}/libplplotadad.so.%{majorplplotadad}.*
%{libada_dir}/plplotadad/

#----------------------------------------------------------------------------

%package -n %{libqtd}
Summary:	Qt driver module and bindings for PLplot
Group:		System/Libraries
Conflicts:	%{_lib}plplot12 < 5.10.0-4
Conflicts:	%{_lib}plplot11 < 5.10.0-4

%description -n %{libqtd}
This package provides the Qt driver module for PLplot. It also provides
C++ bindings to allow use of the PLplot API in Qt applications.

%files -n %{libqtd}
%dir %{_libdir}/%{name}%{baseversion}
%{_libdir}/libplplotqtd.so.%{majorplplotqtd}
%{_libdir}/libplplotqtd.so.%{majorplplotqtd}.*
%{_libdir}/%{name}%{baseversion}/driversd/qt.*

#----------------------------------------------------------------------------

%package -n %{libf95d}
Summary:	Fortran 95 bindings for PLplot
Group:		System/Libraries
Conflicts:	%{_lib}plplot12 < 5.10.0-4
Conflicts:	%{_lib}plplot11 < 5.10.0-4

%description -n %{libf95d}
This package contains the Fortran 95 bindings for PLplot.

%files -n %{libf95d}
%{_libdir}/libplplotf95cd.so.%{majorplplotf95d}
%{_libdir}/libplplotf95cd.so.%{majorplplotf95d}.*
%{_libdir}/libplplotf95d.so.%{majorplplotf95d}
%{_libdir}/libplplotf95d.so.%{majorplplotf95d}.*

#----------------------------------------------------------------------------

%package -n %{libcxxd}
Summary:	C++ bindings for PLplot
Group:		System/Libraries
Conflicts:	%{_lib}plplot12 < 5.10.0-4
Conflicts:	%{_lib}plplot11 < 5.10.0-4

%description -n %{libcxxd}
This package contains the C++ bindings for PLplot.

%files -n %{libcxxd}
%{_libdir}/libplplotcxxd.so.%{majorplplotcxxd}
%{_libdir}/libplplotcxxd.so.%{majorplplotcxxd}.*

#----------------------------------------------------------------------------

%package -n %{libtclmatrixd}
Summary:	Tcl Matrix extension library for PLplot
Group:		System/Libraries
Conflicts:	%{_lib}plplot12 < 5.10.0-4
Conflicts:	%{_lib}plplot11 < 5.10.0-4

%description -n %{libtclmatrixd}
This package provides the Tcl Matrix extension library for PLplot.

%files -n %{libtclmatrixd}
%{_libdir}/libtclmatrixd.so.%{majortclmatrixd}
%{_libdir}/libtclmatrixd.so.%{majortclmatrixd}.*

#----------------------------------------------------------------------------

%package -n %{libtcltkd}
Summary:	Tcl/Tk support for PLplot
Group:		System/Libraries
Conflicts:	%{_lib}plplot12 < 5.10.0-4
Conflicts:	%{_lib}plplot11 < 5.10.0-4

%description -n %{libtcltkd}
This package provides Tcl/Tk support for PLplot. It also provides
Tk driver module.

%files -n %{libtcltkd}
%{_libdir}/libplplottcltkd.so.%{majorplplottcltkd}
%{_libdir}/libplplottcltkd.so.%{majorplplottcltkd}.*
%{_libdir}/%{name}%{baseversion}/driversd/tk.*
%{_libdir}/%{name}%{baseversion}/driversd/tkwin.*

#----------------------------------------------------------------------------

%package -n %{libtcltk_maind}
Summary:	Tcl/Tk support library for PLplot
Group:		System/Libraries
Conflicts:	%{_lib}plplot12 < 5.10.0-4
Conflicts:	%{_lib}plplot11 < 5.10.0-4

%description -n %{libtcltk_maind}
This package provides Tcl/Tk support for PLplot.

%files -n %{libtcltk_maind}
%{_libdir}/libplplottcltk_Maind.so.%{majorplplottcltk_Maind}
%{_libdir}/libplplottcltk_Maind.so.%{majorplplottcltk_Maind}.*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development headers and libraries for PLplot
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	%{libcsiro} = %{EVRD}
Requires:	%{libqsastime} = %{EVRD}
Requires:	%{libadad} = %{EVRD}
Requires:	%{libqtd} = %{EVRD}
Requires:	%{libf95d} = %{EVRD}
Requires:	%{libcxxd} = %{EVRD}
Requires:	%{libtclmatrixd} = %{EVRD}
Requires:	%{libtcltkd} = %{EVRD}
Requires:	%{libtcltk_maind} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{_lib}plplot12 < 5.10.0-17

%description -n %{devname}
%{summary}.

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{includef_dir}/%{name}
#{includef_dir}/#{name}/*.h
%{includef_dir}/%{name}/*.mod
%{_libdir}/libcsiro*.so
%{_libdir}/libqsastime.so
%{_libdir}/libplplot*.so
%{_libdir}/libtclmatrixd.so
%{_libdir}/pkgconfig/plplotd-ada.pc
%{_libdir}/pkgconfig/plplotd-c++.pc
%{_libdir}/pkgconfig/plplotd-f95.pc
%{_libdir}/pkgconfig/plplotd-qt.pc
%{_libdir}/pkgconfig/plplotd-tcl.pc
%{_libdir}/pkgconfig/plplotd-tcl_Main.pc
%{_libdir}/pkgconfig/plplotd.pc
%{includeada_dir}/plplotadad
%dir %{_datadir}/%{name}%{baseversion}/examples
%{_datadir}/%{name}%{baseversion}/examples/CMakeLists.txt
%{_datadir}/%{name}%{baseversion}/examples/Makefile
%{_datadir}/%{name}%{baseversion}/examples/ada
%{_datadir}/%{name}%{baseversion}/examples/c++
%{_datadir}/%{name}%{baseversion}/examples/c
%{_datadir}/%{name}%{baseversion}/examples/cmake
%{_datadir}/%{name}%{baseversion}/examples/f95
%{_datadir}/%{name}%{baseversion}/examples/lena.pgm
%{_datadir}/%{name}%{baseversion}/examples/plplot-test*
%{_datadir}/%{name}%{baseversion}/examples/tcl
%{_datadir}/%{name}%{baseversion}/examples/test_ada.sh
%{_datadir}/%{name}%{baseversion}/examples/test_c.sh
%{_datadir}/%{name}%{baseversion}/examples/test_c_interactive.sh
%{_datadir}/%{name}%{baseversion}/examples/test_cxx.sh
%{_datadir}/%{name}%{baseversion}/examples/test_diff.sh
%{_datadir}/%{name}%{baseversion}/examples/test_f95.sh
%{_datadir}/%{name}%{baseversion}/examples/test_lua.sh
%{_datadir}/%{name}%{baseversion}/examples/test_tcl.sh
%{_datadir}/%{name}%{baseversion}/examples/tk/

#----------------------------------------------------------------------------

%package -n %{pythonname}
Summary:	PLplot support for Python
Group:		Development/Python
Requires:	python
Provides:	%{name}-python = %{EVRD}

%description -n %{pythonname}
%{summary}.

%files -n %{pythonname}
%{python_sitearch}/_plplotcmodule.so
%{python_sitearch}/plplot*
%{python_sitearch}/Plframe.*
%{python_sitearch}/TclSup.*
%{_datadir}/%{name}%{baseversion}/examples/python
%{_datadir}/%{name}%{baseversion}/examples/test_python.sh

#----------------------------------------------------------------------------

%package -n %{ocamlname}
Summary:	PLplot support for OCaml
Group:		Development/Other
Provides:	%{name}-ocaml = %{EVRD}

%description -n %{ocamlname}
%{summary}.

%files -n %{ocamlname}
%{_libdir}/ocaml/%{name}
%{_libdir}/ocaml/stublibs/*
%{_libdir}/ocaml/plcairo/*
%{_libdir}/pkgconfig/plplotd-ocaml.pc
%{_datadir}/%{name}%{baseversion}/examples/ocaml/
%{_datadir}/%{name}%{baseversion}/examples/test_ocaml.sh

#----------------------------------------------------------------------------

%package -n %{javaname}
Summary:	PLplot support for Java
Group:		Development/Java
Requires:	java
Provides:	%{name}-java = %{EVRD}

%description -n %{javaname}
%{summary}.

%files -n %{javaname}
%{_libdir}/%{name}/plplotjavac_wrap.so
%{_datadir}/java/plplot.jar
%{_datadir}/%{name}%{baseversion}/examples/java/
%{_datadir}/%{name}%{baseversion}/examples/test_java.sh

#----------------------------------------------------------------------------

%package -n %{octavename}
Summary:	PLplot support for Octave
Group:		Sciences/Mathematics
Requires:	octave
Provides:	%{name}-octave = %{EVRD}

%description -n %{octavename}
%{summary}.

%files -n %{octavename}
%{_datadir}/plplot_octave/
%{_datadir}/octave/site/m/PLplot/
%{_libdir}/octave/site/oct/*/plplot_octave.oct
%{_datadir}/%{name}%{baseversion}/examples/lena.img
%{_datadir}/%{name}%{baseversion}/examples/octave/
%{_datadir}/%{name}%{baseversion}/examples/test_octave.sh
%{_datadir}/%{name}%{baseversion}/examples/test_octave_interactive.sh

#----------------------------------------------------------------------------

%package -n %{luaname}
Summary:	PLplot support for Lua
Group:		Sciences/Mathematics
Requires:	lua%{lua_version}
Provides:	%{name}-lua = %{EVRD}
Conflicts:	%{_lib}plplot-devel < 5.10.0-5

%description -n %{luaname}
%{summary}.

%files -n %{luaname}
%dir %{_libdir}/lua/%{lua_version}/plplot/
%{_libdir}/lua/%{lua_version}/plplot/plplotluac.so
%{_datadir}/%{name}%{baseversion}/examples/lua/

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{srcversion}
%apply_patches

%build
%cmake \
	-DENABLE_itcl=%{enable_itcl} \
	-DENABLE_itk=%{enable_itk} \
	-DENABLE_pdl=%{enable_pdl} \
	-DENABLE_d=%{enable_d} \
	-DPLD_psttf=%{enable_psttf} \
	-DPL_FREETYPE_FONT_PATH:PATH=%{gnu_font_path} \
	-DCMAKE_C_FLAGS:STRING=%{c_flags} \
	-DTEST_DYNDRIVERS=OFF \
	-DUSE_RPATH:BOOL=OFF \
	-DF95_MOD_DIR:PATH=%{includef_dir}/%{name} \
	-DF77_INCLUDE_DIR:PATH=%{includef_dir}/%{name} \
	-DOCAML_INSTALL_DIR:PATH=%{_libdir}/ocaml \
	-DJAVAWRAPPER_DIR:PATH=%{_libdir}/%{name} \
	-DCMAKE_BUILD_TYPE=Release \
	-DSHAPELIB_INCLUDE_DIR=%{includeshp_dir} \
	-DPLPLOT_ITK_VERSION:STRING=%{itk_version} \
	-DPLPLOT_TK_VERSION:STRING=%{tk_version}
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_libdir}/libplf95demolibd.a

#install ada files into the right place, the -DADA_LIB_DIR variable
#cannot be overloaded
mkdir -p %{buildroot}%{libada_dir}
mkdir -p %{buildroot}%{includeada_dir}
pushd %{buildroot}%{_datadir}/ada/adainclude
mv plplotadad %{buildroot}%{libada_dir}/plplotadad
popd
pushd %{buildroot}%{_libdir}/ada/adalib
mv plplotadad %{buildroot}%{includeada_dir}/plplotadad
popd

#remove remaining *.in example files screwing up find
#requires scripts
rm -f %{buildroot}%{_datadir}/%{name}%{baseversion}/examples/tk/*.in
rm -f %{buildroot}%{_datadir}/%{name}%{baseversion}/examples/tcl/*.in

