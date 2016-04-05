#
# spec file for package skelcd-control-SLED
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


######################################################################
#
# IMPORTANT: Please do not change the control file or this spec file
#   in build service directly, use
#   https://github.com/yast/skelcd-control-SLED repository
#
#   See https://github.com/yast/skelcd-control-SLED/blob/master/CONTRIBUTING.md
#   for more details.
#
######################################################################

Name:           skelcd-control-SLED
Summary:        SLED control file needed for installation
License:        MIT
Group:          Metapackages
BuildRequires:  libxml2-tools
# Added software->default_patterns
BuildRequires:  yast2-installation-control >= 3.1.7

######################################################################
#
# Here is the list of Yast packages which are needed in the
# installation system (inst-sys) for the Yast installer
#

# SLES specific Yast packages needed in the inst-sys
# to provide the functionality needed by this control file
Requires:       yast2-registration
Requires:       yast2-theme-SLE

# Generic Yast packages needed for the installer
Requires:       autoyast2
Requires:       yast2-add-on
Requires:       yast2-buildtools
Requires:       yast2-devtools
Requires:       yast2-fcoe-client
# For creating the AutoYast profile at the end of installation (bnc#887406)
Requires:       yast2-firewall
Requires:       yast2-iscsi-client
Requires:       yast2-kdump
Requires:       yast2-multipath
Requires:       yast2-network >= 3.1.24
Requires:       yast2-nfs-client
Requires:       yast2-ntp-client
Requires:       yast2-proxy
Requires:       yast2-services-manager
Requires:       yast2-slp
Requires:       yast2-trans-stats
Requires:       yast2-tune
Requires:       yast2-update
Requires:       yast2-users
Requires:       yast2-x11

# Architecture specific packages
#
%ifarch s390 s390x
Requires:  yast2-reipl
%endif

%ifarch %ix86 x86_64
Requires:  yast2-vm
%endif

#
######################################################################

Url:            https://github.com/yast/skelcd-control-SLED
AutoReqProv:    off
Version:        12.0.36
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2

%description
SLED control file needed for installation

%prep

%setup -n %{name}-%{version}

%check
#
# Verify syntax
#
make -C control check

%install
#
# Add control file 
#
mkdir -p $RPM_BUILD_ROOT/CD1
install -m 644 control/control.SLED.xml $RPM_BUILD_ROOT/CD1/control.xml

# install LICENSE (required by build service check)
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/doc/packages/%{name}
install -m 644 LICENSE $RPM_BUILD_ROOT/%{_prefix}/share/doc/packages/%{name}

%files
%defattr(644,root,root,755)
/CD1
%doc %dir %{_prefix}/share/doc/packages/%{name}
%doc %{_prefix}/share/doc/packages/%{name}/LICENSE

%changelog
