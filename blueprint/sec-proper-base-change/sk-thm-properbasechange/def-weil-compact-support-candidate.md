+++
id = "def-weil-compact-support-candidate"
kind = "definition"
title = "Compact-support candidate attached to a compactification"
order = 1987
lean = ["AlgebraicGeometry.ProEtale.rightDerivedLowerShriekOfCompactification", "AlgebraicGeometry.ProEtale.rightDerivedLowerShriekOfCompactificationEtaleOrigin"]
uses = ["def-weil-compactifications-refinements", "def-weil-derived-direct-image", "def-weil-extension-by-zero", "def-weil-finite-torsion-constructibility", "def-weil-pbc-etale-origin-witness"]
+++
Let $f:X\to Y$ be a morphism of schemes and let $\Lambda$ be a commutative
coefficient ring; the case of interest is a finite-torsion coefficient ring
$A=A_{E,n}$ of [def-weil-finite-torsion-constructibility]. Let $c=(j,\bar f)$
be a compactification of $f$, i.e. an object of the compactification category
[def-weil-compactifications-refinements] $\operatorname{Comp}(f)$. Using the
derived direct image [def-weil-derived-direct-image] $R\bar f_{*}$ and the
extension-by-zero functor [def-weil-extension-by-zero] $j_!$, set

$$
 Rf_{!,n}^{c}=R\bar f_{*}\,j_!:
 D(X_{\mathrm{proet}},\Lambda)
 \longrightarrow D(Y_{\mathrm{proet}},\Lambda),
$$

a functor attached to the chosen compactification $c$. Here $R\bar f_{*}$ is
computed by a K-injective resolution and $j_!$ is exact, so it is applied
termwise. Let $\mathcal D^{+}_{\mathrm{et}}(X,\Lambda)\subseteq
D(X_{\mathrm{proet}},\Lambda)$ be the full subcategory of complexes that are
bounded below of étale origin [def-weil-pbc-etale-origin-witness]; it
contains the finite-torsion constructible complexes of
[def-weil-finite-torsion-constructibility]. The *compact-support candidate*
attached to $c$ is the restriction of $Rf^c_{!,n}$ to
$\mathcal D^{+}_{\mathrm{et}}(X,\Lambda)$. On
$\mathcal D^{+}_{\mathrm{et}}(X,\Lambda)$ the superscript $c$ may be dropped.
