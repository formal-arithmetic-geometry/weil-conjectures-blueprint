+++
kind = "proof"
of = "det-pe-finite-tor-comparison-noetherian"
+++
*Flatness is preserved.* For Noetherian $\Lambda$ the inverse image of a flat
étale $\Lambda$-module sheaf is flat, by [lem-exc-constant-inverse-image-flat].

*Tor amplitude is preserved.* Suppose $K$ has Tor amplitude in $[a,b]$. As in
[lem-exc-comparison-tor-interval], choose a bounded-above flat resolution $P$ of
$K$ with $P^q=0$ for $q>b$; the cokernel $Q=\operatorname{coker}(P^{a-1}\to P^a)$
is flat since $\operatorname{Tor}_1(Q,N)=H^{a-1}(P\otimes N)=0$ for all $N$, and
$[Q\to P^{a+1}\to\dots\to P^b]$ is a flat representative of $K$ in degrees
$[a,b]$. Its termwise pullback is a bounded complex of flat sheaves representing
$\nu_X^*K$ (exactness of $\nu_X^*$), hence K-flat, and tensoring it with any
pro-étale module sheaf gives a complex in degrees $[a,b]$.

*Tor amplitude is detected.* Suppose $\nu_X^*K$ has Tor amplitude in $[a,b]$ and
let $N$ be an étale module sheaf. Taking bounded-above flat resolutions of $K$
and $N$, whose pullbacks stay flat, and using that $\nu_X^*$ is exact and commutes
with tensor products and direct sums, we get
$\nu_X^*(K\otimes^{\mathrm L}_\Lambda N)\cong
\nu_X^*K\otimes^{\mathrm L}_{\Lambda_X}\nu_X^*N$, which has cohomology only in
$[a,b]$. Since $\nu_X^*$ is exact and faithful on module sheaves,
$H^q(K\otimes^{\mathrm L}N)=0$ whenever $\nu_X^*H^q(K\otimes^{\mathrm L}N)=0$.
So $K$ has Tor amplitude in $[a,b]$.

*The equivalence.* The functor $\nu_X^*$ is an equivalence
$D^b_c(X_{\Et},\Lambda)\to\Dbc(X,\Lambda)$ by
[lem-sf-proetale-constructible-origin], so by the two previous paragraphs an object has finite Tor amplitude if and only if its image does, so
the equivalence restricts to the full subcategories of objects of finite Tor
amplitude.
