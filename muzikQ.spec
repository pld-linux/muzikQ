Summary:	muzikQ is a curses/SDL_mixer based audio player
Summary(hu.UTF-8):	muzikQ egy curses/SDL_mixer alapú audió lejátszó
Name:		muzikQ
Version:	0.2
Release:	0.1
License:	GPL v3
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/muzikq/%{name}-%{version}.tar.gz
# Source0-md5:	bbb357b6260929a7c7124661ed296557
URL:		http://sourceforge.net/projects/muzikq/
BuildRequires:	SDL_mixer-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ncurses-devel
BuildRequires:	smpeg-devel
BuildRequires:	taglib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
muzikQ is a curses/SDL_mixer based audio player currently supporting
mp3 & ogg, has features such as song rating, playlists, ssh and telnet
control.

%description -l hu.UTF-8
muzikQ egy curses/SDL_mixer alapú audió lejátszó, jelenleg mp3 és ogg
formátumokat támogat. A lehetőségei között zene osztályozása,
számlisták, ssh és telnet irányítás van.

%prep
%setup -q

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS="-I/usr/include/ncursesw" \
	 \

%{__make} DESTDIR=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README muzikQ.conf muzikQ.txt
%attr(755,root,root) %{_bindir}/muzikQ
