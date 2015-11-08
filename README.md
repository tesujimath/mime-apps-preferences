# mime-apps-preferences

## Introduction

`mime-apps-preferences` is a graphical utility for defining the preferred
applications for handling different MIME types on XDG desktops,
i.e. all common Linux desktops, and possibly some others.

Existing utilities which address this function tend to require the
user to specify every single MIME type they are interested in, and
associate their preferred application, probably via the file manager.
`mime-apps-preferences` takes a different approach.  The user simply
selects their preferred applications from a list, and these are
installed as the default application handler for *all* the MIME types
which they support.

## Usage

The usage should be fairly intuitive.  The model of preferred
applications is deliberately rather simple.  A single ordered list of
preferred applications is maintained.  This makes it very easy to
select applications, and click on _Prefer_ to add it to the list of
Preferred Applications, or _Remove_ to remove it from that list.

Selecting an application filters the list of MIME types to those
supported by that application, and the list of applications to those
supporting any of those MIME types.  That is, attention is focused on
those applications which are competing to be the handler for that set
of MIME types.  Simmilarly, selecting a MIME type filters the list of
applications to those which handle that particular MIME type.

Any MIME type supported by a unique application is not shown at all,
and neither are such applications, for the simple reason that in this
case, there is no preference to be selected.

The order of Preferred Applications only matters where several
applications have been selected which overlap in their supported MIME
types.  The order may be adjusted by (repeated use of) the _+_ and _-_
buttons.  The granularity offered by `mime-apps-preferences` does not
allow for fine-tuning of different applications for different MIME
types in cases like this, except by overall preference order, and
blacklisting an application/MIME-type pair.

Two examples may help to clarify this.

1. VLC handles audio MIME types, but it is annoying if it gets selected
in preference to a dedicated audio application.  In this case, simply
ensure that your preferred audio application is above VLC in the list
of Preferred Applications.  Then, VLC will be used for all its MIME
types, except for those supported by your other application, which
will be used in preference.

2. LibreOffice Writer handles text/plain, which is also annoying if it
gets selected for that.  By blacklisting this pair, it will never be
chosen in practice to handle text/plain, even if it appears at the top
of the Preferred Applications list.

## Internal Details

`mime-apps-preferences` is a Python/Tkinter script.

It works by updating the `mimeapps.list` file, usually found in `~/.config/mimeapps.list`.

## Caveats

`mime-apps-preferences` will replace any finely tuned settings in
`mimeapps.list` with its simple, but rather comprehensive, view of the world.

`mime-apps-preferences` currently has no support for adding file
associations in the `mimeapps.list` file, and will simply discard them
(for now).

It would be wise to backup the `mimeapps.list` file before first use
of this script, until a satisfactory result is achieved.

## Licence

GNU General Public License v3

## References
+ [freedesktop.org: Association between MIME types and applications](http://standards.freedesktop.org/mime-apps-spec/latest/index.html)
+ [freedesktop.org: XDG Base Directory Specification](http://standards.freedesktop.org/basedir-spec/latest/)
