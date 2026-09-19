+++
id = "def-weil-pbc-derived-exchange"
kind = "definition"
title = "Derived exchange map"
order = 647
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus"]
uses = ["def-weil-pbc-underived-exchange"]
+++
For $K\in D^+(X_{\mathrm{et}})$ choose an injective resolution
$K\xrightarrow{\simeq}I^\bullet$. Apply
$\operatorname{Ex}_{\square,I^r}$ in every degree and use the naturality
lemma to obtain a morphism of complexes

$$
g^{-1}f_*I^\bullet\longrightarrow f'_*g'^{-1}I^\bullet.
$$

Choose a K-injective replacement
$g'^{-1}I^\bullet\xrightarrow{\simeq}J^\bullet$ in the Grothendieck
category of etale abelian sheaves on $X'$. Compose the displayed map with
$f'_*g'^{-1}I^\bullet\to f'_*J^\bullet$ and define

$$
\operatorname{Ex}_{\square,K}:g^{-1}f_*I^\bullet\longrightarrow f'_*J^\bullet
$$

to be its class in $D^+(Y'_{\mathrm{et}})$. The target complex is a model
for $Rf'_*g'^{-1}K$, since $J^\bullet$ is K-injective; the source is a model
for $g^{-1}Rf_*K$ because $g^{-1}$ is exact.
Its class in $D^+(Y'_{\mathrm{et}})$ is

$$
\operatorname{Ex}_{\square,K}:g^{-1}Rf_*K\longrightarrow
Rf'_*g'^{-1}K.
$$
