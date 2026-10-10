+++
kind  = "proof"
of    = "sk-thm-sf-comp-composition"
+++
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
defining $V$ ([sk-thm-properbasechange]), and at a geometric point of
$\overline Y$ outside $Y$ both sides vanish, because the corresponding fibre of
$p$ misses $V$. Apply this to the extension by zero of a complex on $X$ and
then push by $R\bar g_*$: extension by zero along opens composes termwise and
proper derived direct image composes, giving $\alpha_{g,f}$.

*Independence and associativity.* Any two choices are compared by
[sk-prop-sf-comp-coherence], which also makes $\alpha_{g,f}$ natural. For
three morphisms choose, by
[sk-prop-nagata-sketch-comp-category] (i), a single common refinement of all
the compactifications involved; the two composites then restrict to the same
identity over the source and use the same proper base-change maps on each
Cartesian rectangle, so their pasting identity together with the refinement
transitivity of [sk-prop-sf-comp-coherence] gives associativity.
