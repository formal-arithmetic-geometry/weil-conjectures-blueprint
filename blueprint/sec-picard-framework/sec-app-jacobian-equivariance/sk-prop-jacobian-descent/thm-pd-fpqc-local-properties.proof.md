+++
kind  = "proof"
of    = "thm-pd-fpqc-local-properties"
+++
For a field extension $k\subseteq K$ the morphism $\Spec(K)\to\Spec(k)$ is
surjective, flat and quasi-compact (both schemes are one point), so it is an
fpqc covering of $\Spec(k)$ in the sense of Stacks Project, Descent, Section
35.23, Tag [02YJ](https://stacks.math.columbia.edu/tag/02YJ); when $K/k$ is
finite it is moreover a surjective [def-pc-finite-locally-free] morphism. The
scheme $Z_K$ is the base change of [def-pc-base-change], and smoothness and
properness are the notions of [def-pc-morphism-conventions]. The square
formed by $Z_K\to Z$, $Z_K\to\Spec(K)$, $Z\to\Spec(k)$ and
$\Spec(K)\to\Spec(k)$ is cartesian, so every property of morphisms which is
local in the fpqc topology on the target holds for $Z\to\Spec(k)$ as soon as
it holds for $Z_K\to\Spec(K)$.

*(1) Being of finite type and smooth.* Quasi-compactness, being locally of finite
presentation (Stacks Project, Descent, Section 35.23, Tag
[02YJ](https://stacks.math.columbia.edu/tag/02YJ)) and smoothness (Lemma
35.23.29, Tag [02VL](https://stacks.math.columbia.edu/tag/02VL)) are fpqc
local on the target; hence $Z\to\Spec(k)$ is quasi-compact, locally of finite presentation,
in particular of finite type, and smooth. This is the same lemma that Stacks
Project, Lemma 39.9.4, Tag [0BFC](https://stacks.math.columbia.edu/tag/0BFC),
invokes for abelian varieties.

*(1) Properness.* This is one of the properties of morphisms proved to be
local in the fpqc topology on the target in Stacks Project, Descent, Section
35.23, Tag [02YJ](https://stacks.math.columbia.edu/tag/02YJ):
separatedness and universal closedness are separately in the list of that
section, and properness is their conjunction together with being of finite
type, which was settled above.

*(1) Connectedness.* The morphism $Z_K\to Z$ is the base change of the
surjective morphism $\Spec(K)\to\Spec(k)$, hence surjective. The image of a
connected space under a continuous map is connected, so $Z$ is connected
because $Z_K$ is.

*(2)* Properness and smoothness descend as in (1). The relative dimension is
read off on fibres: for $z\in Z$ and a point $z'\in Z_K$ over it, the fibre of
$Z_K$ through $z'$ is the base change of the fibre of $Z$ through $z$ along the
field extension $\kappa(z)\subseteq\kappa(z')$, and dimensions of schemes
locally of finite type over a field are invariant under field extension, so
$Z\to\Spec(k)$ is smooth of relative dimension $n$. For geometric
integrality, let $\Omega$ be a field over $k$ and choose a field $L$ containing
both $\Omega$ and $K$ over $k$ (a residue field of $\Omega\otimes_kK\neq0$).
Then $Z_L=Z_K\times_KL$ is integral, as $Z_K$ is geometrically integral, and
$Z_L\to Z_\Omega$ is faithfully flat. Reducedness descends along faithfully
flat morphisms, and $Z_\Omega$ is irreducible as the image of the irreducible
$Z_L$ under a surjection; so $Z_\Omega$ is integral and $Z$ is geometrically
integral over $k$.
