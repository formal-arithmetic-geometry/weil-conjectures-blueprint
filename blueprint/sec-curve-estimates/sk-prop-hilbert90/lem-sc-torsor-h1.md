+++
id = "lem-sc-torsor-h1"
kind = "lemma"
title = "First cohomology classifies torsors"
order = 886
uses = ["def-sc-gm-torsor", "lem-sc-ext-torsor"]
+++
Let $X$ be a scheme (for instance a curve $C$ as in
[def-sc-curves]) and $G$ a sheaf of
abelian groups on $X_{\Et}$. There is a canonical bijection

$$
H^1(X_{\Et},G)\cong\{\text{isomorphism classes of }G\text{-torsors}\}
$$

(torsors as in [def-sc-gm-torsor]), under which the group law of
$H^1$ corresponds to the contracted product
$(T,T')\mapsto T\wedge T':=(T\times T')/G$ (antidiagonal action) and
$0$ to the trivial torsor $G$. The same holds, with the same proof,
for an abelian sheaf on the Zariski site $X_{\mathrm{Zar}}$.
