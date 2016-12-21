Name     : jdk-felix-osgi-core
Version  : 1.4.0
Release  : 1
URL      : http://www.apache.org/dist/felix/org.osgi.core-1.4.0.jar
Source0  : http://www.apache.org/dist/felix/org.osgi.core-1.4.0.jar
Source1  : http://www.apache.org/dist/felix/org.osgi.core-1.4.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : apache-maven
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms/felix
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java/felix

mv %{SOURCE0} %{buildroot}/usr/share/java/felix/org.osgi.core.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/felix/org.osgi.core.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
    -n "" \
    --pom-base "%{buildroot}/usr/share/maven-poms" \
    --jar-base "%{buildroot}/usr/share/java" \
    "%{buildroot}/usr/share/maven-metadata/felix-osgi-core.xml" \
    "%{buildroot}/usr/share/maven-poms/felix/org.osgi.core.pom" \
    "%{buildroot}/usr/share/java/felix/org.osgi.core.jar"


%files
%defattr(-,root,root,-)
/usr/share/java/felix/org.osgi.core.jar
/usr/share/maven-metadata/felix-osgi-core.xml
/usr/share/maven-poms/felix/org.osgi.core.pom
