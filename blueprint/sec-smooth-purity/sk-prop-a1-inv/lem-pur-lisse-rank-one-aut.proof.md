+++
kind  = "proof"
of    = "lem-pur-lisse-rank-one-aut"
+++
Step 1: (1). By [def-weil-scheme-morphism-properties] local
constancy means that $L$ becomes constant after pullback along a
covering family of the site; let $u:U\to T$ be a member of such a
family, so that $Lu^*L\cong\Lambda_U$. Pullback commutes with the
internal Hom of [def-weil-derived-pullback-tensor-hom], so it
carries the
canonical map $\Lambda_T\to\mathcal Hom(L,L)$ to the canonical map
$\Lambda_U\to\mathcal Hom(\Lambda_U,\Lambda_U)=\Lambda_U$, which is
an isomorphism; a morphism of sheaves which becomes an isomorphism
after pullback along a covering family is itself an isomorphism, by the
sheaf axiom. Hence $\Lambda_T\to\mathcal Hom(L,L)$ is an
isomorphism, and taking global sections writes
$\operatorname{End}(L)=\Gamma(T,\Lambda_T)$ as the ring of locally
constant $\Lambda$-valued functions, whose unit group is
$\Gamma(T,\Lambda_T^\times)$.
Step 2: (2). The composite $\psi\circ\varphi^{-1}$ is an
automorphism of $M$, hence is multiplication by a unique locally
constant unit $u$ by (1) applied to $M$; then
$\psi=u\cdot\varphi$, and conversely $u\cdot\varphi$ is an
isomorphism exactly for a unit $u$. For the final assertion take the
constant function with value $v\in\Lambda^\times$, which is a unit.
