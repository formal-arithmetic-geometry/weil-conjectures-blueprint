+++
kind  = "proof"
of    = "def-weil-algebraically-closed-coefficients"
uses = ["sk-prop-sfb-finite-extension-compatibility"]
+++
By [def-weil-rationalization-karoubi], each $D^b_c(Y,E)$ is the condensed bounded
constructible category over $E_Y$, and the transition functors $-\otimes_EL$ are the
extensions of scalars $L_Y\otimes_{E_Y}-$. Extension of scalars is transitive:
$\overline{\mathbf Q}_{\ell,Y}\otimes_{L_Y}(L_Y\otimes_{E_Y}K)\cong\overline{\mathbf Q}_{\ell,Y}\otimes_{E_Y}K$,
because the coefficient changes compose ([sk-prop-sfb-finite-extension-compatibility]). So
$(E,K)\mapsto\overline{\mathbf Q}_{\ell,Y}\otimes_{E_Y}K$ is a well-defined functor on
$\mathcal C_Y$. It is fully faithful and essentially surjective by
[sk-thm-sfb-qlbar-two-colimit] (4); recall that $D^b_{ctf}=D^b_c$ for rational coefficients.
It sends triangles to distinguished triangles because each extension of scalars
$\overline{\mathbf Q}_{\ell,Y}\otimes_{E_Y}-$ is exact, as $\overline{\mathbf Q}_{\ell,Y}$ is flat
over $E_Y$ ([sk-prop-sfb-finite-extension-compatibility] (1)), and a triangle of
$\mathcal C_Y$ is represented over one finite extension.
