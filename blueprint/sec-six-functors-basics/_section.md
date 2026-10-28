+++
id = "sec-six-functors-basics"
kind = "section"
title = "Six Functors: Basic Constructions"
order = 2227
uses = ["sec-nagata-compactification", "sec-proper-base-change", "sec-smooth-base-change"]
+++
**Content.** This section is §§5–9 of the tex, together with the main theorem
([sk-thm-existence]), which the tex states in §3 and proves in §9, and the
cohomological-dimension facts of §2 that the unbounded finite-coefficient arguments
need ([sk-def-cd], [sk-lem-base-field-cd], [sk-prop-pe-unbounded-classical]). The
coefficient ring $\Lambda$ is admissible: a finite $\ell$-primary ring $A$, or
$\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\Qlb$, and $\Dctf=\Dbc$ in the
$\ell$-adic cases.

The route follows the tex.
- *Constructible sheaves and reduction to finite coefficients* (§5): lattices and descent
  to a finite $E$ ([sk-lem-lattice-atlas], [sk-lem-lisse-finite-descent],
  [sk-thm-sfb-qlbar-two-colimit]), the abelian category of constructible sheaves
  ([sk-lem-coefficient-heart]), continuity of Ext, integral models
  ([sk-lem-integral-models]), and proper direct image of constructible complexes
  ([sk-thm-sfb-proper-base-change]).
- *Construction of the exceptional inverse image* (§6): compactness of constructible
  complexes ([sk-thm-constructible-compactness], [sk-prop-ctf-finite-compact],
  [sk-prop-int-compactness]), $Rf_!=Rp_*j_!$ and its independence of the
  compactification ([sk-prop-sf-comp-coherence]), and $f^!$ by Brown representability
  for every admissible $\Lambda$ ([sk-prop-sf-existence]).
- *$f^!$ preserves constructibility* (§7–§8): the cycle class and the projective line,
  the smooth case ([sk-prop-cohsm]), generic constructibility of $Rj_*$
  ([sk-thm-geo-generic-open]), and the restriction theorems for finite coefficients
  ([sk-prop-sf-rf-shriek-preservation]) and $\ell$-adic coefficients
  ([sk-thm-restriction]).
- *The six functors on $\Dctf$* (§9): [sk-thm-sf-ctf-stability], change of coefficients
  ([sk-prop-scalar-six]), $\Dctf(X,\Qlb)$ as a 2-colimit ([sk-prop-qlbar-two-colimit]),
  and reduction of isomorphisms to finite coefficients ([sk-prop-reduction-to-finite]).

Smooth base change for all admissible coefficients ([sk-thm-sbc-coefficients]) sits
here because it uses §9.
