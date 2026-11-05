+++
id = "lemma-tangent-cones-on-cover--1"
kind = "lemma"
title = "The surface and curves of a common cover"
name_showing = false
order = 984001
aliases = ["bp-r300-1"]
lean = ["AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.regular", "AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.isFinite_π", "AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.etale_π", "AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.isDiscreteValuationRing_H'", "AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.exists_puncturedDiagonal_finite_etale"]
uses = ["lemma-covers-degree-prime-to-ell"]
+++
Let $k$ be algebraically closed, let $X$ be a separated quasi-compact smooth
curve over $k$, and let $h:X\to X$ be a $k$-endomorphism fixing a $k$-point
$y$, with $h^\#\mathfrak m_y\subseteq\mathfrak m_y^2$. Take a common
cover datum as in the Lean construction of Lemma
[lemma-covers-degree-prime-to-ell]: a separated smooth curve $C$ over $k$,
a morphism $p:C\to X$ finite over an open neighbourhood of $y$ and étale
over a punctured neighbourhood of $y$, and a $k$-point $c$ over $y$ with
ramification index $e\geq1$ prime to $\ell$. The same cover is used on both
factors.

Let $T$ be the strict localization of $X\times_k X$ at $(y,y)$, and write
$\Gamma,\Delta,V,H$ for the transposed graph of $h$, the diagonal and the
two axes in $T$. Let $T'$ be the strict localization of $C\times_k C$ at
$y'=(c,c)$, with the induced morphism $\pi:T'\to T$. Write

$$
D'=(\pi^{-1}(\Gamma\cup V))_{\mathrm{red}},\qquad
H'_{\mathrm{red}}=(\pi^{-1}H)_{\mathrm{red}},\qquad
\Delta'_{\mathrm{red}}=(\pi^{-1}\Delta)_{\mathrm{red}}.
$$

Then $T'$ is the strict localization of a smooth surface, and its strict
local ring $R'$ is regular of dimension two. The morphism $\pi$ is finite
and étale over $T-(H\cup V)$. The ring
$\Gamma(H'_{\mathrm{red}},\mathcal O)$ is a discrete valuation ring. Moreover,
the induced morphism

$$
\Delta'_{\mathrm{red}}-D'\longrightarrow\Delta-y
$$

is finite étale with $e^2$ points in every geometric fibre, compatibly
with the maps to $T-(\Gamma\cup V)$.
