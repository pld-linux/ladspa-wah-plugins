Summary:	WAH (wah pedal) LADSPA plugins
Summary(pl.UTF-8):	Wtyczki LADSPA WAH (pedał wah)
Name:		ladspa-wah-plugins
Version:	0.1.0
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/WAH-plugins-%{version}.tar.bz2
# Source0-md5:	d5df8cb2c88a153316a711512c1646c7
Patch0:		%{name}-make.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/ladspa

%description
WAH (wah pedal) LADSPA plugins.

%description -l pl.UTF-8
Wtyczki LADSPA WAH (pedał wah).

%prep
%setup -q -n WAH-plugins-%{version}
%patch0 -p1

%build
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LADSPA_LIB_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/autowah.so
