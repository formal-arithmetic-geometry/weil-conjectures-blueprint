+++
kind = "proof"
of = "det-sp-thick-origin"
uses = ["det-sp-thick-origin-homotopy", "det-sp-defect-definition", "det-sp-constant-family-vanishing"]
+++
Let $E=e^*\operatorname{Sp}_{X,Z}(M_X)$ and let $\phi_a$ be the endomorphisms of
[det-sp-thick-origin-homotopy], so that $\phi_0=\phi_1=\operatorname{id}_E$. Let
$\alpha\colon M_Z\to E$ be the restriction to the zero section of the nearby-cycle unit for the
constant sheaf on $\mathcal D_ZX$.

The map $H_0$ factors as $X\to Z\hookrightarrow X$. Naturality of the pullback exchange for this
factorization gives

$$
\phi_0=\alpha\,\epsilon_{X,Z}(M_X),\qquad
\epsilon_{X,Z}(M_X)\,\alpha=\operatorname{id}_{M_Z}.
$$

The second equality holds because $\epsilon_{X,Z}(M_X)\alpha$ is the specialization unit for the
constant family $Z\times S$ followed by its fixed inverse, which is invertible by
[det-sp-constant-family-vanishing]. Since $\phi_0=\operatorname{id}_E$, the maps $\alpha$ and
$\epsilon_{X,Z}(M_X)$ are inverse isomorphisms, and the cofibre $C_{X,Z}(M_X)$ vanishes.
