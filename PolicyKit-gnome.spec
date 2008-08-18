#
# Conditional build:
%bcond_without	examples
#
Summary:	GNOME dialogs for PolicyKit
Summary(pl.UTF-8):	Okna dialogowe GNOME dla pakietu PolicyKit
Name:		PolicyKit-gnome
Version:	0.9
Release:	1
License:	LGPL v2+ (polkit-gnome library), GPL v2+ (D-Bus service)
Group:		X11/Applications
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	68374b04289ce99d95a9df19d6217344
URL:		http://people.freedesktop.org/~david/polkit-spec.html
BuildRequires:	GConf2-devel
BuildRequires:	PolicyKit-devel >= 0.9
%{?with_examples:BuildRequires:	PolicyKit}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-vfs2-devel >= 2.4
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libsexy-devel >= 0.1.11
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PolicyKit-gnome provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

%description -l pl.UTF-8
Pakiet PolicyKit-gnome udostępnia usługę magistrali sesji D-BUS
służącą do wyświetlania okien dialogowych uwierzytelniania w celu
uzyskania uprawnień.

%package libs
Summary:	PolicyKit add-on library for GNOME
Summary(pl.UTF-8):	Dodatkowa biblioteka PolicyKit dla GNOME
Group:		X11/Libraries
Requires:	PolicyKit-libs >= 0.9
Requires:	gtk+2 >= 2:2.12.0

%description libs
PolicyKit add-on library for GNOME.

%description libs -l pl.UTF-8
Dodatkowa biblioteka PolicyKit dla GNOME.

%package devel
Summary:	Header files for polkit-gnome library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki polkit-gnome
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	PolicyKit-devel >= 0.9
Requires:	dbus-devel >= 1.0
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	libselinux-devel >= 1.30

%description devel
Header files for polkit-gnome library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki polkit-gnome.

%package static
Summary:	Static polkit-gnome library
Summary(pl.UTF-8):	Statyczna biblioteka polkit-gnome
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static polkit-gnome library.

%description static -l pl.UTF-8
Statyczna biblioteka polkit-gnome.

%package apidocs
Summary:	polkit-gnome library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki polkit-gnome
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
polkit-gnome library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki polkit-gnome.

%package demo
Summary:	Demo application for PolicyKit-gnome
Summary(pl.UTF-8):	Aplikacja demonstracyjna dla pakietu PolicyKit-gnome
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description demo
PolicyKit-gnome-demo provides a sample application that demonstrates
the features of both PolicyKit and PolicyKit-gnome. You normally don't
want to have this package installed.

%description demo -l pl.UTF-8
Pakiet PolicyKit-gnome-demo zawiera przykładową aplikację
demonstrującą możliwości pakietów PolicyKit i PolicyKit-gnome. Zwykle
ten pakiet nie powinien być instalowany.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_examples:--disable-examples} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schemas_install polkit-gnome.schemas

%preun
%gconf_schemas_uninstall polkit-gnome.schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/polkit-gnome-authorization
%attr(755,root,root) %{_libdir}/polkit-gnome-manager
%{_sysconfdir}/gconf/schemas/polkit-gnome.schemas
%{_datadir}/dbus-1/services/org.gnome.PolicyKit.service
%{_datadir}/dbus-1/services/org.gnome.PolicyKit.AuthorizationManager.service
%{_datadir}/dbus-1/services/gnome-org.freedesktop.PolicyKit.AuthenticationAgent.service
%{_desktopdir}/polkit-gnome-authorization.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-gnome.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-gnome.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-gnome.so
%{_libdir}/libpolkit-gnome.la
%{_includedir}/PolicyKit/polkit-gnome
%{_pkgconfigdir}/polkit-gnome.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpolkit-gnome.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/polkit-gnome

%if %{?with_examples}
%files demo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/polkit-gnome-example
%{_datadir}/PolicyKit/policy/org.gnome.policykit.examples.policy
%endif
