+++
kind  = "proof"
of    = "det-def-sp-tate-twist-locally-free"
+++
(1) The sheaf $\mu_{\ell^n,X}$ is represented by the finite étale $X$-group scheme
$\mu_{\ell^n}=\Spec\cO_X[t]/(t^{\ell^n}-1)$; it is étale because $\ell$ is invertible.
Let $P_n\to X$ be the scheme of primitive $\ell^n$th roots of unity, the closed and open
subscheme of $\mu_{\ell^n}$ where $t$ has exact order $\ell^n$ in every fibre; it is finite
étale and surjective over $X$ (over a field in which $\ell$ is invertible, $t^{\ell^n}-1$ is
separable and has primitive roots in a separable closure). The maps $t\mapsto t^\ell$ give
finite étale surjections $P_{n+1}\to P_n$. Put $\widetilde X=\varprojlim_nP_n$, an affine
morphism limit of finite étale surjections; it is pro-étale and surjective, hence a
pro-étale cover. The coordinates give $\zeta_n\in\mu_{\ell^n}(\widetilde X)$ with
$\zeta_{n+1}^\ell=\zeta_n$, each of exact order $\ell^n$ in every fibre. The morphism of
finite étale $\widetilde X$-schemes $\coprod_{a\in\mathbf Z/\ell^n}\widetilde X\to\mu_{\ell^n,\widetilde X}$,
given by $\zeta_n^a$ on the $a$-th copy, is a bijection on geometric fibres (the
$\zeta_n^a$ are the $\ell^n$ distinct roots of the separable polynomial $t^{\ell^n}-1$), and
both sides have degree $\ell^n$; a morphism of finite étale schemes that is bijective on
geometric fibres is an isomorphism. This is the isomorphism of (1).

(2) This is [lem-pur-finite-kummer-level], applied with $\ell^N$ the exponent; concretely,
on $\widetilde X$ both sides are identified with $A_{\widetilde X}$ via $\zeta_{r'}$ and
$\zeta_r=\zeta_{r'}^{\ell^{r'-r}}$, and these identifications are compatible with the
Kummer map; since being an isomorphism is local, the map is an isomorphism on $X$.

(3) For finite $A$: by (1), $A_{\widetilde X}(1)=\mu_{\ell^r,\widetilde X}\otimes A_{\widetilde X}\cong A_{\widetilde X}$.
For $\cO_E$: the isomorphisms $(\cO_E/\ell^n)_{\widetilde X}\cong(\cO_E/\ell^n)_{\widetilde X}(1)$,
$a\mapsto\zeta_n\otimes a$ are compatible with the transition maps because
$\zeta_{n+1}\mapsto\zeta_{n+1}^\ell=\zeta_n$. Passing to the limit and using
$\cO_{E,\widetilde X}=\varprojlim_n(\cO_E/\ell^n)_{\widetilde X}$
([det-prop-sfb-qlbar-colimit-x-integral-limit]; the systems $\pi_E^n$ and $\ell^n$ are
cofinal) gives $\cO_{E,\widetilde X}(1)\cong\cO_{E,\widetilde X}$, an isomorphism of
$\cO_{E,\widetilde X}$-modules. Inverting $\ell$
([det-prop-sfb-qlbar-colimit-x-invert-ell]) and taking the colimit over $E$ give the same for
$E$ and $\Qlb$. The isomorphism $\Lambda_X(1)|_{\widetilde X}\cong\Lambda_{\widetilde X}$
shows that $\Lambda_X(1)$ is invertible; tensor powers and duals of invertible modules are
invertible; the evaluation map $\Lambda_X(d)\otimes\Lambda_X(-d)\to\Lambda_X$ is an
isomorphism because it is so locally. Finally an invertible module is flat, so
$K\otimes^{\mathbf L}\Lambda_X(d)=K\otimes\Lambda_X(d)$ termwise, and
$(K(d))(-d)\cong K\otimes\Lambda_X(d)\otimes\Lambda_X(-d)\cong K$.

The explicit construction of the twists for all coefficients at once, including the
convention $\Lambda(m)$ for $m\in\mathbf Z$, is [def-coefficient-twists-detailed].
