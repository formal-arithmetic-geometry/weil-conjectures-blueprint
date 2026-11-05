+++
kind = "proof"
of = "lemma-reduction-derived-nakayama"
order = 211
uses = ["corollary-finite-quotients-their-transition-maps", "lemma-reduction-derived-nakayama--1", "lemma-reduction-derived-nakayama--2", "lemma-reduction-derived-nakayama--3"]
+++
The first assertion follows from the two-term resolution of
$(\mathcal O_E/\pi_E^n)_X$ in
Corollary [corollary-finite-quotients-their-transition-maps]. Tensoring $K$ with the short exact sequence
$0\to\pi_E^n\mathcal O_E/\pi_E^{n+1}\to\mathcal O_E/\pi_E^{n+1}\to
\mathcal O_E/\pi_E^n\to0$, whose first term is isomorphic to
$\mathcal O_E/\pi_E$, gives a triangle $K_1\to K_{n+1}\to K_n$. By
induction $K_1=0$ implies $K_n=0$ for all $n$. Then the derived limit of
the $K_n$ vanishes, and $K=0$ by completeness.

For the last assertion, let $u:K\to L$ be a morphism of derived complete
complexes and $C$ its cone. Derived completeness is preserved by cones,
since both sides of the completion map are exact functors of $K$, so $C$
is derived complete. Reduction modulo $\pi_E$ is exact, so $C_1$ is the
cone of $u_1:K_1\to L_1$, which vanishes when $u_1$ is an isomorphism.
Hence $C=0$, and $u$ is an isomorphism.
