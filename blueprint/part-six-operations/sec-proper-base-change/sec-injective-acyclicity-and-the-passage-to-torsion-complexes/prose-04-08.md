+++
id = "prose-04-08"
kind = "hidden"
title = "Injective acyclicity and the passage to torsion complexes"
order = 186
+++
Degree zero is settled by Proposition [sk-prop-pbc-degree-zero]. To reach
higher degrees we apply it termwise to an injective resolution. This
works as soon as the pullback of an injective sheaf along any base
change is acyclic for the direct image, and the main result of this
subsection, Theorem [sk-thm-iff], says that this vanishing
is equivalent to proper base change.

The difficulty is that $g'^*$ does not preserve injectives, so the
termwise isomorphism $g^*f_*I^m\simeq f'_*g'^*I^m$ of degree zero only
compares $g^*Rf_*F$ with the complex $f'_*g'^*I^\bullet$, which need not
compute $Rf'_*g'^*F$. Injective acyclicity is exactly what closes this
gap. Its advantage over the base change statement itself is that it is
a vanishing condition on single sheaves. It is checked for
$\mathbf P^1$ in the next subsection, and in
Section [sec-pbc-reduction] it passes through composition and descends
along proper surjections by a Leray spectral sequence. We also record
the continuity of étale cohomology under filtered colimits, which
later carries the theorem from sheaves killed by an integer to all
torsion sheaves.
