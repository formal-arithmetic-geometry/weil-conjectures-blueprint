+++
id = "lem-weil-pbc-constant-pullback-unit-continuous-map"
kind = "lemma"
title = "Constant pullback unit on continuous maps"
uses = ["def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lemma-constructible-pullback-constant"]
lean = ["AlgebraicGeometry.Etale.constant_pullback_unit_continuousMap"]
+++
Let $i:Y_0\to Y$ be a morphism of schemes [def-weil-pbc-scheme-conventions], and let $M$ be an abelian group with the discrete topology. For $W\in Y_{\acute et}$ and $g\in\underline M_Y(W)$ `CategoryTheory.constantSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/ConstantSheaf.lean)), let $\lambda_Y(g):|W|\to M$ be the continuous-map representative of $g$, let $\eta(g)\in (i_*i^*\underline M_Y)(W)$ be the inverse-image adjunction unit [def-weil-pbc-inverse-image], and let $c:i^*\underline M_Y\cong\underline M_{Y_0}$ be the constant-sheaf comparison [lemma-constructible-pullback-constant]. Then $\lambda_{Y_0}(c(\eta(g)))=\lambda_Y(g)\circ|\operatorname{pr}_1|$ as continuous maps $|W\times_Y Y_0|\to M$. There is no finiteness hypothesis on $M$.
