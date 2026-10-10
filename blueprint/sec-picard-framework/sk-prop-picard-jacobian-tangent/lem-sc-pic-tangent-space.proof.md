+++
kind  = "proof"
of    = "lem-sc-pic-tangent-space"
+++
Let $k[\varepsilon]=k[x]/(x^2)$. The tangent space of $J$ at the unit is
$T_e=\ker(J(k[\varepsilon])\to J(k))$, and since $J$ represents
$\operatorname{Pic}^0_{C/k}$ it classifies first-order deformations of the
trivial line bundle, i.e. line bundles on
$C_{k[\varepsilon]}:=C\times_kk[\varepsilon]$ reducing to the trivial
bundle modulo $\varepsilon$ (with the normalization of
[def-sc-picard-functor]); such a bundle automatically has degree $0$, the
degree being locally constant in families over the connected
$\operatorname{Spec}k[\varepsilon]$, so the degree-zero condition is
automatic. Cover $C$ by affine opens $\{U_i\}$. Over
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
on $U_i$ by $1+\varepsilon h_i$ changes $g_{ij}$ to
$g_{ij}+h_j-h_i$. The deformations modulo isomorphism are
therefore in bijection, via $(1+\varepsilon g_{ij})\mapsto[(g_{ij})]$,
with the Cech 1-cohomology classes

$$
\check H^1(\{U_i\},\mathcal O)=H^1(C,\mathcal O_C),
$$

the affine Cech computation of
[lem-sc-cech-spectral].

This bijection is $k$-linear for the $k$-vector space structure of
the tangent space
$T_e$:
addition is the group law, i.e. the tensor product of line bundles,
whose transition functions multiply,
$(1+\varepsilon a)(1+\varepsilon b)=1+\varepsilon(a+b)$ (this agrees
with the addition defined through
$k[\varepsilon]\times_kk[\varepsilon]=k[\varepsilon_1,\varepsilon_2]/(\varepsilon_1,\varepsilon_2)^2$);
and $\lambda\in k$ acts by pullback along the $k$-algebra map
$\sigma_\lambda:k[\varepsilon]\to k[\varepsilon]$,
$\varepsilon\mapsto\lambda\varepsilon$, which sends the transition
functions $1+\varepsilon g_{ij}$ to $1+\varepsilon\lambda g_{ij}$, i.e.
the class $[(g_{ij})]$ to $\lambda[(g_{ij})]$. (*Reference for the
general statement that the tangent space of the Picard scheme is
$H^1(C,\mathcal O_C)$: Stacks Project, Picard Schemes of Curves,
Chapter 44, [Tag 0B92](https://stacks.math.columbia.edu/tag/0B92).*)
