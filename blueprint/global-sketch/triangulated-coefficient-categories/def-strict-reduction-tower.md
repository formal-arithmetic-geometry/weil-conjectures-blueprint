+++
id = "def-strict-reduction-tower"
kind = "definition"
title = "Strict reduction tower and derived inverse limit"
order = 11
uses = ["def-finite-reduction", "def-weil-finite-coefficient-datum"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
A strict reduction tower on $Y$ is a sequence of complexes

$$
C_n\in
C\bigl(\Sh(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y)\bigr)
\qquad(n\geq1)
$$

together with actual transition chain maps
$\operatorname{Res}_{Y,n+1}C_{n+1}\to \operatorname{Res}_{Y,n}C_n$ of
$\widehat{\mathcal O}_{E,Y}$-module complexes. Their composites are
required to agree literally, and the induced derived comparison

$$
(\mathcal O_E/\varpi_E^n)_Y
\otimes^L_{(\mathcal O_E/\varpi_E^{n+1})_Y} C_{n+1}
\xrightarrow{\sim} C_n
$$

is required to be an isomorphism. To derive inverse limit, regard this
system as an object of the abelian category of *all* inverse systems of
$\widehat{\mathcal O}_{E,Y}$-module complexes and take a K-injective
replacement there. Strict reduction compatibility is a property of the
chosen system; no assertion that strict compatible systems themselves form
an abelian subcategory is being made. This defines
$R\varprojlim_n\operatorname{Res}_{Y,n}C_n$ in
$D(Y_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y})$, characterized
by the functorial Milnor triangle

$$
R\varprojlim_n\operatorname{Res}_{Y,n}C_n\longrightarrow
\prod_{n\geq1}\operatorname{Res}_{Y,n}C_n
\xrightarrow{1-\mathrm{shift}}
\prod_{n\geq1}\operatorname{Res}_{Y,n}C_n
\longrightarrow
\bigl(R\varprojlim_n\operatorname{Res}_{Y,n}C_n\bigr)[1].
$$
