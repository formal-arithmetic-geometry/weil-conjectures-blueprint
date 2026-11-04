+++
id = "prose-18-02"
kind = "hidden"
title = "Quasi-finite morphisms and curves (1)"
order = 1314
+++
To prove Theorem [theorem-real-constructible-sheaves-are-mixed] we
restrict a sheaf to curves, reassemble it over strata and descend it
along constant extensions. For the reassembly and the descent we need
that quasi-finite direct images preserve weights. For the restriction
we need curves on which given lisse sheaves stay geometrically
irreducible.

The first fact is elementary, because a finite direct image only
permutes stalks. Let $y$ be a point downstairs and $x$ a point over $y$
with residue extension of degree $e$. Frobenius at $y$ cycles the $e$
copies of the stalk at $x$, and its eigenvalues are $e$th roots of the
eigenvalues upstairs. Measured against the residue field, absolute
values are therefore unchanged
(Lemma [lemma-finite-quasi-finite-direct-images]).

The second fact is geometric, since restricting to a curve can lose
monodromy. On $\mathbf G_m\times\mathbf G_m$ with
coordinates $x,y$, in odd characteristic, the double cover $u^2=x$ is
connected, but over the curve $x=1$ it
splits into two copies. Accordingly, the Kummer sheaf of the quadratic
character in $x$ is geometrically nontrivial on the surface but constant
on that curve. In the same way an irreducible sheaf of higher
rank can become reducible on a badly chosen curve. A representation
stays absolutely irreducible on a curve if the image of the
fundamental group of the curve is large enough. We show that this can
be checked in one finite quotient
(Lemma [lemma-detecting-irreducibility-finite-quotient]). It then
suffices that the curve stays connected in one finite étale cover, and
we find such curves with Bertini's irreducibility theorem
(Lemma [lemma-curve-preserving-finite-cover]).
