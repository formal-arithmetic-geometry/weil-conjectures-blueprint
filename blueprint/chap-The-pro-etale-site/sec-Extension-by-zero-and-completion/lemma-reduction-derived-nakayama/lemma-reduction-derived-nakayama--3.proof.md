+++
kind = "proof"
of = "lemma-reduction-derived-nakayama--3"
order = 210003
uses = ["lemma-reduction-derived-nakayama--2"]
+++
Complete $u$ to a distinguished triangle $K\to L\to C\to K[1]$.
The complexes with zero first reduction are closed under shifts, so the
vanishing condition on morphisms into $K$ is also satisfied by $K[1]$.
Apply $\operatorname{Hom}(Z,-)$ to the rotated triangle
$L\to C\to K[1]$. Exactness shows that the same condition holds for $C$.

Derived extension of scalars from $\mathcal O_{E,X}$ to
$\mathbf F_{E,X}$ preserves distinguished triangles. The exact functor
from $\mathbf F_{E,X}$-module objects to sheaves of $\mathbf F_E$-modules
reflects isomorphisms, and so does its derived functor. Hence the
isomorphism $u_1$ implies that the extension of scalars of $C$ vanishes,
and therefore $C_1=0$. By [lemma-reduction-derived-nakayama--2], $C=0$,
so $u$ is an isomorphism.
