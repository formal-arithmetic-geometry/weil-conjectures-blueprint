+++
kind  = "proof"
of    = "det-prop-scalar-six-pullback"
uses = ["det-def-sfb-coefficient-change", "sk-prop-sfb-cartesian-coefficients", "det-lem-int-tensor-projection"]
+++
*(1)* By [sk-prop-sfb-cartesian-coefficients], $f^{-1}\Lambda_Y=\Lambda_X$ and
$f^{-1}\Lambda'_Y=\Lambda'_X$, compatibly with the coefficient change
([det-def-sfb-coefficient-change]); hence $f^*=f^{-1}$ is exact on module sheaves for
both rings and commutes with restriction of scalars. Represent $K$ by a K-flat
complex $Q$ of $\Lambda_Y$-modules. Then $f^{-1}Q$ is K-flat over $\Lambda_X$
(Stacks, Tag 06YV: inverse image preserves K-flat complexes, and here it needs no
deriving), and inverse image of sheaves commutes with tensor products,
$f^{-1}(\Lambda'_Y\otimes_{\Lambda_Y}Q)=f^{-1}\Lambda'_Y\otimes_{f^{-1}\Lambda_Y}f^{-1}Q=\Lambda'_X\otimes_{\Lambda_X}f^{-1}Q$.
The left side represents $f^*(K_{\Lambda'})$ and the right side $(f^*K)_{\Lambda'}$; this is
the associativity of derived pullback for ringed topoi (Stacks, Tag 06YV). The
identification is termwise the canonical isomorphism of sheaves, so it is natural
in $K$ and compatible with $(gf)^{-1}=f^{-1}g^{-1}$.

*(2)* Apply [det-lem-int-tensor-projection] with $L=\Lambda'_X$, viewed as a complex
of $\Lambda_X$-modules:
$$
(a_!M)_{\Lambda'}=a_!M\otimes^{\mathbf L}_{\Lambda_X}\Lambda'_X\simeq a_!\bigl(M\otimes^{\mathbf L}_{\Lambda_S}a^*\Lambda'_X\bigr)=a_!(M_{\Lambda'}),
$$
since $a^*\Lambda'_X=\Lambda'_S$. The isomorphism is $\Lambda'_X$-linear because the
projection-formula map is linear in $L$. Alternatively, for $a=j$ open, both
functors $K\mapsto(j_!K)_{\Lambda'}$ and $K\mapsto j_!(K_{\Lambda'})$ have the same right
adjoint, namely $N\mapsto j^*N$ regarded as a complex of $\Lambda_U$-modules, because
restriction of scalars commutes with $j^*$; so they are canonically isomorphic.
Compatibility with composition follows from the
corresponding compatibility of the projection formula.

*(3)* $\Lambda''_X\otimes^{\mathbf L}_{\Lambda'_X}(\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}K)\simeq\Lambda''_X\otimes^{\mathbf L}_{\Lambda_X}K$
by associativity of the derived tensor product, and $(\Lambda\to\Lambda'')_X$ is the
composite of the coefficient changes ([det-def-sfb-coefficient-change]). The
isomorphisms in (1), (2) are built from canonical isomorphisms of tensor products,
so they are compatible with this one.
