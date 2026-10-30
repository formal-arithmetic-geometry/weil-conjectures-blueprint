+++
id = "prose-20-02"
kind = "hidden"
title = "Quasi-finite maps and curves preserving irreducibility"
order = 764
+++
The proof of Theorem [sk-i-dl-general-real] restricts a sheaf to curves
and then reassembles it over strata and descends it along constant
extensions. For the reassembly and the descent we need that
quasi-finite direct images preserve weights; for the restriction we
need curves on which given lisse sheaves stay geometrically
irreducible.

The first fact is elementary: a finite direct image only permutes
stalks. At a point $y$ downstairs, the $e$ copies of the stalk at a
point over $y$ with residue extension of degree $e$ are cycled by
Frobenius, whose eigenvalues are then $e$th roots of the eigenvalues
upstairs, so absolute values relative to the residue field are
unchanged (Lemma [sk-l-dl-general-quasifinite]). The second is where the
geometry lies. Restricting to a curve can lose
monodromy. On $\mathbf G_m\times\mathbf G_m$ with coordinates $x,y$, in odd
characteristic,
the double cover $u^2=x$ is connected, but over the curve $x=1$ it
splits into two copies, and the Kummer sheaf of the quadratic character
in $x$, geometrically nontrivial on the surface, becomes constant on
that curve. In the same way an irreducible sheaf of higher rank can
become reducible on a badly chosen curve. A representation stays
absolutely irreducible on a curve if the image of the curve's
fundamental group is large enough, and the point is that this can be
checked in one finite quotient
(Lemma [sk-lem-wgen-finite-witness]), so it suffices that the curve stays
connected in one finite étale cover, and that is what Bertini's
irreducibility theorem provides (Lemma [sk-lem-wgen-bertini-cover]).
