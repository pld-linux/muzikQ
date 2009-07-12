Summary:	muzikQ is a curses/SDL_mixer based audio player
Summary(hu.UTF-8):	muzikQ egy curses/SDL_mixer alapú audió lejátszó
Summary(pl.UTF-8):	odtwarzacz plików audio oparty o curses/SDL_mixer
Name:		muzikQ
Version:	0.4
Release:	1
License:	GPL v3
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/muzikq/%{name}-%{version}.tar.gz
# Source0-md5:	ac41ec55a538cbdae36f3121982be470
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

%description -l pl.UTF-8
muzikQ jest konsolowym odtwarzaczem plików audio wykorzystującym
curses i SDL_mixer. Obecnie obsługuje on formaty mp3 i ogg. Pozwala na
tworzenie playlist oraz przypisywanie utoworom "rangi" decydującej o
prawdopodobieństwie wylosowania danego pliku.

%prep
%setup -q -c

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS="-I/usr/include/ncursesw"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README muzikQ.conf muzikQ.txt 
%attr(755,root,root) %{_bindir}/muzikQ
