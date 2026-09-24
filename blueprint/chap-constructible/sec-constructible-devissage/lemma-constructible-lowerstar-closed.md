+++
id = "lemma-constructible-lowerstar-closed"
kind = "lemma"
title = "Pushforward along a closed immersion"
order = 1066
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.lowerStar_of_isClosedImmersion"]
uses = ["lemma-openclosed-vanishing-lowerstar", "prop-constructible-open-closed", "prop-openclosed-lowerstar-fully-faithful"]
+++
If $\mathcal G\in\shv{\et Z}$ is constructible, then so is
$i_*\mathcal G$.

## Proof

By [prop-constructible-open-closed] it suffices to see that
$j^*i_*\mathcal G$ and $i^*i_*\mathcal G$ are constructible. The first is
zero by [lemma-openclosed-vanishing-lowerstar], and the zero sheaf is
constructible (the trivial stratification with one stratum; the zero sheaf
is constant with finite stalks). The second is isomorphic to $\mathcal G$
by the counit isomorphism of
[prop-openclosed-lowerstar-fully-faithful], hence constructible by
[lemma-constructible-iso-invariance].
