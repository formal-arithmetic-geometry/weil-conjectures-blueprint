+++
id = "lemma-openclosed-stalk-lowerstar"
kind = "lemma"
title = "Stalks of $i_*$ on $Z$"
order = 1863
lean = ["AlgebraicGeometry.Etale.lowerStarCompSheafFiberIso", "AlgebraicGeometry.Scheme.initial_pointSmallEtaleElementsBaseChange"]
uses = ["def-kun-separably-closed"]
+++
Let $i\colon Z\to X$ be a closed immersion, let $\bar z$ be a geometric point
of $Z$ and write $\bar x:=i\circ\bar z$ for the corresponding geometric point
of $X$. Then the base-change functor

$$
\Phi\colon\mathrm N(\bar x)\to\mathrm N(\bar z),
\qquad(V,\bar v)\mapsto(V\times_XZ,\bar z),
$$

on the categories $\mathrm N(\bar x)$, $\mathrm N(\bar z)$ of pointed étale
neighbourhoods is initial. Consequently, for every
$\mathcal H\in\shv{\et Z}$,

$$
(i_*\mathcal H)_{\bar x}\cong\mathcal H_{\bar z},
$$

naturally in $\mathcal H$.
