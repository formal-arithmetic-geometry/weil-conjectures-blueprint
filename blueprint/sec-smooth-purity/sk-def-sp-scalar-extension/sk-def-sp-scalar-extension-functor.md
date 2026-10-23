+++
id = "det-sp-scalar-extension-functor"
kind = "definition"
title = "The derived extension-of-coefficients functor and its associativity"
order = 2969
uses = ["lem-sf-flat-model"]
+++
Let $A\to B\to C$ be maps of finite commutative rings killed by a power of
$\ell$, and $T$ a scheme; write $A_T,B_T,C_T$ for the constant coefficient
sheaves on $T_{\mathrm{proét}}$.

1. *Functor.* The derived tensor product
   $(-)_B=-\otimes^{\mathbf L}_{A_T}B_T:D(T_{\mathrm{proét}},A)\to D(T_{\mathrm{proét}},B)$,
   computed on a K-flat representative and regarded as a complex of
   $B_T$-modules through the right factor, sends a morphism $u$ to
   $u_B=u\otimes^{\mathbf L}\mathrm{id}_{B_T}$. It is an exact functor of
   triangulated categories.
2. *Preservation of $\Dctf$.* If $K\in\Dctf(T_{\mathrm{proét}},A)$ has Tor
   amplitude in $[a,b]$, then $K_B\in\Dctf(T_{\mathrm{proét}},B)$ with Tor
   amplitude in $[a,b]$.
3. *Free rank-one sheaves.* If $L$ is a locally free $A_T$-module of rank one
   (for instance a Tate sheaf $A_T(r)$), then $L_B=L\otimes_{A_T}B_T$ is the
   ordinary tensor product, locally free of rank one over $B_T$, and
   $(A_T(r))_B\simeq B_T(r)$.
4. *Associativity.* There is an isomorphism
   $\alpha_K:(K_B)_C\xrightarrow{\sim}K_C$ in $D(T_{\mathrm{proét}},C)$, natural in
   $K$ (so $\alpha_L\circ(u_B)_C=u_C\circ\alpha_K$ for $u:K\to L$), with
   $\alpha$ the identity when $B=C$, and satisfying the evident pentagon for a
   chain $A\to B\to C\to D$.
