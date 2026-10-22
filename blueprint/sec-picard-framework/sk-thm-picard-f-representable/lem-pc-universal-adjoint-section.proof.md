+++
kind  = "proof"
of    = "lem-pc-universal-adjoint-section"
+++
(1) $\mathcal{O}_{X_T}(D)$ is invertible, hence quasi-coherent, and $f_T$ is
proper (a base change of the proper $X\to\operatorname{Spec}k$), hence
quasi-compact and quasi-separated; the direct image of a quasi-coherent module
along a quasi-compact quasi-separated morphism is quasi-coherent.

(2) By the projection formula ([lem-pc-projection-formula], $q=0$),
$f_{T,*}\mathcal{L}\cong f_{T,*}\bigl(\mathcal{O}_{X_T}(D)\otimes f_T^*\mathcal{M}\bigr)\cong
f_{T,*}\mathcal{O}_{X_T}(D)\otimes\mathcal{M}$, which is invertible. Hence

$$
\mathcal{L}\otimes f_T^*(f_{T,*}\mathcal{L})^{-1}
\cong\mathcal{O}_{X_T}(D)\otimes f_T^*\mathcal{M}\otimes
f_T^*\bigl(f_{T,*}\mathcal{O}_{X_T}(D)\bigr)^{-1}\otimes f_T^*\mathcal{M}^{-1}
\cong\mathcal{O}_{X_T}(D)\otimes f_T^*\bigl(f_{T,*}\mathcal{O}_{X_T}(D)\bigr)^{-1}.
$$

(3) Let $\varphi:f_T^*f_{T,*}\mathcal{L}\to\mathcal{L}$ be the adjunction map. The
adjunction map $f_T^*\mathcal{N}\to\mathcal{L}$ is $\varphi$ precomposed with the
isomorphism $f_T^*\mathcal{N}\cong f_T^*f_{T,*}\mathcal{L}$, so it has the same zero
scheme as $\varphi$, and by [lem-pc-zero-scheme-recd] this is also $Z(s)$; it is a
relative effective Cartier divisor, finite locally free of degree $g$ over $T$.
On the other hand, the canonical section $1$ of $\mathcal{O}_{X_T}(D)$ (the
inclusion $\mathcal{I}_D\subseteq\mathcal{O}_{X_T}$, dualized), twisted by
$f_T^*\mathcal{N}'$, is a morphism $s':f_T^*\mathcal{N}'\to\mathcal{L}$ with zero scheme
$D$ ([def-pc-zero-scheme]). By adjunction $s'$ factors as $f_T^*t$ followed by
$\varphi$, where $t:\mathcal{N}'\to f_{T,*}\mathcal{L}$ is its adjoint; hence
$Z(\varphi)\subseteq Z(s')=D$. Both $Z(\varphi)$ and $D$ are closed subschemes of
$X_T$ finite locally free of degree $g$ over $T$, and a closed immersion between
finite locally free $T$-schemes of the same degree is an isomorphism (on
each fibre it is a surjection of $\kappa(t)$-algebras of the same dimension,
so its ideal vanishes by Nakayama). Hence $Z(s)=Z(\varphi)=D$.

The final assertion is (3) for $T=W$, $D=D_{\mathrm{univ}}\cap(W\times X)$ (a point
of $\operatorname{Hilb}^g_{X/k}(W)$, being the restriction of the universal one) and
$\mathcal{N}'=\sigma_W^*\mathcal{O}(D_{\mathrm{univ}})^{-1}$.
