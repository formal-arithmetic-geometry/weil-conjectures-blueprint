+++
id = "lemma-weil-pbc-finite-pullback-closed-fibre"
kind = "lemma"
title = "Finite pullback and closed-fibre restriction"
order = 1082
lean = ["AlgebraicGeometry.Etale.globalSectionsUpperStarMap_comp_squareUpperStarIso"]
uses = ["def-weil-pbc-finite-section-pullback", "lemma-weil-pbc-finite-pullback-composition"]
+++
Consider a commutative square of schemes

$$
\begin{array}{ccc}
Z' & \xrightarrow{a} & T'\\
b\downarrow & & \downarrow u\\
Z & \xrightarrow{i} & T
\end{array}
$$

(for instance $i$ a closed immersion, $u$ finite and $Z'=Z\times_TT'$ the
closed fibre) and an etale sheaf $G$ on $T$ (with values in $\mathcal A$ as in
[def-weil-pbc-finite-section-pullback]). Then pulling a global section back
along $u$ and then along $a$ agrees with restricting it along $i$ and then
pulling back along $b$, modulo the square isomorphism
$b^{-1}i^{-1}G\cong a^{-1}u^{-1}G$: in terms of the pullbacks of global sections,

$$
\Gamma(\theta)\circ b^\sharp\circ i^\sharp=a^\sharp\circ u^\sharp,
$$

where $\theta:b^{-1}i^{-1}G\xrightarrow{\sim}a^{-1}u^{-1}G$ is the composite of
the composition isomorphisms through the inverse image along $ua=ib$.

## Proof

Apply the composition lemma [lemma-weil-pbc-finite-pullback-composition] to the
two equal composites $u\circ a=i\circ b:Z'\to T$: both $a^\sharp\circ u^\sharp$
and $b^\sharp\circ i^\sharp$ are identified with the pullback along this common
composite, by the respective composition isomorphisms. The square isomorphism
$\theta$ is by definition the composite of these two composition isomorphisms,
which gives the displayed equation.
