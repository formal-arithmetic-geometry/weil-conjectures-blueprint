+++
id = "thm-sf-comp-composition"
kind = "theorem"
title = "The composition law for $Rf_!$"
order = 2267
uses = ["cor-weil-pbc-constructible-complete", "cor-weil-pbc-geometric-fiber-finite", "cor-weil-pbc-geometric-fiber-finite-extension", "cor-weil-pbc-geometric-fiber-qbar", "def-weil-compactifications-refinements", "def-weil-pbc-proper-open-comparison", "def-weil-pbc-truncation-exact-couples", "lem-weil-pbc-clopen-section-direct-image", "lem-weil-pbc-exact-couple-differential", "lem-weil-pbc-open-section-clopen", "lem-weil-pbc-proper-open-comparison-composition", "lem-weil-pbc-proper-open-comparison-iso", "lem-weil-pbc-proper-open-comparison-proetale", "lem-weil-pbc-proper-open-identification", "lem-weil-pbc-proper-open-section", "lemma-weil-pbc-exact-couple-abutment", "lemma-weil-pbc-prime-proper-base-change", "lemma-weil-pbc-torsion-assembly", "prop-compactification-coherence-detailed", "prop-compactification-refinement", "prop-weil-proet-finite-proper-base-change", "rem-ptr-weil-pbc-proper-open-comparison-1", "thm-weil-pbc-bounded-below", "thm-weil-pbc-complete-proetale", "thm-weil-pbc-finite-extension", "thm-weil-pbc-finite-level-proetale", "thm-weil-pbc-qbar"]
+++
Let $f:X\to Y$ and $g:Y\to S$ be separated of finite type between finite-type
$k$-schemes. There is a canonical isomorphism

$$
\alpha_{g,f}:\ Rg_!Rf_!\ \xrightarrow{\ \sim\ }\ R(g\circ f)_!
$$

of functors $D^+(X,\Lambda)\to D^+(S,\Lambda)$ on étale-origin complexes,
independent of all compactification choices by [def-weil-pbc-proper-open-comparison], [lem-weil-pbc-clopen-section-direct-image], [lem-weil-pbc-open-section-clopen], [lem-weil-pbc-proper-open-comparison-composition], [lem-weil-pbc-proper-open-comparison-iso], [lem-weil-pbc-proper-open-comparison-proetale], [lem-weil-pbc-proper-open-identification], [lem-weil-pbc-proper-open-section], [prop-compactification-coherence-detailed], [rem-ptr-weil-pbc-proper-open-comparison-1],
equal to the identity when $f$ or $g$ is an identity, and associative:
for a third $h:S\to T$ the two composites
$Rh_!Rg_!Rf_!\to R(hgf)_!$ agree.

## Proof

*Construction.* Compactify $g$ as $Y\xrightarrow{v}\overline Y \xrightarrow{\bar g}S$, and compactify $v\circ f$ as
$X\xrightarrow{a}\overline X\xrightarrow{p}\overline Y$, using
[sk-thm-nagata-compactification]. Put $V=\overline X\times_{\overline Y}Y$,
with its open immersion $b:V\to\overline X$ and proper projection
$p_Y:V\to Y$. Since $p\circ a=v\circ f$, the morphism $a$ factors as
$a=b\circ c$ through an open immersion $c:X\to V$, so
$X\xrightarrow{c}V\xrightarrow{p_Y}Y$ is a compactification of $f$ and
$Rf_!=Rp_{Y*}c_!$ on that model. For every
étale-origin $N$ on $V$ the map

$$
v_!Rp_{Y*}N\ \longrightarrow\ Rp_*b_!N
$$

is an isomorphism: over $Y$ it is proper base change for the Cartesian square
defining $V$ ([cor-weil-pbc-constructible-complete], [cor-weil-pbc-geometric-fiber-finite], [cor-weil-pbc-geometric-fiber-finite-extension], [cor-weil-pbc-geometric-fiber-qbar], [def-weil-pbc-truncation-exact-couples], [lem-weil-pbc-exact-couple-differential], [lemma-weil-pbc-exact-couple-abutment], [lemma-weil-pbc-prime-proper-base-change], [lemma-weil-pbc-torsion-assembly], [prop-weil-proet-finite-proper-base-change], [thm-weil-pbc-bounded-below], [thm-weil-pbc-complete-proetale], [thm-weil-pbc-finite-extension], [thm-weil-pbc-finite-level-proetale], [thm-weil-pbc-qbar]), and at a geometric point of
$\overline Y$ outside $Y$ both sides vanish, because the corresponding fibre of
$p$ misses $V$. Apply this to the extension by zero of a complex on $X$ and
then push by $R\bar g_*$: extension by zero along opens composes termwise and
proper derived direct image composes, giving $\alpha_{g,f}$.

*Independence and associativity.* Any two choices are compared by
[def-weil-pbc-proper-open-comparison], [lem-weil-pbc-clopen-section-direct-image], [lem-weil-pbc-open-section-clopen], [lem-weil-pbc-proper-open-comparison-composition], [lem-weil-pbc-proper-open-comparison-iso], [lem-weil-pbc-proper-open-comparison-proetale], [lem-weil-pbc-proper-open-identification], [lem-weil-pbc-proper-open-section], [prop-compactification-coherence-detailed], [rem-ptr-weil-pbc-proper-open-comparison-1], which also makes $\alpha_{g,f}$ natural. For
three morphisms choose, by
[def-weil-compactifications-refinements], [prop-compactification-refinement] (i), a single common refinement of all
the compactifications involved; the two composites then restrict to the same
identity over the source and use the same proper base-change maps on each
Cartesian rectangle, so their pasting identity together with the refinement
transitivity of [def-weil-pbc-proper-open-comparison], [lem-weil-pbc-clopen-section-direct-image], [lem-weil-pbc-open-section-clopen], [lem-weil-pbc-proper-open-comparison-composition], [lem-weil-pbc-proper-open-comparison-iso], [lem-weil-pbc-proper-open-comparison-proetale], [lem-weil-pbc-proper-open-identification], [lem-weil-pbc-proper-open-section], [prop-compactification-coherence-detailed], [rem-ptr-weil-pbc-proper-open-comparison-1] gives associativity.

Uses: `\Cref{prop:nagata-sketch-comp-category}`, `\Cref{prop:sf-comp-coherence}`, `\Cref{thm:properbasechange}`
