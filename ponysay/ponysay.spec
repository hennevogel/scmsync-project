Name:           ponysay
Version:        3.0.3
Release:        0
Summary:        Cowsay reimplemention for ponies
License:        GPL-3.0+
Group:          Amusements/Toys/Other
Url:            https://github.com/erkin/ponysay
Source:         https://github.com/erkin/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		python38.patch
BuildRequires:  fdupes
BuildRequires:  python3
BuildRequires:  texinfo
BuildRequires:  texlive-collection-latex
Requires:       python3
Requires(post): info
Requires(preun): info
BuildArch:      noarch

%description
ponysay as an awesome terminal application to display ponies speaking
messages in your terminal.
It has many features; you can use its info manual to explore them.

%prep
%setup -q
%patch0 -p1

%build
# Nothing to build.

%install
python3 setup.py \
  --dest-dir=%{buildroot} \
  --prefix=%{_prefix} \
  --freedom=partial \
  --with-everything \
  --with-pdf=%{_docdir}/%{name}/ \
  install
rm -r %{buildroot}%{_infodir}/dir \
  %{buildroot}%{_datadir}/licenses/
%fdupes %{buildroot}/%{_datadir}/%{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}-tool.info%{ext_info}
%install_info --info-dir=%{_infodir} %{_infodir}/ponythink.info%{ext_info}

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}-tool.info%{ext_info}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ponythink.info%{ext_info}

%files
%defattr(-,root,root)
%doc CHANGELOG CONTRIBUTING COPYING CREDITS LICENSE README.md
%doc %{_docdir}/%{name}/
%{_bindir}/pony*
%{_datadir}/%{name}/
%{_infodir}/*%{ext_info}
%{_mandir}/es/man6/
%{_mandir}/sv/man6/
%{_mandir}/tr/man6/
%{_mandir}/man6/
%{_datadir}/bash-completion/
%{_datadir}/zsh/
%{_datadir}/fish/

%changelog
