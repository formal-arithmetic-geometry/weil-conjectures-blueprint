+++
id = "lem-sc-gl-characters"
kind = "lemma"
title = "Homomorphisms $\\mathrm{GL}_{c}\\to\\mathbf G_m$ are powers of the determinant"
order = 2049
uses = ["def-sc-general-linear-group", "def-sc-gm-ga", "def-sc-group-scheme", "def-sc-group-scheme-subgroup", "def-sc-group-scheme-translate", "lem-sc-elementary-generation", "lem-sc-ga-gm-homomorphism", "lem-sc-points-detect-morphisms", "lem-sc-torus-homomorphism-monomial", "lem-sc-translation-automorphism"]
+++
Let $k$ be a field and $c\geq1$. Every morphism of $k$-group
schemes

$$
\chi:\mathrm{GL}_{c,k}\longrightarrow\mathbf G_m
$$

is of the form $\chi(g)=\det(g)^r$ for a unique $r\in\mathbf Z$; in
particular $\chi$ is trivial on the special linear group scheme
$\mathrm{SL}_{c,k}\subseteq\mathrm{GL}_{c,k}$.

## Proof

*Step 1: reduction to an algebraically closed field.* Let
$K=\bar k$. Base change along the faithfully flat morphism
$\Spec K\to\Spec k$ is injective on morphisms: a morphism is
determined by its graph, and a closed subscheme is determined by its
base change along a faithfully flat morphism. Hence it suffices to
treat the case of an algebraically closed field, which we now assume.

*Step 2: the diagonal torus.* The morphism
$\delta:\mathbf G_m^c\to\mathrm{GL}_{c,k}$ dual to
$x_{ij}\mapsto\delta_{ij}T_i$ is a homomorphism of group schemes
([def-sc-general-linear-group], [def-sc-gm-ga]) whose image is
the closed subgroup scheme of diagonal matrices in the sense of
[def-sc-group-scheme-subgroup]. Therefore $\chi\circ\delta$ is a
morphism of $k$-group schemes $\mathbf G_m^c\to\mathbf G_m$, and by
[lem-sc-torus-homomorphism-monomial] there are
$m_1,\dots,m_c\in\mathbf Z$ with

$$
(\chi\circ\delta)^*(t)=T_1^{m_1}\cdots T_c^{m_c}.
$$

*Step 3: the exponents coincide.* For a permutation
$\sigma\in\mathfrak S_c$ let $w_\sigma\in\mathrm{GL}_c(k)$ be the
corresponding permutation matrix and let $c_{w_\sigma}$ be conjugation
by it, an automorphism of the group scheme $\mathrm{GL}_{c,k}$
([lem-sc-translation-automorphism], with
[def-sc-group-scheme-translate]). Since $\chi$ is a homomorphism
of group schemes ([def-sc-group-scheme]) with commutative target,
$\chi\circ c_{w_\sigma}=\chi$ (evaluate on $R$-points). On the other
hand
$c_{w_\sigma}\circ\delta=\delta\circ\sigma_*$, where
$\sigma_*:\mathbf G_m^c\to\mathbf G_m^c$ is the automorphism
$T_i\mapsto T_{\sigma^{-1}(i)}$, which is a homomorphism of group
schemes. Applying $\chi$ gives
$\chi\circ\delta=(\chi\circ\delta)\circ\sigma_*$, i.e. $T_1^{m_1}\cdots T_c^{m_c}=T_{\sigma(1)}^{m_1}\cdots T_{\sigma(c)}^{m_c}$ for every $\sigma$; comparing monomials, the
vector $(m_1,\dots,m_c)$ is constant. Write $m:=m_1=\cdots=m_c$.

*Step 4: unipotent points are killed.* For $i\neq j$ the map
$a\mapsto E_{ij}(a)$ is a morphism of $k$-group schemes
$\mathbf G_a\to\mathrm{GL}_{c,k}$ (its matrix entries are
$\delta_{kl}+a\delta_{ki}\delta_{lj}$, and
$E_{ij}(a)E_{ij}(b)=E_{ij}(a+b)$). Hence
$\chi\circ E_{ij}:\mathbf G_a\to\mathbf G_m$ is a morphism of
$k$-group schemes, and
[lem-sc-ga-gm-homomorphism] shows that it is trivial. Therefore
$\chi$ kills every product of elementary matrices.

*Step 5: conclusion over $K$.* Let $g\in\mathrm{GL}_c(K)$.
Write $g=e_1\Delta e_2$ with $e_1,e_2$ products of elementary
matrices and $\Delta=\operatorname{diag}(t_1,\dots,t_c)$, as
[lem-sc-elementary-generation] allows. By Steps 3 and 4,

$$
\chi(g)=\chi(\Delta)=\prod_{i=1}^{c}t_i^{m}
=\Bigl(\prod_{i=1}^{c}t_i\Bigr)^{m}=\det(\Delta)^m=\det(g)^m,
$$

the second equality by Step 2 and the last since
$\det(e_1)=\det(e_2)=1$. Thus $\chi$ and $\det^m$ agree on every
$K$-point of $\mathrm{GL}_{c,k}$; since $\mathrm{GL}_{c,k}$ is
reduced of finite type over the algebraically closed field $k$ (it is
an open subscheme of affine $c^2$-space) and $\mathbf G_m$ is
separated, [lem-sc-points-detect-morphisms] gives
$\chi=\det^m$.

*Step 6: uniqueness and triviality on $\mathrm{SL}_c$.* If
$\det^{m}=\det^{m'}$ then restricting to the diagonal torus and
comparing the monomials of Step 2 gives $m=m'$; so the exponent, which
Step 2 computes as the exponent of the monomial
$(\chi\circ\delta)^*(t)$, is unique. Finally $\det$ is trivial on
the closed subgroup scheme
$\mathrm{SL}_{c,k}=\Spec k[x_{ij}]/(\det-1)$ of
[def-sc-general-linear-group], which is a closed subgroup scheme in
the sense of [def-sc-group-scheme-subgroup]; hence $\chi$ is
trivial there.
