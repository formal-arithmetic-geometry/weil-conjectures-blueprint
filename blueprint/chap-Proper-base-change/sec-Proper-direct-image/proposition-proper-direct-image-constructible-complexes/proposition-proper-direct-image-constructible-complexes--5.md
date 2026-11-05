+++
id = "proposition-proper-direct-image-constructible-complexes--5"
kind = "proposition"
title = "Finite coefficients"
order = 425010
aliases = ["bp-r129-5"]
lean = ["AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_isProper"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "proposition-comparison-morphism-inverse-image--2", "definition-pro-etale-base-change-map--1"]
+++
Let $A$ be a finite commutative ring and let

$$
\begin{CD}
X' @>{g'}>> X\\
@V{p'}VV @VV{p}V\\
Y' @>{g}>> Y
\end{CD}
$$

be a cartesian square of schemes with $p$ proper. If
$K\in D(X_{\mathrm{pro}\acute{e}t},A)$ is the pullback of a complex in
$D^+(X_{\acute{e}t},A)$, then the base change map (4.5)

$$
g^*Rp_{*,A}K\longrightarrow Rp'_{*,A}g'^*K
$$

is an isomorphism. In particular this applies to bounded constructible complexes
of étale origin; no finite Tor-amplitude hypothesis is needed for this map.
