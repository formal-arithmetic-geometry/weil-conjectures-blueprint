+++
id = "lem-coef-finite-dualizing"
kind = "lemma"
title = "Finite coefficient change for the dualizing object"
order = 2480
uses = ["cor-amb-affine-space-adjunction", "lem-amb-etale-adjoint-locality", "lem-coef-finite-closed-shriek", "lem-fix-compact-support-coefficient-change", "lem-weil-finite-duality-site-comparison", "lem-weil-verdier-preservation-strata"]
+++
Let $a_X:X\to\operatorname{Spec}k$ and
$\omega_{X,A}=Ra_{X,A}^{\times}A$. There is a canonical
isomorphism

$$
u_{X,A,B}:\omega_{X,A}\otimes_A^LB
\xrightarrow{\sim}\omega_{X,B}.
$$

It is the adjoint, for $Ra_{X,B!}\dashv Ra_{X,B}^{\times}$, of

$$
Ra_{X,B!}(\omega_{X,A}\otimes_A^LB)
\cong(Ra_{X,A!}\omega_{X,A})\otimes_A^LB
\longrightarrow A\otimes_A^LB=B.
$$

These maps satisfy the quotient cocycle and carry the reduction
of the dualizing counit to the dualizing counit.
