+++
id = "lem-sc-pic-tangent-space"
kind = "lemma"
title = "The tangent space of the Picard scheme"
order = 852
uses = ["def-pc-geometrically-irreducible", "def-pc-smooth-projective-curve", "def-sc-picard-functor", "lem-sc-cech-spectral", "thm-pc-picard-representable"]
+++
Let $C$ be a smooth projective
curve over a separably closed field $k$ which is
geometrically integral, and let
$\operatorname{Pic}_{C/k}$ be
the Picard functor, represented by a
group scheme locally of finite type over $k$ (which it is by
[thm-pc-picard-representable]). Then
the tangent space of $\operatorname{Pic}_{C/k}$ at the identity
is canonically isomorphic to $H^1(C,\mathcal O_C)$.

## Proof

The tangent space classifies first-order deformations of the
trivial line bundle, i.e. line bundles on
$C_{k[\varepsilon]}:=C\times_kk[\varepsilon]$,
$\varepsilon^2=0$, reducing to the trivial bundle modulo
$\varepsilon$. Cover $C$ by affine opens $\{U_i\}$. Over
$U_i$, every deformation of the trivial bundle is the trivial
bundle (a module over $\mathcal O(U_i)[\varepsilon]$ that is
projective of rank one and reduces to $\mathcal O(U_i)$ is
free), so a deformation is given by transition isomorphisms
$1+\varepsilon g_{ij}$ with
$g_{ij}\in\Gamma(U_i\cap U_j,\mathcal O)$; the cocycle condition

$$
(1+\varepsilon g_{ij})(1+\varepsilon g_{jk})=(1+\varepsilon g_{ik})
$$

reads $g_{ij}+g_{jk}=g_{ik}$, and changing the trivializations
on $U_i$ by $1+\varepsilon h_i$ changes $g_{ij}$ by
$g_{ij}+h_j-h_i$. The deformations modulo isomorphism are
therefore exactly the Cech 1-cohomology classes

$$
\check H^1(\{U_i\},\mathcal O)=H^1(C,\mathcal O_C),
$$

the affine Cech computation of
[lem-sc-cech-spectral]. (*Reference for the
general statement that the tangent space of the Picard scheme is
$H^1(C,\mathcal O_C)$: Stacks Project, Picard Schemes of Curves,
Chapter 44, [Tag 0B92](https://stacks.math.columbia.edu/tag/0B92).*)
