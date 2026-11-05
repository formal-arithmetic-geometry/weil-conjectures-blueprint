+++
kind = "proof"
of = "proposition-pro-etale-site-separably-closed--1"
order = 173004
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-affines-form-basis", "proposition-pro-etale-coverings"]
+++
First identify $(\operatorname{Spec}\Omega)[S]$ with
$\operatorname{Spec}LC(S,\Omega)$. The required ring pushout follows by
evaluating maps at prime localizations and using characteristic functions
of clopen sets. Its underlying space is $S$, and maps between these test
objects correspond to continuous maps of profinite sets. Thus the test
functor is fully faithful.

For an affine weakly étale $\Omega$-scheme $\operatorname{Spec}B$, the
ring $B$ is absolutely flat. Each prime localization is a separable
algebraic field extension of $\Omega$, hence is $\Omega$. Moreover,
$\operatorname{Spec}B$ has a clopen basis and is profinite. The natural
map $LC(\operatorname{Spec}B,\Omega)\to B$ is bijective on local rings
and on spectra, hence is an isomorphism. This classifies the affine
objects; [proposition-pro-etale-affines-form-basis] then gives cover
density.

To reflect covers, take a finite affine refinement as in
[proposition-pro-etale-coverings]. The above identifications turn it
into a finite jointly surjective family of profinite sets. Conversely,
the relative test-object construction takes finite jointly surjective
families to fpqc covers. Their arrows are weakly étale, by the
cancellation and base-change properties of [lemma-stability], so they
are pro-étale covers. These arguments also include the empty object and
the empty covering family, and identify the induced topology with the
coherent topology.
