+++
kind = "proof"
of = "det-thm-sf-pf-adic-projection"
+++
(1) By [sk-lem-int-tensor], $K\otimes^{\mathbf L}p^*L$ and
$Rp_*K\otimes^{\mathbf L}L$ are in $\Dbc$ (pullback and tensor product preserve
integral constructibility, and $Rp_*K\in\Dbc(Y,\mathcal O_E)$ by proper
finiteness, [sk-prop-int-compactness]); in particular both sides are derived
complete. Reduction modulo $\pi_E$ is exact, monoidal and commutes with $p^*$
and $Rp_*$, so it carries the map to the torsion projection formula map for
$K/\pi_E$ and $L/\pi_E$ in $D(Y_{\mathrm{proét}},\mathbf F_E)$, an isomorphism by
Stacks, Tag 0F0G. The cone $C$ of the map is derived complete with
$C\otimes^{\mathbf L}\mathbf F_E=0$, hence $C=0$ by derived Nakayama
([sk-lem-pe-derived-nakayama]). This is the integral case of
[sk-thm-sfb-proper-base-change].

(2) *Tensor closure.* Fix $B\in\Dbc(X,\mathcal O_E)$; the objects $A$ of
$\Loc(\Dbc(X,\mathcal O_E))$ with $A\otimes^{\mathbf L}B\in\Loc(\Dbc(X,\mathcal O_E))$
form a localizing subcategory ($-\otimes^{\mathbf L}B$ is exact and preserves
direct sums) which contains $\Dbc$ by [sk-lem-int-tensor],
hence everything; then fix $A$ and argue in $B$. *Extension.* $Rp_*$
preserves the localizing categories and direct sums there
([sk-prop-int-compactness]). Fix $L\in\Dbc(Y,\mathcal O_E)$: both sides are
exact, direct-sum preserving functors of $K$, isomorphic on $\Dbc$ by (1),
hence isomorphic on $\Loc(\Dbc(X,\mathcal O_E))$ ([sk-lem-sf-determination]).
Then fix $K$ and argue in the same way in $L$.
