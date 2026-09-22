+++
id = "def-pc-smooth-projective-curve"
kind = "definition"
title = "Smooth projective curves"
order = 4218
lean = ["AlgebraicGeometry.IsSmoothProjectiveCurve"]
uses = ["def-pc-curve", "def-pc-projective-morphism"]
+++
Let $k$ be a field. A *smooth projective curve over $k$* is a curve
[def-pc-curve] $X$ over $k$ such that $X\to\operatorname{Spec}(k)$ is
smooth and projective [def-pc-projective-morphism]. In Stacks Project,
Chapter 44 (Picard Schemes of Curves) the phrase *smooth projective curve
over $k$* is used in exactly this sense.

*Import note.* The source's sentence breaks off at a semicolon and the
definition then closes; it is completed with a full stop and nothing else
is added. The properties deferred there are
[rem-ptr-pc-smooth-projective-curve-3].

Unresolved dependencies: def:weil-scheme-morphism-properties
