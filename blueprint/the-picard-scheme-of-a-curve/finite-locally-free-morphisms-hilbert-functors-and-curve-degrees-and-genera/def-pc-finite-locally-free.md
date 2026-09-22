+++
id = "def-pc-finite-locally-free"
kind = "definition"
title = "Finite locally free morphisms"
order = 4251
lean = ["AlgebraicGeometry.IsFiniteLocallyFree"]
uses = ["def-pc-morphism-conventions", "def-pc-base-change", "lem-pc-flf-properties"]
+++
Let $f:X\to S$ be a morphism of schemes. $f$ is *finite locally free of
degree $d$* (for $d\geq0$) if $f$ is finite, flat and locally of finite
presentation [def-pc-morphism-conventions], and for every $s\in S$ the
fibre $X_s$ is a finite set of points with
$$
\dim_{\kappa(s)}\Gamma(X_s,\mathcal{O}_{X_s})=d .
$$
The resulting structure of $f_*\mathcal{O}_X$ is [lem-pc-flf-properties].

*Import note.* The body of this definition is truncated in the source: it
reads only "Let $f:X\to S$ be a morphism of schemes." and then ends. The
text above is the definition the source states in its own pointer remark
[rem-ptr-pc-finite-locally-free-11], copied back here so that the
definition node carries its content; nothing is added beyond what that
remark says.

Unresolved dependencies: def:weil-pbc-scheme-conventions
