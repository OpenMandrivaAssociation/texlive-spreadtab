Name:		texlive-spreadtab
Version:	0.4d
Release:	2
Summary:	Spreadsheet features for LaTeX tabular environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spreadtab
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spreadtab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spreadtab.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to construct tables in a manner
similar to a spreadsheet. The cells of a table have row and
column indices and these can be used in formulas to generate
values in other cells.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/spreadtab
%doc %{_texmfdistdir}/doc/latex/spreadtab

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
