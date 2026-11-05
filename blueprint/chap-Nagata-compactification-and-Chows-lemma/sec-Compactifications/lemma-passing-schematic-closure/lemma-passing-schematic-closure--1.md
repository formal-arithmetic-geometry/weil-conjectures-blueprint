+++
id = "lemma-passing-schematic-closure--1"
kind = "lemma"
title = "Extension by zero along a proper refinement"
name_showing = false
order = 1412001
aliases = ["bp-r437-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward_padicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward_padicIntegers"]
uses = ["definition-constructible-sheaves", "lemma-inverse-image-coefficient-sheaves", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Lean uses the following comparison along a proper refinement in place of
a separate schematic-closure statement.

Let $\ell$ be prime and let $k$ be a field of characteristic $p>0$ with
$p\ne\ell$. Let $X,Z,\overline X$ be separated schemes of finite type over
$k$, with open immersions $j':X\hookrightarrow Z$ and
$j:X\hookrightarrow\overline X$ and a proper $k$-morphism
$h:Z\to\overline X$. Suppose that $h\circ j'=j$ and that the resulting
square with top map $\mathrm{id}_X$ is cartesian, so that $h^{-1}(X)=X$
under the specified identifications.

Let $E\subset\Qbarl$ be a finite extension of $\Ql$. Take
$\Lambda=E$, $\Qbarl$, or $\mathcal O_E$, regarded as a condensed ring,
and use the pullbacks $\Lambda_T$ as coefficients on each scheme $T$.
For every $K\in\Dbc(X,\Lambda)$, the canonical comparison

$$
\rho_K:j_!K\longrightarrow Rh_*j'_!K
$$

is an isomorphism, natural in $K$. It is the unit of
$Lh^*\dashv Rh_*$ followed by the inverse of the restriction comparison
$j'_!K\simeq Lh^*j_!K$. No density hypothesis on either open immersion
is needed.
