+++
id = "thm-av-final"
kind = "theorem"
title = "Abelian-variety estimate"
order = 602
uses = ["def-av-pic", "def-sc-abelian-variety", "def-sc-isogeny", "def-sc-jacobian", "def-sc-mult-n", "def-wf-abelian-tate-module", "lem-sc-connected-finite-order", "lem-sc-divisible-group-structure", "lem-sc-fg-order-prime-etale", "lem-sc-finite-flat-surj-points", "lem-sc-finite-nonempty-point", "lem-sc-isogeny-facts", "lem-sc-isogeny-surjective", "lem-sc-mult-n-finite-flat", "lem-sc-ntorsion-etale", "prop-av-jacobian", "prop-av-jacobian-general", "prop-av-kummer-tate", "prop-av-tate-rank", "rem-ptr-sc-abelian-variety-1", "rem-ptr-sc-isogeny-2"]
+++
Let $A$ be an abelian variety of dimension $g$ over a field $k$, let
$p=\operatorname{char}k$ and let $n\ge1$.

- **(a)** $[n]:A\to A$ is a finite flat surjective homomorphism, hence
an isogeny of degree $n^{2g}$; $A[n]=\ker[n]$ is a finite flat group
scheme over $k$ of order $n^{2g}$.
- **(b)** If $p>0$, then $A[p^e]$ is finite flat of order $p^{2ge}$ for
every $e\ge1$. If $n$ is prime to $p$ (in particular if $p=0$), then
$A[n]$ is finite étale of rank $n^{2g}$.
- **(c)** Let $k$ be algebraically closed and $n$ prime to $p$. Then
$A[n](k)\cong(\Z/n\Z)^{2g}$, and for every extension
$k\subseteq k'$ of algebraically closed fields the canonical map
$A[n](k)\to A[n](k')$ is an isomorphism.
- **(d)** Let $k$ be algebraically closed. Then $A(k)$ is a divisible
abelian group, $A(k)[n]\cong(\Z/n\Z)^{2g}$ for every $n$ prime to $p$,
and for every prime $\ell\ne p$
$$
T_\ell A\cong\Z_\ell^{2g},\qquad V_\ell A\cong\Q_\ell^{2g}.
$$
- **(e)** Let $C$ be a smooth projective geometrically integral curve
of genus $g$ over a field $k$. Then $\Pic^0_{C/k}$ is representable by
an abelian variety $J=J_C$ of dimension $g$ over $k$ (the Jacobian),
$J(K)\cong\Pic^0(C_K)$ for every field extension $K/k$, and for
$\ell\ne\operatorname{char}k$ there are natural Galois-equivariant
isomorphisms
$$
H^1(C_{\bar k},\mu_{\ell^n})\cong J[\ell^n](\bar k)\quad(n\ge1),
\qquad
\varprojlim_nH^1_{\Et}(C_{\bar k},\Z/\ell^n)\cong
\Hom_{\Z_\ell}(T_\ell J,\Z_\ell).
$$

## Proof

*(a)* This is exactly [lem-sc-isogeny-facts], [lem-sc-mult-n-finite-flat]: $[n]$ is a
homomorphism ([sk-prop-av-mult-hom] with [sk-cor-av-commutative]), has
finite fibres ([sk-prop-av-mult-finite]) and is surjective
([sk-prop-av-mult-surjective]), is flat with locally free pushforward of
rank the order of its kernel ([sk-prop-av-isogeny-degree]), and its
degree is computed as $n^{2g}$ from
$[n]^*\cN\cong\cN^{\otimes n^2}$ ([sk-prop-av-mult-n-pullback],
[sk-prop-av-symmetric-ample]) together with
$\deg_{[n]^*\cN}(A)=\deg[n]\deg_{\cN}(A)$
([sk-prop-av-deg-pullback]).

*(b)* The first clause is (a) with $n=p^e$. For the second,
$A[n]$ is finite flat of order $n^{2g}$ by (a); write
$G=A[n]$. If $p>0$, the identity component $G^0$ is a connected
finite flat group scheme, so $\lvert G^0\rvert$ is a power of $p$ by
[lem-sc-connected-finite-order]; as $\lvert G^0\rvert$ divides
$\lvert G\rvert=n^{2g}$ and $p\nmid n$, we get $G^0=\Spec k$, so $G$
is reduced and hence étale over $k$; for $p=0$ the same conclusion is
Cartier's theorem. Both cases are the statement of
[lem-sc-fg-order-prime-etale] applied to the finite flat group scheme
$A[n]$ of order $n^{2g}$.

*(c)* Assume $k$ algebraically closed and $n$ prime to $p$. By
(b), $A[n]$ is finite étale of order $n^{2g}$, so
$\lvert A[n](k)\rvert=n^{2g}$ and $A[n](k)\to A[n](k')$ is bijective
by [sk-prop-av-finite-etale-points]. The group structure
$(\Z/n\Z)^{2g}$ is the content of [lem-sc-ntorsion-etale]: the
prime-power case follows from divisibility of $A(k)$
([lem-sc-finite-flat-surj-points], [lem-sc-finite-nonempty-point], [lem-sc-isogeny-surjective]) and the structure theorem for torsion of a
divisible group ([lem-sc-divisible-group-structure]), and the general case
from the Chinese remainder theorem applied to the coprime-order
subgroup schemes $A[\ell_i^{e_i}]$.

*(d)* Still with $k$ algebraically closed:
$A(k)$ is abelian by [sk-cor-av-commutative] and divisible by
[lem-sc-finite-flat-surj-points], [lem-sc-finite-nonempty-point], [lem-sc-isogeny-surjective]; and $A(k)[n]\cong(\Z/n\Z)^{2g}$ for $n$ prime to
$p$ is clause (c). For the Tate module, each level
$A[\ell^n](k)\cong(\Z/\ell^n\Z)^{2g}$ by (c) and the transition maps
are surjective by [lem-sc-finite-flat-surj-points], [lem-sc-finite-nonempty-point], [lem-sc-isogeny-surjective], so the inverse limit
$T_\ell A$ of [def-wf-abelian-tate-module] is $\Z_\ell^{2g}$; this is
[prop-av-tate-rank], and $V_\ell A=T_\ell A\otimes\Q_\ell$.

*(e)* Over a separably closed field the representability of
$\Pic^0_{C/k}$ by an abelian variety of dimension $g$, together with
the identification $J(k)\cong\Pic^0(C)$ and base change compatibility,
is the quoted input [prop-av-jacobian]; over an arbitrary field the
same statement without a rational point is obtained by descent, which
is [prop-av-jacobian-general]. The Tate-module identification is
[prop-av-kummer-tate]: the Kummer sequence gives
$H^1(C_{\bar k},\mu_{\ell^n})\cong\Pic(C_{\bar k})[\ell^n] =\Pic^0(C_{\bar k})[\ell^n]=J[\ell^n](\bar k)$, compatibly with the
transition maps and with the Galois action, and duality converts the
system into $\Hom_{\Z_\ell}(T_\ell J,\Z_\ell)$.

Uses: [def-sc-isogeny], [rem-ptr-sc-isogeny-2], [def-sc-jacobian], [def-sc-mult-n], [def-av-pic], [def-wf-abelian-tate-module], [def-sc-abelian-variety], [rem-ptr-sc-abelian-variety-1], [lem-sc-connected-finite-order], [lem-sc-divisible-group-structure], [lem-sc-finite-flat-surj-points], [lem-sc-finite-nonempty-point], [lem-sc-isogeny-surjective], [lem-sc-isogeny-facts], [lem-sc-mult-n-finite-flat], [prop-av-jacobian-general], [prop-av-jacobian], [prop-av-kummer-tate], [lem-sc-ntorsion-etale], [lem-sc-fg-order-prime-etale], [prop-av-tate-rank]
