+++
kind = "proof"
of = "lemma-integral-models--2"
order = 294005
uses = ["proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "theorem-comparison-constructible-sheaves", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "proposition-topos-functoriality--3", "definition-w-local-w-strictly-local--4", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-exact-products--1", "proposition-milnor-sequence--3", "definition-classical-pro-etale-sheaves--1", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--2", "corollary-finite-tor-amplitude-under-comparison--1", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--5", "lemma-local-constancy-finite-level--1", "lemma-integral-models--1", "lemma-acyclic-resolutions--1", "proposition-sp-unique-adjoint--1"]
+++
In (1) and (2) we compare two coefficient sheaves related by a flat map
that is an isomorphism modulo every $\pi_E^n$, so they have the same
derived complete objects. For (3)
we use the two characterizations of integral constructibility. For (4) we
combine the dévissage of
Corollary [corollary-coefficient-heart-b] with the lattices of
Lemma [lemma-lattices-after-finite-stratification].

(1) and (2). The map from the constant sheaf $\mathcal O_E$ to
$\mathcal O_{E,X}$ is flat and induces isomorphisms modulo every
$\pi_E^n$ [Stacks, [099L](https://stacks.math.columbia.edu/tag/099L)]. Hence by [Stacks, [099I](https://stacks.math.columbia.edu/tag/099I)] restriction of scalars
is an equivalence on derived complete objects, which is (1).
By [Stacks, [09C1](https://stacks.math.columbia.edu/tag/09C1)], an object of $\Dc(X,\mathcal O_E)$ is a derived complete
complex whose reduction modulo $\pi_E$ is constructible of finite Tor
dimension over $\mathbf F_E$. Over the field $\mathbf F_E$ every
bounded complex has finite Tor dimension. So this
description agrees with the description of $\Dbc(X,\mathcal O_E)$ in
Proposition [proposition-integral-constructibility-criterion], and
together with (1) this gives (2).

*Source:* the proof of Lemma [lemma-integral-models].
