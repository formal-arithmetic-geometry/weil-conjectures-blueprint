+++
kind = "proof"
of = "sk-cor-pe-sections"
+++
(1) Taking sections preserves kernels, and by projectivity every epimorphism
is surjective on sections. Hence the sections functor is
exact, carries acyclic complexes to acyclic complexes, and agrees
with its derived functor, also for unbounded complexes.

(2) Limits of sheaves are computed on sections. For colimits of
modules, we first consider a direct sum $\bigoplus_i M_i$. A section is
locally a finite sum. By quasi-compactness there is a finite covering on which
this description holds, so that a single finite set of summand indices
suffices on all members of the covering. By the sheaf condition, the section
is then a section of the corresponding finite subsum. It follows that evaluation
preserves arbitrary direct sums [Stacks, Tag 0935](https://stacks.math.columbia.edu/tag/0935). An arbitrary
colimit of modules is a cokernel of a map between direct sums, and
the assertion follows from (1).

(3) These objects cover every object, and every cover of one of them
splits. Suppose a sequence becomes exact on all such $W$. Then a section
in a kernel lifts locally on a weakly contractible cover, so it lies in
the image sheaf. Applied to kernels and cokernels, this criterion shows
conservativity, and applied in each degree it gives the statement
for complexes; see [Stacks, Tag 0945](https://stacks.math.columbia.edu/tag/0945).
