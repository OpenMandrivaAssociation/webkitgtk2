#
# BEFORE UPDATING THIS PACKAGE, YOU _MUST_ DO THE FOLLOWING:
# - DO A LOCAL BUILD
# - INSTALL IT IN A TEST MACHINE
# - CHECK THAT 'display_help http://google.com' STILL WORK (INCLUDING CLOSING IT)
# - CHECK THAT MCC STILL RUNS
#
%define debug_package %{nil}
# *** ERROR: same build ID in nonidentical files!
#        /usr/bin/jsc-3
#   and  /usr/bin/jsc-1


# lib is called libwebkitgtk-%{libver}.so.%{major}
%define libver  1.0
%define major   0
%define oname		webkitgtk
%define sname		webkit
%define libname		%mklibname webkitgtk %{libver} %{major}
%define devname		%mklibname webkitgtk %{libver} -d
%define inspectorname	webkit%{libver}-webinspector
%define girname		%mklibname %{sname}-gir %{libver}
%define girjscore	%mklibname jscore-gir %{libver}
%define libjavascriptcoregtk	%mklibname javascriptcoregtk %{libver} %{major}

%define pango	0
%if %{pango}
%define fontreq		pkgconfig(pango)
%define fontback	pango
%else
%define fontreq		pkgconfig(fontconfig) >= 1.0.0
%define fontback	freetype
%endif

Summary:	Web browser engine
Name:		webkitgtk2
Epoch:		2
Version:	1.10.2
Release:	1
License:	BSD and LGPLv2+
Group:		System/Libraries
Url:		https://www.webkitgtk.org
Source0:	http://www.webkitgtk.org/releases/%{oname}-%{version}.tar.xz
# (blino) needed for first-time wizard (display_help) to be able to close its window with javascript
Patch0:		webkit-1.10.2-link.patch
Patch1:		webkit-1.6.1-allowScriptsToCloseWindows.patch
# fedora
Patch2: 	webkit-1.3.10-nspluginwrapper.patch
# suse patches
Patch3:		webkit-gir-fixup.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	%{fontreq}
BuildRequires:	icu-devel >= 49
BuildRequires:	jpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(gail)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(geoclue)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
#no longer needed since 2.0.0
#hope this commit does not broke some rpm's
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libcurl) >= 7.11.0
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.2.0
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.29.90
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	chrpath

%description
WebKit is an open source web browser engine.

#----------------------------------------------------------------------------

%package -n %{sname}%{libver}
Summary:	GTK+ port of WebKit web browser engine - shared files
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{EVRD}
Conflicts:	%{libname} < 1:1.4.1-5
Conflicts:	%{sname} < 1:1.4.1-6
Conflicts:	%{_lib}webkitgtk1.0_2 < 1:1.4.1
%rename %{sname}

%description -n %{sname}%{libver}
WebKit is an open source web browser engine.
This package contains the shared files used by %{sname}%{libver}

%files -n %{sname}%{libver} -f webkitgtk-2.0.lang
%dir %{_datadir}/webkitgtk-1.0
%{_datadir}/webkitgtk-1.0/images
%{_datadir}/webkitgtk-1.0/resources

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
# Needed for Web Inspector feature to work
Requires:	%{inspectorname}

%description -n %{libname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%files -n %{libname}
%{_libdir}/lib%{sname}gtk-%{libver}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libjavascriptcoregtk}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Obsoletes:	%{_lib}javascriptcoregtk1.0 < %{EVRD}

