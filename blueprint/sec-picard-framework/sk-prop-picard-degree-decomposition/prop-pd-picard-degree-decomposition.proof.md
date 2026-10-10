+++
kind  = "proof"
of    = "prop-pd-picard-degree-decomposition"
+++
Since a scheme which is proper over a field and of dimension $1$ is projective over it, $C$ is a smooth projective
curve. Throughout, for a field extension $K/k$ the base change $C_K$ is a smooth
projective curve over $K$, in particular integral, with the $K$-rational
point $P_K$ ([prop-pc-xk-integral], applied with $\sigma=P$); so $C$ is
geometrically integral and [def-pd-fibrewise-degree],
[def-pd-degree-morphism] and [lem-pd-degree-locally-constant] apply.

*Step 0: additivity of the degree over a field.* Let $K/k$ be a field
extension, write $Q=P_K$, and let $\mathcal{N},\mathcal{M}$ be invertible modules
on $C_K$. We claim
$\deg(\mathcal{N}\otimes\mathcal{M})=\deg\mathcal{N}+\deg\mathcal{M}$, with $\deg$ as in
[def-pc-degree-line-bundle]. First, for every invertible $\mathcal{N}'$,
[lem-pc-degree-base-change](2) with $D=Q$ and [lem-pc-degree-agrees-sc]
($\deg\mathcal{O}_{C_K}(Q)=1$ for the $K$-rational point $Q$) give
$\deg(\mathcal{N}'\otimes\mathcal{O}_{C_K}(Q))=\deg\mathcal{N}'+1$; iterating,
$\deg(\mathcal{N}'\otimes\mathcal{O}_{C_K}(Q)^{\otimes n})=\deg\mathcal{N}'+n$ for $n\geq0$.
Now choose $n\geq0$ with $\deg\mathcal{M}+n+\chi(C_K,\mathcal{O}_{C_K})>0$ and put
$\mathcal{M}'=\mathcal{M}\otimes\mathcal{O}_{C_K}(Q)^{\otimes n}$. By
[def-pc-degree-line-bundle],
$\chi(C_K,\mathcal{M}')=\deg\mathcal{M}'+\chi(C_K,\mathcal{O}_{C_K})=\deg\mathcal{M}+n+\chi(C_K,\mathcal{O}_{C_K})>0$,
and since $H^i(C_K,\mathcal{M}')=0$ for $i\geq2$ ([lem-pc-vanishing-above-dim])
the Euler characteristic ([def-pc-euler-characteristic]) is
$\dim_KH^0-\dim_KH^1$, so $H^0(C_K,\mathcal{M}')\neq0$. Let $s$ be a nonzero
global section. As $C_K$ is integral, on an open where
$\mathcal{M}'\cong\mathcal{O}$ the section $s$ is a nonzero element of a domain, hence
a nonzerodivisor; so its zero scheme $D$ is an
effective Cartier divisor,
$s$ identifies $\mathcal{M}'^{\vee}$ with the ideal $\mathcal{I}_D$, and dualizing
gives $\mathcal{M}'\cong\mathcal{I}_D^{\vee}=\mathcal{O}_{C_K}(D)$. Applying
[lem-pc-degree-base-change](2) twice,
$$
\deg(\mathcal{N}\otimes\mathcal{M})+n=\deg(\mathcal{N}\otimes\mathcal{O}_{C_K}(D))
=\deg\mathcal{N}+\deg\mathcal{O}_{C_K}(D)=\deg\mathcal{N}+\deg\mathcal{M}+n,
$$
which is the claim. In particular $\deg\mathcal{O}_{C_K}=0$,
$\deg\mathcal{N}^{\vee}=-\deg\mathcal{N}$, and (iterating from
$\deg\mathcal{O}_C(P)=1$) $\deg\mathcal{O}_C(dP)=d$ for all $d\in\Z$.

*(1) $\deg$ is a homomorphism.* Let $x,y\in\operatorname{Pic}_{C/k}(T)$. Since the
Picard functor is the fppf
sheafification of the Picard presheaf, there is an fppf covering
$\{T_i\to T\}$ (a common refinement of coverings for $x$ and for $y$)
and invertible modules $\mathcal{L}_i,\mathcal{M}_i$ on $C_{T_i}$ whose classes are
$x|_{T_i}$, $y|_{T_i}$; the map from the presheaf to its sheafification
is a homomorphism, and the group law of the presheaf is $\otimes$, so
$(xy)|_{T_i}$ is the class of $\mathcal{L}_i\otimes\mathcal{M}_i$. For $t\in T$ pick
$t_i\in T_i$ over $t$. By the construction of [def-pd-degree-morphism]
and [lem-pd-degree-locally-constant](3), $\deg(xy)(t)$ is the degree of
$(\mathcal{L}_i\otimes\mathcal{M}_i)_{t_i}=(\mathcal{L}_i)_{t_i}\otimes(\mathcal{M}_i)_{t_i}$ on
$C_{\kappa(t_i)}$, which by Step 0 equals
$\deg(x)(t)+\deg(y)(t)$. Hence $\deg(xy)=\deg(x)+\deg(y)$; the remaining
assertions of (1) follow.

*(2) Decomposition.* By [cor-pc-sigma-pic-iso] (with $\sigma=P$) the
class of the identity of $\underline{\operatorname{Pic}}_{C/k}$, the universal class
$\xi\in\operatorname{Pic}_{C/k}(\underline{\operatorname{Pic}}_{C/k})$, is the class of an
invertible module $\mathcal{L}$ on $C\times_k\underline{\operatorname{Pic}}_{C/k}$ (trivial
along $P$). Computing [def-pd-degree-morphism] with the trivial covering,
$\deg(\xi)=\delta$, which is locally constant by
[lem-pd-degree-locally-constant](1). Hence the sets
$U_d:=\delta^{-1}(d)$ are open and closed, pairwise disjoint and cover
$\underline{\operatorname{Pic}}_{C/k}$, so $\underline{\operatorname{Pic}}_{C/k}$ is the scheme-theoretic
disjoint union of the open subschemes $U_d=\underline{\operatorname{Pic}}^d_{C/k}$. Let
$h:T\to\underline{\operatorname{Pic}}_{C/k}$ correspond to $x=h^*\xi$. Since $\deg$ is a
morphism of sheaves and restriction in $\underline{\Z}$ is composition,
$\deg(x)=\delta\circ h$. So $x\in\operatorname{Pic}^d_{C/k}(T)$ iff
$h(T)\subseteq U_d$ iff $h$ factors (uniquely) through the open
subscheme $U_d$; that is, $U_d$ represents the subfunctor
$\operatorname{Pic}^d_{C/k}$ (a subfunctor by
[lem-pd-degree-locally-constant](3)).

*(3) Subgroup scheme.* The unit $e:\operatorname{Spec}k\to\underline{\operatorname{Pic}}_{C/k}$ is the
class of $\mathcal{O}_C$, of degree $0$, so it factors through $U_0$. The
restriction of the multiplication $m$ to the open subscheme
$U_0\times_kU_0$ is the $U_0\times_kU_0$-point
$\operatorname{pr}_1^*\xi\cdot\operatorname{pr}_2^*\xi$ whose degree is $0+0=0$ by (1), so by
(2) it factors through $U_0$; likewise the inverse maps $U_0$ into $U_0$
since $\deg(x^{-1})=-\deg(x)$. Thus $U_0$ is an open and closed
subgroup scheme.

*(4) Translation.* Let $a_d\in\underline{\operatorname{Pic}}_{C/k}(k)$ be the class of
$\mathcal{O}_C(dP)$ and let
$\tau_d=m\circ(\mathrm{id},a_d\circ\pi):\underline{\operatorname{Pic}}_{C/k}\to\underline{\operatorname{Pic}}_{C/k}$,
$\pi$ the structure morphism; on $T$-points $\tau_d(x)=x\cdot(a_d)_T$, which
on a representing module is tensoring with $\operatorname{pr}_C^*\mathcal{O}_C(dP)$. Since
$a_{-d}a_d=[\mathcal{O}_C]=e$, $\tau_{-d}\circ\tau_d=\tau_d\circ\tau_{-d}=\mathrm{id}$,
so $\tau_d$ is an automorphism of the scheme $\underline{\operatorname{Pic}}_{C/k}$. The
fibre of $\operatorname{pr}_C^*\mathcal{O}_C(dP)$ at $t\in T$ is
$\mathcal{O}_C(dP)\otimes_k\kappa(t)$, of degree $d$ by
[lem-pc-degree-base-change](1) and Step 0; so $\deg((a_d)_T)\equiv d$ and,
by (1), $\deg(\tau_d(x))=\deg(x)+d$. Hence $\tau_d$ maps the subfunctor
$\operatorname{Pic}^0_{C/k}$ into $\operatorname{Pic}^d_{C/k}$ and $\tau_{-d}$ maps
$\operatorname{Pic}^d_{C/k}$ into $\operatorname{Pic}^0_{C/k}$; by (2) they restrict to
mutually inverse morphisms $U_0\rightleftarrows U_d$, and
$\tau_d|_{U_0}:\underline{\operatorname{Pic}}^0_{C/k}\to\underline{\operatorname{Pic}}^d_{C/k}$ is an
isomorphism of schemes.
