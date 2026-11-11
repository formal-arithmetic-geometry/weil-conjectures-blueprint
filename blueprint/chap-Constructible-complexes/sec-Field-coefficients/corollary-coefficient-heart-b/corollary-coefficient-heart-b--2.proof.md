+++
kind = "proof"
of = "corollary-coefficient-heart-b--2"
order = 273005
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "definition-constructible-sheaves--1", "definition-constructible-sheaves--2", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-constructible-sheaves--7", "lemma-constructible-sheaves--8", "corollary-coefficient-heart-b--1", "lemma-acyclic-resolutions--1", "proposition-sp-unique-adjoint--1"]
+++
For the second assertion, we argue by induction on the number of nonzero
cohomology sheaves of $K$. If $i$ is the largest degree with $\mathcal H^i(K)\ne0$,
the truncation triangle $\tau_{<i}K\to K\to\mathcal H^i(K)[-i]\to$
exhibits $K$ as the cone of a map
$\mathcal H^i(K)[-i-1]\to\tau_{<i}K$, and $\tau_{<i}K$ has fewer nonzero
cohomology sheaves. This reduces
the claim to a single shifted constructible sheaf. The filtration of this
sheaf from Lemma [lemma-constructible-sheaves](3) yields finitely many short
exact sequences, that is, distinguished triangles, with terms $a_!L$.

*Source:* the proof of Corollary [corollary-coefficient-heart-b].
