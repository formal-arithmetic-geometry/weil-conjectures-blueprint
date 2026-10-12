+++
id = "lemma-nagata-product-ideal-common-blowup"
kind = "lemma"
title = "[stacks-project]"
order = 135
lean = ["AlgebraicGeometry.IsAdmissible.mul", "AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_iso"]
uses = ["cor-nagata-blowup-product-common-refinement", "def-nagata-admissible-blowup", "def-nagata-extended-ideal", "def-nagata-global-blowup", "prop-nagata-global-blowup-cover-independent", "thm-nagata-global-blowup-complement"]
+++
Let $X$ be a scheme, let $U\subseteq X$ be an open subscheme, and let
$\mathcal I_1,\mathcal I_2$ be finite-type quasi-coherent ideals on $X$ with
$V(\mathcal I_1)\cap U=V(\mathcal I_2)\cap U=\varnothing$. Then
$\mathcal I_1\mathcal I_2$ is of finite type with
$V(\mathcal I_1\mathcal I_2)\cap U=\varnothing$, so the blow-ups of
$\mathcal I_1$, $\mathcal I_2$ and $\mathcal I_1\mathcal I_2$ are all
$U$-admissible. Moreover
$\operatorname{Bl}_{\mathcal I_1\mathcal I_2}(X)\cong
\operatorname{Bl}_{\mathcal I_2\mathcal O_{\operatorname{Bl}_{\mathcal I_1}(X)}}(\operatorname{Bl}_{\mathcal I_1}(X))$
over $X$; in particular the blow-up of $\mathcal I_1\mathcal I_2$
dominates the blow-ups of $\mathcal I_1$ and of $\mathcal I_2$ by morphisms
over $X$.
