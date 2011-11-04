# revision 23526
# category Package
# catalog-ctan /macros/latex/contrib/spreadtab
# catalog-date 2011-08-11 15:31:53 +0200
# catalog-license lppl1.3
# catalog-version 0.4a
Name:		texlive-spreadtab
Version:	0.4a
Release:	1
Summary:	Spreadsheet features for LaTeX tabular environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spreadtab
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spreadtab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spreadtab.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows the user to construct tables in a manner
similar to a spreadsheet. The cells of a table have row and
column indices and these can be used in formulas to generate
values in other cells.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/spreadtab/spreadtab.sty
%doc %{_texmfdistdir}/doc/latex/spreadtab/README
%doc %{_texmfdistdir}/doc/latex/spreadtab/spreadtab_doc_en.pdf
%doc %{_texmfdistdir}/doc/latex/spreadtab/spreadtab_doc_en.tex
%doc %{_texmfdistdir}/doc/latex/spreadtab/spreadtab_doc_fr.pdf
%doc %{_texmfdistdir}/doc/latex/spreadtab/spreadtab_doc_fr.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
