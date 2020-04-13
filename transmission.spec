#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : transmission
Version  : 2.94
Release  : 1
URL      : https://github.com/transmission/transmission/archive/2.94.tar.gz
Source0  : https://github.com/transmission/transmission/archive/2.94.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: transmission-bin = %{version}-%{release}
Requires: transmission-data = %{version}-%{release}
Requires: transmission-locales = %{version}-%{release}
Requires: transmission-man = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(appindicator3-0.1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libevent)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(zlib)
Patch1: 0001-libsystemd.patch
Patch2: 0001-norc4.patch

%description
ABOUT
Transmission is a fast, easy, and free BitTorrent client.
It comes in several flavors:

%package bin
Summary: bin components for the transmission package.
Group: Binaries
Requires: transmission-data = %{version}-%{release}

%description bin
bin components for the transmission package.


%package data
Summary: data components for the transmission package.
Group: Data

%description data
data components for the transmission package.


%package locales
Summary: locales components for the transmission package.
Group: Default

%description locales
locales components for the transmission package.


%package man
Summary: man components for the transmission package.
Group: Default

%description man
man components for the transmission package.


%prep
%setup -q -n transmission-2.94
cd %{_builddir}/transmission-2.94
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586795832
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static enable-utp \
enable-daemon \
with-systemd-daemon \
enable-nls \
enable-cli \
enable-external-natpmp
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1586795832
rm -rf %{buildroot}
%make_install
%find_lang transmission-gtk

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/transmission-create
/usr/bin/transmission-daemon
/usr/bin/transmission-edit
/usr/bin/transmission-gtk
/usr/bin/transmission-remote
/usr/bin/transmission-show

%files data
%defattr(-,root,root,-)
/usr/share/applications/transmission-gtk.desktop
/usr/share/icons/hicolor/16x16/apps/transmission.png
/usr/share/icons/hicolor/22x22/apps/transmission.png
/usr/share/icons/hicolor/24x24/apps/transmission.png
/usr/share/icons/hicolor/256x256/apps/transmission.png
/usr/share/icons/hicolor/32x32/apps/transmission.png
/usr/share/icons/hicolor/48x48/apps/transmission.png
/usr/share/icons/hicolor/scalable/apps/transmission.svg
/usr/share/pixmaps/transmission.png
/usr/share/transmission/web/LICENSE
/usr/share/transmission/web/images/favicon.ico
/usr/share/transmission/web/images/favicon.png
/usr/share/transmission/web/images/webclip-icon.png
/usr/share/transmission/web/index.html
/usr/share/transmission/web/javascript/common.js
/usr/share/transmission/web/javascript/dialog.js
/usr/share/transmission/web/javascript/file-row.js
/usr/share/transmission/web/javascript/formatter.js
/usr/share/transmission/web/javascript/inspector.js
/usr/share/transmission/web/javascript/jquery/jquery-migrate.min.js
/usr/share/transmission/web/javascript/jquery/jquery-ui.min.js
/usr/share/transmission/web/javascript/jquery/jquery.min.js
/usr/share/transmission/web/javascript/jquery/jquery.transmenu.min.js
/usr/share/transmission/web/javascript/jquery/jquery.ui-contextmenu.min.js
/usr/share/transmission/web/javascript/jquery/json2.min.js
/usr/share/transmission/web/javascript/notifications.js
/usr/share/transmission/web/javascript/prefs-dialog.js
/usr/share/transmission/web/javascript/remote.js
/usr/share/transmission/web/javascript/torrent-row.js
/usr/share/transmission/web/javascript/torrent.js
/usr/share/transmission/web/javascript/transmission.js
/usr/share/transmission/web/style/jqueryui/images/ui-bg_flat_0_aaaaaa_40x100.png
/usr/share/transmission/web/style/jqueryui/images/ui-bg_flat_75_ffffff_40x100.png
/usr/share/transmission/web/style/jqueryui/images/ui-bg_glass_55_fbf9ee_1x400.png
/usr/share/transmission/web/style/jqueryui/images/ui-bg_glass_65_ffffff_1x400.png
/usr/share/transmission/web/style/jqueryui/images/ui-bg_glass_75_dadada_1x400.png
/usr/share/transmission/web/style/jqueryui/images/ui-bg_glass_75_e6e6e6_1x400.png
/usr/share/transmission/web/style/jqueryui/images/ui-bg_glass_95_fef1ec_1x400.png
/usr/share/transmission/web/style/jqueryui/images/ui-bg_highlight-soft_75_cccccc_1x100.png
/usr/share/transmission/web/style/jqueryui/images/ui-icons_222222_256x240.png
/usr/share/transmission/web/style/jqueryui/images/ui-icons_2e83ff_256x240.png
/usr/share/transmission/web/style/jqueryui/images/ui-icons_454545_256x240.png
/usr/share/transmission/web/style/jqueryui/images/ui-icons_888888_256x240.png
/usr/share/transmission/web/style/jqueryui/images/ui-icons_cd0a0a_256x240.png
/usr/share/transmission/web/style/jqueryui/jquery-ui.min.css
/usr/share/transmission/web/style/transmission/common.css
/usr/share/transmission/web/style/transmission/images/arrow-down.png
/usr/share/transmission/web/style/transmission/images/arrow-up.png
/usr/share/transmission/web/style/transmission/images/blue-turtle.png
/usr/share/transmission/web/style/transmission/images/buttons/torrent_buttons.png
/usr/share/transmission/web/style/transmission/images/compact.png
/usr/share/transmission/web/style/transmission/images/file-priority-high.png
/usr/share/transmission/web/style/transmission/images/file-priority-low.png
/usr/share/transmission/web/style/transmission/images/file-priority-normal.png
/usr/share/transmission/web/style/transmission/images/filter_bar.png
/usr/share/transmission/web/style/transmission/images/filter_icon.png
/usr/share/transmission/web/style/transmission/images/inspector-files.png
/usr/share/transmission/web/style/transmission/images/inspector-info.png
/usr/share/transmission/web/style/transmission/images/inspector-peers.png
/usr/share/transmission/web/style/transmission/images/inspector-trackers.png
/usr/share/transmission/web/style/transmission/images/lock_icon.png
/usr/share/transmission/web/style/transmission/images/logo.png
/usr/share/transmission/web/style/transmission/images/progress.png
/usr/share/transmission/web/style/transmission/images/settings.png
/usr/share/transmission/web/style/transmission/images/toolbar-close.png
/usr/share/transmission/web/style/transmission/images/toolbar-folder.png
/usr/share/transmission/web/style/transmission/images/toolbar-info.png
/usr/share/transmission/web/style/transmission/images/toolbar-pause-all.png
/usr/share/transmission/web/style/transmission/images/toolbar-pause.png
/usr/share/transmission/web/style/transmission/images/toolbar-start-all.png
/usr/share/transmission/web/style/transmission/images/toolbar-start.png
/usr/share/transmission/web/style/transmission/images/turtle.png
/usr/share/transmission/web/style/transmission/images/wrench.png
/usr/share/transmission/web/style/transmission/mobile.css

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/transmission-create.1
/usr/share/man/man1/transmission-daemon.1
/usr/share/man/man1/transmission-edit.1
/usr/share/man/man1/transmission-gtk.1
/usr/share/man/man1/transmission-remote.1
/usr/share/man/man1/transmission-show.1

%files locales -f transmission-gtk.lang
%defattr(-,root,root,-)

