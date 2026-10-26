+++
id = "def-weil-full-cohomological-dimension"
kind = "definition"
title = "Full cohomological dimension"
order = 2295
lean = ["AlgebraicGeometry.ProEtale.HasUniformCohomologicalDimensionLE"]
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$, an integer $n\in\mathbf
Z_{\geq1}$, and put $A=A_{E,n}$, with the finite-torsion coefficient
convention [def-weil-finite-torsion-constructibility]; more generally the
coefficients may be sheaves with values in any Grothendieck abelian category. Let
$p:\overline X\to Y$ be a morphism of schemes [def-weil-scheme-morphism-properties]
(in the applications, a proper morphism of finite-type schemes over a base on which $\ell$
is invertible). Use the derived direct image [def-weil-derived-direct-image] on the small
pro-etale sites [def-weil-pbc-proetale-site], and let $\mathcal H^r$ denote the
cohomology-sheaf functor [def-weil-derived-cohomology-sheaves]. For an integer
$c\in\mathbf Z_{\geq0}$, write $\operatorname{FullCD}(p,A;c)$ if for every object $V\to Y$ of
$Y_{\mathrm{proet}}$, every cartesian square

$$
\begin{array}{ccc}
X'&\longrightarrow&\overline X\\
{\scriptstyle p_V}\downarrow&&\downarrow{\scriptstyle p}\\
V&\longrightarrow&Y
\end{array}
$$

and every sheaf $\mathcal F$ of $A$-modules on $X'_{\mathrm{proet}}$,

$$
 \mathcal H^r\bigl(R(p_V)_*\mathcal F\bigr)=0
 \qquad(r\in\mathbf Z,\ r>c).
$$

Taking $V=Y$ gives in particular $\mathcal H^r(Rp_*\mathcal F)=0$ for $r>c$ and every sheaf
$\mathcal F$ of $A$-modules on $\overline X_{\mathrm{proet}}$.

*Warning.* Because the quantifier ranges over *every* pro-etale sheaf of
$A$-modules, $\operatorname{FullCD}(p,A;c)$ fails in general, even for $p$
proper and smooth of dimension one over an algebraically closed field: for an
elliptic curve $E$ over $\overline{\mathbf F}_p$, $A=\mathbf F_r$ with
$r\neq p$, there is a pro-etale $A$-module sheaf $\mathcal F$ on $E$ (not of
etale origin) with $H^n(E_{\mathrm{proet}},\mathcal F)\neq0$ for every
$n\geq1$. What does hold, with $c=2\dim\overline X$, is the restriction of
the condition to the coefficient sheaves of etale origin.
