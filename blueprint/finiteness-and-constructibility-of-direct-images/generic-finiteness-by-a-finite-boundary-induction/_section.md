+++
id = "generic-finiteness-by-a-finite-boundary-induction"
kind = "section"
title = "Generic finiteness by a finite-boundary induction"
order = 5803
+++
The order of the induction follows Deligne, [SGA
4½, *Finitude*, Sections
2.1–2.8](https://publications.ias.edu/sites/default/files/Number32.pdf). The
argument below supplies the geometric and derived steps explicitly. Every
derived category is an ordinary derived category of étale sheaves.

Duals of lisse complexes [lem-fin-lisse-field-dual] and the compact
direct-image inputs [lem-fin-compact-bounded-and-base-change] feed the
smooth generic statement [lem-asd-smooth-generic-direct-image]. Coordinate
projections lower the generic dimension
[lem-fin-coordinate-generic-dimension] and produce a finite boundary
[lem-fin-projective-coordinate-boundary]; generic radicial smoothing
[lem-fin-generic-radicial-smoothing] with its exchange descent
[lem-fin-radicial-exchange-descent] completes the induction
[thm-fin-deligne-generic-open], over a field
[cor-fin-deligne-open-over-field], and — after the forgetful step
[lem-fin-coefficients-forgetful-direct-image] — with finite coefficients
[cor-fin-deligne-open-finite-coefficients], giving the finite-type
constructibility theorem [thm-dg-finite-type-constructibility].
