+++
kind  = "proof"
of    = "lem-pur-cfiber-stalk"
uses = ["sk-def-sfb-shriek-base-change-morphism", "sk-thm-sfb-shriek-base-change", "thm-cbc-complete-proetale"]
+++
*At $\Lambda=A$.* The stalk is the filtered-neighborhood fiber of [def-weil-pbc-geometric-stalks].
Choose a compactification $c=(j,p)$ of $\pi$
([def-compact-support-direct-image-detailed]); its base change at
$\bar b$ is a compactification of $E_{\bar b}\to\bar b$. The
compatibility of geometric stalks with extension by zero and with the
proper direct image ([thm-cbc-finite-level-proetale] for the
compact-support functors, [cor-weil-pbc-geometric-fiber-finite]
for the proper direct image of the [def-weil-pbc-etale-origin-witness]
representative) gives the displayed comparison, the witnesses being
compatible by [def-compact-support-direct-image-detailed].

*At the other coefficient rings $\Lambda\neq A$ of [def-pur-conventions].*
Here $K$ lies in the condensed category $\Dbc(E,\Lambda)$. The stalk at $\bar b$ is the inverse image along
$\bar b\to B$, and $R\Gamma_c(E_{\bar b},-)$ is the compact-support direct
image along the base change $E_{\bar b}\to\bar b$ of $\pi$. The displayed map
is therefore the compact-support base change morphism of
[sk-def-sfb-shriek-base-change-morphism] for the cartesian square formed by
$\pi$ and $\bar b\to B$, with the base-changed compactification. It is an
isomorphism by [sk-thm-sfb-shriek-base-change] for the rational rings and by
[thm-cbc-complete-proetale] for the ring of integers.
