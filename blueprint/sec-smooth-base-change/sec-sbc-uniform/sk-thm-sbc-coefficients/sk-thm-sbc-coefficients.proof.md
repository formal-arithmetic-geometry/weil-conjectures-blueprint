+++
kind = "proof"
of = "sk-thm-sbc-coefficients"
uses = ["sk-thm-sf-ctf-stability", "sk-thm-pe-constructible-comparison", "sk-thm-sbc-derived", "sk-lem-sbc-exchange-compatibility", "sk-prop-reduction-to-finite"]
+++
By Proposition [sk-thm-sf-ctf-stability], both sides lie in
$D^b_{\mathrm{ctf}}(Y',\Lambda)$. It remains to show that the canonical map
(9.2) is invertible for each kind of coefficient ring.

*Finite rings $A$.* By Theorem [sk-thm-pe-constructible-comparison], constructible
pro-étale sheaves with discrete Noetherian coefficients are
classical, and so $K$ is a bounded classical complex. Since $A$ is
killed by a power of $\ell$, which is invertible on $Y$, smooth base change
for torsion complexes (Theorem [sk-thm-sbc-derived]) applies to $K$.

*Other rings.* The base change map is built from units and counits, so it
commutes with change of coefficients (Lemma [sk-lem-sbc-exchange-compatibility]).
Proposition [sk-prop-reduction-to-finite] therefore extends the finite case
to every admissible $\Lambda$.

Finally, compatibility with pasting and with change of coefficients holds for
the base change map (9.2) itself by Lemma [sk-lem-sbc-exchange-compatibility],
and hence also for the isomorphisms.
