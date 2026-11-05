+++
kind = "proof"
of = "theorem-grothendieck-lefschetz-trace-formula--4"
order = 1017009
uses = ["corollary-trace-functions-direct-image-compact"]
+++
Apply the relative trace identity `AlgebraicGeometry.ProEtale.CondensedRing.weilShriekTraceFunction`, the mainline form of [corollary-trace-functions-direct-image-compact], to $a:X_0\to\operatorname{Spec}\Fq$, the automorphisms $e$ and $1$, and the geometric point of the base. By definition its left side is $L_m(X_0,K')$. Every point of $\operatorname{Fix}_m(e)$ lies over that base point, so the condition imposed on the summation set is automatic. Removing that condition gives the formula. The relative identity is proved first by Noetherian induction from its geometric base cases.
