+++
id = "lem-trf-frobenius-formal-contraction"
kind = "lemma"
title = "The Frobenius is topologically nilpotent on the formal completion"
order = 2477
uses = ["def-trf-scheme-frobenius", "lem-trf-frobenius-differential-vanishing"]
+++
Let $y\in X_0(\mathbf F_{q^m})$ and let $\widehat{\mathcal O}_{X,y}$
be the completion of the local ring at $y$. The induced endomorphism
$\Phi^{m*}$ of $\widehat{\mathcal O}_{X,y}$ sends the maximal ideal
$\widehat{\mathfrak m}_y$ into $\widehat{\mathfrak m}_y^{q^m}$, hence
into $\widehat{\mathfrak m}_y^2$. In particular the graph
correspondence $c=(\operatorname{id}_X,\Phi^m)$ restricts to a
*contracting* correspondence on the formal neighbourhood of $y$ in
the sense of Varshavsky, loc. cit., 2.1: the two legs agree modulo the
square of the maximal ideal.

## Proof

By [def-trf-scheme-frobenius], $\Phi^{m*}(f)=f^{q^m}$ for every
regular function $f$. For $f\in\widehat{\mathfrak m}_y$ one has
$f^{q^m}\in\widehat{\mathfrak m}_y^{q^m}$, and $q^m\ge2$ for $m\ge1$,
so $\widehat{\mathfrak m}_y^{q^m}\subseteq\widehat{\mathfrak m}_y^2$.
The congruence modulo $\widehat{\mathfrak m}_y^2$ of the two legs is
then the vanishing of the differential
[lem-trf-frobenius-differential-vanishing]: on the cotangent level
both legs induce the same map, the identity on the first and zero on the
second, so $c_1$ and $c_2$ agree modulo the square of the maximal
ideal.
