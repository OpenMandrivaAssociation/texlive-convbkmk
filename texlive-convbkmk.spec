# revision 33125
# category Package
# catalog-ctan /support/convbkmk
# catalog-date 2014-03-02 11:29:31 +0100
# catalog-license other-free
# catalog-version 0.09
Name:		texlive-convbkmk
Version:	0.09
Release:	4
Summary:	Correct platex/uplatex bookmarks in PDF created with hyperref
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/convbkmk
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/convbkmk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/convbkmk.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-convbkmk.bin = %{EVRD}

%description
The package provides a small Ruby script that corrects
bookmarks in PDF files created by platex/uplatex, using
hyperref.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/convbkmk
%{_texmfdistdir}/scripts/convbkmk/convbkmk.rb
%doc %{_texmfdistdir}/doc/support/convbkmk/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/convbkmk/convbkmk.rb convbkmk
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
