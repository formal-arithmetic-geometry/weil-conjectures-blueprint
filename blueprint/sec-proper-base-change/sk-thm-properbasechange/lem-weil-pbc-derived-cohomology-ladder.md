+++
id = "lem-weil-pbc-derived-cohomology-ladder"
kind = "lemma"
title = "A morphism of distinguished triangles gives a morphism of the long exact cohomology sequences"
uses = ["def-weil-abstract-derived-category", "def-weil-triangulated-category", "lem-sf-derived-homology-long-exact", "def-weil-pbc-triangles-with-shift"]
lean = ["CategoryTheory.Functor.homologySequenceδ_naturality"]
order = 1983
tags = ["mathlib", "stacks-0147"]
+++
Let $\mathcal C$ be an abelian category, $D(\mathcal C)$ its derived category [def-weil-abstract-derived-category], a triangulated category [def-weil-triangulated-category], with cohomology functors $H^n:D(\mathcal C)\to\mathcal C$, and for a distinguished triangle $T=(X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{w}X[1 ])$ let

$$
\cdots\to H^n(X)\xrightarrow{H^n(u)}H^n(Y)\xrightarrow{H^n(v)}H^n(Z)\xrightarrow{\delta^n_T}H^{n+1}(X)\to\cdots
$$

be its long exact cohomology sequence [lem-sf-derived-homology-long-exact], with $\delta^n_T$ the map induced by $w$ through the identification $H^{n+1}(X)=H^n(X[1 ])$. Let $T'=(X'\xrightarrow{u'}Y'\xrightarrow{v'}Z'\xrightarrow{w'}X'[1 ])$ be another distinguished triangle and $(a,b,c):T\to T'$ a morphism of triangles [def-weil-pbc-triangles-with-shift]. Then for every $n\in\mathbf Z$

$$
H^n(b)\circ H^n(u)=H^n(u')\circ H^n(a),\qquad H^n(c)\circ H^n(v)=H^n(v')\circ H^n(b),\qquad H^{n+1}(a)\circ\delta^n_T=\delta^n_{T'}\circ H^n(c),
$$

so that $(H^n(a),H^n(b),H^n(c))_{n\in\mathbf Z}$ is a morphism of long exact sequences.
