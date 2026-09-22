+++
id = "def-pc-curve"
kind = "definition"
title = "Curves"
order = 4217
lean = ["AlgebraicGeometry.IsVariety", "AlgebraicGeometry.IsCurve"]
uses = ["def-pc-scheme", "def-pc-morphism-conventions", "def-pc-dimension"]
+++
Let $k$ be a field. A *variety over $k$* is a scheme $X$ over $k$ which is
integral and whose structure morphism $X\to\operatorname{Spec}(k)$ is
separated and of finite type [def-pc-morphism-conventions] (Varieties,
Definition 33.3.1, [Tag 020D](https://stacks.math.columbia.edu/tag/020D)).
A *curve over $k$* is a scheme over $k$ which is a variety of dimension $1$
[def-pc-dimension] (Varieties, Definition 33.43.1, [Tag
0A23](https://stacks.math.columbia.edu/tag/0A23)).

*Terminology.* This is the *curve* notion of the Stacks Project (integral
variety of dimension one over an arbitrary base field), and it differs from
the *smooth-curve* convention of the curve-calculation chapter (a nonempty
connected separated scheme of finite type of dimension at most one over an
**algebraically closed** field). That every curve in the present sense over
an algebraically closed field is a smooth curve in that sense is
[lem-pc-curves-are-sc].

*Import note.* The source's terminology paragraph breaks off at a semicolon
and the definition then closes; the clause is completed with a full stop
and the cross-reference the pointer remark [rem-ptr-pc-curve-2] supplies.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:sc-curves
