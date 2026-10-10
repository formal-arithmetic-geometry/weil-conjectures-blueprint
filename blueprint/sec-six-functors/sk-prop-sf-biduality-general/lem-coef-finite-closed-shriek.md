+++
id = "lem-coef-finite-closed-shriek"
kind = "lemma"
title = "Finite coefficient change for closed support"
order = 2139
uses = ["cor-weil-boundary-duality-discharge", "def-weil-open-closed-recollement", "lem-coef-finite-direct-image", "lem-exc-closed-support-triangle", "thm-fix-general-biduality"]
+++
For a closed immersion $i:Z\hookrightarrow X$ and
$M\in D^b_{ctf}(X,A)$, the canonical comparison

$$
b_{i,M}:(Ri_A^!M)\otimes_A^LB
\xrightarrow{\sim}Ri_B^!(M_B)
$$

is an isomorphism. It is the adjoint of

$$
i_*((Ri_A^!M)\otimes_A^LB)
\cong(i_*Ri_A^!M)\otimes_A^LB
\longrightarrow M_B,
$$

where the last map is the tensor product of the closed exceptional
counit. The comparison commutes with the exceptional counit,
composition of closed immersions, and successive coefficient changes.
The analogous assertion holds for a locally closed immersion,
using its factorization into an open and a closed immersion.
