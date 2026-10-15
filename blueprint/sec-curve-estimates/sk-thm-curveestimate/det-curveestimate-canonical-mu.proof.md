+++
kind = "proof"
of = "det-curveestimate-canonical-mu"
+++
The Kummer sequence is exact on $C_{\mathrm{ét}}$ ([lem-sc-kummer-exact]).
Its long exact sequence, with
$H^1(C,\mathbf G_m)=\operatorname{Pic}(C)$ and
$H^q(C,\mathbf G_m)=0$ for $q\geq2$ ([lem-sc-brauer-zero],
[det-thm-br-higher-vanishing]), reads

$$
0\to\mu_n(k)\to\Gamma(C,\mathbf G_m)\xrightarrow{n}\Gamma(C,\mathbf G_m)
\xrightarrow{\delta^1}H^1(C,\mu_n)\to\operatorname{Pic}(C)
\xrightarrow{n}\operatorname{Pic}(C)\xrightarrow{\delta^2}H^2(C,\mu_n)\to0,
$$

and $H^q(C,\mu_n)=0$ for $q\geq3$; compare [lem-sc-kummer-les]. Since $C$ is
proper, connected and reduced, $\Gamma(C,\mathbf G_m)=k^\times$, which is
$n$-divisible because $k$ is algebraically closed. Hence $\delta^1=0$ and
$H^0(C,\mu_n)=\mu_n(k)$, $H^1(C,\mu_n)\cong\operatorname{Pic}(C)[n]$,
$H^2(C,\mu_n)\cong\operatorname{Pic}(C)/n$. This proves 1 and 4.

Apply the snake lemma to multiplication by $n$ on the degree sequence

$$
0\to J(k)\to\operatorname{Pic}(C)\xrightarrow{\deg}\Z\to0
$$

([lem-sc-pic-proper-decomposition]). Multiplication by $n$ on $J(k)$ is
surjective with kernel $J[n](k)$ ([thm-av-final](d)), and on $\Z$ it is
injective with cokernel $\Z/n$. The snake lemma gives

$$
0\to J[n](k)\to\operatorname{Pic}(C)[n]\to0,\qquad
0=J(k)/n\to\operatorname{Pic}(C)/n\xrightarrow{\deg}\Z/n\to0,
$$

so $\operatorname{Pic}(C)[n]=J[n](k)$, of order $n^{2g}$ since $J$ is an
abelian variety of dimension $g$ ([thm-sc-jacobian-representability],
[thm-av-final](c)), and $\deg$ induces an isomorphism
$\operatorname{Pic}(C)/n\cong\Z/n$. Composing with the inverse of the
isomorphism $\operatorname{Pic}(C)/n\cong H^2(C,\mu_n)$ induced by $\delta^2$
gives $\deg_n$ with $\deg_n(\delta^2[L])=\deg L\bmod n$; it is unique because
$\delta^2$ is surjective. This proves 2 and 3.

For 5, $C_{k'}$ is again smooth, proper and connected
([lem-sc-base-change-curve]), and pullback along $\pi:C_{k'}\to C$ maps the
Kummer sequence of $C$ to that of $C_{k'}$, so it commutes with all maps of
the long exact sequences, including the boundary maps. On $H^0$ it is the
inclusion $\mu_n(k)\subseteq\mu_n(k')$, a bijection since both groups have
exactly $n$ elements. On $H^1$ it is the restriction of
$\operatorname{Pic}(C)\to\operatorname{Pic}(C_{k'})$ to $n$-torsion, which
under $J_{C_{k'}}=(J_C)_{k'}$ ([thm-sc-jacobian-representability]) is the
base-change map $J[n](k)\to J[n](k')$, a bijection by [thm-av-final](c). On
$H^2$, write $\deg_n'$ and $\delta'^2$ for the maps of 3 over $k'$. Pullback
of line bundles preserves degree and $\rho^2\circ\delta^2=\delta'^2\circ\pi^*$,
so $\deg_n'\circ\rho^2\circ\delta^2=\deg_n\circ\delta^2$ on
$\operatorname{Pic}(C)$;
since $\delta^2$ is surjective, $\rho^2$ corresponds to the identity of
$\Z/n$. In degrees $q>2$ both sides are zero. Hence every $\rho^q$ is an
isomorphism.
