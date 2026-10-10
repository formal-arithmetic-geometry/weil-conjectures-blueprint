+++
kind  = "proof"
of    = "thm-pd-jacobian-general-field"
+++
Fix a separable closure $k_s$ of $k$ as in [def-pd-separable-closure].
Since a scheme which is proper over a field and of dimension $1$ is projective over it, the curve is a
[def-pc-smooth-projective-curve]; being smooth and geometrically
connected, it is [def-pc-geometrically-irreducible] (its geometric fibre
is regular, hence normal, and connected, hence irreducible). It is of genus
$g$ in the sense of
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

*Step 9 (the geometric points).* Take $T=\Spec(\bar k)$, a $k$-scheme.
The curve $C_{\bar k}$ has a $\bar k$-rational point because $\bar k$ is
algebraically closed, so by [lem-pc-rational-hyp] and [thm-pc-pic-split]
(with $\operatorname{Pic}(\Spec\bar k)=0$ by [lem-pc-pic-of-field]) the canonical map from the
Picard presheaf,
$\operatorname{Pic}(C_{\bar k})\to\operatorname{Pic}_{C_{\bar k}/\bar k}(\bar k)$,
is an isomorphism; by [lem-pd-picard-base-change] the target is
$\operatorname{Pic}_{C/k}(T)$, the value of the Picard functor of $C/k$ on
the $k$-scheme $T$. For a point $T$ the fibrewise degree
([def-pd-fibrewise-degree]) of a class is the degree of the invertible
module on $C_{\bar k}$, so the degree-zero parts correspond:
$\operatorname{Pic}^0_{C/k}(T)=\operatorname{Pic}^0(C_{\bar k})$ in the
sense of [def-sc-pic0]. Composing with the value on $T$ of the
isomorphism $h_J\cong\operatorname{Pic}^0_{C/k}$ of Step 7 gives the
identification $J(\bar k)=h_J(T)=\operatorname{Pic}^0(C_{\bar k})$.

*Step 10 (equivariance).* Let $\sigma\in\Gamma$. The map
$\sigma^\sharp:T\to T$ is a morphism in $(\mathit{Sch}/k)_{fppf}$, so every
functor on that category assigns to it an endomorphism of its value on $T$;
for $h_J$ this is $x\mapsto x\circ\sigma^\sharp$, the action through the
$k$-structure of $J$, and for the Picard presheaf of $C/k$ it is pullback
along $\mathrm{id}_C\times\sigma^\sharp:C_{\bar k}\to C_{\bar k}$, the
action through the $k$-structure of $C$ (it preserves degrees, since
$\mathrm{id}_C\times\sigma^\sharp$ is an isomorphism of schemes over the
automorphism $\sigma^\sharp$ of the base). Both the canonical map from the
Picard presheaf to its sheafification $\operatorname{Pic}_{C/k}$ and the
isomorphism $h_J\cong\operatorname{Pic}^0_{C/k}$ of Step 7 are natural
transformations of functors on $(\mathit{Sch}/k)_{fppf}$, so they commute
with the endomorphisms induced by $\sigma^\sharp$. Hence every map in the
chain of Step 9 commutes with the action of $\sigma$, i.e. the
identification $J(\bar k)=\operatorname{Pic}^0(C_{\bar k})$ is
$\Gamma$-equivariant. The rules $\sigma\mapsto F(\sigma^\sharp)$ are left
actions because both $F$ and $\Spec$ are contravariant. Finally, restriction
to $\operatorname{Gal}(k_s/k)$ is an isomorphism
$\Gamma\to\operatorname{Gal}(k_s/k)$ because $\bar k/k_s$ is purely
inseparable, so every $k$-automorphism of $k_s$ extends uniquely to
$\bar k$.

*Step 11 (torsion).* The identification of Step 9 is an isomorphism of
groups, because the isomorphism of Step 7 is one of group-valued functors
and the map from the Picard presheaf is additive. The $\bar k$-points of
the kernel $J[\ell^n]$ of multiplication by $\ell^n$ on $J$ are the
$\ell^n$-torsion of the group $J(\bar k)$, since taking $T$-points commutes
with kernels. A $\Gamma$-equivariant group isomorphism maps the
$\ell^n$-torsion subgroup isomorphically and equivariantly onto the
$\ell^n$-torsion subgroup, which gives
$J[\ell^n](\bar k)\cong\operatorname{Pic}^0(C_{\bar k})[\ell^n]$
equivariantly.
