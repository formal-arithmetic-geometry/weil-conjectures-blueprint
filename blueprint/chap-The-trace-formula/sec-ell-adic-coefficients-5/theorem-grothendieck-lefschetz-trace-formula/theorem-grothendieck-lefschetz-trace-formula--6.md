+++
id = "theorem-grothendieck-lefschetz-trace-formula--6"
kind = "theorem"
title = "Finite-dimensional stalks and bounded cohomology"
order = 1017012
aliases = ["bp-r311-6"]
lean = ["AlgebraicGeometry.WeilSheaf.finiteDimensional_stalkObj", "AlgebraicGeometry.WeilComplex.exists_finset_isZero_homologySheaf"]
uses = ["definition-weil-structure", "definition-constructible-sheaves"]
+++
Let $X_0$ be any scheme over $\Fq$ and let $\ell\nmid q$. The stalk of a constructible $\Qlb$-Weil sheaf at every geometric point $\operatorname{Spec}\overline{\Fq}\to X_0\times_{\Fq}\overline{\Fq}$ is finite-dimensional over $\Qlb$.

For a bounded $\Qlb$-Weil complex $K$ there is a finite set $S\subset\mathbf Z$ such that $\mathcal H^j(K)=0$ for $j\notin S$. Consequently only finitely many finite-dimensional cohomology stalks contribute to the local alternating trace. This is the cohomological form used by Lean in place of the assertion of perfectness for every admissible coefficient ring.
