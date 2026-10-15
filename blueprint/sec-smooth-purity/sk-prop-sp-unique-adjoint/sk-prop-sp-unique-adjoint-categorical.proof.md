+++
kind = "proof"
of = "det-sp-unique-right-adjoint"
+++
*Transposes.* For an adjunction $F\dashv J$ with counit $\varepsilon^J$, the map
$\operatorname{Hom}(A,JK)\to\operatorname{Hom}(FA,K)$, $\phi\mapsto\varepsilon^J(K)\circ F\phi$, is
a bijection, natural in $A$ and $K$. So $\gamma(K)$ and $\delta(K)$ exist and are
unique.

*Naturality.* For $u:K\to K'$, both $\gamma(K')\circ Gu$ and $Ju\circ\gamma(K)$
have $J$-transpose $u\circ\varepsilon^G(K)$: the first by naturality of
$\varepsilon^G$, $\varepsilon^J(K')\circ F\gamma(K')\circ FGu=\varepsilon^G(K')\circ FGu=u\circ\varepsilon^G(K)$;
the second by naturality of $\varepsilon^J$,
$\varepsilon^J(K')\circ FJu\circ F\gamma(K)=u\circ\varepsilon^J(K)\circ F\gamma(K)=u\circ\varepsilon^G(K)$.
Hence they are equal. Likewise for $\delta$.

*Inverse.* The $G$-transpose of $\delta(K)\circ\gamma(K)$ is
$\varepsilon^G(K)\circ F\delta(K)\circ F\gamma(K)=\varepsilon^J(K)\circ F\gamma(K)=\varepsilon^G(K)$,
which is also the $G$-transpose of $\mathrm{id}_{GK}$; so
$\delta(K)\circ\gamma(K)=\mathrm{id}$. Symmetrically
$\gamma(K)\circ\delta(K)=\mathrm{id}_{JK}$.

*Uniqueness.* If $\gamma'(K):GK\to JK$ satisfies
$\varepsilon^J(K)\circ F\gamma'(K)=\varepsilon^G(K)$, its $J$-transpose is
$\varepsilon^G(K)$, the same as that of $\gamma(K)$, so $\gamma'(K)=\gamma(K)$.
