+++
kind  = "proof"
of    = "sk-thm-av-final"
+++
*(a)* This is exactly [sk-prop-av-isogeny]: $[n]$ is a
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
$G=A[n]$ and let $\bar k$ be an algebraic closure of $k$. Then
$G_{\bar k}=A_{\bar k}[n]$ is a finite flat group scheme over $\bar k$
of order $n^{2g}$, prime to $p$, so it is étale over $\bar k$ by
[sk-prop-av-prime-p-etale] (for $p>0$: the identity component
$(G_{\bar k})^0$ is a connected finite flat group scheme, so its order
is a power of $p$ by [sk-prop-av-connected-order] and divides
$n^{2g}$, whence $(G_{\bar k})^0=\Spec\bar k$; every connected
component of $G_{\bar k}$ is a translate of $(G_{\bar k})^0$ by a
$\bar k$-point, so $G_{\bar k}$ is reduced, hence étale over the
algebraically closed $\bar k$; for $p=0$ this is Cartier's theorem).
Finally étaleness descends to $k$: $G$ is flat over $k$ and
$\Omega_{G/k}\otimes_k\bar k\cong\Omega_{G_{\bar k}/\bar k}=0$, so
$\Omega_{G/k}=0$ and $G$ is étale over $k$. (The passage to
$\bar k$ is needed: over an imperfect $k$ a finite reduced $k$-scheme
need not be étale, so one cannot conclude directly from
$G^0=\Spec k$.)

*(c)* Assume $k$ algebraically closed and $n$ prime to $p$. By
(b), $A[n]$ is finite étale of order $n^{2g}$, so
$\lvert A[n](k)\rvert=n^{2g}$ and $A[n](k)\to A[n](k')$ is bijective
by [sk-prop-av-finite-etale-points]. The group structure
$(\Z/n\Z)^{2g}$ is the content of [sk-prop-av-ntorsion-etale]: the
prime-power case follows from divisibility of $A(k)$
([sk-prop-av-divisible]) and the structure theorem for torsion of a
divisible group ([sk-prop-av-divisible-structure]), and the general case
from the Chinese remainder theorem applied to the coprime-order
subgroup schemes $A[\ell_i^{e_i}]$.

*(d)* Still with $k$ algebraically closed:
$A(k)$ is abelian by [sk-cor-av-commutative] and divisible by
[sk-prop-av-divisible]; and $A(k)[n]\cong(\Z/n\Z)^{2g}$ for $n$ prime to
$p$ is clause (c). For the Tate module, each level
$A[\ell^n](k)\cong(\Z/\ell^n\Z)^{2g}$ by (c) and the transition maps
are surjective by [sk-prop-av-divisible], so the inverse limit
$T_\ell A$ of [sk-def-av-tate] is $\Z_\ell^{2g}$; this is
[sk-prop-av-tate-rank], and $V_\ell A=T_\ell A\otimes\Q_\ell$.

The Jacobian instance of these statements is not treated here: the
representability of $\Pic^0_{C/k}$ by an abelian variety is
[sk-prop-jacobian] and, over an arbitrary field,
[sk-prop-jacobian-descent] ([sec-picard-framework]); the Kummer
identification of $H^1$ of a curve with the Tate module of its
Jacobian is part of the real-purity section ([sk-d-real-jacobian]).
