+++
id = "lem-weil-pbc-zero-dimensional-cohomology"
kind = "lemma"
title = "Etale cohomology in dimension zero"
lean = ["AlgebraicGeometry.zero_dimensional_etale_cohomology"]
order = 1394
uses = ["def-weil-pbc-curve-setting", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $k$ be algebraically closed and let $C$ be a separated finite-type
$k$-scheme of dimension at most zero. For an abelian etale sheaf
$F$, its etale cohomology is canonically

$$
 H^q(C,F)=
 \begin{cases}
  \displaystyle\prod_{c\in|C|}F_{\bar c},&q=0,\\
  0,&q>0,
 \end{cases}
$$

where the product is finite and $F_{\bar c}$ denotes the geometric stalk at
$c$.
