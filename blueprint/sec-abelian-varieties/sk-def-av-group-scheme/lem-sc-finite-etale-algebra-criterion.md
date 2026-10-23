+++
id = "lem-sc-finite-etale-algebra-criterion"
kind = "lemma"
title = "Finite étale group schemes and finite étale algebras"
lean = ["Algebra.Etale.iff_subsingleton_kaehlerDifferential_of_field", "AlgebraicGeometry.etale_SpecMap_algebraMap_tfae", "AlgebraicGeometry.Scheme.Hom.etale_iff_etale_\u0393Algebra_of_isFinite"]
order = 450
uses = ["def-sc-group-scheme", "def-weil-pbc-scheme-conventions"]
+++
Let $k$ be a field and $A$ a finite $k$-algebra. Then
$\Spec A\to\Spec k$ is étale (in the sense of
[def-weil-pbc-scheme-conventions]) if and only if $\Omega_{A/k}=0$,
if and only if $A$ is a finite étale $k$-algebra, i.e. a finite
product of finite separable field extensions of $k$. In particular a
finite $k$-group scheme $G$ ([def-sc-group-scheme]) is étale over $k$
if and only if $\Gamma(G,\mathcal O_G)$ is a finite étale $k$-algebra.
