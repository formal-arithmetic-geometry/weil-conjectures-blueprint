+++
id = "sk-prop-first-formula"
kind = "proposition"
title = "P4: the constant sheaf and the skyscraper are exchanged"
order = 2700
lean = ["AlgebraicGeometry.Etale.fourierTransformUnitIso", "AlgebraicGeometry.Etale.fourierTransformSkyscraperZeroIso"]
uses = ["sk-lem-as-properties", "sk-prop-stalk", "sk-thm-derived-duality", "sk-thm-frobenius"]
tags = ["sketch"]
+++
Let $k$ be finite or algebraically closed and $V=\Aone_k$; let
$\underline{E}$ be the constant sheaf with value $E$, the unit of
$\Dbc(-,E)$, and $\delta_0=i_{0*}\underline{E}$ the skyscraper with value
$E$ at the origin $i_0:\{0\}\hookrightarrow V^\vee$ (resp. $V$), in degree
$0$. Then, in $\Dbc(V^\vee,E)$,

$$
\FT_\psi(\underline{E})\cong\delta_0(-1)[-1],\qquad
\FT_\psi(\delta_0)\cong\underline{E}[1],
$$

$(-1)$ being the Tate twist of [sk-def-fourier-set]. (The transform is
$E$-linear; the same formulas for the constant sheaf $\Qlb$ and the
$\Qlb$-skyscraper follow by the extension of scalars $-\otimes_E\Qlb$.)
