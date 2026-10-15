+++
kind  = "proof"
of    = "det-nagata-density-normalization-sheaves"
uses = ["det-nagata-density-normalization-setup", "sk-prop-sf-open-closed-triangle"]
+++
*Step 1: the operations are exact.* By
part (2) of [det-nagata-density-normalization-setup], $\overline X$ is qcqs,
$j_V:V\hookrightarrow\overline X$ is a quasi-compact open immersion, and
$i:Z\hookrightarrow\overline X$ is its closed complement. The open–closed
proposition ([sk-prop-sf-open-closed-triangle]) therefore applies to the
pair $(j_V,i)$ on $\overline X$: $i^*$ and $i_*$ are exact, and every
$\Lambda_{\overline X}$-module sheaf $N$ sits in a natural exact sequence

$$
0\longrightarrow j_{V,!}j_V^*N\longrightarrow N\xrightarrow{\ \eta\ }
i_*i^*N\longrightarrow0 .
$$

It applies likewise to the quasi-compact open immersions $j$ and $j_Z$
(quasi-compact by part (1) of [det-nagata-density-normalization-setup]), so $j_!$ and
$j_{Z,!}$ are exact.

*Step 2: base change.* By part (3) of [det-nagata-density-normalization-setup], the
square with sides $j_Z:X\to Z$, $i:Z\to\overline X$, $j:X\to\overline X$
and $\mathrm{id}_X$ is cartesian. Compatibility of extension by zero with
base change in open–closed squares gives a natural isomorphism
$i^*j_!M\simeq j_{Z,!}M$.

*Step 3: the restriction to $V$ vanishes.* Again by
part (3) of [det-nagata-density-normalization-setup], $X\times_{\overline X}V$ is
empty, so base change along $j_V$ gives $j_V^*j_!M\simeq0$: extension by
zero along $j$ is supported on $X$.

*Step 4: conclusion for sheaves.* Apply the exact sequence of Step 1 to
$N=j_!M$. Its first term $j_{V,!}j_V^*j_!M$ vanishes by Step 3, so
$\eta:j_!M\to i_*i^*j_!M$ is injective and surjective, i.e. an isomorphism.
Composing with $i_*$ of the isomorphism of Step 2 gives
$j_!M\simeq i_*j_{Z,!}M$, natural in $M$.

*Step 5: complexes.* The functors $j_!$, $j_{Z,!}$ and $i_*$ are exact, so on
the derived category they are computed by applying them degreewise to any
representing complex, and they preserve quasi-isomorphisms. The natural
isomorphism of Step 4 applied in each degree is compatible with the
differentials by naturality, so it is an isomorphism of complexes
$j_!K\simeq i_*j_{Z,!}K$ for every unbounded complex $K$, and it descends to
$D(\overline X_{\mathrm{pro\acute{e}t}},\Lambda_{\overline X})$.
