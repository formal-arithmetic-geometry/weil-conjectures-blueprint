+++
id = "lemma-nagata-product-ideal-common-blowup"
kind = "lemma"
title = "[stacks-project]"
order = 356
lean = ["AlgebraicGeometry.IsAdmissible.mul", "AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_iso"]
uses = ["cor-nagata-blowup-product-common-refinement", "thm-nagata-global-blowup-complement"]
+++
Let $X$ be qcqs, let $U\subseteq X$ be a quasi-compact open, and let
$\mathcal I_1,\mathcal I_2$ be finite-type quasi-coherent ideals on $X$ with
$\mathcal I_1|_U=\mathcal I_2|_U=\mathcal O_U$. The blow-up of
$\mathcal I_1\mathcal I_2$ canonically dominates the blow-ups of
$\mathcal I_1$ and of $\mathcal I_2$, and all three blow-ups are
$U$-admissible.

## Proof

Let $\pi_i\colon\operatorname{Bl}_{\mathcal I_1\mathcal I_2}(X) \to\operatorname{Bl}_{\mathcal I_i}(X)$ be the two maps supplied by
[cor-nagata-blowup-product-common-refinement]. The product ideal is
also the unit ideal on $U$, so each of the three blow-ups restricts to $U$
by [thm-nagata-global-blowup-complement]; hence all are
$U$-admissible and the displayed maps are the required domination maps.
