+++
id = "thm-pd-jacobian-general-field"
kind = "theorem"
title = "The Jacobian over an arbitrary ground field"
order = 874
uses = ["cor-pd-finite-level", "cor-pd-pic0-base-change", "def-pc-base-change", "def-pc-genus", "def-pc-geometrically-irreducible", "def-pc-picard-functor", "def-pc-smooth-projective-curve", "def-pd-degree-morphism", "def-pd-descent-datum", "def-pd-fibrewise-degree", "def-pd-separable-closure", "def-sc-abelian-variety", "def-sc-group-scheme", "def-sc-jacobian", "def-sc-pic0", "lem-pc-dim-base-change", "lem-pc-pic-of-field", "lem-pc-rational-hyp", "lem-pd-canonical-descent-datum", "lem-pd-descent-cocycle", "lem-pd-group-scheme-descent", "lem-pd-picard-base-change", "thm-pc-pic-split", "thm-pd-effective-descent", "thm-pd-fpqc-local-properties", "thm-pd-geometric-pic0"]
lean = ["AlgebraicGeometry.exists_jacobian_descent"]
+++
Let $k$ be any field and let $C$ be a
$k$-scheme which is proper and smooth of relative dimension $1$ over $k$
and geometrically connected, of genus
$g$ ([def-pc-genus]). Then there is an
abelian variety $J$ over $k$ of dimension
$g$, together with a natural isomorphism of group-valued functors

$$
h_J\;\cong\;\operatorname{Pic}^0_{C/k},
$$

where $\operatorname{Pic}^0_{C/k}=\ker(\deg)$ is the
degree-zero part of the
Picard functor; that is, $J$ represents the
degree-zero relative Picard fppf sheaf. Moreover for every field extension
$K/k$ the base change is the Jacobian of the
base change,

$$
J_K\;\cong\;\operatorname{Pic}^0_{C_K/K},
$$

naturally in $K$.

Let moreover $\bar k$ be an algebraic closure of $k$ and $k_s\subseteq\bar k$ the separable
closure of $k$ in it, put
$C_{\bar k}=C\times_k\bar k$, and let
$\Gamma=\operatorname{Aut}(\bar k/k)$, which restriction identifies with
$\operatorname{Gal}(k_s/k)$. For $\sigma\in\Gamma$ write
$\sigma^\sharp=\Spec(\sigma)$, a $k$-automorphism of $\Spec(\bar k)$. The
induced identification

$$
J(\bar k)\;=\;\operatorname{Pic}^0(C_{\bar k})
$$

is *$\Gamma$-equivariant* for the natural actions: on the left through the
$k$-structure of $J$, $\sigma\cdot x=x\circ\sigma^\sharp$ for
$x\in J(\bar k)=\operatorname{Hom}_k(\Spec\bar k,J)$; on the right through
the $k$-structure of $C$, $\sigma\cdot[\mathcal L]=
[(\mathrm{id}_C\times\sigma^\sharp)^*\mathcal L]$. In particular, for every
prime $\ell$ and every $n\ge1$, restricting to $\ell^n$-torsion gives a
$\Gamma$-equivariant isomorphism

$$
J[\ell^n](\bar k)\;\cong\;\operatorname{Pic}^0(C_{\bar k})[\ell^n].
$$

No $k$-rational point of $C$ is assumed.
