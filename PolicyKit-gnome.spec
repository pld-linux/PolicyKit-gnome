#
# TODO:
# - update pl summary and description
#
Summary:	GNOME dialogs for PolicyKit
Summary(pl.UTF-8):	PolicyKit - narzędzia dla GNOME
Name:		PolicyKit-gnome
Version:	0.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	efda5749835fba0ee7ff8eb8f3fda393
URL:		http://people.freedesktop.org/~david/polkit-spec.html
BuildRequires:	PolicyKit-devel >= 0.5
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gnome-common >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PolicyKit-gnome provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

%description -l pl.UTF-8
PolicyKit - narzędzia dla GNOME.

%package demo
Summary:	Demo application for PolicyKit-gnome
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description demo
PolicyKit-gnome-demo provides a sample application that demonstrates
the features of both PolicyKit and PolicyKit-gnome. You normally don't
want to have this package installed.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS TODO
%attr(755,root,root) %{_libdir}/polkit-gnome-manager
%{_datadir}/dbus-1/services/org.gnome.PolicyKit.service

%files demo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/polkit-gnome-example
%attr(755,root,root) %{_libdir}/polkit-gnome-example-helper
%{_datadir}/PolicyKit/policy/polkit-gnome-example.policy
