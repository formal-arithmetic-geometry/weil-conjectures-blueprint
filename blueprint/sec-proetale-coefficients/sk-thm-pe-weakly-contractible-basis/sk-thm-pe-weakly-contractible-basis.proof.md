+++
kind = "proof"
of = "sk-thm-pe-weakly-contractible-basis"
+++
Apply [sk-thm-pe-wc-cover] to each affine chart ([det-pe-wcb-cover]). For the splitting
assertion, a faithfully flat weakly étale $D$-algebra refines, by
[sk-thm-pe-indetale-refinement], to a faithfully flat ind-étale $D$-algebra.
[sk-prop-pe-wc-rings] splits this refinement and hence splits the original map
([det-pe-wcb-split-cover]). Every cover of the affine $U$ refines to a finite affine cover;
its disjoint union is a single faithfully flat weakly étale affine cover and therefore
splits. The inverse images of its finitely many components give a finite clopen partition
of $U$ subordinate to the original cover ([det-pe-wcb-clopen-partition]).

Now an epimorphism $F\to h_U$ has lifts of $\mathrm{id}_U$ after a covering of $U$. Refine
that covering by the clopen partition just constructed and glue the lifts on its disjoint
pieces. This gives a global lift of $\mathrm{id}_U$, hence a section. The same argument,
after pulling back an arbitrary epimorphism along a map from $h_U$, proves projectivity
([det-pe-wcb-projective]). See Stacks, Tags 098F and 0990.
