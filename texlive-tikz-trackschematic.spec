Name:		texlive-tikz-trackschematic
Version:	63480
Release:	2
Summary:	A TikZ library for creating track diagrams in railways
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-trackschematic
License:	isc
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-trackschematic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-trackschematic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This TikZ library is a toolbox of symbols geared primarily
towards creating track schematic for either research or
educational purposes. It provides a TikZ frontend to some of
the symbols which may be needed to describe situations and
layouts in railway operation. The library is divided into
sublibraries: topology, trafficcontrol, vehicles,
constructions, electrics, symbology, and measures.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-trackschematic
%doc %{_texmfdistdir}/doc/latex/tikz-trackschematic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
