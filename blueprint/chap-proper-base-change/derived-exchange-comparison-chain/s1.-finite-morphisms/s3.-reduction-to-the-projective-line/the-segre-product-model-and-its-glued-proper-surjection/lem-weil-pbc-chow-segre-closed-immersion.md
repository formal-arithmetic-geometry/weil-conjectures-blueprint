+++
id = "lem-weil-pbc-chow-segre-closed-immersion"
kind = "lemma"
title = "The Segre embedding is a closed immersion"
order = 1581
uses = ["def-weil-pbc-chow-segre-embedding", "def-weil-pbc-scheme-conventions"]
+++
The Segre embedding of [def-weil-pbc-chow-segre-embedding] is a closed
immersion.

## Proof

We check the criterion for a closed immersion on the distinguished affine
charts of the target, which cover $\mathbf P^N_Y$. Let $e=(e_1,\dots,e_m)$,
$0\leq e_i\leq n_i$, and let $D_+(X_e)\subseteq\mathbf P^N_Y$ be the
corresponding distinguished chart. Its preimage under $s$ is

$$
 s^{-1}(D_+(X_e))=\prod_{i=1}^m D_+(x_{i,e_i}),
$$

an affine $Y$-scheme: the chart $D_+(x_{i,e_i})$ of $\mathbf P^{n_i}_Y$ is
affine, and a finite product of affine schemes over an affine base is affine.
On these charts, after normalizing $X_e=1$ and $x_{i,e_i}=1$, the morphism $s$
is given by the ring homomorphism of polynomial rings

$$
 \mathcal O_{\mathbf P^N_Y}(D_+(X_e))
 \longrightarrow\bigotimes_{i=1}^m\mathcal O_{\mathbf P^{n_i}_Y}
 \bigl(D_+(x_{i,e_i})\bigr),
 \qquad
 \frac{X_f}{X_e}\longmapsto\prod_{i=1}^m\frac{x_{i,f_i}}{x_{i,e_i}},
$$

which sends the coordinate $\frac{X_f}{X_e}$ to the corresponding monomial.
This map is surjective: for each $i$ and each $0\leq f_i\leq n_i$, the
monomial for the multi-index $f=(e_1,\dots,e_{i-1},f_i,e_{i+1},\dots,e_m)$
equals the single ratio $x_{i,f_i}/x_{i,e_i}$, so the image contains every
generator of the target polynomial ring. Hence $s$ is affine-locally (on the
target) the morphism of affine schemes induced by a surjective ring
homomorphism, i.e. a closed immersion. Since being a closed immersion is local
on the target, $s$ is a closed immersion (cf. Stacks Project, Constructions,
Tag [01WD](https://stacks.math.columbia.edu/tag/01WD) = Lemma 27.13.6).
