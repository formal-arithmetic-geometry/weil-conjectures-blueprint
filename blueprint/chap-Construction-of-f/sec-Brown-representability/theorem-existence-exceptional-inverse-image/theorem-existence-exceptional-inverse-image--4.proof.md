+++
kind = "proof"
of = "theorem-existence-exceptional-inverse-image--4"
order = 526009
uses = ["lemma-hypotheses-brown-representability--3"]
+++
To see that $f^!$ preserves direct sums, we test the canonical map
$\bigoplus_\alpha f^!N_\alpha\to f^!(\bigoplus_\alpha N_\alpha)$
on a compact generator $G\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and its shifts.
On the source, compactness of $G$ and adjunction give

$$
\Hom\Bigl(G[n],\bigoplus_\alpha f^!N_\alpha\Bigr)
=\bigoplus_\alpha\Hom(G[n],f^!N_\alpha)
=\bigoplus_\alpha\Hom(Rf_!G[n],N_\alpha).
$$

On the target, adjunction and compactness of $Rf_!G\in D^b_{\mathrm{ctf}}(Y,\Lambda)$
give the same group. The map therefore induces bijections on
$\Hom(G[n],-)$ for all compact generators $G$ and all $n$. Applying the
detection property to its cone, we see that it is an isomorphism.

*Source:* the proof of Theorem [theorem-existence-exceptional-inverse-image].
