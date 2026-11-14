+++
kind = "proof"
of = "dag-sk-thm-pe-indetale-refinement"
tags = ["sheaf-dag"]
+++
1. *The local rigidity argument.* The simultaneous strict-localization construction for the
pair $R\to B$ gives compatible ind-étale refinements $R\to C$ and $B\to D$, with both
spectra w-local and with closed points of $D$ mapping to closed points of $C$
(`def-weil-pbc-weak-etale-refinement`, built from the first stage of
[dag-sk-thm-pe-wc-cover]). The map $C\to D$ is still weakly étale by
`sk-lem-pe-weakly-etale-stability`, and the local rings of $C$ at closed points are
strictly henselian. Olivier's rigidity theorem says that a weakly étale local map out of a
strictly henselian local ring is an isomorphism (`thm-weil-pbc-weak-etale-strict-local`;
Stacks, Tag 092Z). Applied at closed points, and then at their generalizations, it shows
that $C\to D$ identifies local rings. The ind-Zariski refinement theorem for maps
identifying local rings (`lem-weil-pbc-local-rings-ind-zariski`) now gives a faithfully flat
ind-Zariski $D\to D'$ such that $C\to D'$ is ind-Zariski. Taking $B'=D'$ proves the
assertion (`thm-weil-pbc-weak-etale-refinement`). See Stacks, Tag 097Z for the compatible
refinement and the proof. (uses `def-weil-pbc-weak-etale-refinement`, `sk-thm-pe-wc-cover`, `sk-lem-pe-weakly-etale-stability`, `thm-weil-pbc-weak-etale-strict-local`, `lem-weil-pbc-local-rings-ind-zariski`, `thm-weil-pbc-weak-etale-refinement`)

Proof dependencies not drawn: `def-weil-pbc-weak-etale-refinement`, `sk-thm-pe-wc-cover`, `sk-lem-pe-weakly-etale-stability`, `thm-weil-pbc-weak-etale-strict-local`, `lem-weil-pbc-local-rings-ind-zariski`, `thm-weil-pbc-weak-etale-refinement`.
