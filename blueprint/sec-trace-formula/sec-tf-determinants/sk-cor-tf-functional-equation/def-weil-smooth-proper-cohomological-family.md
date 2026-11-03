+++
id = "def-weil-smooth-proper-cohomological-family"
kind = "definition"
title = "The smooth-proper cohomological family"
lean = ["AlgebraicGeometry.Scheme.frobeniusCharpolyRev"]
order = 3871
uses = ["def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-weil-sheaf-complex", "prop-cohomological-finiteness", "det-def-sfb-pulled-back-coefficients", "sk-def-sf-weil-complexes"]
+++
Fix the finite-field datum $p,a,q,k_0,k$, where $q=p^a$. Let $X_0/k_0$ be
smooth and proper of pure dimension $d\in\mathbf
Z_{\geq0}$, and put $X=X_0\times_{k_0}k$. For every prime $\ell\neq p$, write
$\Ql=\mathbf Q_\ell$, and let
$K_{X,\ell}=\mathbf Q_{\ell,X}=p_X^*\Ql$ be the coefficient sheaf of the
condensed ring $\Ql$ on $X_{\mathrm{proét}}$
([det-def-sfb-pulled-back-coefficients]), with its canonical Weil structure
([sk-def-sf-weil-complexes]); let $F_\ell$ be the global geometric Frobenius on
$\RGamma(X_{\mathrm{proét}},K_{X,\ell})$, using the geometric-Frobenius convention
[def-weil-frobenius-detailed]. Fix an indeterminate $T$. For every integer $i$ with
$0\leq i\leq2d$, define

$$
 V_{i,\ell}=H^i(X,\Ql):=H^i\RGamma(X_{\mathrm{proét}},\mathbf Q_{\ell,X}),
\qquad
 F_{i,\ell}=F_\ell\vert_{V_{i,\ell}}.
$$

Define

$$
 P_{i,\ell}(T)=
 \det(1-TF_{i,\ell}\mid V_{i,\ell})\in\Ql[T].
$$

It has constant coefficient $1$, degree $\dim_{\Ql}V_{i,\ell}$, and leading
coefficient $(-1)^{\dim V_{i,\ell}}\det(F_{i,\ell})$.

The finiteness of the spaces $V_{i,\ell}$, the invertibility of the operators
$F_{i,\ell}$, and the vanishing of $H^i(X,\Ql)$ outside $0\leq i\leq2d$ are
the content of the cohomological-finiteness proposition
[prop-cohomological-finiteness]; they are not part of the definition of the
family.
