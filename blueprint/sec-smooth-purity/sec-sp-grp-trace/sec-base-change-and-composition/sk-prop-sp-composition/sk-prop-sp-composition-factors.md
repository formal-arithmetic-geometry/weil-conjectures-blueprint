+++
id = "det-sp-composition-factors"
kind = "lemma"
title = "Composition of orientations and of tensor maps"
order = 3377
uses = ["det-sp-composition-comparisons", "det-sp-orientation-charts", "prop-pur-affine-space-composition-law"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be smooth of pure relative dimensions $d$
and $e$, with coefficients a finite ring $\Lambda=A$ or towers
$\mathcal O_E/\ell^\bullet$.

1. *Orientation.* Under
   $\omega_{g\circ f}\simeq f^!\omega_g\simeq f^*\omega_g\otimes\omega_f$ (composition and
   the tensor map for $f$ at $\omega_g$) and the twist additivity
   $\Lambda(d+e)[2d+2e]\simeq\Lambda(d)[2d]\otimes\Lambda(e)[2e]$, the orientation of
   $g\circ f$ is the tensor product of $f^*$ of the orientation of $g$ with the
   orientation of $f$.
2. *Tensor maps.* Under $(g\circ f)^!\simeq f^!g^!$, the tensor map
   $(g\circ f)^*K\otimes\omega_{g\circ f}\to(g\circ f)^!K$ equals the iterate: the tensor
   map for $g$ pulled back by $f$ and tensored with $\omega_f$, followed by the
   tensor map for $f$ at $g^!K$.

Consequently $\gamma_{g\circ f}(K)=\gamma_f(g^!K)\circ f^*(\gamma_g(K))(d)[2d]$ under
the canonical identifications.
