+++
id = "thm-galois-torsor-h1"
kind = "theorem"
title = "Torsors and first etale cohomology"
lean = ["CategoryTheory.Sheaf.Torsor.lifts", "CategoryTheory.Sheaf.Torsor.lifts_equiv_lifts_add", "CategoryTheory.Sheaf.Torsor.exists_hom_app_eq_sub_of_lifts_equiv", "CategoryTheory.Sheaf.Torsor.exists_equiv_lifts", "CategoryTheory.Sheaf.Torsor.classH1", "CategoryTheory.Sheaf.Torsor.classH1_lifts", "CategoryTheory.Sheaf.Torsor.exists_quotientEquiv_H_one"]
order = 2108
uses = ["def-galois-categories", "def-weil-pbc-etale-cohomology", "def-weil-pbc-finite-torsors", "lem-galois-flasque", "thm-galois-lc-etale"]
+++
In the situation of [def-galois-categories], let $M$ be a finite
abelian group. Then the construction below is a canonical bijection

$$
\operatorname{Tor}^1(Y,M)\xrightarrow{\ \sim\ }H^1(Y_{\Et},\underline M),
$$

natural in $(Y,M)$.
