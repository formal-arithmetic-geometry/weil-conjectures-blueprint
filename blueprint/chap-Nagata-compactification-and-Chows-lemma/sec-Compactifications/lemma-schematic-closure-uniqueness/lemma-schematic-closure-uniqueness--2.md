+++
id = "lemma-schematic-closure-uniqueness--2"
kind = "lemma"
title = "Flat base change of the schematic image"
name_showing = false
order = 1406002
aliases = ["bp-r435-2"]
lean = ["AlgebraicGeometry.Scheme.Hom.ker_of_isPullback"]
uses = []
+++
Let $f:X\to T$ be a quasi-compact morphism and $q:T'\to T$ a
flat morphism. In a cartesian square with projections
$p_1:X'\to X$ and $p_2:X'\to T'$, put
$\mathcal I_f=\ker(\mathcal O_T\to f_*\mathcal O_X)$. Then
$$
\ker(\mathcal O_{T'}\to (p_2)_*\mathcal O_{X'})
=\mathcal I_f\mathcal O_{T'}.
$$
Equivalently, the scheme-theoretic image of $p_2$ is the base
change to $T'$ of the scheme-theoretic image of $f$.
Taking $q$ to be the inclusion of an open subscheme shows that
schematic closure commutes with restriction to opens of $T$.
