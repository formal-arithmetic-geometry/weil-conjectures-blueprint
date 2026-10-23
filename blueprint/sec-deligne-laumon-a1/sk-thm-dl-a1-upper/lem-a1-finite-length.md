+++
id = "lem-a1-finite-length"
kind = "lemma"
title = "Finite length of a lisse Weil sheaf on a curve"
lean = ["AlgebraicGeometry.WeilSheaf.IsLisse.induction_on_shortExact"]
order = 4021
uses = ["sk-lem-coefficient-heart", "def-weil-weil-sheaf-complex", "sk-def-sf-weil-complexes"]
+++
Let $C_0$ be a smooth geometrically connected curve and let
$\mathcal F$ be a lisse $\Qlb$-Weil sheaf
on $C_0$: a lisse $\overline{\mathbf Q}_{\ell,C}$-module on $C_{\mathrm{proét}}$
([sk-lem-coefficient-heart]) with a Weil structure ([sk-def-sf-weil-complexes],
[def-weil-weil-sheaf-complex]). Then
$\mathcal F$ has finite length in the category of lisse Weil sheaves:
there is a finite Frobenius-stable filtration

$$
0=\mathcal F_0\subset\mathcal F_1\subset\cdots\subset\mathcal F_m=\mathcal F
$$

with each graded piece $\mathcal F_r/\mathcal F_{r-1}$ irreducible
(with respect to the Weil-sheaf structure).
