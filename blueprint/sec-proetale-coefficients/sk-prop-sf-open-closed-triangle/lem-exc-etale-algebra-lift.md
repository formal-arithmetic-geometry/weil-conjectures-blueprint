+++
id = "lem-exc-etale-algebra-lift"
kind = "lemma"
title = "Etale algebras lift across an arbitrary quotient"
lean = ["Algebra.SquareJacobianPresentation.CoefficientLift.etale_and_reduction_equiv", "Algebra.exists_etale_coefficientLift"]
order = 1110
uses = ["def-exc-etale-algebra-lift", "def-weil-pbc-scheme-conventions", "lem-exc-etale-jacobian-presentation"]
+++
The algebra of [def-exc-etale-algebra-lift] is etale of finite presentation
over $A$, and its specified reduction
$B^{\mathrm{lift}}/IB^{\mathrm{lift}}\to\overline B$ is an isomorphism.
Hence every etale finite-presentation $A/I$-algebra has such a lift, with no
nilpotence assumption on $I$.
