+++
kind = "proof"
of = "lem-weil-pbc-ext-exact-functor-identity-comparison"
uses = ["def-pc-ext", "def-weil-abstract-derived-category"]
+++
Since $F$ preserves finite limits and finite colimits, it acts termwise on complexes and preserves quasi-isomorphisms, so it induces a functor on the derived category. The termwise identity functor induces the identity, and $e$ induces a natural isomorphism from the induced functor $F$ to the identity. This follows from the universal property of the localization [def-weil-abstract-derived-category]. The components of this isomorphism commute with shifts because $e$ acts termwise.

By [def-pc-ext], $x$ is a morphism $A[0]\to B[0][n]$ in the derived category. Apply naturality of the induced isomorphism to $x$. The source component is $\operatorname{mk}_0(e_A)$, the target component is $\operatorname{mk}_0(e_B)[n]$, and the identity functor leaves $x$ unchanged. This gives exactly the asserted equality $\operatorname{mk}_0(e_B)\circ F_*x=x\circ\operatorname{mk}_0(e_A)$.
