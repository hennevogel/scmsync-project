#
# spec file for package webhook
#
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           webhook
Version:        2.8.1
Release:        0
Summary:        Small server for creating HTTP endpoints (hooks)
License:        MIT
URL:            https://github.com/adnanh/webhook/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go
BuildRequires:  golang-packaging
%{go_provides}

%description
Webhook is a lightweight configurable tool written in Go, that allows
you to easily create HTTP endpoints (hooks) on your server, which you
can use to execute configured commands. You can also pass data from
the HTTP request (such as headers, payload or query variables) to
your commands. webhook also allows you to specify rules which have to
be satisfied in order for the hook to be triggered.

For example, if you're using Github or Bitbucket, you can use webhook
to set up a hook that runs a redeploy script for your project on your
staging server, whenever you push changes to the master branch of
your project.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -Dpm 0755 webhook %{buildroot}%{_bindir}/webhook

%files
%license LICENSE
%{_bindir}/webhook

%changelog
