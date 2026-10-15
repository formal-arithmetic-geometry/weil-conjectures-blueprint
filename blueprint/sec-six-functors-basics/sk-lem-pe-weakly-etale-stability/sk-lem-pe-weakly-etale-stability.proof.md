+++
kind = "proof"
of = "sk-lem-pe-weakly-etale-stability"
+++
Base change preserves flatness of a morphism and its diagonal. For a composite
$V\to U\to X$, the diagonal factors through $V\times_UV\to V\times_XV$, which is a base
change of $\Delta_{U/X}$; this gives the assertion about composites.

For an $X$-map $h\colon U\to V$, the graph $U\to U\times_XV$ is a base change of the flat
diagonal of $V/X$, and the projection $U\times_XV\to V$ is flat because $U/X$ is flat.
Their composite is $h$, while $\Delta_h$ is a base change of $\Delta_{U/X}$. Zariski
locality follows from locality of flatness.

For ind-étale rings, tensor products commute with filtered colimits, and finite
presentation lets one choose a finite stage for each étale algebra; this gives base change
and transitivity. The same arguments show that a filtered colimit of étale algebras has
flat multiplication map (Stacks, Tag 092A). The ring-theoretic statements are
[lem-weil-pbc-ind-etale-stability]; the statement about $X$-morphisms between weakly étale
objects is [lem-trf-weakly-etale-between-objects].
