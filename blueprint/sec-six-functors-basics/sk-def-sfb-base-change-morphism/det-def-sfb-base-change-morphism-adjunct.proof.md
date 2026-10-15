+++
kind = "proof"
of = "det-def-sfb-base-change-morphism-adjunct"
+++
For an adjunction $L\dashv R$ with unit $\eta'$ and counit $\varepsilon'$, the map
$\beta\mapsto\varepsilon'_B\circ L\beta$ is a bijection from natural transformations $A\Rightarrow RB$ to
natural transformations $LA\Rightarrow B$, with inverse $\gamma\mapsto R\gamma\circ\eta'_A$ (the
triangle identities). By definition $\mathrm{BC}_{sq}=Rf'_*(\gamma)\circ\eta'_{Lg^*Rf_*}$ with
$\gamma=Lg'^*\varepsilon\circ(\theta_{sq})_{Rf_*}$, so it is the transformation corresponding to
$\gamma$. Explicitly,
$$
\varepsilon'_{Lg'^*}\circ Lf'^*\bigl(Rf'_*\gamma\circ\eta'\bigr)=\gamma\circ\varepsilon'_{Lf'^*Lg^*Rf_*}\circ Lf'^*\eta'_{Lg^*Rf_*}=\gamma,
$$
by naturality of $\varepsilon'$ and the triangle identity $\varepsilon'_{Lf'^*}\circ Lf'^*\eta'=\mathrm{id}$.
Uniqueness is injectivity of the bijection.
