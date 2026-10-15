+++
kind = "proof"
of = "det-cor-int-compactness-ii-extension-zero"
+++
(1) $j_!$ is left adjoint to $j^*$, hence preserves direct sums (colimits).
It is exact and preserves all limits (Stacks, Tag 09BP); in particular it
commutes with $R\varprojlim$. Being exact and $\mathcal O_E$-linear, it
commutes with the cone of multiplication by $\pi_E^n$, i.e. with reduction
modulo $\pi_E^n$.

(2) Let $K\in\Dbc(U,\mathcal O_E)$. By (1), $j_!K$ is derived complete
(it is $j_!R\varprojlim_nK_n=R\varprojlim_nj_!K_n$) and its reduction is
$j_!(K\otimes^{\mathbf L}\mathcal O_E/\pi_E)$, the extension by zero of a bounded
constructible torsion complex, which is bounded constructible. So
$j_!K\in\Dbc(X,\mathcal O_E)$; this is [sk-lem-int-tensor]
(compare [lem-sfb-dc-open-lower-shriek-preserves]).

(3) The full subcategory of $K\in\Loc(\Dbc(U,\mathcal O_E))$ with
$j_!K\in\Loc(\Dbc(X,\mathcal O_E))$ is closed under shifts and cones (as $j_!$
is exact) and under direct sums (as $j_!$ preserves them), so it is localizing;
by (2) it contains $\Dbc(U,\mathcal O_E)$, hence it is everything.
