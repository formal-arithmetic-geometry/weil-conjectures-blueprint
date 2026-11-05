+++
kind = "proof"
of = "corollary-point-counting-zeta-function--2"
order = 1039009
uses = ["theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function"]
+++
Apply the cohomological trace formula of
[theorem-grothendieck-lefschetz-trace-formula] to the constant Weil sheaf
$\overline{\mathbf Q}_{\ell,X}$, viewed as a Weil complex in degree zero.
Its stalks are one-dimensional and their Frobenius operators are the
identity. Thus the trace function of [definition-trace-function] is
constantly $1$, as expressed by
`AlgebraicGeometry.WeilSheaf.traceFunction_adicConstant`.

The points over $\mathbf F_{q^m}$ form a finite set. The sum of their
local traces is therefore their cardinality, and the trace formula gives
the asserted equality. Boundedness of compactly supported cohomology
makes the sum over degrees finite.
