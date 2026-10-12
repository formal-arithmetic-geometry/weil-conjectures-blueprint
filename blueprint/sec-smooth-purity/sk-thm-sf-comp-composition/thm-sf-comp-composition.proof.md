+++
kind  = "proof"
of    = "thm-sf-comp-composition"
+++
*Construction.* Compactify $g$ as $Y\xrightarrow{v}\overline Y \xrightarrow{\bar g}S$, and compactify $v\circ f$ as
$X\xrightarrow{a}\overline X\xrightarrow{p}\overline Y$, using
Nagata's theorem [thm-nagata-compactification]. Put $V=\overline X\times_{\overline Y}Y$,
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
defining $V$ ([thm-weil-pbc-finite-level-proetale]), and at a geometric point of
$\overline Y$ outside $Y$ both sides vanish, because the corresponding fibre of
$p$ misses $V$ ([cor-weil-pbc-geometric-fiber-finite]). Apply this to the extension by zero of a complex on $X$ and
then push by $R\bar g_*$: extension by zero along opens composes termwise and
proper derived direct image composes
([lem-weil-derived-direct-image-composition]), giving $\alpha_{g,f}$.

*Independence and associativity.* Any two choices are compared by
[prop-compactification-coherence-detailed], which also makes $\alpha_{g,f}$ natural. For
three morphisms choose, by
[def-weil-compactifications-refinements], [prop-compactification-refinement] (i), a single common refinement of all
the compactifications involved; the two composites then restrict to the same
identity over the source and use the same proper base-change maps on each
Cartesian rectangle, so their pasting identity together with the refinement
transitivity of [prop-compactification-coherence-detailed] gives associativity.
