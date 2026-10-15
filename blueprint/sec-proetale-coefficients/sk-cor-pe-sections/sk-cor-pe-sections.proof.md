+++
kind = "proof"
of = "sk-cor-pe-sections"
+++
By [sk-thm-pe-weakly-contractible-basis] every object of $X_{\mathrm{proét}}$ has an affine
weakly contractible covering family, and by [sk-cor-pe-wc-sections] each member has exact
sections.

If a sequence becomes exact on all such $W$, a section in a kernel lifts locally on a
weakly contractible cover, so it lies in the image sheaf. Applying this criterion to
kernels and cokernels proves conservativity, and applying it degreewise treats complexes
([det-pe-sections-conservative]; for finite coefficient rings see also
[lem-sf-proetale-vanishing-detection]).

Limits of sheaves are computed sectionwise. For colimits of modules, first consider a
direct sum $\bigoplus_iM_i$. A section is locally a finite sum; quasi-compactness gives a
finite covering on which this description holds, so one finite set of summand indices
suffices on all covering members. The sheaf condition then identifies the section with a
section of that finite subsum. Evaluation therefore preserves arbitrary direct sums
(Stacks, Tag 0935). An arbitrary colimit of modules is a cokernel of a map between direct
sums, and exactness of evaluation gives the assertion ([det-pe-sections-limits-colimits]).
See Stacks, Tag 0945 for the conservative criterion.
