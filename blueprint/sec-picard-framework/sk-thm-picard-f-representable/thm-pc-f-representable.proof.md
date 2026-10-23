+++
kind  = "proof"
of    = "thm-pc-f-representable"
uses = ["lem-pc-f-open-subfunctor", "lem-pc-zero-scheme-recd"]
+++
*Preliminaries.* The scheme $X$ is projective over $k$: it is separated
of finite type of dimension $1$ over a field, hence quasi-projective, and a
proper quasi-projective scheme over a field is projective
([Tag 0B45](https://stacks.math.columbia.edu/tag/0B45)). Being
geometrically integral, it is integral; so $X$ is a smooth projective
curve in the sense of [def-pc-smooth-projective-curve], to which the
lemmas on smooth projective curves used below apply; all of them hold
over an arbitrary field.

Let $H$ be the given $k$-scheme representing $\operatorname{Hilb}^g_{X/k}$
(such an $H$ exists by [thm-pc-hilb-curves], and any two are canonically
isomorphic), and let $D_{\mathrm{univ}}\subset H\times X$ be the universal
object, the element of $\operatorname{Hilb}^g_{X/k}(H)$ corresponding to
$\mathrm{id}_H$; it is a relative effective Cartier divisor on
$H\times X/H$ by [lem-pc-cartier-criterion] ((1)$\Rightarrow$(2), the
projection $H\times X\to H$ being smooth of relative dimension $1$), as in
[lem-pc-universal-divisor]. Let

$$
\mathcal{L}_H:=\mathcal{O}(D_{\mathrm{univ}})\otimes
\mathrm{pr}_H^*\sigma_H^*\mathcal{O}(D_{\mathrm{univ}})^{\otimes-1}
$$

be the normalized universal module ($\sigma_H:H\to H\times X$ is the
section of $\mathrm{pr}_H$ induced by $\sigma$; the cancellation of the
$\sigma$-factors in
$\sigma_H^*\mathcal{L}_H=\sigma_H^*\mathcal{O}(D_{\mathrm{univ}})\otimes \sigma_H^*\mathrm{pr}_H^*\sigma_H^*\mathcal{O}(D_{\mathrm{univ}})^{-1}\cong\mathcal{O}_H$,
because $\mathrm{pr}_H\circ\sigma_H=\mathrm{id}_H$, shows
$\mathcal{L}_H\in\operatorname{Pic}_{X/k,\sigma}(H)$, [def-pc-pic-sigma-functor]). By the
Yoneda lemma ([def-pc-representable-functor]) the element
$\mathcal{L}_H$ defines a natural transformation $h_H\to\operatorname{Pic}_{X/k,\sigma}$.

Since $F\subseteq\operatorname{Pic}_{X/k,\sigma}$ is an open subfunctor
([lem-pc-f-open-subfunctor]), applied to the element
$\mathcal{L}_H\in\operatorname{Pic}_{X/k,\sigma}(H)$ there is an open
$W\subseteq H$ such that, by [def-pc-subfunctor], a morphism $a:T\to H$ of
$k$-schemes factors through $W$ if and only if
$(a\times\mathrm{id}_X)^*\mathcal{L}_H\in F(T)$. Applying the Yoneda lemma again
we obtain the commutative diagram

$$
\begin{array}{ccc}
h_W & \xrightarrow{\ \psi\ } & F\\[-2pt]
\downarrow & & \downarrow\\[-2pt]
h_H & \xrightarrow{\ \ } & \operatorname{Pic}_{X/k,\sigma}
\end{array}
$$

and we show that the top horizontal arrow $\psi$ is an isomorphism.

*Construction of the inverse.* Let $\mathcal{L}\in F(T)$ for a scheme
$T$ over $k$; let $\mathcal{N}$ be an invertible $\mathcal{O}_T$-module with
$Rf_{T,*}\mathcal{L}\cong\mathcal{N}[0]$, and let $s$ be the adjoint section of
$\mathcal{L}\otimes f_T^*\mathcal{N}^{-1}$ ([lem-pc-zero-scheme-recd]). By
[lem-pc-zero-scheme-recd], $D:=Z(s)$ is a relative effective Cartier
divisor on $X_T/T$ which is finite locally free of degree $g$; hence
$D\in\operatorname{Hilb}^g_{X/k}(T)$ ([def-pc-hilb-functor]) and, by the
representability of $\operatorname{Hilb}^g_{X/k}$ by $H$, there
is a unique morphism $m:T\to H$ with $D=(m\times\mathrm{id}_X)^*D_{\mathrm{univ}}$
(the universal object of [lem-pc-universal-divisor]).

*$m$ factors through $W$.* By
[lem-pc-recd-pullback] the pullback of the relative effective
Cartier divisor $D_{\mathrm{univ}}$ along $m$ is the divisor with
associated module

$$
(m\times\mathrm{id})^*\mathcal{O}(D_{\mathrm{univ}})\cong\mathcal{O}_{X_T}(D)\cong\mathcal{M}
=\mathcal{L}\otimes f_T^*\mathcal{N}^{-1}
$$

(the second isomorphism holds because the section $s$ of $\mathcal{M}$ has zero
scheme $D$, so $s$ generates the ideal sheaf $\mathcal{I}_D$ at the points where
it does not vanish and the identification $D=Z(s)$ gives
$\mathcal{O}_{X_T}(D)=\mathcal{I}_D^\vee$; write $u$ for this isomorphism). We compute:

$$
(m\times\mathrm{id})^*\mathcal{L}_H
=(m\times\mathrm{id})^*\mathcal{O}(D_{\mathrm{univ}})
\otimes\mathrm{pr}_T^*\bigl(m^*\sigma_H^*\mathcal{O}(D_{\mathrm{univ}})\bigr)^{-1}
=\mathcal{O}_{X_T}(D)\otimes\mathrm{pr}_T^*\sigma_T^*\mathcal{O}_{X_T}(D)^{-1}
$$

(using $(m\times\mathrm{id})\circ\sigma_T=\sigma_H\circ m$ and
$(m\times\mathrm{id})^*\mathrm{pr}_H^*=\mathrm{pr}_T^*m^*$). Since $\sigma_T^*\mathcal{O}_{X_T}(D)\cong\sigma_T^*\mathcal{M}$
$=\sigma_T^*\mathcal{L}\otimes\sigma_T^*f_T^*\mathcal{N}^{-1} =\mathcal{O}_T\otimes\mathcal{N}^{-1} =\mathcal{N}^{-1}$ (because $\mathcal{L}\in\operatorname{Pic}_{X/k,\sigma}(T)$ and
$\sigma_T^*f_T^*=\mathrm{id}$; here $\sigma_T^*\mathcal{O}_{X_T}(D)$ means the pullback of
the corresponding quotient of the ideal sheaf, equivalently the fibre of
$\mathcal{O}(D)$ along $\sigma_T$), we get

$$
(m\times\mathrm{id})^*\mathcal{L}_H\cong\mathcal{O}_{X_T}(D)\otimes f_T^*\mathcal{N}
\cong\mathcal{L}\otimes f_T^*\mathcal{N}^{-1}\otimes f_T^*\mathcal{N}\cong\mathcal{L}.
$$

Thus $(m\times\mathrm{id})^*\mathcal{L}_H\cong\mathcal{L}$ lies in $F(T)$, so
by the defining property of $W$ the morphism $m$ factors through $W$; we
still write $m:T\to W$.

*$\psi$ is bijective on points, with inverse
$\theta:\mathcal{L}\mapsto m$.* The transformation
$\psi:a\mapsto(a\times\mathrm{id})^*\mathcal{L}_H$ is natural in $T$, since
pullbacks compose. The composite $\psi\circ\theta=\mathrm{id}$ on $F(T)$ was
computed above ($(m\times\mathrm{id})^*\mathcal{L}_H\cong\mathcal{L}$). For the
other composite $h_W(T)\to F(T)\to h_W(T)$, $a\mapsto\mathcal{L}':=(a\times\mathrm{id})^*\mathcal{L}_H\mapsto a'$,
let $D_a:=(a\times\mathrm{id})^{-1}(D_{\mathrm{univ}})$, the point of
$\operatorname{Hilb}^g_{X/k}(T)$ classified by $a$; it is a relative
effective Cartier divisor with
$\mathcal{O}_{X_T}(D_a)\cong(a\times\mathrm{id})^*\mathcal{O}(D_{\mathrm{univ}})$
([lem-pc-recd-pullback]). As computed above,
$\mathcal{L}'\cong\mathcal{O}_{X_T}(D_a)\otimes f_T^*\mathcal{N}'$ with
$\mathcal{N}'=a^*\sigma_H^*\mathcal{O}(D_{\mathrm{univ}})^{-1}$ invertible, and
$\mathcal{L}'\in F(T)$ since $a$ factors through $W$. By
[lem-pc-universal-adjoint-section](3) the adjoint section of $\mathcal{L}'$
([lem-pc-zero-scheme-recd]) has zero scheme $D_a$, so $a'$ is the morphism
classifying $D_a$, i.e. $a'=a$ by the uniqueness in the universal property.
Hence $\psi_T$ is bijective for every $T$, and the natural transformation
$\psi$ is an isomorphism of functors $h_W\cong F$, i.e. $F$ is
representable (by the open subscheme $W$ of $H$, which is a scheme: open
subschemes of schemes are schemes).
Taking for $j:W\to H$ the inclusion of this open subscheme gives the
statement.
