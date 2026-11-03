+++
kind = "proof"
of = "det-sp-scalar-extension-functor"
+++
(1) $D(T_{\mathrm{proét}},A)$ has K-flat resolutions, so the derived tensor
product is defined and exact in each variable; the $B_T$-module structure
comes from the right factor, so $(-)_B$ lands in $D(T_{\mathrm{proét}},B)$ and
is functorial.

(2) *Tor amplitude.* By [lem-sf-flat-model] (its statement for an arbitrary
scheme on the pro-étale site; no constructibility of the terms is needed), $K$ is
represented by a bounded complex $P$ in degrees $[a,b]$ of flat $A_T$-modules.
Then $K_B$ is represented by the termwise tensor product $P\otimes_{A_T}B_T$, a
bounded complex in degrees $[a,b]$ of flat $B_T$-modules (flatness is preserved by
base change), and its Tor amplitude over $B_T$ lies in $[a,b]$ since for every
$B_T$-module $N$, $K_B\otimes^{\mathbf L}_{B_T}N\simeq P\otimes_{A_T}N$ is computed by
the complex $P\otimes_{A_T}N$ in degrees $[a,b]$.

*Constructibility.* Since $A$ is Noetherian and $B$ is a finite $A$-module, choose a
resolution $F\to B$ by finite free $A$-modules $F^{-i}=A^{n_i}$, and let
$F_{\geq-N}$ be its stupid truncation. The cone of $F_{\geq-N}\to F$ is
concentrated in degrees $\leq-N-1$, so, $K$ having Tor amplitude in $[a,b]$,
$K\otimes^{\mathbf L}_A F_{\geq-N}\to K\otimes^{\mathbf L}_AF\simeq K_B$ induces
isomorphisms on $\mathcal H^r$ for $r>b-N$. The left side is a finite iterated
cone of the objects $K^{\oplus n_i}[i]$, $0\le i\le N$, of
$D^b_c(T_{\mathrm{proét}},A)$, hence has constructible cohomology sheaves. Taking
$N$ large for each $r\in[a,b]$ shows that the cohomology sheaves of $K_B$ are
constructible, so $K_B\in\Dctf(T_{\mathrm{proét}},B)$.

(3) A locally free module is flat, so the derived tensor product is the
ordinary one, which is locally $A_T\otimes_{A_T}B_T=B_T$. The Tate sheaf
$A_T(r)$ is $(\mathbf Z/\ell^m)_T(r)\otimes A_T$ for $\ell^mA=0$, and
associativity of the ordinary tensor product gives $(A_T(r))_B\simeq B_T(r)$.

(4) For a K-flat representative $P$ of $K$, $P\otimes_{A_T}B_T$ is K-flat over
$B_T$ (since $(P\otimes_{A_T}B_T)\otimes_{B_T}N=P\otimes_{A_T}N$), so
$(K_B)_C$ is represented by $(P\otimes_{A_T}B_T)\otimes_{B_T}C_T$, and the
associativity isomorphism of tensor products of sheaves of modules
$(P\otimes_{A_T}B_T)\otimes_{B_T}C_T\cong P\otimes_{A_T}C_T$ defines
$\alpha_K$. It is natural because the associativity isomorphism of modules is,
it is the identity for $B=C$ by the unit isomorphism, and the pentagon for
$A\to B\to C\to D$ is the pentagon of the associativity isomorphisms of the
tensor product of modules.
