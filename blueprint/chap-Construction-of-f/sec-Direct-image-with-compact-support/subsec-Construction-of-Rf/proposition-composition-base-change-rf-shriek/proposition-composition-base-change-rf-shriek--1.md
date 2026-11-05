+++
id = "proposition-composition-base-change-rf-shriek--1"
kind = "proposition"
title = "Composition isomorphism"
order = 516002
aliases = ["bp-r157-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicIntegers", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_comp"]
uses = ["proposition-construction-independence-rf-shriek", "definition-constructible-sheaves", "definition-compactification-refinement"]
+++
For $k$-morphisms $X\xrightarrow fY\xrightarrow gZ$ in the shared context,
and $\Lambda=\Qbarl$ or $\Lambda=\Oe$, there is a specified natural isomorphism
$$
C_{f,g}:R(gf)_{!,\Lambda}\xrightarrow{\sim}Rg_{!,\Lambda}Rf_{!,\Lambda}
$$
on $\Dbc(X_{\mathrm{pro}\acute{e}t},\Lambda)$. It is constructed from the
compactification comparisons of
[proposition-construction-independence-rf-shriek].

For finite coefficients there is also the following étale statement. Let
$\Lambda$ be a finite commutative ring and let $X\xrightarrow fY\xrightarrow gZ$
be morphisms of arbitrary schemes such that $f$, $g$ and $gf$ admit
factorizations as an open immersion followed by a proper morphism; the open
immersions need not be quasi-compact. There exists a natural isomorphism
$R(gf)_{!,\Lambda}\simeq Rg_{!,\Lambda}Rf_{!,\Lambda}$ on the unbounded category
$D(X_{\mathrm{\acute{e}t}},\Lambda)$. This existence statement does not specify
associativity or unit equations.
