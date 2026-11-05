+++
id = "prose-01-09"
kind = "hidden"
title = "Conventions"
order = 19
+++
We fix a prime $\ell$ and a field $k$ that is finite or algebraically
closed, of characteristic different from $\ell$. Unless said otherwise,
schemes are separated and of finite type over $k$, and morphisms are
$k$-morphisms. The hypothesis on $k$ is used to bound the
$\ell$-cohomological dimension of $k$
(Lemma [sk-lem-base-field-cd]). The constructions of
Sections [sec-n-coefficients] and [sec-n-ambient] make sense for arbitrary
schemes.

All coefficient rings are regarded as condensed rings, and in every case
the coefficient sheaf $\Lambda_X$ on $X$ is the pullback of $\Lambda$
along the map from $X$ to a point (Section [sec-n-coefficients]). For a
finite ring $A$ this pullback is the classical constant sheaf.

Derived categories are the classical ones: $D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is
the derived category of the abelian category of sheaves of
$\Lambda_X$-modules. All functors are derived, and we write $f^*$,
$Rf_*$, $Rf_!$ and $f^!$. Unless another category is named,
$f^*:D(Y_{\mathrm{pro}\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ and
$Rf_*:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$; the
categories on which $Rf_!$ and $f^!$ act are fixed where these functors
are defined. Sizes are taken with respect to a fixed universe, large enough to
contain the w-contractible covers of Theorem [sk-thm-pe-wc-cover].
