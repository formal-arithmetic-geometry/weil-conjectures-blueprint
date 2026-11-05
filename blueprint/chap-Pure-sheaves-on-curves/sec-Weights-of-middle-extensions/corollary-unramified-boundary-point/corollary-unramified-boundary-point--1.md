+++
id = "corollary-unramified-boundary-point--1"
kind = "corollary"
title = "An unramified boundary point (1)"
name_showing = false
order = 1183001
aliases = ["bp-r365-1"]
lean = []
uses = ["definition-lisse-sheaves", "definition-weil-structure", "definition-weights", "proposition-topos-functoriality", "definition-weil-representation"]
+++
This boundary-point assertion is bypassed by the Lean proof of the main theorem,
which uses [corollary-unramified-boundary-point--2] for a sheaf already lisse
on the whole curve.

Let $\mathcal F$ be a lisse sheaf, pure of weight $a$, on a smooth
geometrically connected curve with a point removed. If the inertia at the removed point acts
trivially, then the stalk at that point of the direct image of
$\mathcal F$ to the curve is pure of weight $a$.
