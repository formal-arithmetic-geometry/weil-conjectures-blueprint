+++
kind = "proof"
of = "corollary-finite-quotients-their-transition-maps--2"
order = 181004
uses = ["lemma-reduction-derived-nakayama--1"]
+++
Write $q_n:R\to B_n$ for the quotient map of clause [corollary-finite-quotients-their-transition-maps--1]. Since
$q_n\circ\pi_E^n=0$ by exactness of that sequence in the middle, the zero map
in degree $-1$ and $q_n$ in degree $0$ form a chain map
$[R\xrightarrow{\pi_E^n}R]\to B_n[0]$. The cohomology of the two-term complex
is $\ker(\pi_E^n)$ in degree $-1$ and $\coker(\pi_E^n)$ in degree $0$. By
clause [corollary-finite-quotients-their-transition-maps--1] the kernel is zero and $q_n$ induces an isomorphism
$\coker(\pi_E^n)\simeq B_n$. Hence the augmentation is a quasi-isomorphism.

The pair $(\pi_E,\mathrm{id})$ is a chain map from
$[R\xrightarrow{\pi_E^{n+1}}R]$ to $[R\xrightarrow{\pi_E^n}R]$, because
$\pi_E^n\circ\pi_E=\pi_E^{n+1}=\mathrm{id}\circ\pi_E^{n+1}$. In degree $0$
it is the identity of $R$, and the reduction map $r:B_{n+1}\to B_n$ satisfies
$r\circ q_{n+1}=q_n$. So the square formed by the two augmentations,
$(\pi_E,\mathrm{id})$ and $r[0]$ commutes already on the level of complexes.
Since the augmentations are quasi-isomorphisms, $(\pi_E,\mathrm{id})$
represents $r$ in $D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$.

*Source:* the proof of Corollary [corollary-finite-quotients-their-transition-maps].
