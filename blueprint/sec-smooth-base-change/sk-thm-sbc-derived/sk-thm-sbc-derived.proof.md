+++
kind = "proof"
of = "sk-thm-sbc-derived"
uses = ["sk-thm-smooth-base-change", "sk-lem-sbc-exchange-compatibility", "sk-thm-pe-direct-image-comparison", "sk-cor-pe-classical-derived"]
+++
For a classical sheaf the assertion is
[sk-thm-smooth-base-change], applied to the underlying
abelian sheaf, which is killed by $n$. The exchange map is
$\Lambda$-linear by its unit–counit construction, so it is an
isomorphism of $\Lambda$-module sheaves.

For a complex, choose $a$ with $K\in D^{\geq a}$. The hypercohomology
spectral sequences of the two sides have terms

$$
 g^*R^pf_*H^q(K),\qquad R^pf'_*u^*H^q(K),
 \qquad p\geq0,\quad q\geq a,
$$

and the exchange map induces on them the sheaf comparison, an
isomorphism by the preceding paragraph. In each total degree only
finitely many pairs $(p,q)$ occur, so these shifted first-quadrant
spectral sequences converge and the map on abutments is an isomorphism;
alternatively, truncate $K$ above the relevant total degree first. Finally,
[sk-thm-pe-direct-image-comparison] and
[sk-cor-pe-classical-derived] show that the direct and inverse
images involved are classical, and
[sk-lem-sbc-exchange-compatibility] identifies the comparison with
the exchange map $\operatorname{Ex}_{g,f}(K)$.

*Complement.* Each of the three étale statements is reduced to the degreewise statement of
[sk-thm-smooth-base-change] by a finite-range comparison and a truncation criterion.
