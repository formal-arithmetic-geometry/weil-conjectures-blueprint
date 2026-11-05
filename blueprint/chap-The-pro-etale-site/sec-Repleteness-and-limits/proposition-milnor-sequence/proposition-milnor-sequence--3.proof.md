+++
kind = "proof"
of = "proposition-milnor-sequence--3"
order = 91006
uses = ["corollary-evaluation-weakly-contractible-objects", "proposition-milnor-sequence--1"]
+++
Evaluate on an affine weakly contractible object $W$. By
[corollary-evaluation-weakly-contractible-objects], evaluation
preserves products and cokernels, so the transitions become
surjections of $\mathcal R(W)$-modules. Choose right inverses $s_n$
to them. Given $(a_n)$, set $m_0=0$ and
$m_{n+1}=s_n(m_n-a_n)$. Then $m_n-t_n(m_{n+1})=a_n$, so $1-T$ is
surjective on sections over $W$. Since these evaluations detect
exactness, $1-T$ is an epimorphism of sheaves. Its cokernel is zero,
and [proposition-milnor-sequence--1] identifies this cokernel with
$H^1$ of the Roos complex.

The tuple of ordinary limit projections identifies
$(\varprojlim_nM_n)[0]$ with the kernel of $1-T$ on the product of
the degree-zero complexes. Together with the epimorphism just
proved, this gives a short exact sequence of complexes. The
canonical map from its kernel to $\Cone(1-T)[-1]$ is a
quasi-isomorphism: it is the map induced by the kernel inclusion
and the zero null-homotopy. Localization at quasi-isomorphisms
makes this particular comparison an isomorphism in the derived
category.
