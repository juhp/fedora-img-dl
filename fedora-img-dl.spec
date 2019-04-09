# generated by cabal-rpm-0.13.1
# https://fedoraproject.org/wiki/Packaging:Haskell

Name:           fedora-img-dl
Version:        0.1
Release:        1%{?dist}
Summary:        Fedora image download tool

License:        GPLv3+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
#BuildRequires:  ghc-html-conduit-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-hxt-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-optparse-applicative-devel
#BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unix-devel
#BuildRequires:  ghc-xdg-userdirs-devel
BuildRequires:  ghc-xml-conduit-devel
# End cabal-rpm deps

%description
Tool to download Fedora iso and image files.


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%global cabal cabal
%cabal update
%cabal sandbox init
%cabal install --only-dependencies
%ghc_bin_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_bin_install
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
# End cabal-rpm files


%changelog
* Mon Apr  8 2019 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1-1
- spec file generated by cabal-rpm-0.13.1