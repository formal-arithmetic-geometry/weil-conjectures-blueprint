+++
kind  = "proof"
of    = "def-sfb-continuous-map-condensed-ring"
+++
The functions $C(S,T)$ form a ring under pointwise operations, because $T$ is a
topological ring. Precomposition is a ring homomorphism and is strictly functorial, so
$\underline T$ is a presheaf of rings. The forgetful functor from rings to sets preserves
and reflects limits. So it suffices that the presheaf of sets $S\mapsto C(S,T)$ is a
sheaf.

Profinite sets have finite disjoint coproducts, and their effective epimorphisms are the
continuous surjections. Hence a presheaf is a sheaf for the coherent topology if and only
if both of the following hold:

- (a) it takes finite coproducts to products;
- (b) for every continuous surjection $q\colon S'\to S$ it satisfies the equalizer
  condition $F(S)\to F(S')\rightrightarrows F(S'\times_SS')$.

(a) holds because a finite disjoint union of profinite sets is a union of clopen pieces,
so a map out of it is continuous exactly when it is continuous on each piece. For (b), let
$b\in C(S',T)$ agree on both projections from $S'\times_SS'$, i.e. let $b$ be constant on
the fibres of $q$. Then $b=a\circ q$ for a unique map of sets $a\colon S\to T$, unique
because $q$ is surjective. Now $q$ is a continuous surjection from a compact space onto a
Hausdorff space, so it is closed and hence a quotient map. Therefore $a$ is continuous.

By part 3 of [det-def-sfb-ring-object], the underlying abelian sheaf of the sheaf of rings
$\underline T$ is a ring object. It is commutative when all the rings $C(S,T)$ are, which
holds when $T$ is commutative.
