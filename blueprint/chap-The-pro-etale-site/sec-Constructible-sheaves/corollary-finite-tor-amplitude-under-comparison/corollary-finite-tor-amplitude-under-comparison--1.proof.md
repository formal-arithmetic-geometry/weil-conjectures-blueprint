+++
kind = "proof"
of = "corollary-finite-tor-amplitude-under-comparison--1"
order = 152002
uses = ["theorem-comparison-constructible-sheaves", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image"]
+++
Take the derived comparison, its natural isomorphism on complexes, and its
bounded constructible equivalence from [theorem-comparison-constructible-sheaves].
We first compare the same interval $[a,b]$ on both sites.

A complex has Tor amplitude in $[a,b]$ if and only if it has a representative
by flat sheaves which is zero outside $[a,b]$. Choose such a representative
$P$ of $K$. The comparison inverse image preserves flat sheaves and zero
objects, so $\nu_X^*P$ is again flat in every degree and zero outside
$[a,b]$. The natural isomorphism on complexes identifies its localization
with $\nu_X^*K$. Applying the flat-model criterion on the pro-étale site
gives Tor amplitude in $[a,b]$ against every pro-étale module sheaf.

Conversely, suppose that $\nu_X^*K$ has Tor amplitude in $[a,b]$. Choose
a K-flat representative $P'$ of $K$ whose terms are flat. The ringed-topos
pullback theorem shows that its termwise comparison inverse image is
K-flat; the pullback in that theorem agrees with the specified comparison
by uniqueness of left adjoints. For an arbitrary étale module sheaf $M$,
test the assumed Tor bound against $\nu_X^*M$ in degree zero. The
comparison inverse image commutes with this ordinary tensor test and its
cohomology, and detects zero sheaves by exactness and faithfulness
([proposition-comparison-morphism-inverse-image] and
[theorem-classical-sheaves-essential-image]). It follows that
$H^q(P'\otimes_\Lambda M)=0$ for $q<a$ or $q>b$.
Tensor-test cohomology agrees for any two K-flat representatives of the
same derived object.
Thus the same vanishing holds for every K-flat representative of $K$,
which proves the reverse implication.

Finally, having some finite Tor interval is invariant under isomorphism.
Restrict the bounded constructible equivalence to the full subcategories
with this property. Full faithfulness is inherited, and reflection of
the interval gives essential surjectivity: an inverse image under the
bounded constructible equivalence of a finite-Tor object again has finite
Tor amplitude. Restricting the original natural isomorphism identifies
the forward functor with $\nu_X^*$ as asserted.
