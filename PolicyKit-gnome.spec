Summary:	PolicyKit - GNOME utilities
Summary(pl.UTF-8):	PolicyKit - narzędzia dla GNOME
Name:		PolicyKit-gnome
Version:	0.3
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	4f7a7b23051a59e0c29248605e98d56a
URL:		http://people.freedesktop.org/~david/polkit-spec.html
BuildRequires:	PolicyKit-devel >= 0.3
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gnome-common >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PolicyKit - GNOME utilities.

%description -l pl.UTF-8
PolicyKit - narzędzia dla GNOME.

%prep
%setup -q

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/polkit-gnome-example
%attr(755,root,root) %{_libexecdir}/polkit-gnome
%attr(755,root,root) %{_libexecdir}/polkit-gnome-example-helper
%{_datadir}/PolicyKit/policy/polkit-gnome-example.policy
%{_datadir}/dbus-1/services/org.gnome.PolicyKit.service
