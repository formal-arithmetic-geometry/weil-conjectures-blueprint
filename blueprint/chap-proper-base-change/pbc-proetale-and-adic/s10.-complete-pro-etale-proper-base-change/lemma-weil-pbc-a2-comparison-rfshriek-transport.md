+++
id = "lemma-weil-pbc-a2-comparison-rfshriek-transport"
kind = "lemma"
title = "Site-comparison and exceptional-image transport to A2"
order = 1908
uses = ["def-weil-pbc-a2-constructible-rebind", "def-weil-pbc-epsilon-comparison", "def-weil-pbc-projection-compactification", "lemma-weil-pbc-epsilon-direct-image", "lemma-weil-pbc-epsilon-pullback", "lemma-weil-pbc-projection-formula-identity-compactification"]
+++
Under the identity-on-objects site functor of S8, the A2 notation
$\nu_Z^*$ is the functor $\epsilon_Z^{-1}$. The A2 pullback comparison
$c_g$, direct-image comparison $d_f$, and etale-origin isomorphism therefore
transport to the S8 maps with the same components. Moreover the A1 typed
input category $\mathcal D_n(Z)$ transports by the identity on objects and
morphisms to $\mathsf C_n(Z)$, and on a proper map

$$
Rf_!^{(1,f)}=Rf_*:\mathsf C_n(X)\longrightarrow\mathsf C_n(Y).
$$

Thus the $Rf_!$ field of the A2 six-operation target has exactly the displayed
source and target on $\mathsf C_\square(X)$. These transports are independent
of whether the A1, A2, S8, or S9 alias is used.

## Proof

Both $\nu_Z$ and $\epsilon_Z$ are the geometric morphism induced by the
functor that sends an etale object to the same object of the pro-etale site.
Their inverse images are the same sheafified left Kan extension, so the
identity of the indexing categories identifies them. Expanding $c_g$ gives
the S8 pullback square, and expanding $d_f$ gives the S8 unit followed by the
same derived direct image. The component formulas and their naturality
squares are therefore literally equal, not merely abstractly isomorphic.

A1 denoted by $\mathcal D_n(Z)$ the typed finite torsion constructible
category whose construction was assigned to A2. A2 realizes that input as
the full subcategory defined by its finite-torsion constructibility witness.
Consequently the transport functor and its inverse are both the identity on
underlying complexes and maps; their two composites are definitional
identities. The selected A1 exceptional image is $Rp_*j_!$. This is the S9
definition of $Rf_!^{(j,p)}$. When $f$ is proper, the selected
compactification is $(1_X,f)$, so $j_!=1$ and both expressions are $Rf_*$.
The identity-compactification lemma shows that the projection-formula arrows
also agree. Since all transports are identities on representatives, changing
only the displayed alias cannot change an object, a morphism, or a coherence
equation.

Unresolved dependencies: def:weil-a1-rfshriek-selected, def:weil-a1-torsion-derived-category, def:weil-a2-etale-origin-datum, def:weil-a2-etale-proetale-direct-image-comparison, def:weil-a2-etale-proetale-pullback-comparison, def:weil-a2-six-operation-coefficient-target
