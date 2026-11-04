+++
kind = "proof"
of = "lemma-projection-formula-integral-coefficients"
order = 607
uses = ["proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-compactness-proper-direct-image", "lemma-checking-isomorphisms-constructible-complexes"]
+++
On $\Dbc$ this is Proposition [proposition-proper-direct-image-constructible-complexes], and we
extend it by checking one variable at a time. Both sides make sense, since
$M\otimes^{\mathbf L}p^*N$ lies in $\Loc(D^b_{\mathrm{ctf}}(X,\mathcal O_E))$. For $M$
and $N$ in $\Dbc$ this is Lemma [lemma-inverse-image-tensor-product].
The tensor product commutes with direct sums and cones in each variable.
Hence the argument of
Proposition [proposition-projection-formula-rational-coefficients]
extends it first to all $M$ and then to all $N$. In each variable, with the
other fixed, both sides are exact and preserve direct sums. For the
variable $M$ this holds because $Rp_*$ preserves direct sums
(Proposition [proposition-compactness-proper-direct-image]).
Lemma [lemma-checking-isomorphisms-constructible-complexes], applied
first in $M$ and then in $N$, now extends the isomorphism to the
localizing categories.
