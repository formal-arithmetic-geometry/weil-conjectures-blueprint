+++
id = "prop-finite-compact-support-constructibility"
kind = "theorem"
title = "Finite-level bounded constructibility for proper support"
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerShriek", "AlgebraicGeometry.ProEtale.constructibleIn_rightDerivedLowerShriek"]
order = 3171
tags = ["latex:proposition"]
uses = ["def-compact-support-direct-image-detailed", "def-weil-compact-support-candidate", "def-weil-compactifications-refinements", "def-weil-constructible-intervals", "def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "def-weil-extension-by-zero", "def-weil-finite-torsion-constructibility", "def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-fin-extension-by-zero", "obl-fin-comparison", "prop-weil-pbc-comparison-direct-image", "sbc-thm-finiteness-finite-type", "thm-constructible-serre", "lem-sf-proetale-constructible-origin"]
+++
Let $K_0$ be a field, let $X,Y$ be
finite-type $K_0$-schemes, and let
$f:X\to Y$ be a
separated finite-type
$K_0$-morphism. Fix a prime $\ell$, write $\Ql=\mathbf Q_\ell$, and
require that its image in $K_0$ is invertible. Choose a finite extension
$E/\Ql$, an integer $n\in\mathbf Z_{\geq1}$,
and put $A=A_{E,n}$. Let $Rf_{!,n}$ be the coherent finite-level
compact-support direct image
functor associated to the
compactification candidates.
The comparison maps for refinements are identities and satisfy the cocycle
condition, and $D^b_c(X,A)$ uses
finite-torsion
constructibility. For $a,b\in\mathbf Z$ with $a\leq b$, write

$$
D_c^{[a,b]}(X,A)=\{K\in D^b_c(X,A):
\mathcal H^r(K)=0\text{ for }r\notin[a,b]\},
$$

where $D^b_c(X,A)$ has the
finite-torsion
constructibility condition, and $\mathcal H^r$ is the
cohomology-sheaf functor.
The ambient
derived direct-image functor
$Rf_{!,n}$ restricts to an exact triangulated functor

$$
Rf_{!,n}:D^b_c(X,A_{E,n})
\longrightarrow D^b_c(Y,A_{E,n}).
$$

For each cohomological interval
$[a,b]$ with $a,b\in\mathbf Z$ and
$a\leq b$, and each integer $e\geq0$ such that every
geometric fiber of $f$ has
dimension at most $e$, there
are integers $a'\leq b'$, independent of the compactification, such that
for every $K\in D_c^{[a,b]}(X,A_{E,n})$ one has

$$
Rf_{!,n}K\in D_c^{[a',b']}(Y,A_{E,n}).
$$

The restriction and its amplitude bound commute with finite coefficient
reduction.

*General finite coefficients.* The finiteness part does not need
$A=A_{E,n}$. Let $A$ be any finite commutative ring annihilated by $\ell^N$
for some $N\geq1$. Let $K$ be a bounded complex of $A$-modules on $X$ (on
$X_{\Et}$, or on $X_{\mathrm{proet}}$ through an étale model) whose cohomology
sheaves lie in $[a,b]$ and are constructible with finite stalks. Then for
every compactification $f=\bar f\circ j$ the complex $R\bar f_*j_!K$ has
constructible cohomology sheaves in $[a,b+2e]$. In particular, for
$Y=\Spec k$ with $k$ separably closed, its cohomology modules are finite
$A$-modules. This uses only bounded constructibility. It does not assert that
restriction of scalars from $A$ to $\mathbf Z/\ell^N$ preserves finite Tor
amplitude.
