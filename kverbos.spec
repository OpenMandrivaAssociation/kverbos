Summary: An educational program that helps people practice Spanish verbs
Name: kverbos
Version: 2.0
Release: %mkrel 2
Source: http://www.mzgz.de/kverbos/%name-%version.tar.gz
License: GPLv2+
Group: Education
Url: http://www.mzgz.de/kverbos/ekverbos.htm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdeedu4-devel

%description
Kverbos allows the user to learn the forms of Spanish verbs. The program
suggests a verb and a time and the user enters the different verb forms.
The program corrects the user input and gives feedback. 

The user can edit the list of the verbs that can be studied. The program
can build regular verb forms by itself. Irregular verb forms have to be
entered by the user.

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_datadir/config.kcfg/*.kcfg
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
