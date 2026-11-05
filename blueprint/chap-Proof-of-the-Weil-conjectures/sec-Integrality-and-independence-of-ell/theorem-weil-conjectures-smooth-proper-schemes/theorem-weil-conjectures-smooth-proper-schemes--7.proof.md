+++
kind = "proof"
of = "theorem-weil-conjectures-smooth-proper-schemes--7"
order = 1388008
uses = []
+++
The determinant of $F$ is a unit. Thus the reverse characteristic polynomial has the same degree as the characteristic polynomial, namely $\dim_K V$. Lean applies `LinearMap.natDegree_charpolyRev` with this unit determinant. The specialization to $\overline P_{i,\ell}$ follows from its definition; the comparison with $b_i$ also uses the integral realization.
