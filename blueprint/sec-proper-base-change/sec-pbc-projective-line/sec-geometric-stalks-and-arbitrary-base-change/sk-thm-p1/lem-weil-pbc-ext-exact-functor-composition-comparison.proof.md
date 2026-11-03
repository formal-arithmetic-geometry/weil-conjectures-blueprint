+++
kind = "proof"
of = "lem-weil-pbc-ext-exact-functor-composition-comparison"
uses = ["def-pc-ext", "def-weil-abstract-derived-category"]
+++
An additive functor preserving finite limits and colimits acts termwise on complexes and preserves quasi-isomorphisms, so $F$, $G$ and $H$ induce functors $F_D$, $G_D$, $H_D$ on derived categories, commuting with shifts. The natural isomorphism $e$ induces a natural isomorphism $H_D\cong(G\circ F)_D$, and composing it with the canonical isomorphism $(G\circ F)_D\cong G_D\circ F_D$ gives a comparison $\tilde e:H_D\xrightarrow{\sim}G_D\circ F_D$, which commutes with shifts. On a single complex $A[0]$, under the identifications $H_D(A[0])\cong H(A)[0]$ and $G_DF_D(A[0])\cong GF(A)[0]$, the component $\tilde e_{A[0]}$ is $e_A[0]$: the two maps of complexes to be compared are $e_A$ in degree zero, where the single-complex comparisons are identities, and zero in all other degrees. ([def-weil-abstract-derived-category]).

By [def-pc-ext], $x$ is a morphism $A[0]\to B[0][n]$ in the derived category, composition of Ext classes is composition of shifted morphisms, and $H_*x$, $G_*F_*x$ are the images of $x$ under $H_D$ and $G_DF_D$ after the single-complex identifications. Naturality of $\tilde e$ at $x$, together with its compatibility with the shift $[n]$, gives $\tilde e_{B[0]}[n]\circ H_D(x)=G_DF_D(x)\circ\tilde e_{A[0]}$. Substituting the description of $\tilde e$ on single complexes from the first step and cancelling the single-complex identifications yields $\operatorname{mk}_0(e_B)\circ H_*x=G_*F_*x\circ\operatorname{mk}_0(e_A)$.
