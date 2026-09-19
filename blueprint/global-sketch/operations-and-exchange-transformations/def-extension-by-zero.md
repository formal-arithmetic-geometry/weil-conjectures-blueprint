+++
id = "def-extension-by-zero"
kind = "definition"
title = "Extension by zero at completed and field coefficients"
order = 36
uses = ["def-derived-complete-integral-object", "def-finite-derived-extension-by-zero", "def-finite-reduction", "def-qbar-ambient-derived-category", "def-strict-reduction-tower", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients", "thm-qbar-functor-descent"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For an open immersion $j:U\hookrightarrow\overline X$ and a
derived-complete integral complex
$K\in D^b_c(U,\mathcal O_E)$, define the
derived-complete extension

$$
j_!K:=R\varprojlim_n\operatorname{Res}_{\overline X,n}
j_{!,n}\operatorname{red}_{U,n}(K).
$$

For $E$-coefficients the same section formula defines the exact functor
$j_!$, and common-stage descent defines the ambient functor

$$
j_!:D(U,\Qlb)\longrightarrow D(\overline X,\Qlb).
$$

Thus $j_{!,n}$ always denotes the finite-level
operation, whereas $j_!$ denotes the integral, rational, or
algebraically closed coefficient operation.
