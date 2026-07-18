%global tl_name convbkmk
%global tl_revision 49252
%global tl_bin_links convbkmk:%{_texmfdistdir}/scripts/convbkmk/convbkmk.rb

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.30
Release:	%{tl_revision}.1
Summary:	Correct platex/uplatex bookmarks in PDF created with hyperref
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/convbkmk
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/convbkmk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/convbkmk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(convbkmk.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The package provides a small Ruby script that corrects bookmarks in PDF
files created by platex/uplatex, using hyperref.

