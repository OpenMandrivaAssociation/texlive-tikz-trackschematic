%global tl_name tikz-trackschematic
%global tl_revision 63480

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.1
Release:	%{tl_revision}.1
Summary:	A TikZ library for creating track diagrams in railways
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-trackschematic
License:	isc
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-trackschematic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-trackschematic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This TikZ library is a toolbox of symbols geared primarily towards
creating track schematic for either research or educational purposes. It
provides a TikZ frontend to some of the symbols which may be needed to
describe situations and layouts in railway operation. The library is
divided into sublibraries: topology, trafficcontrol, vehicles,
constructions, electrics, symbology, and measures.

