+++
kind = "proof"
of = "lemma-proper-direct-image-unbounded-complexes--3"
order = 487007
uses = ["definition-lisse-sheaves", "definition-ind-etale-pro-etale-weakly--1", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--3", "definition-constructible-sheaves--4", "lemma-constructible-sheaves--3", "lemma-constructible-sheaves--6", "proposition-ind-constructible-sheaves--2", "proposition-ind-constructible-sheaves--3", "proposition-ind-constructible-sheaves--7", "lemma-proper-direct-image-unbounded-complexes--1", "definition-compactification-refinement--1", "definition-relative-picard-functor--2"]
+++
The finite window used here is clause [lemma-proper-direct-image-unbounded-complexes--2].

*Direct sums, assertion (3).* The window (5.6)
reduces us to families with cohomology in a common finite interval. For
such a family $(M_\alpha)$ we show by induction on the length of the interval
that the map
$\bigoplus_\alpha Rp_*M_\alpha\to Rp_*(\bigoplus_\alpha M_\alpha)$ is an
isomorphism. For length zero,
$M_\alpha$ is a shifted object of $\IndCons(X,\Lambda)$, and the claim is
the assertion about direct sums in Lemma [lemma-uniform-bound-proper-direct-image], in
each degree. For the inductive step, we take the direct sum of the truncation
triangles that split off the top cohomology sheaf and apply the five lemma
to the long exact cohomology sequences.

Now let $(K_\alpha)$ be arbitrary and fix $q$. Since direct sums of sheaves
are exact, cohomology and truncations commute with direct sums. The
objects $\tau_{\geq q-2d-1}\tau_{\leq q}K_\alpha$ have cohomology in the
common interval $[q-2d-1,q]$. Applying (5.6) to each
$K_\alpha$ and to $\bigoplus_\alpha K_\alpha$, and the first paragraph to
the truncated family, we see that
$\bigoplus_\alpha Rp_*K_\alpha\to Rp_*(\bigoplus_\alpha K_\alpha)$ is an
isomorphism on $\mathcal H^q$. Since $q$ is arbitrary, the map is an isomorphism.

*Source:* the proof of Lemma [lemma-proper-direct-image-unbounded-complexes].
