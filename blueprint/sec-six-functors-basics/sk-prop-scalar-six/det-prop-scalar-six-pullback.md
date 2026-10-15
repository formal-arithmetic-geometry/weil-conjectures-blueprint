+++
id = "det-prop-scalar-six-pullback"
kind = "lemma"
title = "Coefficient change commutes with inverse image and extension by zero"
uses = ["sk-def-sfb-coefficient-change", "sk-prop-sfb-cartesian-coefficients", "det-lem-int-tensor-projection"]
+++
Let $\Lambda\to\Lambda'$ be a map of condensed rings and write
$K_{\Lambda'}=\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}K$ ([sk-def-sfb-coefficient-change]).

1. For a morphism $f\colon X\to Y$ and $K\in\D(Y_{\mathrm{proét}},\Lambda)$ there is a
   natural isomorphism $(f^*K)_{\Lambda'}\simeq f^*(K_{\Lambda'})$ in
   $\D(X_{\mathrm{proét}},\Lambda')$. For $g\colon Y\to W$ the isomorphism for $g\circ f$ is
   the composite of those for $f$ and $g$ under $(gf)^*=f^*g^*$.
2. For a locally closed immersion $a\colon S\hookrightarrow X$ (in particular an open
   immersion $j$ or a closed immersion $i$) and $M\in\D(S_{\mathrm{proét}},\Lambda)$ there
   is a natural isomorphism $(a_!M)_{\Lambda'}\simeq a_!(M_{\Lambda'})$, compatible with
   composition of immersions; for $a=i$ closed this reads
   $(i_*M)_{\Lambda'}\simeq i_*(M_{\Lambda'})$.
3. For a composite $\Lambda\to\Lambda'\to\Lambda''$ one has
   $(K_{\Lambda'})_{\Lambda''}\simeq K_{\Lambda''}$, compatibly with the isomorphisms in (1) and (2).
