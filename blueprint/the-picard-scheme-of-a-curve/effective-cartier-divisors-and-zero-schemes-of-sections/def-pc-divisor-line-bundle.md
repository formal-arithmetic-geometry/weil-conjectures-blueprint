+++
id = "def-pc-divisor-line-bundle"
kind = "definition"
title = "The module O_X(D) of an effective Cartier divisor"
order = 4223
lean = ["AlgebraicGeometry.divisorLineBundle"]
+++
Let $S$ be a scheme and let $D\subset S$ be an effective Cartier divisor
with ideal sheaf $\mathcal{I}_D$. The associated module is
$$
 \mathcal O_S(D):=\mathcal I_D^{\vee},
$$
the dual of the ideal sheaf, which is invertible because $\mathcal I_D$ is;
its canonical section is the inclusion
$\mathcal I_D\hookrightarrow\mathcal O_S$.

*Import note.* The body of this definition is truncated in the source: it
reads only "Let $S$ be a scheme and let $D\subset S$ be an effective
Cartier divisor with ideal sheaf $\mathcal I_D$." and then ends, with the
module itself never named. The display above states the construction whose
properties [lem-pc-divisor-line-bundle-properties] proves — that
$\mathcal O_S(D)$ is invertible with a canonical section whose zero scheme
is $D$ — and the reconstruction is flagged here rather than left silent.

Unresolved dependencies: def:sc-effective-cartier-divisor, def:sc-invertible-module, def:sc-divisor
