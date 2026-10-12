+++
kind  = "proof"
of    = "lem-weil-pbc-constructible-noetherian-finite-selection"
+++
Choose the finite partition of [lem-weil-pbc-irreducible-lisse-strata], and a
geometric generic point $\bar\eta_i$ of each $S_i$. The group
$F_{\bar\eta_i}$ is finite. For each of its nonzero elements choose one
$\phi_\lambda$ detecting it, and let $L_i$ be the resulting finite set of
indices. The map

$$
 F|_{S_i}\longrightarrow
 \bigoplus_{\lambda\in L_i}G_\lambda|_{S_i}
$$

is injective at $\bar\eta_i$, hence is a monomorphism on all of $S_i$ by
[lem-weil-pbc-lisse-generic-kernel]. Take $L_0=\bigcup_iL_i$. At any geometric
point of $X$, projection to the summands indexed by its stratum's $L_i$ shows
that the $L_0$-map is injective. Exactness of the geometric stalk functors
makes every stalk of its kernel zero; conservativity of geometric stalks then
makes the kernel zero. No finiteness or constructibility of the target sheaves
is needed.
