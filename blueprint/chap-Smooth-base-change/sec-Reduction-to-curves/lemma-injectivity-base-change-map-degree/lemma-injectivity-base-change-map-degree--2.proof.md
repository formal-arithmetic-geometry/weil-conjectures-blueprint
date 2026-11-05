+++
kind = "proof"
of = "lemma-injectivity-base-change-map-degree--2"
order = 672005
uses = ["definition-derived-base-change-map", "lemma-injectivity-base-change-map-degree--3"]
+++
Embed $N$ into an injective sheaf $I$. Naturality of the base change
map gives the map on cokernels. Since $g^{-1}R^qf_*I=0$, the maps
from $M$ and $N$ to $I$ also induce maps from their cokernels to
$R^qf'_*g'^{-1}I$. By the universal property of the cokernel, the
composite

$$
\operatorname{coker}(b_M^q)\longrightarrow
\operatorname{coker}(b_N^q)\longrightarrow R^qf'_*g'^{-1}I
$$

is the map induced by $M\hookrightarrow N\hookrightarrow I$.
It is injective by [lemma-injectivity-base-change-map-degree--3].
Hence its first factor is injective.