%description -n %{libjavascriptcoregtk}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%files -n %{libjavascriptcoregtk}
%{_libdir}/libjavascriptcoregtk-%{libver}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for WebKit GTK+ port
Group:		Development/GNOME and GTK+
Provides:	webkitgtk-devel = %{version}-%{release}
Provides:	libwebkitgtk-devel = %{version}-%{release}
Provides:	%{mklibname webkitgtk -d} = %{version}-%{release}
Requires:	%{libname} = %{EVRD}
Requires:	%{libjavascriptcoregtk} = %{EVRD}
Requires:	%{girjscore} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description -n %{devname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%files -n %{devname}
%{_libdir}/lib%{sname}gtk-%{libver}.so
%{_libdir}/libjavascriptcoregtk-%{libver}.so
%{_includedir}/%{sname}gtk-%{libver}
%{_libdir}/pkgconfig/%{sname}-%{libver}.pc
%{_libdir}/pkgconfig/javascriptcoregtk-%{libver}.pc
%{_datadir}/gir-1.0/JSCore-%{libver}.gir
%{_datadir}/gir-1.0/WebKit-%{libver}.gir
%{_datadir}/gtk-doc/html/webkitgtk/*

#----------------------------------------------------------------------------

%package -n %{sname}-gtklauncher
Summary:	WebKit GTK+ example application
Group:		Development/GNOME and GTK+

%description -n %{sname}-gtklauncher
GtkLauncher is an example application for WebKit GTK+.

%files -n %{sname}-gtklauncher
%{_libdir}/%{sname}/GtkLauncher

#----------------------------------------------------------------------------

%package -n %{sname}-jsc
Summary:	JavaScriptCore shell for WebKit GTK+
Group:		Development/GNOME and GTK+

%description -n %{sname}-jsc
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%files -n %{sname}-jsc
%{_bindir}/jsc-1

#----------------------------------------------------------------------------

%package -n %{inspectorname}
Summary:	Data files for WebKit GTK+'s Web Inspector
Group:		System/Libraries
%rename		webkit-webinspector

%description -n %{inspectorname}
WebKit GTK+ has a feature called the Web Inspector, which allows
detailed analysis of any given page's page source, live DOM hierarchy
and resources. This package contains the data files necessary for Web
Inspector to work.

%files -n %{inspectorname}
%{_datadir}/%{sname}gtk-%{libver}/webinspector

#----------------------------------------------------------------------------

%package -n %{girjscore}
Summary:	GObject Introspection interface description for JSCore
Group:		System/Libraries
Conflicts:	%{_lib}webkitgtk1.0_2 < %{EVRD}

%description -n %{girjscore}
GObject Introspection interface description for JSCore.

%files -n %{girjscore}
%{_libdir}/girepository-1.0/JSCore-%{libver}.typelib

#----------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface description for %{sname}
Group:		System/Libraries
Conflicts:	%{_lib}webkitgtk1.0_2 < %{EVRD}

%description -n %{girname}
GObject Introspection interface description for WebKit.

%files -n %{girname}
%{_libdir}/girepository-1.0/WebKit-%{libver}.typelib

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1
# Don't force -O2
sed -i 's/-O2//g' configure.ac

%build
# Use linker flags to reduce memory consumption on low-mem architectures
%ifarch %{arm}
%define lowmemflags -Wl,--no-keep-memory -Wl,--reduce-memory-overheads
export CFLAGS="`echo %{optflags} %lowmemflags | sed -e 's/-gdwarf-4//' -e 's/-fvar-tracking-assignments//' -e 's/-frecord-gcc-switches//'`"
mkdir -p bfd
ln -s %{_bindir}/ld.bfd bfd/ld
export PATH=$PWD/bfd:$PATH
export CC="%{__cc} -fuse-ld=bfd"
export CXX="%{__cxx} -fuse-ld=bfd"
%global ldflags %{ldflags} -fuse-ld=bfd
%else
export CFLAGS="`echo %{optflags} | sed -e 's/-gdwarf-4//' -e 's/-fvar-tracking-assignments//' -e 's/-frecord-gcc-switches//'`"
%endif

export CXXFLAGS="$CFLAGS"

%configure2_5x \
	--enable-dependency-tracking \
	--with-gtk=2.0 \
	--with-gstreamer=0.10 \
	--disable-webkit2 \
	--with-font-backend=%{fontback} \
	--enable-jit \
	--enable-video \
	--enable-introspection

make V=1 -j4

%install
%makeinstall_std
mkdir -p %{buildroot}%{_libdir}/%{sname}
install -m 755 Programs/GtkLauncher %{buildroot}%{_libdir}/%{sname}

# only useful for testing, should not be installed system-wide.
# reported upstream as 22812 - AdamW 2008/12
rm -rf %{buildroot}%{_libdir}/libtestnetscapeplugin.*

# Remove lib64 rpaths
chrpath --delete %{buildroot}%{_libexecdir}/%{sname}/GtkLauncher

%find_lang webkitgtk-2.0

