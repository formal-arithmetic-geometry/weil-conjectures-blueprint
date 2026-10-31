+++
id = "prose-09-05"
kind = "hidden"
title = "Degree zero and reduction to a smooth curve"
order = 399
+++
The induction on the degree starts with direct images of sheaves of
sets, for which the base change map can be computed on sections. In degree
zero, sections of $f_*F$ over $V$ are sections of $F$ over $V\times_YX$,
and the question is whether pulling back to a $Y'$-scheme $U$ over $V$
creates new sections. It does not when $U\to V$ is flat and qcqs with
geometrically connected fibres, since pullback along such a map does not
change sections of the pullback of an étale sheaf. Locally, a smooth $g$ factors as such a map
followed by an étale one, and the same factorization, base changed to
$X$, computes $f'_*g'^{-1}F$ (Lemma [sk-prop-deg0]). Only
flatness, finite presentation and geometrically reduced fibres are used.

The rest of the subsection prepares the induction. We formulate the
statement to be proved in degree $q$ in a form that survives étale
localization, composition and changes of the source and of the base, and
we use étale coordinates to reduce to smooth affine curves.
