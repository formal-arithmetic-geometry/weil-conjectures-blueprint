+++
kind = "proof"
of = "lemma-integral-models--6"
order = 294013
uses = ["proposition-pro-etale-affines-form-basis", "definition-lisse-sheaves", "lemma-lattices-after-finite-stratification", "definition-ind-etale-pro-etale-weakly--2", "lemma-stability--6", "lemma-stability--7", "proposition-pro-etale-coverings--2", "lemma-extremally-disconnected-covers--3", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "lemma-acyclicity-pulled-back-injectives--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "definition-local-cohomology--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--2", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-constructible-sheaves--8", "corollary-coefficient-heart-b--2", "lemma-descent-finite-coefficient-field--2", "lemma-acyclic-resolutions--1", "proposition-comparison-etale-derived-category--5", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1"]
+++
(4) For $\overline{\mathbf Q}_\ell$, we first descend to a finite $E$ by
Lemma [lemma-descent-finite-coefficient-field]. By
Corollary [corollary-coefficient-heart-b], every object of $\Dbc(X,E)$ is
obtained by finitely many cones and shifts from sheaves $a_!L$ with $L$
lisse. We refine the stratum $S$ by a finite stratification as in
Lemma [lemma-lattices-after-finite-stratification]. This replaces $a_!L$
by finitely many extensions of such sheaves, and on each new stratum $L$
contains a lattice $L_0$ with $L_0[1/\ell]=L$. Then $a_!L=(a_!L_0)[1/\ell]$.
The reduction of $L_0$ modulo $\pi_E^n$ is a locally constant sheaf of
finitely presented $\mathcal O_E/\pi_E^n$-modules, so it comes from the
étale site by [Stacks, [099Y](https://stacks.math.columbia.edu/tag/099Y)]. Thus $L_0\in\Dbc(S,\mathcal O_E)$, and
$a_!L_0\in\Dbc(X,\mathcal O_E)$ by (3).

*Source:* the proof of Lemma [lemma-integral-models].
