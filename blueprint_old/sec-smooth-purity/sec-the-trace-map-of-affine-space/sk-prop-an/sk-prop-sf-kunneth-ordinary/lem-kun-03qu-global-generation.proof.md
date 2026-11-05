+++
kind  = "proof"
of    = "lem-kun-03qu-global-generation"
+++
By the argument of [lem-kun-03qu-sep-closed] (every etale
$K$-scheme is a disjoint union of copies of $\Spec K$, and the
identity point is terminal among the pointed etale neighbourhoods of
itself), the stalk of $F$ at every geometric point equals
$\Gamma(\Spec K_{\Et},F)$. The evaluation morphism
$\bigoplus_{s\in\Gamma(\Spec K_{\Et},F)}\underline{\mathbf Z}\to F$
of [def-kun-global-generated] therefore has, at every geometric
point, the stalk
$\bigoplus_{s\in\Gamma(\Spec K_{\Et},F)}\mathbf Z\to \Gamma(\Spec K_{\Et},F)$, the canonical surjection; it is thus
surjective on every geometric stalk, hence an epimorphism of sheaves
because the stalk functors are exact
([prop-weil-pbc-geometric-stalks-exact]) and conservative
([lemma-weil-pbc-geometric-stalk-conservative]). Hence $F$ is
globally generated.
