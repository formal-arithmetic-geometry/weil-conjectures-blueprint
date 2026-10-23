+++
id = "lem-weil-pbc-pullback-preserves-bounded-constructible"
kind = "lemma"
title = "Pullback preserves bounded constructibility"
order = 1054
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_leftDerivedFunctor_upperStar_obj", "AlgebraicGeometry.ProEtale.DerivedCategory.boundedConstructible.mapDerivedCategory_upperStar", "AlgebraicGeometry.Etale.boundedConstructible_leftDerivedUpperStar"]
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-operations", "lem-weil-pbc-comparison-pullback", "prop-weil-pbc-inverse-image-exact"]
+++
Let $\Lambda$ be a finite commutative ring and $g:V'\to V$ a morphism of
schemes. Write $\Dbc(V_{\Proet},\Lambda)$ for the bounded constructible
complexes of [def-weil-pbc-proetale-modules], the pullbacks of the bounded
constructible etale complexes of [def-weil-pbc-constructible-complexes]. The
derived pullback $Lg^*=g^{-1}$ restricts to an
exact triangulated functor
$$
 Lg^*:\Dbc(V_{\Proet},\Lambda)\longrightarrow\Dbc(V'_{\Proet},\Lambda),
$$
and carries the class of objects with cohomology in $[a,b]$ into the same
class.
