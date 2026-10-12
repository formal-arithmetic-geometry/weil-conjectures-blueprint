+++
kind  = "proof"
of    = "lem-kun-hocolim-truncations"
+++
By [lem-kun-complex-colimit-hocolim] the homotopy colimit is
computed by the termwise colimit of the complexes
$\tau_{\le N}E$, and cohomology commutes with termwise filtered
colimits of complexes. For each fixed $q$ one has
$\mathcal H^q(\tau_{\le N}E)=\mathcal H^q(E)$ for all $N\ge q$ by
[def-kun-truncations], so
$\mathcal H^q(\operatorname{hocolim}_N\tau_{\le N}E) =\varinjlim_N\mathcal H^q(\tau_{\le N}E)=\mathcal H^q(E)$. As this
holds for every $q$, the canonical morphism is a quasi-isomorphism,
hence an isomorphism of the derived category by
[def-weil-pbc-derived-categories].
