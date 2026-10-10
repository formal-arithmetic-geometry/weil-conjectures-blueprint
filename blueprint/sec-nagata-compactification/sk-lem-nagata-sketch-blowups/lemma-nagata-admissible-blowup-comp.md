+++
id = "lemma-nagata-admissible-blowup-comp"
kind = "lemma"
title = "Composition of admissible blow-ups, [stacks-project]"
order = 162
lean = ["AlgebraicGeometry.IsAdmissible.exists_comp"]
uses = ["def-nagata-admissible-blowup", "def-nagata-composition-of-blowups-comparison", "def-nagata-global-blowup", "lemma-nagata-admissible-blowup-over-open", "lemma-nagata-composition-center-ideal", "lemma-nagata-composition-extended-ideal-equality", "prop-nagata-global-blowup-cover-independent", "thm-nagata-composition-of-blowups"]
+++
Let $X$ be quasi-compact and quasi-separated and let $U\subseteq X$ be an
open subscheme. Let $b_1\colon X_1=\operatorname{Bl}_{\mathcal I_1}(X)\to X$
be a $U$-admissible blow-up and let
$X_2=\operatorname{Bl}_{\mathcal I_2}(X_1)\to X_1$ be a
$b_1^{-1}(U)$-admissible blow-up. Then there are a finite type
quasi-coherent ideal $\mathcal K$ on $X$ with
$V(\mathcal K)\cap U=\varnothing$ and an isomorphism
$X_2\cong\operatorname{Bl}_{\mathcal K}(X)$ over $X$. In particular, the
composite $X_2\to X_1\to X$ is a $U$-admissible blow-up.

## Proof

Both centers $\mathcal I_1$ and $\mathcal I_2$ are of finite type, so
[thm-nagata-composition-of-blowups], applied to $\mathcal I=\mathcal I_1$
and the closed subscheme $Z'=V(\mathcal I_2)\subseteq X_1$, gives a finite
type quasi-coherent ideal $\mathcal K$ on $X$ with

$$
|V(\mathcal K)|=|V(\mathcal I_1)|\cup b_1(|V(\mathcal I_2)|)
$$

and an isomorphism $X_2=\operatorname{Bl}_{\mathcal I_2}(X_1)\cong\operatorname{Bl}_{\mathcal K}(X)$
over $X$. It remains to see that $V(\mathcal K)\cap U=\varnothing$. First,
$V(\mathcal I_1)\cap U=\varnothing$ because $b_1$ is $U$-admissible.
Second, if $x=b_1(x')\in U$ with $x'\in V(\mathcal I_2)$, then
$x'\in b_1^{-1}(U)\cap V(\mathcal I_2)$, which is empty because the second
blow-up is $b_1^{-1}(U)$-admissible. Hence
$b_1(|V(\mathcal I_2)|)\cap U=\varnothing$ as well, so
$V(\mathcal K)\cap U=\varnothing$ and $\operatorname{Bl}_{\mathcal K}(X)\to X$
is $U$-admissible. No quasi-compactness of $U$ is used.
