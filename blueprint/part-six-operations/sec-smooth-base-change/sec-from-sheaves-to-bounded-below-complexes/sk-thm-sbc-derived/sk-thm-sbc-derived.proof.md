+++
kind = "proof"
of = "sk-thm-sbc-derived"
uses = ["sk-thm-smooth-base-change", "sk-lem-sbc-exchange-compatibility", "sk-thm-pe-direct-image-comparison", "sk-cor-pe-classical-derived"]
+++
For a classical sheaf the assertion is
Theorem [sk-thm-smooth-base-change], applied to the underlying
abelian sheaf, which is killed by $n$. Since the base change map is
constructed from units and counits, it is $\Lambda$-linear, and so it is an
isomorphism of $\Lambda$-module sheaves.

For a complex, choose an integer $m$ with $K\in D^{\geq m}$. The hypercohomology
spectral sequences of the two sides have terms

$$
g^*R^pf_*H^q(K),\qquad R^pf'_*g'^*H^q(K),
\qquad p\geq0,\quad q\geq m,
$$

and the base change map induces on them the comparison for sheaves, which is an
isomorphism by the preceding paragraph. Since in each total degree only
finitely many pairs $(p,q)$ occur, these shifted first quadrant
spectral sequences converge, and a map of convergent spectral sequences
that is an isomorphism on $E_2$ is an isomorphism on abutments. Finally,
Theorem [sk-thm-pe-direct-image-comparison] and
Corollary [sk-cor-pe-classical-derived] show that the direct and inverse
images involved are classical, and
Lemma [sk-lem-sbc-exchange-compatibility] identifies the comparison with
(9.2).
