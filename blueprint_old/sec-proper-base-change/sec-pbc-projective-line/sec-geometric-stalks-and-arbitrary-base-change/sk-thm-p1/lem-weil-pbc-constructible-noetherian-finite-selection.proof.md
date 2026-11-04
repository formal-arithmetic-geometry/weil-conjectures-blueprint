+++
kind  = "proof"
of    = "lem-weil-pbc-constructible-noetherian-finite-selection"
uses  = ["lem-weil-pbc-irreducible-lisse-strata", "lem-weil-pbc-lisse-generic-kernel"]
+++
Choose the finite partition of [lem-weil-pbc-irreducible-lisse-strata], and for each $S_i$
the geometric point $\bar\eta_i$ over its generic point given by an algebraic
closure of the residue field. The module
$F_{\bar\eta_i}$ is finite ($\Lambda$ being finite and the stalks finitely generated). For each of its nonzero elements choose one
$\phi_\lambda$ detecting it, and let $L_i$ be the resulting finite set of
indices. The map

$$
 F|_{S_i}\longrightarrow
 \bigoplus_{\lambda\in L_i}G_\lambda|_{S_i}
$$

is injective at $\bar\eta_i$, hence is a monomorphism on all of $S_i$ by
[lem-weil-pbc-lisse-generic-kernel]. Take $L_0=\bigcup_iL_i$. At the geometric
point $\bar x$ of every point of $X$, projection to the summands indexed by its stratum's $L_i$ shows
that the $L_0$-map is injective. Exactness of the geometric stalk functors
makes every stalk of its kernel zero; conservativity of geometric stalks then
makes the kernel zero. No finiteness or constructibility of the target sheaves
is needed.
