+++
id = "thm-pd-jacobian-general-field"
kind = "theorem"
title = "The Jacobian over an arbitrary ground field"
order = 2673
uses = ["cor-pd-finite-level", "cor-pd-pic0-base-change", "def-pc-base-change", "def-pc-genus", "def-pc-geometrically-irreducible", "def-pc-picard-functor", "def-pc-smooth-projective-curve", "def-pd-degree-morphism", "def-pd-descent-datum", "def-pd-separable-closure", "def-sc-abelian-variety", "def-sc-group-scheme", "def-sc-jacobian", "lem-pc-dim-base-change", "lem-pd-canonical-descent-datum", "lem-pd-descent-cocycle", "lem-pd-group-scheme-descent", "thm-pd-effective-descent", "thm-pd-fpqc-local-properties", "thm-pd-geometric-pic0"]
+++
Let $k$ be any field and let $C$ be a
smooth projective curve over $k$
which is
geometrically connected, of genus
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

naturally in $K$. No $k$-rational point of $C$ is assumed.

## Proof

Fix a separable closure $k_s$ of $k$ as in [def-pd-separable-closure].
The curve is a [def-pc-smooth-projective-curve] which is
[def-pc-geometrically-irreducible], of genus $g$ in the sense of
[def-pc-genus], and its degree-zero Picard functor is the
[def-pd-degree-morphism] inside the [def-pc-picard-functor].

*Step 1 (the geometric object).* By [thm-pd-geometric-pic0] the
degree-zero part $\operatorname{Pic}^0_{C_{k_s}/k_s}$ is represented by an
abelian variety $J_s$ over $k_s$ of dimension $g$. In particular the functor
$\operatorname{Pic}^0_{C/k}$ of [def-pd-degree-morphism] becomes
representable after base change to $k_s$, by
[cor-pd-pic0-base-change].

*Step 2 (the canonical descent datum).* By
[lem-pd-canonical-descent-datum] and [lem-pd-descent-cocycle] the
scheme $J_s$ carries a canonical
descent datum ([def-pd-descent-datum])
over $\Spec(k_s)/\Spec(k)$; it is canonical because it is produced by Yoneda
from the single functor $\operatorname{Pic}^0_{C/k}$, so no Galois action is
chosen.

*Step 3 (reduction to a finite level).* By [cor-pd-finite-level]
there are a finite separable extension $K/k$, a projective scheme $J_K$ of
finite presentation over $K$, and a descent datum over $\Spec(K)/\Spec(k)$
which base changes to the datum of Step 2, with $J_K\times_KK_s\cong J_s$.

*Step 4 (effectivity).* The extension $k\subseteq K$ is finite, so
$\Spec(K)\to\Spec(k)$ is surjective finite locally free, and
[thm-pd-effective-descent] applies to the projective $J_K$: the descent
datum is effective, giving a scheme $J$ over $k$ with
$J\times_kK\cong J_K$ and hence $J\times_kk_s\cong J_s$.

*Step 5 (the group structure).* The group law of the abelian variety
$J_s$ is defined over $K$ at the finite level, because it is part of the
functor $\operatorname{Pic}^0_{C/k}$ restricted to $K$, and it is compatible
with the descent datum by construction. [lem-pd-group-scheme-descent]
therefore descends it, so that $J$ is a $k$-group scheme in the sense of
[def-sc-group-scheme], with $J_K$ the given group scheme.

*Step 6 (the geometric properties).* The scheme $J_K=J\times_kK$ is
smooth over $K$ and proper over $K$, and it is connected, because it is the
base change of the abelian variety $J_s$ of Step 1 along
$\Spec(k_s)/\Spec(K)$ and an abelian variety is a variety, hence connected
([def-sc-abelian-variety]). By
[thm-pd-fpqc-local-properties] the scheme $J$ is therefore of finite type,
smooth and proper over $k$, and connected. By
[lem-pc-dim-base-change] applied to the flat extension $k\subseteq K$,
$\dim J=\dim J_K=\dim J_s=g$, the last equality by Step 1. By Stacks Project,
Remark 39.9.12, Tag
[0H2U](https://stacks.math.columbia.edu/tag/0H2U), a group scheme over a
field which is proper, connected and smooth is an abelian variety; hence $J$
is an abelian variety over $k$ of dimension $g$ in the sense of
[def-sc-abelian-variety].

*Step 7 (the functorial identification).* By Steps 1 and 4 the scheme
$J$ satisfies $J\times_kk_s\cong J_s$, and $J_s$ represents
$\operatorname{Pic}^0_{C_{k_s}/k_s}$, which by
[cor-pd-pic0-base-change] is the base change of
$\operatorname{Pic}^0_{C/k}$. The two functors
$h_J=\operatorname{Hom}_k(-,J)$ and $\operatorname{Pic}^0_{C/k}$ on
$(\mathit{Sch}/k)_{fppf}$ therefore become isomorphic after base change along
the faithfully flat morphism $\Spec(k_s)\to\Spec(k)$; an fppf sheaf is
determined by its base change along a faithfully flat cover, so
$h_J\cong\operatorname{Pic}^0_{C/k}$. Concretely, the isomorphism is the one
whose base change to $k_s$ is the representing isomorphism of $J_s$; it is
canonical because the representing isomorphism is. In the vocabulary of
[def-sc-jacobian] this says that $J$ is a Jacobian of $C$ over $k$.

*Step 8 (base change of the functor).* For an arbitrary field extension
$K/k$, apply the already proved statement to the curve $C_K$ over $K$: it is
smooth projective and geometrically connected of genus $g$ as well, so its
degree-zero Picard functor is representable by an abelian variety $J'$ over
$K$. Since $\operatorname{Pic}^0_{C_K/K}$ is the base change of
$\operatorname{Pic}^0_{C/k}$ by [cor-pd-pic0-base-change], and
$h_{J_K}=h_J\times_kK$, the two representing objects $J_K$ and $J'$ of the
same functor are canonically isomorphic, which is the asserted natural
isomorphism $J_K\cong\operatorname{Pic}^0_{C_K/K}$.
