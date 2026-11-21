+++
kind = "proof"
of = "dag-def-pur-signed-line-ordinary-constraint-data"
tags = ["sheaf-dag"]
+++
1. Work in the ambient K-flat-fixed module category and tensor presentation supplied by `def-sf-ringed-kflat-tensor-representative-data` and `lem-weil-pbc-kflat-fixed-tensor-triangulated`. The signed powers and their scalar normalizations are those of [dag-def-pur-signed-line-scalar-normalization-data], while the canonical signed-power tower is the one recorded in `lem-pur-signed-line-scalar-tensor-tower`. By the power definitions of `def-sp-scalar-tensor-comparison-data`, P^$[0]$ is A, P^$[1]$ is P, and P^[n+2] is P^[n+1] tensor P. The signed negative power P^[-(n+1)] is the internal Hom of P^[n+1] into A. For the given maps u, p and e, define the conjunction of the scalar-unit, reassociation, and evaluation pure-section formulas as follows. (uses `def-sp-scalar-tensor-comparison-data`)
2. The scalar-unit clause requires, for every module sheaf N, every site object V, x in N(V) and r in A(V), that the section map of u at N sends x tensor r to r x. Here and below a pure tensor denotes its image in the sheafified tensor, as expressed by siteSheafTensorTmul in Lean.
3. The reassociation clause requires, for every n >= 0, N and V, x in N(V), y in P^[n+1](V) and q in P(V), that the section map of p_n at N sends (x tensor y) tensor q to x tensor (y tensor q), with the inner tensor on the right regarded as a section of P^[n+2]. This is exactly the second universally quantified conjunct in OrdinaryLineConstraints.
4. The evaluation clause requires, for every n >= 0, N and V, x in N(V), phi in P^[-(n+1)](V) and y in P^[n+1](V), that the section map of e_n at N sends (x tensor phi) tensor y to phi(y)x. Evaluation is the value of phi at the identity slice object: in Lean the scalar is phi.app (op (Over.mk (𝟙 V.unop))) y, with V represented as an object of the opposite site. Taking these three clauses as a conjunction defines precisely OrdinaryLineConstraints(A,P,u,p,e); it specifies the given maps without asserting their existence.

Proof dependencies not drawn: `def-sp-scalar-tensor-comparison-data`.
