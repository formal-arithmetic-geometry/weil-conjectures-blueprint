+++
id = "lem-wf-constant-twist-cohomology"
kind = "lemma"
title = "Projection formula for a constant twist"
lean = ["AlgebraicGeometry.WeilSheaf.nonempty_higherLowerShriek_constantTwist_iso"]
order = 4225
uses = ["def-weil-pbc-scheme-conventions", "def-wf-constant-weil-twist", "fix-prop-projection-formula"]
+++
In the setting of [def-wf-constant-weil-twist], let
$h:X_0\to Y_0$ be a
separated finite-type
morphism of separated finite-type $k_0$-schemes, let
$\mathcal K$ be a constructible $\Qlb$-Weil complex on $X_0$, and
let $\mathcal B_b$ be the
constant Weil twist on $Y_0$.
There is a Frobenius-compatible isomorphism

$$
Rh_!\bigl(\mathcal K\otimes h^*\mathcal B_b\bigr)
\;\cong\;Rh_!\mathcal K\otimes\mathcal B_b.
$$
