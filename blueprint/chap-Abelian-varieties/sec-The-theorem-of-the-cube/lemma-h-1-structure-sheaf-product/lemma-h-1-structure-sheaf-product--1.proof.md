+++
kind = "proof"
of = "lemma-h-1-structure-sheaf-product--1"
order = 1481002
uses = []
+++
Let $\mathcal I_{p_0}$ and $\mathcal I_{q_0}$ be the ideal sheaves of
the two points. Properness and geometric integrality give
$H^0(P,\mathcal O_P)=H^0(Q,\mathcal O_Q)=K$. A global function
vanishing at a $K$-point is therefore zero, so
$H^0(P,\mathcal I_{p_0})=H^0(Q,\mathcal I_{q_0})=0$.

Apply the degree-one Künneth vanishing statement
`AlgebraicGeometry.Scheme.IdealSheafData.Kunneth.subsingleton_H_one_toModules_prodIdeal`
to these two ideals. Its hypotheses hold because proper schemes are
quasi-compact and separated. Here is the computation behind that
statement. Choose finite affine covers of $P$ and $Q$. On a product
$U\times_K V$ of affine opens, multiplication identifies sections of
$\mathcal J$ with
$\mathcal I_{p_0}(U)\otimes_K\mathcal I_{q_0}(V)$, compatibly with
restriction. The absence of global sections makes the degree-zero
differentials of the two ideal-sheaf Čech complexes injective. The
tensor-product argument then expresses every degree-one cocycle on
the product cover as a coboundary. Finally, the affine Čech comparison
identifies this cohomology with $H^1(P\times_K Q,\mathcal J)$, proving
the assertion.
