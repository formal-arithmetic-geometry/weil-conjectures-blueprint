+++
kind = "proof"
of = "lemma-kunneth-formula-compact-supports--1"
order = 1222001
uses = ["proposition-construction-independence-rf-shriek", "proposition-proper-direct-image-extension-zero", "proposition-composition-base-change-rf-shriek"]
+++
Choose compactifications $Z\xrightarrow{j}\overline Z\xrightarrow{r}X$
of $u$ and $X\xrightarrow{i}\overline X\xrightarrow{s}S$ of $f$.
Compactify $i\circ r$ as
$\overline Z\xrightarrow{j'}W\xrightarrow{r'}\overline X$ so that
the square formed by $r,j',i,r'$ is cartesian. The exchange map
$i_!Rr_*\to Rr'_*j'_!$ is an isomorphism, as expressed by
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerStarOpenImmersionLowerShriekExchange_padicAlgCl`.
Its inverse, together with composition for proper direct images and
for extension by zero, identifies
$R(s\circ r')_*(j'\circ j)_!$ with $Rf_!Ru_!$.
Independence of compactification identifies the former with
$R(f\circ u)_!$. All these identifications are natural.
