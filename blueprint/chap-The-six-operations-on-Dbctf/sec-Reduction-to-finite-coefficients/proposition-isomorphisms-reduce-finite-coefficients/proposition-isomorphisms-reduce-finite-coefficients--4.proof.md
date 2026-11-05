+++
kind = "proof"
of = "proposition-isomorphisms-reduce-finite-coefficients--4"
order = 653009
uses = ["proposition-isomorphisms-reduce-finite-coefficients--3", "proposition-dctf-x-qbar-2-colimit--2", "lemma-integral-models"]
+++
Descend $K$ to a finite extension $E$ by Proposition [proposition-dctf-x-qbar-2-colimit], and apply the preceding rational clause and the assumed compatibility for $E\to\overline{\mathbf Q}_\ell$.

For the exceptional base-change map, Lean combines descent and integral models in `AlgebraicGeometry.ProEtale.exists_padicAlgCl_iso_integralModel`. It transfers the map first along $\mathcal O_E\to E$, then along $E\to\overline{\mathbf Q}_\ell$, using the respective comparison isomorphisms. Naturality transports the resulting isomorphism from the chosen model to $K$. The formalized conclusion is about that particular base-change map, including its image under pullback, rather than arbitrary $F,G,\theta$.
