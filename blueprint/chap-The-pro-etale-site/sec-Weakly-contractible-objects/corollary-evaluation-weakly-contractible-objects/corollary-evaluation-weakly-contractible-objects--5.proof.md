+++
kind = "proof"
of = "corollary-evaluation-weakly-contractible-objects--5"
order = 79011
uses = ["lemma-stability--3"]
+++
(2) Limits of sheaves are computed on sections, so only colimits need an
argument. We first consider a direct sum $\bigoplus_iM_i$. The direct sum
sheaf is the sheafification of the presheaf direct sum, so a section over
$W$ is, locally on $W$, a finite sum of sections of the $M_i$. Since $W$
is affine, hence quasi-compact as an object of the site, a finite
covering suffices, and a single finite set of indices $i$ serves for all
members of this covering. By the sheaf condition, the section is then a
section of the corresponding finite subsum, and finite sums commute with
evaluation. It follows that evaluation preserves arbitrary direct sums
[Stacks, [0935](https://stacks.math.columbia.edu/tag/0935)]. An arbitrary colimit of modules is the cokernel of a map
between direct sums, and evaluation preserves cokernels by (1). Hence it
preserves all colimits.

*Source:* the proof of Corollary [corollary-evaluation-weakly-contractible-objects].
