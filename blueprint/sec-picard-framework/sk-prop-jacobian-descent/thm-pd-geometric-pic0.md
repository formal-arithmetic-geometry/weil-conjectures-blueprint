+++
id = "thm-pd-geometric-pic0"
kind = "theorem"
title = "The degree-zero Picard functor over a separable closure"
lean = ["AlgebraicGeometry.exists_jacobian_pullback"]
order = 886
uses = ["def-pc-genus", "def-pc-geometrically-irreducible", "def-pc-smooth-projective-curve", "def-pd-degree-morphism", "def-pd-separable-closure", "def-sc-abelian-variety", "def-sc-jacobian", "def-sc-pic0", "lem-pd-geometric-curve", "thm-sc-jacobian-representability", "thm-sc-theorem-of-the-base"]
+++
Let $k$ be a field, let $C$ be a
smooth projective curve over $k$
which is geometrically integral,
of genus $g$ ([def-pc-genus]), and let $k_s$ be a
separable closure of $k$. Then the
degree-zero part
$\operatorname{Pic}^0_{C_{k_s}/k_s}$ is representable, and the representing
object $J_s$ is an abelian variety over
$k_s$ of dimension $g$; moreover $J_s(k_s)=\operatorname{Pic}^0(C_{k_s})$
under the canonical identification of [def-sc-pic0].
