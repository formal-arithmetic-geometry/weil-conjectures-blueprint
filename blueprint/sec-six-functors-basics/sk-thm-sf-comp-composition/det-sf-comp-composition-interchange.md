+++
id = "det-sf-comp-composition-interchange"
kind = "lemma"
title = "Interchanging proper direct image and extension by zero"
order = 2526
uses = ["det-sf-comp-coherence-single", "det-sf-determination-localizing", "sk-prop-proper-base-change-unbounded"]
+++
Let $\Lambda$ be admissible. Let $p:\overline X\to Y$ be proper, let
$i:Y\to\overline Y$ be a quasi-compact open immersion, and let
$\overline X\xrightarrow{j'}W\xrightarrow{r}\overline Y$ be a compactification of
$i\circ p$ with $\overline X$ dense in $W$. Then:

1. $r^{-1}(Y)=\overline X$ (as open subschemes of $W$), and $r$ restricts to $p$
over $Y$;
2. for $A\in D(\overline X_{\mathrm{proét}},\Lambda)$ there is a unique map
$\iota_A:i_!Rp_*A\to Rr_*j'_!A$ in $D(\overline Y_{\mathrm{proét}},\Lambda)$ whose
restriction to $Y$ is the identity of $Rp_*A$;
3. $\iota_A$ is an isomorphism for every $A\in\Loc(\Dctf(\overline X,\Lambda))$.
