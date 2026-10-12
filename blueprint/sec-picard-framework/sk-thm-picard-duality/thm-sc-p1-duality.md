+++
id = "thm-sc-p1-duality"
kind = "theorem"
title = "Duality on the projective line"
order = 702
uses = ["def-sc-ext-sheaf", "def-sc-kahler-differentials", "def-sc-p1-standard", "lem-pc-projective-space-serre-pairing", "lem-sc-ext-locally-free", "lem-sc-four-lemma", "lem-sc-p1-graded-resolution", "lem-sc-p1-hi-vanishing", "lem-sc-p1-monomial", "lem-sc-p1-twist-exists"]
+++
Let $k$ be an algebraically closed field. For every coherent
$\mathcal O_{\mathbf P^1_k}$-module $\mathcal G$, with

$$
\omega_{\mathbf P^1}:=\Omega^1_{\mathbf P^1_k/k}\cong\mathcal O(-2)
$$

([def-sc-kahler-differentials],
[lem-sc-p1-monomial](iii)), there are canonical isomorphisms

$$
H^1(\mathbf P^1_k,\mathcal G)^{\vee}\;\cong\;
\operatorname{Hom}_{\mathcal O_{\mathbf P^1}}\bigl(\mathcal G,
\omega_{\mathbf P^1}\bigr),
$$

$$
H^0(\mathbf P^1_k,\mathcal G)^{\vee}\;\cong\;
\operatorname{Ext}^1_{\mathbf P^1}\bigl(\mathcal G,
\omega_{\mathbf P^1}\bigr)
$$

(with $\operatorname{Ext}$ of [def-sc-ext-sheaf]; all groups
involved are finite-dimensional, the cohomology of coherent modules
on a proper scheme over a field being finite-dimensional).
