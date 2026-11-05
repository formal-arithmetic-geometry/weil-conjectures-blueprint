+++
kind = "proof"
of = "corollary-evaluation-weakly-contractible-objects"
order = 80
uses = ["definition-w-local-w-strictly-local", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility", "proposition-pro-etale-coverings"]
+++
All three parts follow from the fact that every epimorphism onto a
sheaf is surjective on sections over $W$, together with the fact that
such $W$ cover every object. Exactness and conservativity
follow directly, and for colimits we need in addition that $W$ is
quasi-compact.

(1) Taking sections is left exact for any object of a site, since it
preserves kernels. By weak contractibility every epimorphism of sheaves
is surjective on sections over $W$, so the sections functor is also right
exact. An exact functor carries acyclic complexes to acyclic complexes,
and so it agrees with its derived functor, also for unbounded complexes.
In particular $H^q(W,F)=0$ for $q>0$.

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

(3) Suppose that a sequence $F'\to F\to F''$ with composite zero becomes
exact on all affine weakly contractible $W$. A local section of the
kernel of $F\to F''$ is, after restriction to a covering by such $W$,
the image of a section of $F'$, because these objects cover every object.
Hence it lies in the image sheaf, and the sequence is exact. Applied to
kernels and cokernels of a map, this criterion shows that a map which is
an isomorphism on all such $W$ is an isomorphism, and applied in each
degree it gives the statement for complexes; see [Stacks, [0945](https://stacks.math.columbia.edu/tag/0945)].
