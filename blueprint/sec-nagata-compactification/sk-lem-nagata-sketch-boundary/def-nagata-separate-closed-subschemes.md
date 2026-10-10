+++
id = "def-nagata-separate-closed-subschemes"
kind = "definition"
title = "Closed-boundary separation blow-up"
order = 247
lean = ["AlgebraicGeometry.separationBlowup"]
uses = ["def-nagata-admissible-blowup", "def-nagata-global-blowup", "def-nagata-strict-transform", "lemma-nagata-separate-closed-data-exists"]
+++
Let $X$ be a scheme, let $U\subseteq X$ be an open subscheme, and let
$\mathcal I_1,\mathcal I_2\subseteq\mathcal O_X$ be finite type
quasi-coherent ideals with closed subschemes $Z_i=V(\mathcal I_i)$ such that
$Z_1\cap Z_2\cap U=\varnothing$. Define
$\mathsf{SepBl}_U(Z_1,Z_2)\to X$ to be the blow-up of $X$ along the finite
type ideal $\mathcal I_1+\mathcal I_2$; since
$V(\mathcal I_1+\mathcal I_2)=Z_1\cap Z_2$ is disjoint from $U$, this is a
$U$-admissible blow-up.

When $X$ is qcqs, $U$ is quasi-compact and the $Z_i\hookrightarrow X$ are of
finite presentation, a different $U$-admissible separating blow-up comes from
the Tag 080P preparation: choose the centre $C\hookrightarrow Z$ of
[lemma-nagata-separate-closed-data-exists], where
$Z=V(\mathcal I_1\mathcal I_2)$, and blow up $X$ along the composite
finite-presentation centre $C\hookrightarrow Z\hookrightarrow X$. Since $C$
is disjoint from $Z\times_XU$, its image in $X$ is disjoint from $U$, so this
blow-up is also $U$-admissible.
