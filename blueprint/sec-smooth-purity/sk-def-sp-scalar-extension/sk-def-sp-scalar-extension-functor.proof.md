+++
kind = "proof"
of = "det-sp-scalar-extension-functor"
+++
(1) $D(T_{\mathrm{proét}},A)$ has K-flat resolutions, so the derived tensor
product is defined and exact in each variable; the $B_T$-module structure
comes from the right factor, so $(-)_B$ lands in $D(T_{\mathrm{proét}},B)$ and
is functorial.

(2) By [lem-sf-flat-model], $K$ is represented by a bounded complex $P$ in
degrees $[a,b]$ of flat constructible $A_T$-modules. Then $K_B$ is represented
by the termwise tensor product $P\otimes_{A_T}B_T$, a bounded complex in
degrees $[a,b]$ of flat $B_T$-modules (flatness is preserved by base change),
whose terms are constructible: on each stratum where a term of $P$ is locally
constant with finite stalks, so is its tensor with the finite constant sheaf
$B_T$. Its cohomology sheaves are therefore constructible, and its Tor
amplitude over $B_T$ lies in $[a,b]$ since for every $B_T$-module $N$,
$K_B\otimes^{\mathbf L}_{B_T}N\simeq P\otimes_{A_T}N$ is computed by the
complex $P\otimes_{A_T}N$ in degrees $[a,b]$.

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
