# Generated from jaro_winkler-1.5.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jaro_winkler

Name: rubygem-%{gem_name}
Version: 1.5.4
Release: 1%{?dist}
Summary: An implementation of Jaro-Winkler distance algorithm written \ in C extension which supports any kind of string encoding
License: MIT
URL: https://github.com/tonytonyjan/jaro_winkler
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(rake-compiler)
BuildRequires: rubygem(minitest)

%description
jaro_winkler is an implementation of Jaro-Winkler \
distance algorithm which is written in C extension and will fallback to pure \
Ruby version in platforms other than MRI/KRI like JRuby or Rubinius. Both of \
C and Ruby implementation support any kind of string encoding, such as \
UTF-8, EUC-JP, Big5, etc.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

find -type f -name '*.so'

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}/*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Thu Oct 20 2022 Pavel Valena <pvalena@redhat.com> - 1.5.4-1
- Initial package
