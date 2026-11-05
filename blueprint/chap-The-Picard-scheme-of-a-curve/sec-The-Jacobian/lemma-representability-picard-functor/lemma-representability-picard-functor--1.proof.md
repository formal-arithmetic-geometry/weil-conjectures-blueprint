+++
kind = "proof"
of = "lemma-representability-picard-functor--1"
order = 1544002
uses = []
+++
Let $\xi_0\in F(A)$ be the universal section. For $m\in G(k)$,
the section $m_A^{-1}\xi_0\in G(A)$ defines a chart with image
$m^{-1}F$. Multiplication by $m$ identifies this chart with $F$,
so its inclusion is representable by open immersions. Smallness of
$G(k)$ gives a small family of these charts.

For $x\in G(T)$ and $t\in T$, apply the hypothesis over
$K=\kappa(t)$ to $x_K$. Choose $m\in G(k)$ with $m_Kx_K\in F(K)$.
The locus in $T$ where $m_Tx$ belongs to $F$ is open and contains
$t$. Thus the charts cover $G$ locally on every test scheme.
The Zariski sheaf condition allows them to be glued to a representing
scheme, by
`AlgebraicGeometry.Scheme.LocalRepresentability.isRepresentable_of_isSheaf_over`.
The group operations on $G$ give a group scheme structure by Yoneda,
as in `CategoryTheory.GrpObj.ofRepresentableBy`.

For the second assertion, fix $a\in A'$ and apply the same argument
to the universal section of $G(A')$ at $a$. It gives $m\in G(k)$
and an open subscheme $U\subset A'$ containing $a$, where that
section multiplied on the left by $m$ belongs to $F$. The section
$m_A^{-1}\xi_0$ defines a morphism $A\to A'$ factoring through $U$.
Conversely, the translated universal section on $U$ gives a morphism
$U\to A$. These maps are inverse by representability and cancellation
in $G$, so $A\simeq U$. This proves the required open immersion
through $a$ without using sheaf gluing.
