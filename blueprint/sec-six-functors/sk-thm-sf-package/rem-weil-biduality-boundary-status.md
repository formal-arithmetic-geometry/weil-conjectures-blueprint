+++
id = "rem-weil-biduality-boundary-status"
kind = "remark"
title = "Finite-stage completion and coefficient scope"
order = 3380
uses = ["cor-coef-finite-verdier", "cor-weil-boundary-duality-discharge", "cor-weil-finite-constructible-hom", "lem-weil-coefficient-frobenius", "lem-weil-finite-duality-site-comparison", "lem-weil-geometric-generic-exchange", "lem-weil-verdier-preservation-strata", "thm-coef-integral-verdier", "thm-fix-general-biduality", "thm-weil-etale-geometric-biduality", "sk-thm-pd-verdier-duality"]
+++
Constructible preservation
is proved independently in [lem-weil-verdier-preservation-strata];
the generic restriction comparisons of
[lem-weil-geometric-generic-exchange] justify the dimension
induction in [thm-weil-etale-geometric-biduality].
The etale–pro-etale comparison
[lem-weil-finite-duality-site-comparison] gives the finite-stage
theorem [thm-fix-general-biduality]. Boundary exchange is the
subsequent consequence [cor-weil-boundary-duality-discharge],
and general finite-stage internal-Hom preservation is
[cor-weil-finite-constructible-hom].

These geometric statements concern $A_{E,n}$. [cor-coef-finite-verdier]
normalizes the finite duals. The other admissible coefficient rings follow by
the reductions of [sk-thm-pd-verdier-duality]: derived Nakayama for
$\mathcal O_E$ ([thm-coef-integral-verdier]), integral models for $E$, and
descent to a finite $E$ for $\Qlb$. The point calculation
[lem-weil-coefficient-frobenius] remains an algebraic ingredient.
