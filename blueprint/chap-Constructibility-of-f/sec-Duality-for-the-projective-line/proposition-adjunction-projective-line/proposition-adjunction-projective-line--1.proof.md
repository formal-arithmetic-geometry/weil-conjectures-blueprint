+++
kind = "proof"
of = "proposition-adjunction-projective-line--1"
order = 553002
uses = ["lemma-cycle-class-cartier-divisor", "lemma-class-diagonal-projective-line", "proposition-forgetting-supports-composition", "definition-projection-formula-map", "theorem-proper-base-change-classical-pro"]
+++
Use the Gysin map of the diagonal, with the Kummer-boundary convention:
its cycle class is $-c_1(\mathcal O(\Delta))$. This is the negative of the
class in [lemma-cycle-class-cartier-divisor], paired with the trace
$t_p=-\operatorname{Tr}_p$. The two signs cancel in the integral identities of
[lemma-class-diagonal-projective-line] identify its contractions along the
two projections with the identity. The pulled-back object
$\Lambda_S(1)[2]$ has trivial self-braiding: the Tate sheaf has rank one
and the shift is even.

Proper base change and the projection formula turn this diagonal map into
a kernel transformation. The two contractions give the two triangle
identities for the resulting kernel adjunction, with trace counit.
This is the construction used by
`AlgebraicGeometry.Etale.exists_projectiveLineAdjunction_of_class`.

Transport the left adjoint through $Rp_!\simeq Rp_*$ and the right adjoint
through the natural identification
$p^*K(1)[2]\simeq\Lambda_{\mathbf P^1_S}(1)[2]\otimes_\Lambda^{\mathbf L}p^*K$.
The trace comparison and the projection formula identify the transported
counit with the displayed composite.
