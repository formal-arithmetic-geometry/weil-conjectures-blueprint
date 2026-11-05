+++
kind = "proof"
of = "lemma-projection-formula-integral-coefficients"
order = 613
uses = ["lemma-stability", "proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves", "definition-lisse-sheaves", "definition-pro-etale-base-change-map", "lemma-proper-direct-image-unbounded-complexes", "lemma-inverse-image-tensor-product", "proposition-proper-direct-image-extension-zero", "lemma-checking-isomorphisms-constructible-complexes"]
+++
On $\Dbc$ this is Proposition [proposition-proper-direct-image-constructible-complexes]. Both sides make sense on the localizing categories, because
$M\otimes^{\mathbf L}p^*N$ lies in $\Loc(D^b_{\mathrm{ctf}}(X,\mathcal O_E))$. For $M$ and $N$ in $\Dbc$ this is Lemma [lemma-inverse-image-tensor-product], and since the tensor product commutes with direct sums and cones in each variable, the argument of
Proposition [proposition-projection-formula-rational-coefficients]
extends it to the localizing categories. Indeed, fix one variable. Both sides are then exact and preserve direct sums in the other; for the variable $M$ this holds because $Rp_*$ preserves direct sums
(Proposition [proposition-compactness-proper-direct-image]).
Therefore Lemma [lemma-checking-isomorphisms-constructible-complexes], applied first in $M$ and then in $N$, extends the isomorphism from $\Dbc$ to the
localizing categories.
