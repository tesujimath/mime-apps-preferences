Name:           mime-apps-preferences
Version:        0.5
Release:        1%{?dist}
Summary:        Graphical selection of preferred applications for MIME types.

License:        GPLv3
URL:            https://github.com/tesujimath/mime-apps-preferences
Source0:        https://github.com/tesujimath/mime-apps-preferences/archive/%{name}-%{version}.tar.gz

#BuildRequires:  
Requires:       python tkinter
BuildArch:      noarch

%description
%{name} is a graphical utility for defining the preferred
applications for handling different MIME types on XDG desktops,
i.e. all common Linux desktops, and possibly some others.

Existing utilities which address this function tend to require the
user to specify every single MIME type they are interested in, and
associate their preferred application, probably via the file manager.
%{name} takes a different approach.  The user simply
selects their preferred applications from a list, and these are
installed as the default application handler for *all* the MIME types
which they support.

%define debug_package %{nil}

%prep
%setup -q

%build
# nothing to do, it's just a script

%install
rm -rf %{buildroot}
install -D %{name}  %{buildroot}%{_bindir}/%{name}
install -D %{name}.desktop  %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING README.md
%{_bindir}/*
%{_datadir}/applications/*

%changelog
* Mon Nov  9 2015 Simon Guest <simon.guest@tesujimath.org>
- first packaging
