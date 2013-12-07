# revision 26384
# category Package
# catalog-ctan /macros/latex/contrib/spreadtab
# catalog-date 2012-05-14 12:19:39 +0200
# catalog-license lppl1.3
# catalog-version 0.4b
Name:		texlive-spreadtab
Version:	0.4b
Release:	4
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
%{_texmfdistdir}/tex/latex/spreadtab/spreadtab.sty
%doc %{_texmfdistdir}/doc/latex/spreadtab/README
%doc %{_texmfdistdir}/doc/latex/spreadtab/spreadtab_doc_en.pdf
%doc %{_texmfdistdir}/doc/latex/spreadtab/spreadtab_doc_en.tex
%doc %{_texmfdistdir}/doc/latex/spreadtab/spreadtab_doc_fr.pdf
%doc %{_texmfdistdir}/doc/latex/spreadtab/spreadtab_doc_fr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
